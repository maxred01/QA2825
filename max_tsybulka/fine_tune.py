import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer
from datasets import load_dataset

model_name = "unsloth/llama-3-8b-bnb-4bit"
dataset_name = "timdettmers/openassistant-guanaco"
new_model_name = "my-llama-3-finetuned"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto", # Автоматически распределит слои по GPU/CPU
    trust_remote_code=True,
)
model.config.use_cache = False
model.config.pretraining_tp = 1

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,  # Ранг матриц LoRA
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"] # Модули для Llama
)

dataset = load_dataset(dataset_name, split="train")
# Форматируем данные в текст. Guanaco уже в формате: "### Human: ... ### Assistant: ..."
def format_dataset(example):
    # Можно добавить общий промпт-шаблон
    example["text"] = f"### Human: {example['instruction']} ### Assistant: {example['response']}"
    return example
dataset = dataset.map(format_dataset)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,          # 1 эпохи часто достаточно
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    save_steps=50,
    logging_steps=10,
    learning_rate=2e-4,
    weight_decay=0.001,
    fp16=True,
    optim="paged_adamw_32bit",
    max_grad_norm=0.3,
    warmup_ratio=0.03,
    group_by_length=True,
    lr_scheduler_type="constant",
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=512,          # Увеличьте, если нужно
    tokenizer=tokenizer,
    args=training_args,
)

trainer.train()

trainer.model.save_pretrained(new_model_name)
tokenizer.save_pretrained(new_model_name)
print(f"Модель сохранена в {new_model_name}")

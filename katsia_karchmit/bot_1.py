from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess
import os
import sys
import zipfile
import time
import asyncio
from pathlib import Path
import ollama
import aiogram

API_TOKEN = '8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4'

# ПУТИ ОТНОСИТЕЛЬНО МЕСТОПОЛОЖЕНИЯ bot_l.py
BASE_DIR = Path(__file__).parent.absolute()  # D:\QA2825\katsia_karchmit
ALLURE_RESULTS_DIR = BASE_DIR / "allure-results"
ALLURE_REPORT_DIR = BASE_DIR / "allure-report"

async def execute_command(cmd: list, update: Update, timeout: int = 300) -> str:
    """Выполняет shell-команду с таймаутом и возвращает результат"""
    try:
        # Преобразуем список в строку для subprocess
        cmd_str = " ".join(cmd)
        proc = await asyncio.create_subprocess_shell(
            cmd_str,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
        output = f"STDOUT:\n{stdout.decode().strip()}" if stdout else ""
        output += f"\nSTDERR:\n{stderr.decode().strip()}" if stderr else ""
        return output.strip()
    except asyncio.TimeoutError:
        return f"❌ Таймаут ({timeout} сек)"
    except Exception as e:
        return f"⚠️ Ошибка: {str(e)}"


async def run_all_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю тесты...")

    all_tests_path = BASE_DIR / "home_work" / "home_work_9" / "test"

    # Проверяем существование пути
    if not all_tests_path.exists():
        await update.message.reply_text(f"❌ Путь не найден: {all_tests_path}")
        return

    # Подготовка директории для результатов
    ALLURE_RESULTS_DIR.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in ALLURE_RESULTS_DIR.glob("*"):
        if file.is_file():
            file.unlink()

    # Запуск pytest с правильными путями
    result = await execute_command(
        ["pytest", "-s", "-v", str(all_tests_path), f"--alluredir={ALLURE_RESULTS_DIR}"],
        update
    )

    # Проверка наличия результатов тестов
    if not any(ALLURE_RESULTS_DIR.iterdir()):
        await update.message.reply_text("⚠️ Внимание: allure-results пуст. Возможно, тесты не запустились.")
        return

    # Отправка сокращенного отчета
    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line or "PASSED" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )

async def run_ui_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск UI тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю UI тесты...")

    ui_tests_path = BASE_DIR / "home_work" / "home_work_9" / "test" / "ui"

    # Проверяем существование пути
    if not ui_tests_path.exists():
        await update.message.reply_text(f"❌ Путь не найден: {ui_tests_path}")
        return

    # Подготовка директории для результатов
    ALLURE_RESULTS_DIR.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in ALLURE_RESULTS_DIR.glob("*"):
        if file.is_file():
            file.unlink()

    # Запуск pytest с правильными путями
    result = await execute_command(
        ["pytest", "-s", "-v", str(ui_tests_path), f"--alluredir={ALLURE_RESULTS_DIR}"],
        update
    )

    # Проверка наличия результатов тестов
    if not any(ALLURE_RESULTS_DIR.iterdir()):
        await update.message.reply_text("⚠️ Внимание: allure-results пуст. Возможно, тесты не запустились.")
        return

    # Отправка сокращенного отчета
    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line or "PASSED" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )

async def run_api_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск API тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю API тесты...")

    api_tests_path = BASE_DIR / "home_work" / "home_work_9" / "test" / "api"

    # Проверяем существование пути
    if not api_tests_path.exists():
        await update.message.reply_text(f"❌ Путь не найден: {api_tests_path}")
        return

    # Подготовка директории для результатов
    ALLURE_RESULTS_DIR.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in ALLURE_RESULTS_DIR.glob("*"):
        if file.is_file():
            file.unlink()

    # Запуск pytest с правильными путями
    result = await execute_command(
        ["pytest", "-s", "-v", str(api_tests_path), f"--alluredir={ALLURE_RESULTS_DIR}"],
        update
    )

    # Проверка наличия результатов тестов
    if not any(ALLURE_RESULTS_DIR.iterdir()):
        await update.message.reply_text("⚠️ Внимание: allure-results пуст. Возможно, тесты не запустились.")
        return

    # Отправка сокращенного отчета
    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line or "PASSED" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )


async def generate_allure_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Генерация отчета и отправка архива"""
    try:
        # Проверка наличия результатов тестов
        if not ALLURE_RESULTS_DIR.exists() or not any(ALLURE_RESULTS_DIR.iterdir()):
            await update.message.reply_text("❌ Нет данных для отчета: папка allure-results пуста или отсутствует")
            return

        # Генерация отчета
        await update.message.reply_text("📈 Генерирую Allure-отчет...")
        ALLURE_REPORT_DIR.mkdir(exist_ok=True)

        gen_result = await execute_command(
            ["allure", "generate", str(ALLURE_RESULTS_DIR), "-o", str(ALLURE_REPORT_DIR), "--clean"],
            update
        )

        # Проверка наличия сгенерированного отчета
        report_index = ALLURE_REPORT_DIR / "index.html"
        if not report_index.exists():
            await update.message.reply_text("❌ Ошибка генерации: index.html не найден в allure-report")
            return

        # Создание архива
        await update.message.reply_text("📦 Создаю архив...")
        timestamp = int(time.time())
        zip_name = f"allure_report_{timestamp}.zip"
        zip_path = BASE_DIR / zip_name  # Сохраняем в той же директории

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Добавляем allure-report
            for root, _, files in os.walk(ALLURE_REPORT_DIR):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-report", os.path.relpath(file_path, ALLURE_REPORT_DIR))
                    zipf.write(file_path, arcname=arcname)

            # Добавляем allure-results
            for root, _, files in os.walk(ALLURE_RESULTS_DIR):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-results", os.path.relpath(file_path, ALLURE_RESULTS_DIR))
                    zipf.write(file_path, arcname=arcname)

        # Отправка архива
        await update.message.reply_text("📤 Отправляю архив...")
        with open(zip_path, 'rb') as zip_file:
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=zip_file,
                filename=zip_name,
                caption="📊 Allure Report (включая исходные данные)"
            )

        # Очистка временных файлов
        os.remove(zip_path)
        await update.message.reply_text("✅ Отчет успешно отправлен!")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Критическая ошибка: {str(e)}")


async def full_cycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Полный цикл: тесты + отчет"""
    await run_all_tests(update, context)
    await generate_allure_report(update, context)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я чат-бот дипломного проекта. Помогаю запускать автоматически тесты для проверки работы сайта. \nОтлично налаженная работа сайта - гарантия довольного клиента для бизнеса. \nНапиши /about, чтобы узнать обо мне; \n/run_api_tests, чтобы запустить api тесты; \n/run_ui_tests, чтобы запустить ui тесты; \n/allure_report, чтобы сформировать отчет о пройденных тестах; \n/full_cycle, чтобы запустить все тесты и сформировать отчет ')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text= 'Я ,Екатерина Карчмит, написала чат-бот @zrobim_bot, чтобы запускать тесты для проверки сайта Zrobim.by в рамках подготовки дипломного проекта.\nПрохожу обучение в IT ШАГ по специальности "Ручное и автоматизированное тестирование". \nМотивированный начинающий QA с сильной любознательностью и стремлением к деталям. \nМои контакты: тел.+375(33)314 42 30; \ne-mail - yekaterina.karchmit@mail.ru; \nLinkedIn - https://www.linkedin.com/in/katsiaryna-karchmit-39b513364?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app  '
    await update.message.reply_text(about_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    await update.message.chat.send_action(action='typing')

    try:
        response = ollama.chat(model='llama3.2:1b-instruct-q3_K_S',
                               messages=[{'role': 'user', 'content': user_message}])

        await update.message.reply_text(response['message']['content'])


    except Exception as e:
        await update.message.reply_text(f'Ошибка: {str(e)}')

def main():
    application = Application.builder().token("8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4").build()

    handlers = [
        CommandHandler("run_all_tests", run_all_tests),
        CommandHandler("run_ui_tests", run_ui_tests),
        CommandHandler("run_api_tests", run_api_tests),
        CommandHandler("allure_report", generate_allure_report),
        CommandHandler("full_cycle", full_cycle),
        CommandHandler("about", about),
        CommandHandler("start", start),
        CommandHandler("handle_message", handle_message)
    ]

    for handler in handlers:
        application.add_handler(handler)

    print('Бот запущен')
    application.run_polling()


if __name__ == "__main__":
    main()
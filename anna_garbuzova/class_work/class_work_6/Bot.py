from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext

API_TOKEN = "8003196291:AAEJg8rUllORuLN-8rJ6GHF5UwRAJS_3aR0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я пример бота дип.проекта! Напиши /about чтобы узнать обо мне')

async def about(update: Update, context:ContextTypes.DEFAULT_TYPE):
    about_text = "Я Аня, прохожу курс автоматизации тестирования и написала этот бот @testQA2825bot чтобы запускать API и UI тесты, а также формировать отчет в Allure. \n\n Чтобы запустить API test - пиши /api,\n UI тест - пиши /ui,\n сформировать отчет - пиши /allureresult \n\n Если будут вопросы - мой тг @animonella :)"
    await update.message.reply_text(about_text)

def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))

    print('Бот запущен')
    app.run_polling()

if __name__ == '__main__':
    main()

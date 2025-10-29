from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8423095564:AAEj2-_bd1laQXoOV1aOLX5jK7eXaluJKtg'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я пример бота дип. проекта! Напиши /about чтобы узнать обо мне')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = 'Я Максим написал бот что\n бзапускать тесты'
    await update.message.reply_text(about_text)


def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('about', about))
    app.add_handler(CommandHandler('start', start))

    print('Бот запущен')
    app.run_polling()

if __name__ == "__main__":
    main()
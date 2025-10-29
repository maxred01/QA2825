from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8484773386:AAGpNZ4tFuub5-xvCX28UKa-MLNbek7nwcE'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ола амиго! Я бот-помощник, чтобы узнать подробную инфу напиши /about')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = 'Я @bto03942734_bot, который запускает тесты из заданных категорий.\nМой создатель - @anvoyt.\n Научилась создавать телеграм-бота и вот он есть я.\nПожелаем ей всего лучшего и ты можешь идти дальше кликать по кнопкам'
    await update.message.reply_text(about_text)


def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))

    print('Bot is ready')
    app.run_polling()


if __name__ == "__main__":
    main()

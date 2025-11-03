from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8353078171:AAEC9OJgRfq1gIG6n2Uhb8YbvJKaalaRcXM'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доброго времени суток! Я дипломный проект, созданный для запуска тестов, чтобы узнать подробную инфу напиши /about\nДругие команды:\n/api - запускает api тесты\n/ui - запускает ui тесты')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = ('Я @dp2825_bot, дипломный проект моего создателя - @anvoyt.\nЯ запускаю тесты, которые ты можешь выбрать из заданных категорий и наблюдать за их выполнением.\nСписок команд можешь найти нажав кнопку "меню" в левом нижнем углу).\nЕще немного информации о создателе:\nЕе зовут Аня, учиться в IT Академии "ШАГ" на мануального и автоматизированного тестировщика.\nЕсли вдруг вам понадобиться тестировщик, можете с ней связаться:\n@anvoyt - telegram,\nhttps://www.linkedin.com/in/anna-voytovich-8543a322a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app - LinkedIn.')
    await update.message.reply_text(about_text)

def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))

    print('Bot is ready')
    app.run_polling()


if __name__ == "__main__":
    main()

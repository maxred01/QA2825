from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8469106065:AAGOFco3cFxbanN_JI0gRL9ErSTLiEEu568'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Хей, я бот дипломного проекта!\nМеню бота:\n1.Напиши /about , чтобы узнать обо мне\n2.Напиши /api , чтобы начать api тесты\n3.Напиши /ui , чтобы начать ui тесты\n4.Напиши /allurereports, чтобы создать allure отчёт')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = 'Здесь я создал бота для того, чтоб реализовать авто тесты\nХочу упростить привычный взгляд на авто тесты и взглянуть с другой стороны\n\nБота зовут - @emnotem\nМой телеграм аккаунт - @asperatus99'
    await update.message.reply_text(about_text)


def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))


    print('Бот запущен')
    app.run_polling()

if __name__ == "__main__":
    main()
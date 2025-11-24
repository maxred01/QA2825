from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я пример чат-бота дипломного проекта. Напиши /about чтобы узнать обо мне')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text= 'Я Катя написала чат-бот @zrobim_bot, чтобы запускать тесты для проверки сайта Zrobim.by в рамках подготовки дипломного проекта.\nПрохожу обучение в IT ШАГ по специальности "Ручное и автоматизированное тестирование". \nМои контакты - LinkedIn - https://www.linkedin.com/in/katsiaryna-karchmit-39b513364?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app '
    await update.message.reply_text(about_text)


def main():
    app= Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))

    print('Бот запущен')
    app.run_polling()
if __name__ == "__main__":
    main()
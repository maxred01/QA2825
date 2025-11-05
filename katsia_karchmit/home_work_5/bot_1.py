from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я пример чат-бота дипломного проекта. Помогаю запускать автоматически тесты для проверки работы сайта. Отлично налаженная работа сайта - гарантия довольного клиента для бизнеса. Напиши /about чтобы узнать обо мне')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text= 'Я ,Екатерина Карчмит, написала чат-бот @zrobim_bot, чтобы запускать тесты для проверки сайта Zrobim.by в рамках подготовки дипломного проекта.\nПрохожу обучение в IT ШАГ по специальности "Ручное и автоматизированное тестирование". \nМотивированный начинающий QA с сильной любознательностью и стремлением к деталям. \nОбладаю аналитическим складом ума и терпением для кропотливой работы. \nВладею следующими техническими навыками (Hard Skills): \n- cоставляла тест-кейсы и чек-листы для веб-приложений, оформляла баг-репорты в Jira; \n- базовые знания API-тестирования: отправка запросов в Postman (GET/POST/PUT/DELETE), проверка статус-кодов и структуры ответов, чтение JSON; \n- простые SQL-запросы для проверки данных в БД (SELECT, WHERE, JOIN); \n- использую Chrome DevTools для анализа элементов страницы и сетевых запросов (просмотр элементов, вкладка Network); \n- понимание структуры страницы (HTML/CSS); \n- понимание клиент-серверной архитектуры (HTTP-методы, статус-коды); \n- базовые навыки работы в Linux (навигация в терминале, управление файлами, анализ логов); \n- базовые навыки в языке программирования Python; \n- основы автоматизации (работа с GIT, Allure, PyCharm). \nМои контакты: тел.+375(33)314 42 30; \ne-mail - yekaterina.karchmit@mail.ru; \nLinkedIn - https://www.linkedin.com/in/katsiaryna-karchmit-39b513364?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app  '
    await update.message.reply_text(about_text)


def main():
    app= Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))

    print('Бот запущен')
    app.run_polling()
if __name__ == "__main__":
    main()
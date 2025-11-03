from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = '8469106065:AAGOFco3cFxbanN_JI0gRL9ErSTLiEEu568'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Хей, я бот дипломного проекта для начинающего тестировщика!\n\nВот, что я могу тебе предложить:\n\n'
                                    '1)  Напиши /about , чтобы узнать обо мне и создателе.\n\n'
                                    '2)  Напиши /api , чтобы начать api тесты, которые помогают выявить ошибки и оценить общую работоспособность системы.\n\n'
                                    '3)  Напиши /ui , чтобы начать ui тесты, которые проверяют пользовательский интерфейс ПО, оценивает его визуальные элементы, функциональность, удобство использования и т.д.\n\n'
                                    '4)  Напиши /allurereports, чтобы создать allure отчёт, который покажет информацию о результатах тестирования.')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = ('Здравствуй, дорогой пользователь!\n\nЯ создал бота для того, чтоб реализовать авто тесты с помощью функционала бота. Предлагаю сменить привычный взгляд на авто тесты и использовать другой формат. Да, я не первый, кто решил так сделать, но такое ведь не часто встретишь?!  \n\n'
                  'Бот умеет делать базовые авто тесты с упором на api и ui тесты, а также выдать allure отчёт по совершённым тестам.\n\n'
                  'Меня зовут Талако Александр Тимофеевич!\n'
                  'Я начинающий тестировщик без опыта работы, но имеющий большое рвение и скрытый потенциал им стать.\n\n'
                  'Владею следующим:\n'
                  'TestRail, TestLink, Jmeter, Jira, JSON, XML, HTML, DevTools, SQL-запросы, Postman, Python, Pycharm, Git, Allure\n'
                  'Этот список будет дополняться :)\n\n'
                  'Также хочу отметить, что нравится мне область информационной безопасности и стать специалистом в этой области — это то, к чему я стремлюсь.\n'
                  '"Белый хакер" — звучит ярко и серьёзно. Поэтому предстоит большая работа.\n\n'
                  'P.S. Начал понемногу осваивать Kali Linux. Данный дистрибутив достаточно распространённый и вполне понятен в изучении.\n\n'
                  'Бота зовут — @emnotem_bot\nМой телеграм аккаунт — @asperatus99')
    await update.message.reply_text(about_text)

def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('about', about))


    print('Бот запущен')
    app.run_polling()

if __name__ == "__main__":
    main()
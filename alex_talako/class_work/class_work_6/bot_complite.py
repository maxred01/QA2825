from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import zipfile
import time
import asyncio
from pathlib import Path


async def execute_command(cmd: str, update: Update, timeout: int = 300) -> str:
    """Выполняет shell-команду с таймаутом и возвращает результат"""
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
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


async def run_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю тесты...")

    # Подготовка директории для результатов
    results_dir = Path("./allure-results")
    results_dir.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    # Запуск pytest
    result = await execute_command(
        "pytest -s -v test_allure_in_class.py --alluredir=./allure-results",
        update
    )

    # Проверка наличия результатов тестов
    # if not any(results_dir.iterdir()):
    #     await update.message.reply_text("⚠️ Внимание: allure-results пуст. Возможно, тесты не запустились.")
    #     return

    # Отправка сокращенного отчета
    short_result = "\n".join([line for line in result.split("\n") if "FAILED" in line or "ERROR" in line])
    await update.message.reply_text(
        f"📊 Результаты тестов:\n{short_result[:3000]}" if short_result else "✅ Все тесты прошли успешно!"
    )


async def generate_allure_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Генерация отчета и отправка архива"""
    try:
        # Проверка наличия результатов тестов
        results_dir = Path("./allure-results")
        if not results_dir.exists() or not any(results_dir.iterdir()):
            await update.message.reply_text("❌ Нет данных для отчета: папка allure-results пуста или отсутствует")
            return

        # Генерация отчета
        await update.message.reply_text("📈 Генерирую Allure-отчет...")
        report_dir = Path("./allure-report")
        report_dir.mkdir(exist_ok=True)

        gen_result = await execute_command(
            "allure generate ./allure-results --clean -o ./allure-report",
            update
        )

        # Проверка наличия сгенерированного отчета
        report_index = report_dir / "index.html"
        if not report_index.exists():
            await update.message.reply_text("❌ Ошибка генерации: index.html не найден в allure-report")
            return

        # Создание архива
        await update.message.reply_text("📦 Создаю архив...")
        timestamp = int(time.time())
        zip_name = f"allure_report_{timestamp}.zip"

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Добавляем allure-report
            for root, _, files in os.walk(report_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-report", os.path.relpath(file_path, report_dir))
                    zipf.write(file_path, arcname=arcname)

            # Добавляем allure-results
            for root, _, files in os.walk(results_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("allure-results", os.path.relpath(file_path, results_dir))
                    zipf.write(file_path, arcname=arcname)

        # Отправка архива
        await update.message.reply_text("📤 Отправляю архив...")
        with open(zip_name, 'rb') as zip_file:
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=zip_file,
                filename=zip_name,
                caption="📊 Allure Report (включая исходные данные)"
            )

        # Очистка временных файлов
        os.remove(zip_name)
        await update.message.reply_text("✅ Отчет успешно отправлен!")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Критическая ошибка: {str(e)}")


async def full_cycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Полный цикл: тесты + отчет"""
    await run_tests(update, context)
    await generate_allure_report(update, context)


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
    application = Application.builder().token("8469106065:AAGOFco3cFxbanN_JI0gRL9ErSTLiEEu568").build()

    handlers = [
        CommandHandler("runtests", run_tests),
        CommandHandler("allurereport", generate_allure_report),
        CommandHandler("fullreport", full_cycle),
        CommandHandler("about", about),
        CommandHandler("start", start)
    ]

    for handler in handlers:
        application.add_handler(handler)

    print('Бот запущен')
    application.run_polling()


if __name__ == "__main__":
    main()

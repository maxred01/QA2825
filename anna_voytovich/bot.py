from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
import logging
import zipfile
import time
import asyncio
import ollama, aiogram
from pathlib import Path

API_TOKEN = '8353078171:AAEC9OJgRfq1gIG6n2Uhb8YbvJKaalaRcXM'


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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Доброго времени суток! Я дипломный проект, созданный для запуска тестов, чтобы узнать подробную инфу напиши /about'
        '\nДругие команды:\n'
        '/api - запуск api тестов\n'
        '/ui - запуск ui тестов\n /all_tests - запуск ui и api тестов вместе \n'
        '/allure_report - генерирует отчет о результатах тестов \n '
        '/full_report - запускает все тесты и генерирует отчет о результатах тестов')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = ('Я @dp2825_bot, дипломный проект моего создателя - @anvoyt.'
                  '\nЯ запускаю тесты, которые ты можешь выбрать из заданных категорий и наблюдать за их выполнением.\nСписок команд можешь найти нажав кнопку "меню" в левом нижнем углу).\nЕще немного информации о создателе:\nЕе зовут Аня, учиться в IT Академии "ШАГ" на мануального и автоматизированного тестировщика.\nЕсли вдруг вам понадобиться тестировщик, можете с ней связаться:\n@anvoyt - telegram,\nhttps://www.linkedin.com/in/anna-voytovich-8543a322a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app - LinkedIn.')
    await update.message.reply_text(about_text)


async def run_api_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "pytest -s -v homework/POM/test/api/ --alluredir=./allure-results",
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


async def run_ui_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "pytest -s -v homework/POM/test/ui/ --alluredir=./allure-results",
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


async def run_all_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "pytest -s -v homework/POM/test --alluredir=./allure-results",
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
    await run_all_tests(update, context)
    await generate_allure_report(update, context)


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
    application = Application.builder().token("8353078171:AAEC9OJgRfq1gIG6n2Uhb8YbvJKaalaRcXM").build()

    handlers = [
        CommandHandler("all_tests", run_all_tests),
        CommandHandler("ui", run_ui_tests),
        CommandHandler("api", run_api_tests),
        CommandHandler("allure_report", generate_allure_report),
        CommandHandler("full_report", full_cycle),
        CommandHandler("about", about),
        CommandHandler("start", start),
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    ]


    for handler in handlers:
        application.add_handler(handler)
    print('Bot is ready')
    application.run_polling()


if __name__ == "__main__":
    main()

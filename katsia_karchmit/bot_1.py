from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess, os, sys

API_TOKEN = '8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4'

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


async def run_all_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю тесты...")

    # Подготовка директории для результатов
    results_dir = Path("home_work/home_work_9/allure-results")
    results_dir.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    # Запуск pytest
    result = await execute_command(
        "pytest -s -v home_work/home_work_9/tests --alluredir=./allure-results",
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
    results_dir = Path("home_work/home_work_9/allure-results")
    results_dir.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    # Запуск pytest
    result = await execute_command(
        "pytest -s -v home_work/home_work_9/tests/ui --alluredir=./allure-results",
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

async def run_api_tests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запуск тестов и сохранение результатов"""
    await update.message.reply_text("🔍 Запускаю тесты...")

    # Подготовка директории для результатов
    results_dir = Path("home_work/home_work_9/allure-results")
    results_dir.mkdir(exist_ok=True)

    # Очистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    # Запуск pytest
    result = await execute_command(
        "pytest -s -v home_work/home_work_9/tests/api --alluredir=./allure-results",
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
        results_dir = Path("home_work/home_work_9/allure-results")
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
                    arcname = os.path.join("home_work/home_work_9/allure-results", os.path.relpath(file_path, results_dir))
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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я пример чат-бота дипломного проекта. Помогаю запускать автоматически тесты для проверки работы сайта. Отлично налаженная работа сайта - гарантия довольного клиента для бизнеса. Напиши /about чтобы узнать обо мне, ')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text= 'Я ,Екатерина Карчмит, написала чат-бот @zrobim_bot, чтобы запускать тесты для проверки сайта Zrobim.by в рамках подготовки дипломного проекта.\nПрохожу обучение в IT ШАГ по специальности "Ручное и автоматизированное тестирование". \nМотивированный начинающий QA с сильной любознательностью и стремлением к деталям. \nОбладаю аналитическим складом ума и терпением для кропотливой работы. \nВладею следующими техническими навыками (Hard Skills): \n-  оформляла тест-кейсы, чек-листы для веб-приложений, баг-репорты в Jira; \n- базовые знания API-тестирования: отправка запросов в Postman (GET/POST/PUT/DELETE), проверка статус-кодов и структуры ответов, чтение JSON; \n- простые SQL-запросы для проверки данных в БД (SELECT, WHERE, JOIN); \n- использую Chrome DevTools для анализа элементов страницы и сетевых запросов (просмотр элементов, вкладка Network); \n- понимание структуры страницы (HTML/CSS); \n- понимание клиент-серверной архитектуры (HTTP-методы, статус-коды); \n- базовые навыки работы в Linux (навигация в терминале, управление файлами, анализ логов); \n- базовые навыки в языке программирования Python; \n- основы автоматизации (работа с GIT, Allure, PyCharm). \nМои контакты: тел.+375(33)314 42 30; \ne-mail - yekaterina.karchmit@mail.ru; \nLinkedIn - https://www.linkedin.com/in/katsiaryna-karchmit-39b513364?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app  '
    await update.message.reply_text(about_text)


def main():
    application = Application.builder().token("8451173974:AAFo5AlYwFQHegpbQC1l00BSfYhwG4Pjss4").build()

    handlers = [
        CommandHandler("run_all_tests", run_all_tests),
        CommandHandler("run_ui_tests", run_ui_tests),
        CommandHandler("run_api_tests", run_api_tests),
        CommandHandler("allurereport", generate_allure_report),
        CommandHandler("fullreport", full_cycle),
        CommandHandler("about", about),
        CommandHandler("start", start)
    ]

    for handler in handlers:
        application.add_handler(handler)

    application.run_polling()


if __name__ == "__main__":
    main()
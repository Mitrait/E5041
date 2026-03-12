# E5041.pro — сайт-визитка Попова Евгения Валерьевича

Установка:
1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. copy .env.example .env
5. python manage.py migrate
6. python manage.py runserver

!!!!!ВАЖНО УЧТИ ПРИ СБОРКЕ - pydantic-core решён навсегда через PyO3 ABI3 (библиотека видит Python 3.14 без recompilation).
Обратная связь ТОЛЬКО через Telegram-бот @E5041_bot.

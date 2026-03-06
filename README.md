# E5041.pro — сайт-визитка Попова Евгения Валерьевича (эксперт по 152-ФЗ, официальный представитель DocShell 4.0 в Сочи)

## Установка (PyCharm + PowerShell + Python 3.14+)
1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. copy .env.example .env
5. python manage.py migrate
6. python manage.py runserver

!!!!!ВАЖНО УЧТИ ПРИ СБОРКЕ - pydantic-core решён навсегда через PyO3 ABI3 (библиотека видит Python 3.14 без recompilation — указать в requirements.txt и README).
Все зависимости взять с wheels, совместимыми с Python 3.14 (django 6+, django-tailwind и т.д.).
Обратная связь ТОЛЬКО через Telegram-бот @E5041_bot.

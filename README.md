# scooter-api-tests-python

## Автоматизация API

Автотест проверяет:
1. создание заказа;
2. получение заказа по трек-номеру.

## Запуск

Создать виртуальное окружение:

    python3 -m venv .venv

Активировать:

    source .venv/bin/activate

Установить зависимости:

    pip install pytest requests

Запустить тесты:

    pytest -v

## Работа с базой данных

SQL-запросы для заданий находятся в файле `orders.sql`.
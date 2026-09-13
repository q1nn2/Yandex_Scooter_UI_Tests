# Sprint_6 — UI-тесты сервиса «Яндекс.Самокат»

Финальный проект 6 спринта курса автоматизации тестирования.

## Что проверяется

- 8 вопросов блока «Вопросы о важном»;
- позитивный сценарий заказа самоката с двумя наборами данных;
- обе точки входа в заказ: верхняя и нижняя кнопки «Заказать»;
- переход по логотипу «Самокат» на главную страницу;
- переход по логотипу Яндекса в новое окно на главную страницу Дзена.

## Технологии

- Python
- Pytest
- Selenium WebDriver
- Mozilla Firefox
- Page Object Model
- Allure

## Структура

```text
Sprint_6/
├── locators/
│   ├── __init__.py
│   ├── base_page_locators.py
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/
│   ├── __init__.py
│   ├── test_faq.py
│   ├── test_navigation.py
│   └── test_order.py
├── allure_results/
├── conftest.py
├── data.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Установка зависимостей

```powershell
python -m pip install -r requirements.txt
```

Firefox должен быть установлен на компьютере. Selenium Manager автоматически подберёт драйвер для Firefox при первом запуске.

## Запуск тестов

```powershell
pytest
```

## Запуск с формированием Allure results

```powershell
Remove-Item -Recurse -Force allure_results -ErrorAction SilentlyContinue
New-Item -ItemType Directory allure_results
pytest --alluredir=allure_results
```

## Просмотр Allure-отчёта

```powershell
allure serve allure_results
```

После успешного прогона результаты из папки `allure_results` нужно добавить в Git и запушить в ветку `develop`.

## Git для сдачи

В `main` оставляется начальная версия проекта. Решение находится в ветке `develop`.

На GitHub создаётся Pull Request:

`develop -> main`

До зачёта проекта Pull Request не нужно сливать в `main`.

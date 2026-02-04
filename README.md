# UI Autotests (Selenium + PyTest + Allure)

Проект UI-автотестов для формы: https://practice-automation.com/form-fields/

## Требования задания выполнены

- Язык: **Python 3.10+**
- Инструменты: **Selenium WebDriver**, **PyTest**
- Поиск элементов: используются селекторы **ID**, **CSS**, **XPath**
- Паттерны: **Page Object Model**, PageFactory-подход (ленивые элементы через helper), **Fluent** (цепочки вызовов)
- Отчёты: **Allure** (+ attachments: screenshot/text)

---

## Структура проекта

```text
autotest/
├── pages/
│   └── form_fields_page.py
├── tests/
│   └── test_form_fields.py
├── utils/
│   └── driver_factory.py
├── conftest.py
├── .env.example
└── README.md
```

## Браузер

В проекте используется **Google Chrome for Testing (Stable)**.

Версия:
- Chrome: **144.0.7559.133**
- Platform: **Windows (win64)**

Браузер загружается с официального сайта:
https://googlechromelabs.github.io/chrome-for-testing/

## Запуск проекта с использованием **uv**

В проекте используется uv в качестве менеджера зависимостей и виртуального окружения.

### Установка зависимостей

Из корня проекта выполните команду:

```bash
uv sync
```
Команда:
- создаст виртуальное окружение
- установит все зависимости из **pyproject.toml**
- зафиксирует версии в **uv.lock**

Укажите путь до chrome.exe в файле .env

### Запуск автотестов с генерацией Allure-результатов
```bash
uv run pytest --alluredir=allure-results
```
После выполнения команды будет создана папка allure-results с результатами прогона тестов.

### Просмотр Allure-отчёта

Для открытия HTML-отчёта выполните:
```bash
allure serve allure-results
```
Отчёт автоматически откроется в браузере.

*Примечание:*
Для работы **Allure CLI** требуется установленная **Java** (рекомендуется **Temurin JDK 17**).

## Альтернативный способ запуска (pip)

Если вы не используете uv, проект можно запустить стандартным способом:

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Тест-кейсы

### Позитивный кейс

Предусловие:
1.	Открыть браузер
2.	Перейти по ссылке https://practice-automation.com/form-fields/

Шаги:
1.	Заполнить поле Name
2.	Заполнить поле Password
3.	Из списка What is your favorite drink? выбрать Milk и Coffee
4.	Из списка What is your favorite color? выбрать Yellow
5.	В поле Do you like automation? выбрать любой вариант
6.	Поле Email заполнить строкой формата name@example.com
7.	В поле Message написать количество инструментов, описанных в пункте Automation tools и написать инструмент из списка Automation tools, содержащий наибольшее количество символов
8.	Нажать на кнопку Submit 

Ожидаемый результат:

Отображается alert с текстом: **Message received!**

### Негативный кейс

Предусловие:
1.	Открыть браузер
2.	Перейти по ссылке https://practice-automation.com/form-fields/

Шаги:
1.	Поле Name оставить пустым
2.	Заполнить поле Password
3.	Из списка What is your favorite drink? выбрать Milk и Coffee
4.	Из списка What is your favorite color? выбрать Yellow
5.	В поле Do you like automation? выбрать любой вариант
6.	Поле Email заполнить строкой формата name@example.com
7.	В поле Message написать количество инструментов, описанных в пункте Automation tools и написать инструмент из списка Automation tools, содержащий наибольшее количество символов
8.	Нажать на кнопку Submit 

Ожидаемый результат:

Форма не отправляется.  
Срабатывает встроенная HTML5-валидация обязательного поля **Name** — браузер отображает подсказку вида “Заполните это поле”.

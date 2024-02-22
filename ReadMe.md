Описание
--------

Автотесты для проверки работы сайтов

Первый сценарий: проверяем некоторые ссылки и размеры изображений на странице.

Второй сценарий: проверяем, что при выборе региона меняется соответствующая информация.

Запуск
------

1) Install all requirements:

    ```bash
    pip install -r requirements.txt
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v
    ```

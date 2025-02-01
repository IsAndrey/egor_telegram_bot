# Учебный Телеграм Бот Бобик

### Бот Бобик космический рэйнджер и охотник на кошек
- Получите токен вашего телеграм бота и сохраните в файл .env
- Получите токен на сайте https://api.nasa.gov/ и сохраните в файл .env
- Запустите Бобика, он умеет здороваться, ловить кошек и исследовать космос.

### Инструкция по запуску

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/IsAndrey/egor_telegram_bot.git
```

```
cd egor_telegram_bot
```

Cоздать, активировать виртуальное окружение и обновить пакетный менеджер:

* Если у вас Linux/macOS

    ```
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    ```

* Если у вас Windows

    ```
    python -m venv venv
    source venv/scripts/activate
    python -m pip install --upgrade pip
    ```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Получить токены доступа для Телеграм и НАСА и записать их в файл .env

Запустить проект:

* Если у вас Linux/macOS

    ```
    python3 bot.py
    ```

* Если у вас Windows

    ```
    python bot.py
    ```

Для завершения работы бота используйте сочетание клавиш Ctrl+C
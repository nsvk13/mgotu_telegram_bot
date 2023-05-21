# mgotu_telegram_bot
Телеграм-бот для просмотра расписания каждой группы. Также с доступом к ChatGPT.

## Зависимости

```
aiogram==2.25.1
aiohttp==3.8.4
aiosignal==1.3.1
async-timeout==4.0.2
attrs==23.1.0
Babel==2.9.1
certifi==2023.5.7
charset-normalizer==3.1.0
frozenlist==1.3.3
idna==3.4
magic-filter==1.0.9
multidict==6.0.4
python-dotenv==1.0.0
pytz==2023.3
yarl==1.9.2
```

## Архитектура проекта

```
└── mgotu_telegram_bot/
    ├── handlers/
    │   ├── menu/
    │   │   └── keyboard.py
    │   ├── openai/
    │   │   └── chat_gpt3_5.py
    │   └── schedule/
    │       └── parse_schedule.py
    ├── .gitignore
    ├── main.py
    └── requirements.txt
```

## Установка виртуального окружения

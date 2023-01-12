# chat_join_request_bot

Данный бот позволяет автоматически принимать заявки пользователей в закрытые Telegram-каналы, а сразу после вступления – присылать им сообщения в «личку».

## Документация

Бот написан на библиотеке python-telegram-bot

1. [Документация](https://python-telegram-bot.org/)
2. [python-telegram-bot на GitHub](https://github.com/python-telegram-bot/python-telegram-bot)

## Настройка канала и бота в Telegram

1. Создайте нового бота с помощью бота @BotFather
2. С помощью @BotFather дайте боту возможность администрировать приватные каналы (команда /mybots -> ваш бот -> Bot Settings -> Group Admin Rights)
3. Добавьте бота в канал (канал должен быть приватным)
4. Создайте в настройках канала новый Invite Link (Edit -> Invite Links -> Create a New Link -> необходимо «включить» параметр Request Admin Approval)

## Настройка кода бота

1. Выполните в консоли команды:
```
#клонируем репозиторий:
git clone https://github.com/KhramovKhramov/chat_join_request_bot.git

#создаем виртуальное окружение (пример для MacOS):
python3 -m venv .venv

#активируем виртуальное окружение (пример для MacOS):
source .venv/bin/activate

#устанавливаем зависимости:
pip install -r requirements.txt
```

2. Создайте в корне проекта файл settings.py и добавьте туда следующее:
```
API_KEY = 'API-ключ вашего Telegram-бота, который вам выдал бот BotFather'
```

3. В файле bot.py измените значение переменной message – добавьте туда текст, который бот будет отправлять пользователю. Если будете использовать html-разметку, к аргументам context.bot.send_message добавьте parse_mode='html'.

## Запуск

Запустите команду при активированном виртуальном окружении:
```
python main.py
```
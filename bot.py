import logging

from telegram.ext import Application, ChatJoinRequestHandler

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

app = Application.builder().token(settings.API_KEY).build()


async def aprrove_chat_request(update, context):
    user = update.effective_user  # Получаем данные о пользователе
    await update.chat_join_request.approve()  # Принимаем пользователя в канал
    message = 'Введите текст, который хотите отправить пользователю'
    await context.bot.send_message(
        chat_id=user.id, text=message)  # Отправляем ему сообщение

app.add_handler(ChatJoinRequestHandler(aprrove_chat_request))

if __name__ == '__main__':
    logging.info("Бот стартовал")
    app.run_polling()

from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN, OWNER_ID

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    mention = f"{user.first_name}"
    keyboard = [
        [
            InlineKeyboardButton("Source Code", url=f"https://github.com/Shauryanoobhai/EditGuardianBot"),
            InlineKeyboardButton("Support Chat", url=f"https://t.me/Ahjin_Sprt")
        ],
        [
            InlineKeyboardButton("Add me to group", url=f"https://t.me/LiShiyaBot?startgroup=true")
        ],
        [
            InlineKeyboardButton("Owner", url=f"https://t.me/LeviAckerman1709"),
        ]
    ]

    context.bot.send_photo(chat_id=update.effective_chat.id, photo="https://te.legra.ph/file/5a9550c10d934ff11f7b8.jpg")
    update.message.reply_text(f"Hello! {mention}! I am Edit Guardian bot I delete Edited message", reply_markup=InlineKeyboardMarkup(keyboard))

def check_edit(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    edited_message = update.edited_message
    if not edited_message:
        return  # Ignore if no edited message

    chat_id = edited_message.chat_id
    message_id = edited_message.message_id
    user_id = edited_message.from_user.id
    user_mention = f"{edited_message.from_user.first_name}"
    if user_id == OWNER_ID:
        return  # Ignore if owner edits the message
    # Send a message notifying about the deletion
    bot.send_message(chat_id=chat_id, text=f"{user_mention} just edited a message🤡. I deleted his edited message🙂‍↕️🤡.")
    bot.delete_message(chat_id=chat_id, message_id=message_id)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Start command handler
    dp.add_handler(CommandHandler("start", start))

    # Message edit handler
    dp.add_handler(MessageHandler(Filters.update.edited_message, check_edit))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
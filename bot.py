import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your actual bot token
BOT_TOKEN = '7562589658:AAGuSqJOzLPbpBjRGhMfkduwn6eiZu5QfkE'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    # Welcome message
    welcome_text = (
        "Welcome to Mrjaisal! 🎉🎉🎉\n\n"
        "At Mrjaisal, we are building a decentralized exchange in Telegram, "
        "specializing in trading memecoins and new tokens. We feature a unique "
        "memepad for launching new meme-based projects and incorporate gamified "
        "mechanics to enhance user engagement.\n\n"
        "Here's what you can do with Mrjaisal now:\n"
        "💯 Farm Mrjaisal Points: Play our Drop game to earn Mrjaisal Points (MJ)\n"
        "🤔 Invite Friends: Bring your friends and family for more MJ! More friends = more BPs\n"
        "🥊 Complete Quests: Finish tasks to rack up even more MJ!\n\n"
        "Start farming points now, and who knows what cool stuff you'll snag with them soon! 🚀🚀\n\n"
        "Stay Mrjaisal! 🌟"
    )

    # Buttons
    keyboard = [
        [InlineKeyboardButton("Launch MrJaisal", url="https://arvindjaisal.github.io/mrjaisal")],
        [InlineKeyboardButton("Join community", url="https://t.me/Bitc0inIndia")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with buttons
    await context.bot.send_message(chat_id=chat_id, text=welcome_text, reply_markup=reply_markup)

def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

    # Log that the bot is starting
    logger.info("Bot started. Listening for updates...")

if __name__ == '__main__':
    main()

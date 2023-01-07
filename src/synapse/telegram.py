"""
Don't forget to enable inline mode with @BotFather

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import os
import logging
from html import escape
from uuid import uuid4
from synapse.api.routes.oai import create_completion, clean_completion
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    res = update.message.text
    """Send a message when the command /start is issued."""
    await update.message.reply_text(res)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text
    res = clean_completion(create_completion("text-davinci-003", prompt, temperature=0.5, max_tokens=2000))
    """Send a message when the command /start is issued."""
    await update.message.reply_text(res)

async def codex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text
    res = clean_completion(create_completion("text-davinci-002", prompt, temperature=0.5, max_tokens=2000))
    """Send a message when the command /start is issued."""
    await update.message.reply_text(res)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    msg = f"""
    Puzzled (@pzzldbot)
        An intelligent bot for quickly summarizing content in almost any medium leveraging OpenAI's text-davinci-003 (ChatGPT) engine.
        Additionally, the codex is included as well just less emphasized within the scope of the project.
    ---
    /chatgpt
    /codex
    /start
    /help brings up this message

    """
    await update.message.reply_text(msg)


def bot() -> None:
    """Run the bot."""
    token = os.environ.get("TELOXIDE_TOKEN")
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chatgpt", chatgpt))
    application.add_handler(CommandHandler("codex", codex))
    application.add_handler(CommandHandler("help", help_command))
    

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    bot()

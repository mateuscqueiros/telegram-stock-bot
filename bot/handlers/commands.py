from telegram import Update
from telegram.ext import ContextTypes

from bot.quotes import QuoteError, format_change_percent, format_price, get_quote

HELP_TEXT = (
    "Comandos disponíveis:\n"
    "/start — mensagem de boas-vindas\n"
    "/help — esta ajuda\n"
    "/cotacao TICKER — cotação da B3 (ex: /cotacao PETR4)\n"
    "/alerta TICKER PRECO — alerta quando o preço atingir o limite"
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Olá! Sou o bot de cotações da B3.\n"
        "Use /help para ver os comandos disponíveis."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(HELP_TEXT)


async def cotacao_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Uso: /cotacao TICKER\nExemplo: /cotacao PETR4")
        return

    ticker = context.args[0]
    try:
        quote = await get_quote(ticker)
    except QuoteError as exc:
        await update.message.reply_text(str(exc))
        return

    message = (
        f"*{quote.name}* (`{quote.ticker}`)\n"
        f"Preço: {format_price(quote.price)}\n"
        f"Variação: {format_change_percent(quote.change_percent)}"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

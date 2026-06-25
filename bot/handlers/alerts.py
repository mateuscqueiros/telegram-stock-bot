from dataclasses import dataclass

from telegram import Update
from telegram.ext import ContextTypes

from bot.quotes import QuoteError, format_price, get_quote

# 1 alerta por chat, em memória
_alerts: dict[int, "Alert"] = {}


@dataclass
class Alert:
    chat_id: int
    ticker: str
    target_price: float
    triggered: bool = False


async def alerta_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 2:
        await update.message.reply_text(
            "Uso: /alerta TICKER PRECO\nExemplo: /alerta PETR4 35.00"
        )
        return

    ticker = context.args[0].upper()
    try:
        target_price = float(context.args[1].replace(",", "."))
    except ValueError:
        await update.message.reply_text("Preço inválido. Use um número, ex: 35.00")
        return

    if target_price <= 0:
        await update.message.reply_text("O preço deve ser maior que zero.")
        return

    chat_id = update.effective_chat.id
    _alerts[chat_id] = Alert(chat_id=chat_id, ticker=ticker, target_price=target_price)

    await update.message.reply_text(
        f"Alerta configurado para *{ticker}* quando o preço atingir "
        f"{format_price(target_price)} ou mais.",
        parse_mode="Markdown",
    )


async def check_alerts(context: ContextTypes.DEFAULT_TYPE) -> None:
    for chat_id, alert in list(_alerts.items()):
        if alert.triggered:
            continue

        try:
            quote = await get_quote(alert.ticker)
        except QuoteError:
            continue

        if quote.price >= alert.target_price:
            alert.triggered = True
            await context.bot.send_message(
                chat_id=chat_id,
                text=(
                    f"Alerta disparado!\n"
                    f"*{quote.name}* (`{quote.ticker}`) atingiu "
                    f"{format_price(quote.price)} (limite: {format_price(alert.target_price)})."
                ),
                parse_mode="Markdown",
            )

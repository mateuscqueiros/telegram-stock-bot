import logging

from telegram.ext import Application, CommandHandler

from bot.config import ALERT_INTERVAL_SECONDS, TELEGRAM_TOKEN
from bot.handlers.alerts import alerta_command, check_alerts
from bot.handlers.commands import cotacao_command, help_command, start_command

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("cotacao", cotacao_command))
    application.add_handler(CommandHandler("alerta", alerta_command))

    job_queue = application.job_queue
    if job_queue is not None:
        job_queue.run_repeating(check_alerts, interval=ALERT_INTERVAL_SECONDS, first=10)
    else:
        logger.warning("JobQueue indisponível — alertas periódicos desativados.")

    logger.info("Bot iniciado. Pressione Ctrl+C para parar.")
    application.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()

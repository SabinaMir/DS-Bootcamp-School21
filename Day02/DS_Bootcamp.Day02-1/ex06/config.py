import logging
import config

num_of_steps = 3 
report_template = """
Report

We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tail_fraction}% and {head_fraction}%, respectively.
Our forecast is that in the next {steps} observations we will have: {forecast_tails} tail and {forecast_heads} heads.
"""

# Telegram настройки
telegram_webhook_url = "https://api.telegram.org/bot7531777328:AAHu9QlYOtCtqxDNMXOBx1l03AgFh-Wvwok/sendMessage"
telegram_chat_id = "574376013"

# Логирование
logging.basicConfig(
    filename="analytics.log",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

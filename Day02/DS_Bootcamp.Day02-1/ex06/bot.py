import requests

# Ваш токен бота
BOT_TOKEN = "7531777328:AAHu9QlYOtCtqxDNMXOBx1l03AgFh-Wvwok"

# URL для получения обновлений
url = f"https://api.telegram.org/bot7531777328:AAHu9QlYOtCtqxDNMXOBx1l03AgFh-Wvwok/getUpdates"

# Отправка запроса
response = requests.get(url)
data = response.json()

# Посмотреть chat_id
print(data)

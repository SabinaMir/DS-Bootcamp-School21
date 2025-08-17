import requests
import logging
import config

class Research:
    def __init__(self, filename):
        self.filename = filename
        logging.debug(f"Research initialized with file: {filename}")

    def file_reader(self, has_header=True):
        logging.debug("Reading file.")
        with open(self.filename, "r") as file:
            lines = file.readlines()

        if len(lines) < 2 and has_header:
            logging.error("File must have a header and at least one line of data.")
            raise ValueError("The file must have a header and at least one line of data.")

        if has_header:
            lines = lines[1:]

        data = []
        for line in lines:
            values = line.strip().split(",")
            if len(values) != 2 or not all(value in {"0", "1"} for value in values):
                logging.error("Invalid data format in file.")
                raise ValueError("Data lines must contain exactly two values, each being '0' or '1'.")
            data.append([int(value) for value in values])

        logging.debug(f"File read successfully: {len(data)} lines.")
        return data

    def send_telegram_message(self, message):
        logging.debug("Sending Telegram message.")
        payload = {
            "chat_id": config.telegram_chat_id,
            "text": message,
        }
        response = requests.post(config.telegram_webhook_url, json=payload)

        if response.status_code == 200:
            logging.debug("Telegram message sent successfully.")
        else:
            logging.error(f"Failed to send Telegram message: {response.text}")

class Analytics:
    def __init__(self, data):
        self.data = data
        logging.debug("Analytics initialized.")

    def counts(self):
        logging.debug("Calculating counts.")
        heads = sum(row[0] for row in self.data)
        tails = sum(row[1] for row in self.data)
        logging.debug(f"Counts: Heads={heads}, Tails={tails}")
        return heads, tails

    def fractions(self):
        logging.debug("Calculating fractions.")
        heads, tails = self.counts()
        total = heads + tails
        head_fraction = (heads / total) * 100
        tail_fraction = (tails / total) * 100
        logging.debug(f"Fractions: Heads={head_fraction}%, Tails={tail_fraction}%")
        return round(head_fraction, 2), round(tail_fraction, 2)

    def predict_random(self, num_predictions):
        logging.debug(f"Generating {num_predictions} random predictions.")
        from random import randint
        predictions = []
        for _ in range(num_predictions):
            predictions.append([randint(0, 1), 1 - randint(0, 1)])
        logging.debug(f"Random predictions: {predictions}")
        return predictions

    def save_file(self, data, filename, extension="txt"):
        logging.debug(f"Saving data to file: {filename}.{extension}")
        file_path = f"{filename}.{extension}"
        with open(file_path, "w") as file:
            if isinstance(data, str):
                file.write(data)
            elif isinstance(data, list):
                for item in data:
                    file.write(",".join(map(str, item)) + "\n")
            else:
                logging.error("Unsupported data format for saving.")
                raise ValueError("Data must be a string or a list.")
        logging.debug(f"Data saved to {file_path}.")
        return file_path

import logging
from config import num_of_steps, report_template
from analytics import Research, Analytics


def main():
    file_path = "data.csv"  # Example file path
    try:
        research = Research(file_path)
        data = research.file_reader(has_header=True)

        analytics = Analytics(data)
        heads, tails = analytics.counts()
        head_fraction, tail_fraction = analytics.fractions()

        predictions = analytics.predict_random(num_of_steps)
        forecast_heads = sum(row[0] for row in predictions)
        forecast_tails = sum(row[1] for row in predictions)

        report = report_template.format(
            total=len(data),
            tails=tails,
            heads=heads,
            tail_fraction=tail_fraction,
            head_fraction=head_fraction,
            steps=num_of_steps,
            forecast_tails=forecast_tails,
            forecast_heads=forecast_heads,
        )

        print(report)

        analytics.save_file(report, "report", "txt")
        research.send_telegram_message("The report has been successfully created.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        research.send_telegram_message("The report hasn’t been created due to an error.")


if __name__ == "__main__":
    main()

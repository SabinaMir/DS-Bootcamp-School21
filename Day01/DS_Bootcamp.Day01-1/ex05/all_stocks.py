import sys

def main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # Проверяем, что передан ровно один аргумент
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]

    # Проверка на двойные запятые или запятая с пробелом
    if ',,' in input_string or ', ,' in input_string:
        return

    # Разделяем строку на части
    expressions = input_string.split(',')

    for expr in expressions:
        # Убираем пробелы вокруг выражения и приводим к правильному регистру
        expr = expr.strip()

        if not expr:  # Если выражение пустое, пропускаем
            continue

        # Проверяем, является ли это тикером
        ticker = expr.upper()
        if ticker in STOCKS:
            company_name = get_company_name(ticker, COMPANIES)
            print(f"{ticker} is a ticker symbol for {company_name}")
            continue

        # Проверяем, является ли это названием компании
        company_name = expr.title()
        if company_name in COMPANIES:
            ticker = COMPANIES[company_name]
            price = STOCKS[ticker]
            print(f"{company_name} stock price is {price}")
            continue

        # Если ни то, ни другое
        print(f"{expr} is an unknown company or an unknown ticker symbol")


def get_company_name(ticker, companies):
    """
    Находит название компании по тикеру.
    """
    for company, company_ticker in companies.items():
        if company_ticker == ticker:
            return company
    return None


if __name__ == "__main__":
    main()

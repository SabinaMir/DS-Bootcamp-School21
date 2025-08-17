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

    if len(sys.argv) !=2:  
        return
    ticker = sys.argv[1].upper()
    if ticker in STOCKS:
        company_name = get_company_name(ticker)
        
        price = STOCKS[ticker]
        print(f"{company_name} {price}") 
    else:
        print("Unknown company")

def get_company_name(ticker):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    # Находим название компании, соответствующее тикеру
    for company, company_ticker in COMPANIES.items():
        if company_ticker == ticker:
            return company
    return None        
if __name__== "__main__":
    main()            
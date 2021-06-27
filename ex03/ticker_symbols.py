import sys


def get_ticker_info(ticker):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    companies = {v: k for k, v in companies.items()}
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79, 'NFLX': 416.90,
        'TSLA': 724.88, 'NOK': 3.37
    }

    ticker = ticker.upper()
    try:
        print(companies[ticker], stocks[ticker])
    except KeyError:
        print('Unknown ticker')


def check_argv():
    if len(sys.argv) != 2:
        sys.exit()


def main():
    check_argv()
    get_ticker_info(sys.argv[1])


if __name__ == '__main__':
    main()

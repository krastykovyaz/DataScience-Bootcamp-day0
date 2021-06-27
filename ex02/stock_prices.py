import sys


def get_company(name):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79, 'NFLX': 416.90,
        'TSLA': 724.88, 'NOK': 3.37
    }

    try:
        print(stocks[companies[name.title()]])
    except KeyError:
        print('Unknown company')


def check_argv():
    if len(sys.argv) != 2:
        sys.exit()


def main():
    check_argv()
    get_company(sys.argv[1])


if __name__ == '__main__':
    main()

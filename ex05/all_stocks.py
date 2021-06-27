import sys


def get_info(line):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    rev_companies = {v: k for k, v in companies.items()}
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79, 'NFLX': 416.90,
        'TSLA': 724.88, 'NOK': 3.37
    }
    result_info = []
    for obj in line.split(','):
        obj = obj.strip()
        if not obj:
            return
        if obj.upper() in stocks:
            obj = obj.upper()
            result_info.append(
                f'{obj} is a ticker symbol for {rev_companies[obj]}')
        elif obj.title() in companies:
            obj = obj.title()
            result_info.append(
                f'{obj} stock price is {stocks[companies[obj]]}')
        else:
            result_info.append(
                f'{obj} is an unknown company or an unknown ticker symbol')

    print('\n'.join(result_info))


def check_argv():
    if len(sys.argv) != 2:
        sys.exit()


def main():
    check_argv()
    get_info(sys.argv[1])


if __name__ == '__main__':
    main()

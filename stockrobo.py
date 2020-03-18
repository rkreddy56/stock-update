import sys
import time
import robin_stocks as r
from tabulate import tabulate
import sms
import twilio

# from pprint import pprint


def format_dollar(price):
    return "$ {0}".format(str(price))


def get_movers():
    movers = r.get_top_movers(direction="DOWN")
    return movers


def get_symbol_information(symbol):
    names = r.stocks.get_name_by_symbol(symbol=symbol)
    return names


def get_symbols():
    response = r.options.get_aggregate_positions(info=None)
    symbols = {x["symbol"] for x in response}
    return [get_symbol_information(symbol) for symbol in symbols]


def get_portfolio():
    portfolio = r.profiles.load_portfolio_profile()
    return portfolio


def get_portfolio_status():
    data = get_portfolio()
    print(data["market_value"])
    result = [
        ["Market Value", format_dollar(data["market_value"])],
        ["Equity", format_dollar(data["equity"])],
        [
            "Extended Hours Market Value",
            format_dollar(data["extended_hours_market_value"]),
        ],  # noqa
        ["Extended Hours Equity", format_dollar(data["extended_hours_equity"])],  # noqa
        [
            "Total Balance",
            format_dollar(data["extended_hours_portfolio_equity"]),
        ],  # noqa
    ]
    table = tabulate(result, headers=["Title", "Value"], tablefmt="psql")  # noqa
    return table


def get_stock_status():
    pass


def send_alert():
    data = get_portfolio()
    total = float(data["extended_hours_portfolio_equity"])
    profit = 10000
    if total > profit:
        twilio.send_profitmsg(data["extended_hours_portfolio_equity"])
    elif total < 6000:
        twilio.send_lossmsg(data["extended_hours_portfolio_equity"])

def start():
    symbols = get_symbols()
    portfolio = get_portfolio_status()
    sendsms = send_alert()
    print(portfolio)
    print(sendsms)
    print("\n\n")
    print(f"Symbols Owned: {', '.join(symbols)}")
    print("\n\n")
    print("See you in 15 secs ...")


def main():
    # remove the store_session= false to ignore login everytime
    # login = r.login("rkreddy56@gmail.com", "Warriors_123", store_session=False) 
    login = r.login("rkreddy56@gmail.com", "Warriors_123")
    if not login:
        sys.exit(1)

    while True:
        try:
            start()
            time.sleep(15)
        except KeyboardInterrupt:
            print("\n Thank you for using us...")
            r.logout()
            break


if __name__ == "__main__":
    sys.exit(main())


import json
import os

DATA_FILE = "portfolio.json"


def load_portfolio():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved portfolio. Starting empty.")
    return {}


def save_portfolio(portfolio):
    with open(DATA_FILE, "w") as file:
        json.dump(portfolio, file, indent=4)


def get_number(prompt, minimum=0, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if value < minimum or (not allow_zero and value == 0):
                print("Enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a number.")


def add_stock(portfolio):
    symbol = input("Stock symbol (e.g. AAPL): ").strip().upper()

    if not symbol:
        print("Symbol cannot be empty.")
        return

    name = input("Company name: ").strip()
    if not name:
        print("Company name cannot be empty.")
        return

    shares = get_number("Number of shares: ")
    purchase_price = get_number("Purchase price per share: ")
    current_price = get_number("Current price per share: ", allow_zero=True)

    if symbol in portfolio:
        old = portfolio[symbol]
        total_shares = old["shares"] + shares
        old["purchase_price"] = (
            old["shares"] * old["purchase_price"]
            + shares * purchase_price
        ) / total_shares
        old["shares"] = total_shares
        old["current_price"] = current_price
        old["name"] = name
    else:
        portfolio[symbol] = {
            "name": name,
            "shares": shares,
            "purchase_price": purchase_price,
            "current_price": current_price
        }

    save_portfolio(portfolio)
    print(f"{symbol} added successfully!")


def view_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_invested = 0
    total_value = 0

    print("\n--- YOUR STOCK PORTFOLIO ---")

    for symbol, stock in portfolio.items():
        invested = stock["shares"] * stock["purchase_price"]
        value = stock["shares"] * stock["current_price"]
        profit_loss = value - invested

        total_invested += invested
        total_value += value

        print(f"\n{symbol} - {stock['name']}")
        print(f"Shares: {stock['shares']:g}")
        print(f"Average purchase price: ${stock['purchase_price']:.2f}")
        print(f"Current price: ${stock['current_price']:.2f}")
        print(f"Invested: ${invested:.2f}")
        print(f"Current value: ${value:.2f}")
        print(f"Profit/Loss: ${profit_loss:+.2f}")

    overall = total_value - total_invested

    print("\n--- PORTFOLIO SUMMARY ---")
    print(f"Total invested: ${total_invested:.2f}")
    print(f"Current value: ${total_value:.2f}")
    print(f"Total profit/loss: ${overall:+.2f}")


def update_price(portfolio):
    symbol = input("Enter stock symbol to update: ").strip().upper()

    if symbol not in portfolio:
        print("Stock not found.")
        return

    price = get_number("Enter new current price per share: ", allow_zero=True)
    portfolio[symbol]["current_price"] = price
    save_portfolio(portfolio)
    print(f"{symbol} price updated successfully!")


def remove_stock(portfolio):
    symbol = input("Enter stock symbol to remove: ").strip().upper()

    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"{symbol} removed.")
    else:
        print("Stock not found.")


def main():
    portfolio = load_portfolio()

    while True:
        print("\n=== STOCK PORTFOLIO TRACKER ===")
        print("1. Add stock")
        print("2. View portfolio")
        print("3. Update stock price")
        print("4. Remove stock")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            update_price(portfolio)
        elif choice == "4":
            remove_stock(portfolio)
        elif choice == "5":
            print("Portfolio saved. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()


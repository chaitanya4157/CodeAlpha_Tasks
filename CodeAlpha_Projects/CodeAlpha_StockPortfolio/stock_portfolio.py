stock_prices = {
    "apple": 200,
    "google": 150,
    "tesla": 100,
    "microsoft": 250,
    "amazon": 180
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").lower().strip()

    if stock == "done":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    quantity = input("Enter quantity: ").strip()

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Please enter a valid positive quantity.")
        continue

    quantity = int(quantity)

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    price = stock_prices[stock]
    value = price * quantity

    print(f"{quantity} share(s) of {stock.title()} added.")
    print(f"Price per share: ₹{price}")
    print(f"Investment for this entry: ₹{value}")

print("\nPortfolio Summary")

if not portfolio:
    print("No stocks were added.")
else:
    total_investment = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value

        print(f"\n{stock.title()}")
        print(f"Quantity: {quantity} share(s)")
        print(f"Price per share: ₹{price}")
        print(f"Total value: ₹{value}")

    print(f"\nTotal Investment: ₹{total_investment}")

print("Thank you for using the Stock Portfolio Tracker!")
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0
portfolio = []

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        total_investment += value

        portfolio.append([stock, quantity, stock_prices[stock], value])

        print("Investment value:", value)
    else:
        print("Stock not available.")

# Display result
print("\n----- Portfolio Summary -----")

for item in portfolio:
    print("Stock:", item[0],
          "| Quantity:", item[1],
          "| Price:", item[2],
          "| Value:", item[3])

print("\nTotal Investment Value:", total_investment)

# Save result to CSV file
with open("portfolio.csv", "w") as file:
    file.write("Stock,Quantity,Price,Value\n")

    for item in portfolio:
        file.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")

    file.write(f"Total Investment,,,{total_investment}\n")

print("Portfolio saved to portfolio.csv")

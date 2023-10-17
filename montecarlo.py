import yfinance as yf

# Define your portfolio
portfolio = [
    {'symbol': 'AAPL', 'shares': 10, 'purchase_price': 150.0},
    {'symbol': 'MSFT', 'shares': 15, 'purchase_price': 200.0},
    {'symbol': 'GOOGL', 'shares': 5, 'purchase_price': 2500.0},
]

# Fetch historical data
for stock in portfolio:
    data = yf.download(stock['symbol'], start="2022-01-01", end="2023-01-01")
    stock['data'] = data

# Calculate portfolio metrics
portfolio_value = 0
total_investment = 0

for stock in portfolio:
    stock_data = stock['data']
    current_price = stock_data['Adj Close'][-1]
    stock['current_price'] = current_price
    stock['current_value'] = current_price * stock['shares']
    portfolio_value += stock['current_value']
    total_investment += stock['shares'] * stock['purchase_price']

# Calculate returns
portfolio_return = (portfolio_value - total_investment) / total_investment * 100

# Print portfolio details
for stock in portfolio:
    print(f"Symbol: {stock['symbol']}")
    print(f"Shares: {stock['shares']}")
    print(f"Purchase Price: ${stock['purchase_price']:.2f}")
    print(f"Current Price: ${stock['current_price']:.2f}")
    print(f"Current Value: ${stock['current_value']:.2f}\n")

print(f"Portfolio Value: ${portfolio_value:.2f}")
print(f"Total Investment: ${total_investment:.2f}")
print(f"Portfolio Return: {portfolio_return:.2f}%")



import yfinance as yf
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Data Collection
# Define the stock symbols and date range
stock_symbol1 = "D05.SI"  # Replace with the symbol of the first stock
stock_symbol2 = "C6L.SI"  # Replace with the symbol of the second stock
# start_date = "2022-01-01"  # Replace with your desired start date
# end_date = "2023-10-16"    # Replace with your desired end date
start_date = datetime.datetime.today() - datetime.timedelta(1500)
end_date = datetime.datetime.today()

# Download historical data using yfinance
stock1 = yf.download(stock_symbol1, start=start_date, end=end_date)
stock2 = yf.download(stock_symbol2, start=start_date, end=end_date)

# Step 3: Calculate Daily Returns
stock1['Daily_Return'] = stock1['Adj Close'].pct_change().dropna()
stock2['Daily_Return'] = stock2['Adj Close'].pct_change().dropna()

# Step 4: Correlation Analysis
correlation = stock1['Daily_Return'].corr(stock2['Daily_Return'])

print("Correlation between {} and {} daily returns: {:.2f}".format(stock_symbol1, stock_symbol2, correlation))

# Step 5: Visualization (Optional)
plt.scatter(stock1['Daily_Return'], stock2['Daily_Return'], alpha=0.5)
plt.xlabel('{} Daily Returns'.format(stock_symbol1))
plt.ylabel('{} Daily Returns'.format(stock_symbol2))
plt.title('Correlation Analysis')
plt.show()


# Calculate the correlation matrix between the two stocks
correlation_matrix = pd.concat([stock1['Daily_Return'], stock2['Daily_Return']], axis=1).corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()



# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data in 3D
ax.scatter(stock1['Daily_Return'], stock2['Daily_Return'], [correlation], c='r', marker='o')

# Set labels for the axes
ax.set_xlabel('{} Daily Returns'.format(stock_symbol1))
ax.set_ylabel('{} Daily Returns'.format(stock_symbol2))
ax.set_zlabel('Correlation Coefficient')

# Set the title
ax.set_title('3D Correlation Analysis')

plt.show()


# Step 5: Visualization (3D Plot)
# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data in 3D
ax.scatter(stock1['Daily_Return'], stock2['Daily_Return'], [correlation], c='r', marker='o')

# Set labels for the axes
ax.set_xlabel('{} Daily Returns'.format(stock_symbol1))
ax.set_ylabel('{} Daily Returns'.format(stock_symbol2))
ax.set_zlabel('Correlation Coefficient')

# Set the title
ax.set_title('3D Correlation Analysis')

plt.show()


# Step 5: Visualization (Violin Plot)
# Reshape the data for Seaborn
data = pd.concat([stock1['Daily_Return'], stock2['Daily_Return']], axis=1)
data.columns = [f'{stock_symbol1} Returns', f'{stock_symbol2} Returns']

# Create a violin plot using Seaborn
plt.figure(figsize=(8, 6))
sns.violinplot(data=data, palette="pastel", inner="stick")
plt.title('Violin Plot of Daily Returns')
plt.ylabel('Returns')
plt.show()

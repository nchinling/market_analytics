import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define parameters
initial_investment = 10000  # Initial investment amount
annual_contribution = 2000  # Annual contribution to the portfolio
years = 10                  # Number of years for simulation
num_simulations = 10000      # Number of simulations

# Stock parameters
mean_returns = [0.12, 0.15]  # Mean annual returns of the two stocks
std_devs = [0.2, 0.3]        # Standard deviations of returns
correlation_matrix = [[1.0, 0.6], [0.6, 1.0]]  # Correlation matrix between the two stocks

# Perform Monte Carlo simulation
simulation_results = []

for _ in range(num_simulations):
    portfolio_value = initial_investment
    annual_returns = []

    for year in range(years):
        # Generate correlated random returns for the two stocks
        returns = np.random.multivariate_normal(mean_returns, correlation_matrix)
        portfolio_return = np.sum(returns)

        # Update the portfolio value with returns and contributions
        portfolio_value = portfolio_value * (1 + portfolio_return) + annual_contribution

        annual_returns.append(portfolio_value)

    simulation_results.append(annual_returns)

# Convert the results to a DataFrame
simulation_df = pd.DataFrame(simulation_results).T

# Print the Monte Carlo simulation results
for year in range(years):
    print(f"Year {year + 1} Portfolio Values:")
    print(simulation_df.iloc[year])
    print()

# Plot the Monte Carlo simulation results
plt.figure(figsize=(12, 6))
plt.plot(simulation_df)
plt.xlabel('Years')
plt.ylabel('Portfolio Value')
plt.title('Monte Carlo Simulation of Stock Portfolio')
plt.show()

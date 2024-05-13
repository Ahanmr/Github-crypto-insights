import pandas as pd
import matplotlib.pyplot as plt

# Load data
bittensor_github_stats = pd.read_csv('/path/to/bittensor_github_stats.csv')
bittensor_token_price = pd.read_csv('/path/to/bittensor_token_price.csv')

# Convert date columns to datetime format and set as index
bittensor_github_stats['date'] = pd.to_datetime(bittensor_github_stats['date'])
bittensor_token_price['Date'] = pd.to_datetime(bittensor_token_price['Date'])
bittensor_github_stats.set_index('date', inplace=True)
bittensor_token_price.set_index('Date', inplace=True)

# Merge datasets on date
bittensor_merged = pd.merge(bittensor_github_stats, bittensor_token_price, left_index=True, right_index=True, how='inner')

# Remove potential outliers in token price data
bittensor_filtered = bittensor_merged[bittensor_merged['Close'] > 1]

# Calculate correlation coefficients
correlation = bittensor_filtered[['Cumulative Commits', 'Close']].corr()

# Define timeframe for analysis
end_date = bittensor_filtered.index.max()
short_term = bittensor_filtered.loc[end_date - pd.DateOffset(months=1):]
medium_term = bittensor_filtered.loc[end_date - pd.DateOffset(months=3):]
long_term = bittensor_filtered

# Correlation calculation for different timeframes
short_term_corr = short_term[['Cumulative Commits', 'Close']].corr().iloc[0, 1]
medium_term_corr = medium_term[['Cumulative Commits', 'Close']].corr().iloc[0, 1]
long_term_corr = long_term[['Cumulative Commits', 'Close']].corr().iloc[0, 1]

# Visualization: Scatter Plot
plt.figure(figsize=(12, 6))
plt.scatter(bittensor_filtered['Cumulative Commits'], bittensor_filtered['Close'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Cumulative Commits vs. Closing Token Price')
plt.xlabel('Cumulative Commits')
plt.ylabel('Closing Token Price (USD)')
plt.grid(True)
plt.show()

# Visualization: Line Graphs
fig, ax1 = plt.subplots(figsize=(12, 6))
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Cumulative Commits', color=color)
ax1.plot(bittensor_filtered.index, bittensor_filtered['Cumulative Commits'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Close (USD)', color=color)
ax2.plot(bittensor_filtered.index, bittensor_filtered['Close'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Cumulative Commits and Closing Token Price Over Time')
fig.tight_layout()
plt.show()

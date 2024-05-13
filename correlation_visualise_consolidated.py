import pandas as pd
import matplotlib.pyplot as plt

# Load the data for Fetch.ai, Numerai, and Oraichain
fetchai_github_stats = pd.read_csv('fetchai_github_stats.csv')
fetchai_token_price = pd.read_csv('fetchai_token_price.csv')
numerai_github_stats = pd.read_csv('numerai_github_stats.csv')
numerai_token_price = pd.read_csv('numerai_token_price.csv')
oraichain_github_stats = pd.read_csv('oraichain_github_stats.csv')
oraichain_token_price = pd.read_csv('oraichain_token_price.csv')

# Convert date columns to datetime and set as index
fetchai_github_stats['date'] = pd.to_datetime(fetchai_github_stats['date'])
fetchai_token_price['Date'] = pd.to_datetime(fetchai_token_price['Date'])
numerai_github_stats['date'] = pd.to_datetime(numerai_github_stats['date'])
numerai_token_price['Date'] = pd.to_datetime(numerai_token_price['Date'])
oraichain_github_stats['date'] = pd.to_datetime(oraichain_github_stats['date'])
oraichain_token_price['Date'] = pd.to_datetime(oraichain_token_price['Date'])

fetchai_github_stats.set_index('date', inplace=True)
fetchai_token_price.set_index('Date', inplace=True)
numerai_github_stats.set_index('date', inplace=True)
numerai_token_price.set_index('Date', inplace=True)
oraichain_github_stats.set_index('date', inplace=True)
oraichain_token_price.set_index('Date', inplace=True)

# Merge datasets on date
fetchai_merged = pd.merge(fetchai_github_stats, fetchai_token_price, left_index=True, right_index=True, how='inner')
numerai_merged = pd.merge(numerai_github_stats, numerai_token_price, left_index=True, right_index=True, how='inner')
oraichain_merged = pd.merge(oraichain_github_stats, oraichain_token_price, left_index=True, right_index=True, how='inner')

# Filter to remove potential outliers or irrelevant data points
fetchai_filtered = fetchai_merged[fetchai_merged['Close'] > 0.01]
numerai_filtered = numerai_merged[numerai_merged['Close'] > 0.01]
oraichain_filtered = oraichain_merged[oraichain_merged['Close'] > 0.01]

# Calculate correlations for new projects
fetchai_correlation = fetchai_filtered[['Cumulative Commits', 'Close']].corr().iloc[0, 1]
numerai_correlation = numerai_filtered[['Cumulative Commits', 'Close']].corr().iloc[0, 1]
oraichain_correlation = oraichain_filtered[['Cumulative Commits', 'Close']].corr().iloc[0, 1]

print(fetchai_correlation, numerai_correlation, oraichain_correlation)

# Define a figure for scatter plots for the new projects
plt.figure(figsize=(18, 6))

# Scatter plot for Fetch.ai
plt.subplot(1, 3, 1)
plt.scatter(fetchai_filtered['Cumulative Commits'], fetchai_filtered['Close'], color='purple', alpha=0.5)
plt.title('Fetch.ai Commits vs. Price')
plt.xlabel('Cumulative Commits')
plt.ylabel('Closing Token Price (USD)')

# Scatter plot for Numerai
plt.subplot(1, 3, 2)
plt.scatter(numerai_filtered['Cumulative Commits'], numerai_filtered['Close'], color='orange', alpha=0.5)
plt.title('Numerai Commits vs. Price')
plt.xlabel('Cumulative Commits')
plt.ylabel('Closing Token Price (USD)')

# Scatter plot for Oraichain
plt.subplot(1, 3, 3)
plt.scatter(oraichain_filtered['Cumulative Commits'], oraichain_filtered['Close'], color='teal', alpha=0.5)
plt.title('Oraichain Commits vs. Price')
plt.xlabel('Cumulative Commits')
plt.ylabel('Closing Token Price (USD)')

plt.tight_layout()
plt.show()

# Define a figure for line graphs for the new projects
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))

# Line graph for Fetch.ai
axes[0].plot(fetchai_filtered.index, fetchai_filtered['Cumulative Commits'], color='purple', label='Commits')
axes[0].set_title('Fetch.ai Commits and Price Over Time')
axes[0].set_ylabel('Commits')
ax2 = axes[0].twinx()
ax2.plot(fetchai_filtered.index, fetchai_filtered['Close'], color='purple', linestyle='--', label='Price')
ax2.set_ylabel('Price (USD)')

# Line graph for Numerai
axes[1].plot(numerai_filtered.index, numerai_filtered['Cumulative Commits'], color='orange', label='Commits')
axes[1].set_title('Numerai Commits and Price Over Time')
axes[1].set_ylabel('Commits')
ax2 = axes[1].twinx()
ax2.plot(numerai_filtered.index, numerai_filtered['Close'], color='orange', linestyle='--', label='Price')
ax2.set_ylabel('Price (USD)')

# Line graph for Oraichain
axes[2].plot(oraichain_filtered.index, oraichain_filtered['Cumulative Commits'], color='teal', label='Commits')
axes[2].set_title('Oraichain Commits and Price Over Time')
axes[2].set_ylabel('Commits')
ax2 = axes[2].twinx()
ax2.plot(oraichain_filtered.index, oraichain_filtered['Close'], color='teal', linestyle='--', label='Price')
ax2.set_ylabel('Price (USD)')

plt.tight_layout()
plt.show()

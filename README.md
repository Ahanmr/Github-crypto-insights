# Github-crypto-insights

## Rank Projects by Activity
- Collect data on the number of commits and repositories created for each crypto project.
- Rank the projects based on these metrics and graph the evolution of this ranking over time.

### Markdown Table for Cumulative Commits by Year

| Year | Bittensor | Fetch.ai | Numerai | Ocean Protocol | Oraichain | SingularityNET | Total |
|------|-----------|----------|---------|----------------|-----------|----------------|-------|
| 2011 | -         | -        | 4       | -              | -         | -              | 4     |
| 2014 | -         | 458      | 7       | -              | -         | -              | 465   |
| 2015 | -         | 2140     | 14      | -              | -         | -              | 2154  |
| 2016 | -         | 3599     | 19      | -              | -         | -              | 3618  |
| 2017 | 59        | 10294    | 690     | -              | 2         | 235            | 11280 |
| 2018 | 1420      | 20685    | 1286    | 1648           | 833       | 4256           | 30128 |
| 2019 | 3578      | 29041    | 1486    | 4648           | 1457      | 14107          | 54317 |
| 2020 | 7395      | 38950    | 1856    | 11748          | 3985      | 19581          | 83515 |
| 2021 | 11551     | 43030    | 2320    | 18111          | 9646      | 23677          | 108335|
| 2022 | 16239     | 44062    | 2395    | 27379          | 14076     | 25679          | 129830|
| 2023 | 22746     | 44293    | 2674    | 35545          | 20867     | 26830          | 152955|
| 2024 | 25005     | 44432    | 2731    | 36042          | 22681     | 28134          | 159025|

![Picture 1](./Picture%201.png)


### Markdown Table for Cumulative Repositories by Year

| Year | Bittensor | Fetch.ai | Numerai | Ocean Protocol | Oraichain | SingularityNET | Total |
|------|-----------|----------|---------|----------------|-----------|----------------|-------|
| 2011 | -         | -        | 0       | -              | -         | -              | 0     |
| 2014 | -         | 0        | 0       | -              | -         | -              | 0     |
| 2015 | -         | 0        | 0       | -              | -         | -              | 0     |
| 2016 | -         | 0        | 0       | -              | -         | -              | 0     |
| 2017 | 0         | 0        | 0       | -              | 0         | 2              | 2     |
| 2018 | 0         | 3        | 0       | 9              | 0         | 38             | 50    |
| 2019 | 0         | 15       | 0       | 16             | 0         | 63             | 94    |
| 2020 | 1         | 33       | 8       | 29             | 8         | 78             | 157   |
| 2021 | 3         | 43       | 44      | 37             | 44        | 94             | 265   |
| 2022 | 14        | 50       | 68      | 54             | 68        | 102            | 356   |
| 2023 | 27        | 52       | 110     | 78             | 110       | 115            | 492   |
| 2024 | 31        | 57       | 119     | 81             | 119       | 125            | 532   |

![Picture 1](./Picture%202.png)

## Correlations
- Use statistical methods to determine the correlation between developer activity and project token price.
- Analyze the correlation in different timeframes (short-term, medium-term, long-term) to understand if phases of high or low activity impact token price.

| Project        | Correlation Coefficient | Analysis                                                                                     |
|----------------|-------------------------|----------------------------------------------------------------------------------------------|
| Bittensor      | 0.81                    | Strong positive correlation, indicating higher developer activity generally leads to higher token prices. |
| Ocean Protocol | 0.26                    | Weak positive correlation, suggesting some level of association between developer activity and token prices. |
| SingularityNET | 0.40                    | Moderate positive correlation, developer activity somewhat influences token prices.         |
| Fetch.ai       | 0.38                    | Moderate positive correlation, similar to SingularityNET in developer influence on token prices. |
| Numerai        | 0.26                    | Weak positive correlation, minimal but noticeable effect of developer activity on token prices. |
| Oraichain      | -0.49                   | Moderate negative correlation, increased developer activity might lead to lower token prices, suggesting potential overvaluation concerns during high activity phases. |


### Bittensor
The data for Bittensor consists of:
* GitHub Stats: Tracks cumulative commits over time. It appears that the "Cumulative Repos" column may contain missing values.
* Token Price: Includes open, high, low, close, adjusted close prices, and volume for each day.

The merged dataset for Bittensor includes both the cumulative commits and token prices (open, high, low, close, adjusted close, volume). However, there's a noticeable issue with the token price data on March 5, 2023, where the price significantly diverges from subsequent days. This could be a data error or anomaly. It appears that there is a very low close price (0.126083) on March 5, 2023, which is significantly different from the other prices that start from around 34 and go up to several hundred. This anomalous value may skew our correlation analysis if left unaddressed.

1. Address any data errors or inconsistencies, particularly in the token price.
2.Calculate the correlation between the cumulative commits and the token prices (specifically, the daily closing price as a general representative of the token's value).
3. Explore the correlation in different timeframes (short-term, medium-term, long-term).

The Pearson correlation coefficient between cumulative commits and the closing price of the token for Bittensor is approximately 0.81. This indicates a strong positive correlation, suggesting that as developer activity (measured by cumulative commits) increases, the token price tends to increase as well.

Next, we can analyze the correlation in different timeframes:

1. Short-term: Last 1 month
2. Medium-term: Last 3 months
3. Long-term: Entire dataset timeframe

Here are the correlation coefficients between cumulative commits and closing token price across different timeframes for Bittensor:

1. Short-term (Last 1 month): −0.86
2. Medium-term (Last 3 months): −0.68
3. Long-term: 0.81

These results suggest:
1. In the long-term, there is a strong positive correlation, indicating that higher developer activity is generally associated with higher token prices over extended periods.
2. In contrast, in the short-term and medium-term, there is a strong negative correlation, which suggests that recent increases in developer activity might coincide with decreases in token price or vice versa.

This contrasting behavior could be due to various factors, including market reactions to immediate news or developments, which might not reflect the underlying value driven by cumulative development activity. Other external factors could also be influencing these prices in the shorter frames.

### OCEAN Protocol


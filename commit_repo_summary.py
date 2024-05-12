import pandas as pd
import json
import matplotlib.pyplot as plt

input_token_file = "singularitynet_token_price.csv"
output_file = "singularitynet_github_stats.csv"
file_path = 'singularitynet_commits.json'
csv_file_path = 'commit_summary_singularitynet.csv' #csv generate
repos_file_path = 'singularitynet_repos.json'

# Loading the token price data
token_price_data = pd.read_csv(input_token_file)

# Display the first few rows of the dataframe
token_price_data.head()

# Open the JSON file and load the data
with open(file_path, 'r') as file:
    commits_data = json.load(file)

# Normalize the data to create a flat pandas DataFrame
commits_df = pd.json_normalize(commits_data)

# Show the structure of the new DataFrame
commits_df.info(), commits_df.head()

# Correctly iterate over the nested list structure and extract commit details
commit_list = []

# Read data from file again in case of any read errors previously
with open(file_path, 'r') as file:
    data = json.load(file)

# # Re-examine how to access nested lists of commits
# for commit_batch in data:
#     for commit in commit_batch:
#         if commit is not None:  # Check to avoid any None values that could cause errors
#             commit_details = {
#                 'sha': commit['sha'],
#                 'author_name': commit['commit']['author']['name'],
#                 'author_email': commit['commit']['author']['email'],
#                 'date': commit['commit']['author']['date'],
#                 'message': commit['commit']['message'],
#                 'committer_name': commit['commit']['committer']['name'],
#                 'committer_email': commit['commit']['committer']['email'],
#                 'committer_date': commit['commit']['committer']['date']
#             }
#             commit_list.append(commit_details)
#         else:
#             continue

commit_list = []  # Assuming this is defined somewhere in your code as an empty list

# Re-examine how to access nested lists of commits
for commit_batch in data:
    if isinstance(commit_batch, list):  # Ensure the commit_batch is a list
        for commit in commit_batch:
            if isinstance(commit, dict):  # Check if commit is indeed a dictionary
                try:
                    commit_details = {
                        'sha': commit['sha'],
                        'author_name': commit['commit']['author']['name'],
                        'author_email': commit['commit']['author']['email'],
                        'date': commit['commit']['author']['date'],
                        'message': commit['commit']['message'],
                        'committer_name': commit['commit']['committer']['name'],
                        'committer_email': commit['commit']['committer']['email'],
                        'committer_date': commit['commit']['committer']['date']
                    }
                    commit_list.append(commit_details)
                except KeyError as e:
                    print(f"Missing key in commit data: {e}")
                except TypeError as e:
                    print(f"Type error in commit data processing: {e}, commit data: {commit}")
            else:
                print(f"Warning: Expected a dictionary for commit but found {type(commit)}")
    else:
        print(f"Warning: Expected a list for commit_batch but found {type(commit_batch)}")


# Create a DataFrame from the list of dictionaries
commits_df = pd.DataFrame(commit_list)

# Convert 'date' and 'committer_date' to datetime for easier analysis
commits_df['date'] = pd.to_datetime(commits_df['date'])
commits_df['committer_date'] = pd.to_datetime(commits_df['committer_date'])

commits_df.info(), commits_df.head()

# Group by date and count the number of commits per day
commits_per_day = commits_df.groupby(commits_df['date'].dt.date).size()

# Display the number of commits per day
commits_per_day
# Group by date and get unique committers per day
active_committers_per_day = commits_df.groupby(commits_df['date'].dt.date)['committer_email'].nunique()

# Display the number of active committers per day
active_committers_per_day

# Combine the commits per day and active committers per day into one DataFrame
summary_df = pd.DataFrame({
    'Commits': commits_per_day,
    'Active Committers': active_committers_per_day
}).reset_index()

# Join with additional attributes from the original data (using the most common values for simplicity)
additional_attributes = commits_df.groupby(commits_df['date'].dt.date).agg({
    'author_name': pd.Series.mode,
    'committer_name': pd.Series.mode,
    'message': pd.Series.mode
}).reset_index()

# Convert the 'date' column in both DataFrames to datetime to ensure compatibility
summary_df['date'] = pd.to_datetime(summary_df['date'])
additional_attributes['date'] = pd.to_datetime(additional_attributes['date'])


# Merge the summary with additional attributes correctly using the 'date' column
summary_df = pd.merge(summary_df, additional_attributes, left_on='date', right_on='date', how='left')

# Save to CSV
# csv_file_path = 'commit_summary_numerai.csv'
summary_df.to_csv(csv_file_path, index=False)

summary_df.head(), csv_file_path

# Load the JSON file containing repository data
repos_data = pd.read_json(repos_file_path)

# Display the first few rows of the DataFrame to understand its structure
repos_data.head()

# Convert the 'created_at' column to datetime and count the number of repositories created by date
repos_data['created_at'] = pd.to_datetime(repos_data['created_at'])
repos_count_by_date = repos_data.groupby(repos_data['created_at'].dt.date).size()

# Display the counts of repositories created by date
repos_count_by_date

# Calculate the total number of commits from the commit summary data
total_commits = summary_df['Commits'].sum()

# Calculate the total number of repositories created from the repository data
total_repositories = repos_data.shape[0]

print(total_commits, total_repositories)


# Preparing data for repositories created over time
repos_data['created_at'] = pd.to_datetime(repos_data['created_at']).dt.date
repo_creation_counts = repos_data['created_at'].value_counts().sort_index().cumsum()


# Convert the repo_creation_counts to a DataFrame for easier merging
repo_creation_df = repo_creation_counts.reset_index()
repo_creation_df.columns = ['date', 'Cumulative Repos']
repo_creation_df['date'] = pd.to_datetime(repo_creation_df['date'])

# Calculate the cumulative sum of commits over time
summary_df['Cumulative Commits'] = summary_df['Commits'].cumsum()

# Merge the cumulative commits and cumulative repositories data on date
combined_data = pd.merge(summary_df[['date', 'Cumulative Commits']], repo_creation_df, on='date', how='outer')
combined_data.sort_values('date', inplace=True)
combined_data.fillna(method='ffill', inplace=True)  # Forward fill to handle days with no new data

# Plotting the combined data
plt.figure(figsize=(14, 7))
plt.plot(combined_data['date'], combined_data['Cumulative Commits'], marker='o', linestyle='-', label='Cumulative Commits')
plt.plot(combined_data['date'], combined_data['Cumulative Repos'], marker='o', linestyle='-', label='Cumulative Repositories')
plt.title('Cumulative Commits and Repositories Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Count')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

combined_data.to_csv(output_file, index=False)
import json
import pandas as pd

# Load JSON data from a file
def load_commit_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Flatten the data and create a DataFrame
def process_commit_data(data):
    # Initialize lists to store extracted information
    commits = []

    # Extract relevant data from each commit
    for batch in data:  # Assuming data might be nested
        for commit in batch:
            commit_info = {
                'sha': commit['sha'],
                'author': commit['commit']['author']['name'],
                'email': commit['commit']['author']['email'],
                'date': pd.to_datetime(commit['commit']['author']['date']),
                'message': commit['commit']['message'],
                'url': commit['html_url'],
                'repo_name': commit['url'].split('/')[-4],  # Extracts repository name from the URL
                'verified': commit['commit']['verification']['verified']
            }
            commits.append(commit_info)
    
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(commits)
    return df

# Analyze the DataFrame to find the most active contributors by year
def analyze_contributors(df):
    # Extract year from date and create a new column
    df['year'] = df['date'].dt.year

    # Group by year and author to count the number of commits
    contributor_counts = df.groupby(['year', 'author']).size().reset_index(name='commit_count')
    
    # Sort contributors by year and the number of commits in descending order
    sorted_contributors = contributor_counts.sort_values(by=['year', 'commit_count'], ascending=[True, False])
    
    # Return top contributors per year
    top_contributors_per_year = sorted_contributors.groupby('year').head(5)
    return top_contributors_per_year

# Main function to load, process, and analyze commit data
def main(file_path):
    data = load_commit_data(file_path)
    df = process_commit_data(data)
    top_contributors_per_year = analyze_contributors(df)
    print(top_contributors_per_year)
    top_contributors_per_year.to_csv("top_10_contributors_yearwise-fetchai.csv", index=False)

# Specify the path to your JSON file
file_path = 'fetchai_commits.json'
main(file_path)

import json

def extract_repo_commit_counts(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Dictionary to hold repository names and commit counts
    repo_commit_counts = {}
    
    # Loop through each commit in the data
    for commit_batch in data:
        for commit in commit_batch:
            # Extract the repository URL from the commit information
            repo_url = commit['url']

            # Extract the repository name using the URL
            # Assuming the URL format is 'https://api.github.com/repos/{owner}/{repo}/commits/{sha}'
            repo_name = repo_url.split("/")[5]  # This indexes directly to the repo name in the URL split parts

            # Increase the count of commits for the found repository name
            if repo_name in repo_commit_counts:
                repo_commit_counts[repo_name] += 1
            else:
                repo_commit_counts[repo_name] = 1
    
    return repo_commit_counts

# Path to the JSON file containing commits
json_file_path = 'numerai_commits.json'
repo_commit_counts = extract_repo_commit_counts(json_file_path)
print(repo_commit_counts)

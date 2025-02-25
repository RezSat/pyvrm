import os
import subprocess
import random
from datetime import datetime, timedelta

# Configuration
repo_path = "."  # Current directory (repo)
start_date = datetime(2025, 1, 1)  # Start date (Jan 1, 2025)
end_date = datetime.now()          # Current date
file_name = "backdated_file.txt"   # File to modify
num_commits = 50                   # Adjust the number of commits
remote_name = "origin"             # Your GitHub remote name (default: origin)
branch_name = "main"               # Change to the branch you want to push to

# Change directory to the repo
os.chdir(repo_path)

for i in range(num_commits):
    # Generate a random date between start_date and end_date
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    
    # Format the date for Git
    formatted_date = random_date.strftime('%Y-%m-%dT%H:%M:%S')

    # Modify the file
    with open(file_name, "a") as f:
        f.write(f"Backdated commit {i+1} on {formatted_date}\n")

    # Stage and commit with a backdated timestamp
    env = {
        "GIT_AUTHOR_DATE": f"{formatted_date} +0000",
        "GIT_COMMITTER_DATE": f"{formatted_date} +0000"
    }
    
    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "-m", f"Backdated commit {i+1} on {formatted_date}"], env=env)
    
    # Push each commit immediately
    subprocess.run(["git", "push", remote_name, branch_name])

print("Backdating and pushing completed successfully!")


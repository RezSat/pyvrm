import os
import subprocess
import random
from datetime import datetime, timedelta

# Configuration
repo_path = "."  # Current directory (repo)
start_date = datetime(2025, 2, 25)  # Start date (Jan 1, 2025)
end_date = datetime.now()          # Current date
file_name = "backdated_file.txt"   # File to modify
num_commits = 300                   # Adjust the number of commits
remote_name = "origin"             # Your GitHub remote name (default: origin)
branch_name = "main"               # Change to the branch you want to push to
user_name = "Yehan Wasura"            # Set your name
user_email = "yehantest@gmail.com"     # Set your email

# Change directory to the repo
os.chdir(repo_path)

# Set git identity (this avoids the "Author identity unknown" error)
subprocess.run(["git", "config", "user.name", user_name])
subprocess.run(["git", "config", "user.email", user_email])

# Create a list of all the dates in the range [start_date, end_date]
date_range = []
current_date = start_date
while current_date <= end_date:
    date_range.append(current_date)
    current_date += timedelta(days=1)

# Ensure every date has at least 10 commits
for date in date_range:
    if random.random() > 0.6:
        for _ in range(random.randrange(20,40)):  # 10 commits per day
            formatted_date = date.strftime('%Y-%m-%dT%H:%M:%S')
        
            # Modify the file
            with open(file_name, "a") as f:
                f.write(f"Backdated commit on {formatted_date}\n")
        
            # Stage and commit with a backdated timestamp
            env = {
                "GIT_AUTHOR_DATE": f"{formatted_date} +0000",
                "GIT_COMMITTER_DATE": f"{formatted_date} +0000"
            }
        
            subprocess.run(["git", "add", file_name])
            subprocess.run(["git", "commit", "-m", f"Backdated commit on {formatted_date}"], env=env)
    
        # Push each commit immediately (after each date is filled)
        subprocess.run(["git", "push", remote_name, branch_name])

# Now handle the random additional commits after the end datei
'''
for i in range(num_commits):
    # Generate a random date between start_date and end_date
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - datetime(2024, 2, 2)).total_seconds()))
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

'''
'''
remaining_commits = num_commits - (len(date_range) * 10)
if remaining_commits > 0:
    for _ in range(remaining_commits):
        # Randomly pick a date in the future (after the end_date)
        random_future_date = end_date + timedelta(days=random.randint(1, 365))
        formatted_date = random_future_date.strftime('%Y-%m-%dT%H:%M:%S')

        # Modify the file
        with open(file_name, "a") as f:
            f.write(f"Backdated commit on {formatted_date}\n")
        
        # Stage and commit with a backdated timestamp
        env = {
            "GIT_AUTHOR_DATE": f"{formatted_date} +0000",
            "GIT_COMMITTER_DATE": f"{formatted_date} +0000"
        }
        
        subprocess.run(["git", "add", file_name])
        subprocess.run(["git", "commit", "-m", f"Backdated commit on {formatted_date}"], env=env)

        # Push each commit immediately
        subprocess.run(["git", "push", remote_name, branch_name])
'''
print("Backdating and pushing completed successfully!")



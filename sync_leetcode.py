import requests
import os
import json

# Ensure solutions directory exists
if not os.path.exists("solutions"):
    os.makedirs("solutions")

# Get session cookie from environment variable
session_cookie = os.getenv("LEETCODE_SESSION")
cookies = {"LEETCODE_SESSION": session_cookie}
headers = {"Referer": "https://leetcode.com/"}

# Fetch submissions
url = "https://leetcode.com/api/submissions/?offset=0&limit=20"
response = requests.get(url, headers=headers, cookies=cookies)
submissions = response.json().get("submissions_dump", [])
print(f"Fetched submissions: {submissions}")

# Save accepted solutions
for submission in submissions:
    if submission["status_display"] == "Accepted":
        title = submission["title_slug"]  # Use title_slug for cleaner filenames
        code = submission["code"]
        with open(f"solutions/{title}.py", "w") as f:
            f.write(code)
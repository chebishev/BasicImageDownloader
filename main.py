import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check your env file for BASE_URL and NUMBER_OF_FILES
base_url = os.getenv("BASE_URL")
start_num = 1
end_num = int(os.getenv("NUMBER_OF_FILES", 2))  # Default to 2 if not set
# Be sure that FIRST_FILE_NAME is set in your .env file
first_file_name = os.getenv("FIRST_FILE_NAME")
file_extension = os.getenv("FILE_EXTENSION")

for i in range(start_num, end_num + 1):
    # first image has no number at the end
    if i == 1:
        url = f"{base_url}"
        filename = first_file_name + file_extension
    else:
        url = f"{base_url}"
        filename = f"{first_file_name}{i}{file_extension}"

    print(f"Downloading {url}...")
    response = requests.get(url + filename)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Saved as {filename}")
    else:
        print(f"Failed to download {url}")

print("Done!")

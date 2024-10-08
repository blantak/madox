import requests
import os
import subprocess
import sys
#updated
def download_file(github_url, token):
    # Set up the headers with the token for authentication
    headers = {
        'Authorization': f'token {token}'  # Use 'token' prefix for GitHub tokens
    }

    # Send a GET request to the GitHub raw file URL
    response = requests.get(github_url, headers=headers, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        filename = os.path.basename(github_url)  # Extract filename from URL

        # Save the file
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File '{filename}' downloaded successfully.")
        return filename  # Return the downloaded filename
    else:
        print(f"Failed to download file: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    # Replace this URL with the raw file URL from your private GitHub repository
    github_file_url = "https://raw.githubusercontent.com/blantak/madox/main/tada.py"  # Updated URL format

    # Hardcoded personal access token
    token = "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"  # Replace with your actual token

    # Download the file and get its path
    downloaded_file_path = download_file(github_file_url, token)
    
    if downloaded_file_path:
        # Call the helper script to delete this script and rename the downloaded file
        subprocess.run([sys.executable, "helper.py", downloaded_file_path])

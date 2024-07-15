import boto3
from pathlib import Path
import os  # For environment variable access

# Replace with your bucket name and file key
bucket_name = "lpfiles17"
file_key = "House Price India.csv"

# Get AWS credentials securely from environment variables (recommended)
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Error handling for missing credentials
if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    print("Error: Missing AWS credentials in environment variables. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.")
    exit(1)

# Create S3 client
s3 = boto3.client('s3')

# Local download path (modify as needed)
local_path = Path("artificr", "dataingecation", file_key)

# Create the directory structure if it doesn't exist
local_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed

# Download the file with error handling
try:
  s3.download_file(bucket_name, file_key, str(local_path))
  print("File downloaded successfully!")
except Exception as e:
  print(f"Error downloading file: {e}")

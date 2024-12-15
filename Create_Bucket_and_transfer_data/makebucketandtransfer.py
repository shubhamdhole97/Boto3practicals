import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# AWS session setup with access key, secret access key, and region
session = boto3.session.Session(profile_name='default')

# Create an S3 client
s3 = session.client('s3')

# Bucket name
bucket_name = 'bucket1512'

# Function to create an S3 bucket in us-east-1
def create_bucket(bucket_name):
    try:
        # For us-east-1, the CreateBucketConfiguration is not required
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully in us-east-1.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

# Function to upload a file to the S3 bucket
def upload_file(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name
    
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded as '{object_name}' to bucket '{bucket_name}'.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"Error uploading file: {e}")

# Create the bucket and upload the file
if __name__ == "__main__":
    create_bucket(bucket_name)
    upload_file('xyz.txt', bucket_name, 'xyz1.txt')

import boto3
import os

# IAM Credentials
access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']



# Create a boto3 session using IAM user's access key and secret key
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1'
)

# Create an EC2 client using the session
ec2_client = session.client('ec2')

# Check the status of all EC2 instances
response = ec2_client.describe_instances()
# Loop through all instances and check if they are running
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            print(f"Instance {instance['InstanceId']} is running")
        else:
            print(f"Instance {instance['InstanceId']} is not running")

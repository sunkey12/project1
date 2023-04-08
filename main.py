import boto3

# IAM Credentials
access_key = 'AKIAWNVPEYV5ZXT4HVPW'
secret_key = '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'


# Region
#REGION = 'eu-west-1'
#region = 'eu-west-1'

import boto3

# Create a boto3 session using IAM user's access key and secret key
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='eu-west-1'
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

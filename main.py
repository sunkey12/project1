import boto3

# IAM Credentials
access_key = $AWS_ACCESS_KEY_ID
secret_key = $AWS_SECRET_ACCESS_KEY


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
        if instance['State']['Name'] == 'stopped':
            print(f"Instance {instance['InstanceId']} is stopped")
        else:
            print(f"Instance {instance['InstanceId']} is not stopped")

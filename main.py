import boto3
import os

# IAM Credentials
#  access_key = $AWS_ACCESS_KEY_ID
#  secret_key = $AWS_SECRET_ACCESS_KEY

access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']

print(access_key)

# Create a boto3 session using IAM user's access key and secret key
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='eu-west-1'
)
print("1")
# Create an EC2 client using the session
ec2_client = session.client('ec2')

# Check the status of all EC2 instances
response = ec2_client.describe_instances()
print("2')
# Loop through all instances and check if they are running
for reservation in response['Reservations']:
      print("3")
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'stopped':
            print(f"Instance {instance['InstanceId']} is stopped")
        else:
            print(f"Instance {instance['InstanceId']} is not stopped")

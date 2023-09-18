import boto3

# Declare profile name
session = boto3.Session(profile_name='leveluptech')

# Initialize the SNS client
sns = session.client('sns', region_name='us-east-1')  # Specify your AWS region here

# Define the SNS topic name
topic_name = 'customer_order_tracker'

# Create the SNS topic
response = sns.create_topic(Name=topic_name)

# Print the ARN of the newly created SNS topic
print("SNS topic created with ARN:", response['TopicArn'])

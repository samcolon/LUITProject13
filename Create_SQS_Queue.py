import boto3

# Declare profile name
session = boto3.Session(profile_name='leveluptech')

# Initialize the SQS client
sqs = session.client('sqs')

# Define the queue name
queue_name = 'customer_order_tracker'

# Create the SQS queue
response = sqs.create_queue(QueueName=queue_name)

# Print the URL of the newly created queue
print("SQS queue created with URL:", response['QueueUrl'])


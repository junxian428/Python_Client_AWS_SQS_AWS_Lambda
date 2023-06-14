import boto3
import json

def send_message_to_sqs():
    # Set up the SQS client with the AWS region
    sqs_client = boto3.client('sqs', region_name='')
    queue_url = 'https://'  # Replace with the URL of your SQS queue

    # Prepare your message payload as a Python dictionary
    message = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'from PC'
    }

    # Send the message to the SQS queue
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    print('Message sent to SQS queue.')

# Invoke the function to send the message
send_message_to_sqs()

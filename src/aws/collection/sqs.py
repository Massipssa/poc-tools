import boto3
import time
import os

# Replace with your AWS credentials and region
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = 'YOUR_REGION'
queue_url = 'YOUR_QUEUE_URL'

sqs_client = boto3.client('sqs',
                          region_name=region_name,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)


def send_message(message_body):
    sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)


def read_message():
    while True:
        response = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
        # Check if there are any messages
        if 'Messages' in response:
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            print(f"Received message: {message['Body']}")
            # Delete the message from the queue
            sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)

        # Add a delay before polling the queue again (optional)
        time.sleep(2)


if __name__ == '__main__':
    test_message = "Hello SQS"
    send_message(test_message)
    read_message()

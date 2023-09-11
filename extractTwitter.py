import boto3
import tweepy
import json

# Declare aws keys to push data into AWS kinesis
aws_access_key_id = 'XXXXXXXXXXXXXXXXXXXXX'
aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXX'

# Declare Twitter API keys to extract data
api_key = 'XXXXXXXXXXXXXXXXXXXXX'
api_key_secret = 'XXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXX'

def extractTwitter():
    #Authorization of API key and api secret
    auth = tweepy.OAuthHandler(api_key, api_key_secret)

    #Set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    #Calling the api
    api = tweepy.API(auth)

    #Extract the users by screen_names
    users = api.lookup_users(screen_name=['elonmusk'])

    #Convert to Json
    for user in users:
        user_json = json.dumps(user._json)
    return user_json

def pushKinesis():
    #Replace this with your Kinesis stream name
    stream_name = 'google-colab'

    # Initialize the Kinesis client
    kinesis_client = boto3.client(
        'kinesis',
        region_name='ap-south-1',  # Replace with your desired AWS region
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Data to be sent to the Kinesis stream
    data = extractTwitter()

    # Put the data into the Kinesis stream
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=data,
        PartitionKey='1'
    )

    # Print the response
    print("Data sent successfully. Response:", response)

if __name__ == '__main__':
    pushKinesis()

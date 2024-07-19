from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import os.path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# Use the refreshed credentials for your API requests


# Scopes for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Function to fetch detailed email data for each id
def fetch_email_data(service, message_id):
    email = service.users().messages().get(userId='me', id=message_id).execute()

    return email


# Load the JSON data
json_data = '''{
    "messages": [
        {
            "id": "190c48cdd9ef77ea",
            "threadId": "190c48cdd9ef77ea"
        },
        {
            "id": "190c48b7d926b3f7",
            "threadId": "190c48b7d926b3f7"
        },
        {
            "id": "190be1f7842b6ac2",
            "threadId": "190be1f7842b6ac2"
        },
        {
            "id": "190bbf97bb17a179",
            "threadId": "190bbf97bb17a179"
        },
        {
            "id": "190b671e371e9d67",
            "threadId": "190b671e371e9d67"
        },
        {
            "id": "1908de1dac0d54c9",
            "threadId": "1908de1dac0d54c9"
        },
        {
            "id": "19063f17d318c9bd",
            "threadId": "19063f17d318c9bd"
        },
        {
            "id": "1903936ede0f2dbc",
            "threadId": "1903936ede0f2dbc"
        },
        {
            "id": "1900ddf6854d5a4d",
            "threadId": "1900ddf6854d5a4d"
        },
        {
            "id": "18fe2a4275cdb24c",
            "threadId": "18fe2a4275cdb24c"
        },
        {
            "id": "18fb611ea0a4cbda",
            "threadId": "18fb611ea0a4cbda"
        },
        {
            "id": "18fa0c872cfed249",
            "threadId": "18fa0c872cfed249"
        }
        ],
    "nextPageToken": "02737309315071802819",
    "resultSizeEstimate": 201
}'''
# Parse the JSON data
data = json.loads(json_data)

# Collect the message ids
ids = [message['id'] for message in data['messages']]

# Obtain OAuth 2.0 credentials and authorize the client
creds = None
token_path = 'token.json'
credentials_path = 'credentials.json'

if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

# Build the Gmail service
service = build('gmail', 'v1', credentials=creds)

# Fetch detailed data for each message id
detailed_emails = []
for message_id in ids:
    email_data = fetch_email_data(service, message_id)


# Print or process the detailed email data
for email in detailed_emails:
    print(json.dumps(email, indent=2))  # Pretty-print the email data



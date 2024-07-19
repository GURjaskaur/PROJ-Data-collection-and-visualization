from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import os.path
from datetime import datetime
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz

# Scopes for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Function to fetch detailed email data for each id
def fetch_email_data(service, message_id):
    email = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    return email

# Function to extract the date and day of the week from email headers
def get_email_date(email_data):
    headers = email_data['payload']['headers']
    for header in headers:
        if header['name'] == 'Date':
            date_str = header['value']
            parsed_date = parsedate_tz(date_str)
            if parsed_date:
                timestamp = mktime_tz(parsed_date)
                email_date = datetime.fromtimestamp(timestamp)
                return email_date.strftime('%Y-%m-%d'), email_date.strftime('%A')
    return None, None

# Load the JSON data
json_data = '''{
    "messages": [
        {
            "id": "18acd762da05b17c",
            "threadId": "18acd762da05b17c"
        },
        {
            "id": "18aa2d3c093362b0",
            "threadId": "18aa2d3c093362b0"
        },
        {
            "id": "18a889cf9bad06c1",
            "threadId": "18a889cf9bad06c1"
        },
        {
            "id": "18a761e7583fffbf",
            "threadId": "18a761e7583fffbf"
        },
        {
            "id": "18a69e895a9a1bee",
            "threadId": "18a69e895a9a1bee"
        },
        {
            "id": "18a51020e5ba2004",
            "threadId": "18a51020e5ba2004"
        },
        {
            "id": "18a47a066b687aee",
            "threadId": "18a47a066b687aee"
        },
        {
            "id": "18a2c64eef890917",
            "threadId": "18a2c64eef890917"
        },
        {
            "id": "18a2127aa7e99acf",
            "threadId": "18a2127aa7e99acf"
        },
        {
            "id": "18a1b716077c6d7c",
            "threadId": "18a1b716077c6d7c"
        },
        {
            "id": "189ff5b17b218b96",
            "threadId": "189ff5b17b218b96"
        },
        {
            "id": "189ef7f44064d322",
            "threadId": "189ef7f44064d322"
        },
        {
            "id": "189c5de8baf2ba87",
            "threadId": "189c5de8baf2ba87"
        },
        {
            "id": "18998ad98f5feb4c",
            "threadId": "18998ad98f5feb4c"
        },
        {
            "id": "18969d11384746af",
            "threadId": "18969d11384746af"
        },
        {
            "id": "1894f6aed9ef23c8",
            "threadId": "1894f6aed9ef23c8"
        },
        {
            "id": "1893c550b2aea45a",
            "threadId": "1893c550b2aea45a"
        },
        {
            "id": "18910c20307dce92",
            "threadId": "18910c20307dce92"
        },
        {
            "id": "188e6e79495384b4",
            "threadId": "188e6e79495384b4"
        },
        {
            "id": "188c9bf5fd710021",
            "threadId": "188c9bf5fd710021"
        },
        {
            "id": "1887c0f75f763263",
            "threadId": "1887c0f75f763263"
        },
        {
            "id": "188238995a78192f",
            "threadId": "188238995a78192f"
        },
        {
            "id": "18805107fafb8e84",
            "threadId": "18805107fafb8e84"
        },
        {
            "id": "187e0b615722487f",
            "threadId": "187e0b615722487f"
        },
        {
            "id": "187b45fd717ce9e9",
            "threadId": "187b45fd717ce9e9"
        },
        {
            "id": "187a463cc30dda40",
            "threadId": "187a463cc30dda40"
        },
        {
            "id": "18785634ab9b2f67",
            "threadId": "18785634ab9b2f67"
        },
        {
            "id": "1875a2a0a215b8f8",
            "threadId": "1875a2a0a215b8f8"
        },
        {
            "id": "1872cf9f8be074cd",
            "threadId": "1872cf9f8be074cd"
        },
        {
            "id": "186ffb4ba757afec",
            "threadId": "186ffb4ba757afec"
        },
        {
            "id": "186d47d32279c570",
            "threadId": "186d47d32279c570"
        },
        {
            "id": "186a91e935ae1f69",
            "threadId": "186a91e935ae1f69"
        },
        {
            "id": "186a1c030cda840b",
            "threadId": "186a1c030cda840b"
        },
        {
            "id": "186a1bff4aeb2072",
            "threadId": "186a1bff4aeb2072"
        },
        {
            "id": "186a1bf1a0e11dac",
            "threadId": "186a1bf1a0e11dac"
        },
        {
            "id": "1868308fbb326ae2",
            "threadId": "1868308fbb326ae2"
        },
        {
            "id": "1867d572e20141dc",
            "threadId": "1867d572e20141dc"
        },
        {
            "id": "1864f1aa0b2560a5",
            "threadId": "1864f1aa0b2560a5"
        },
        {
            "id": "18620ca11f652d1f",
            "threadId": "18620ca11f652d1f"
        },
        {
            "id": "185f1e6111a50ce2",
            "threadId": "185f1e6111a50ce2"
        },
        {
            "id": "185c5da6119bb518",
            "threadId": "185c5da6119bb518"
        },
        {
            "id": "18592b3864e26057",
            "threadId": "18592b3864e26057"
        },
        {
            "id": "18568c4affed38cc",
            "threadId": "18568c4affed38cc"
        },
        {
            "id": "18561c9851e4d2a8",
            "threadId": "18561c9851e4d2a8"
        },
        {
            "id": "1854dd3f2ffbd600",
            "threadId": "1854dd3f2ffbd600"
        },
        {
            "id": "1853f0556881807a",
            "threadId": "1853f0556881807a"
        },
        {
            "id": "1852877c70e9fa9f",
            "threadId": "1852877c70e9fa9f"
        },
        {
            "id": "1852358da1332cde",
            "threadId": "1852358da1332cde"
        },
        {
            "id": "18515e9db19db544",
            "threadId": "18515e9db19db544"
        },
        {
            "id": "1850f3456317841c",
            "threadId": "1850f3456317841c"
        },
        {
            "id": "1850606baa56a83c",
            "threadId": "1850606baa56a83c"
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
    date_str, day_of_week = get_email_date(email_data)
    if date_str:
        detailed_emails.append({
            'id': message_id,
            'date': date_str,
            'day_of_week': day_of_week
        })

# Print or process the detailed email data
for email in detailed_emails:
    print(json.dumps(email, indent=2))  # Pretty-print the email data

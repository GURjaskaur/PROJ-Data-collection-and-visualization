from datetime import datetime, timedelta

# Convert expires_in to an expiry timestamp
expires_in = 3461  # seconds
issue_time = datetime.utcnow()
expiry_time = issue_time + timedelta(seconds=expires_in)

# Convert expiry_time to string format
expiry_timestamp = expiry_time.isoformat() + "Z"
print(expiry_timestamp)
import json
from datetime import datetime
import pytz

# Sample JSON data (you would typically read this from a file)
json_data = '''{
    "id": "19005c630b02f76f",
    "threadId": "19005c630b02f76f",
    "labelIds": [
        "UNREAD",
        "CATEGORY_UPDATES",
        "INBOX"
    ],
    "snippet": "Hey GURjaskaur! A third-party OAuth application (Anaconda) with read:user and user:email scopes was recently authorized to access your account. Visit https://github.com/settings/connections/",
    "payload": {
        "partId": "",
        "mimeType": "text/plain",
        "filename": "",
        "headers": [
            {
                "name": "Delivered-To",
                "value": "gurjas2525@gmail.com"
            },
            {
                "name": "Received",
                "value": "by 2002:ac8:4d59:0:b0:440:f3d0:6792 with SMTP id x25csp934477qtv;        Mon, 10 Jun 2024 22:29:53 -0700 (PDT)"
            },
            {
                "name": "X-Google-Smtp-Source",
                "value": "AGHT+IHeTWzYbZ56AxdaRFWaRFLwnE8KMf9h00qH60asI1e91jmRB9kRLqYfoSBrm/xeUeC/LRpM"
            },
            {
                "name": "X-Received",
                "value": "by 2002:a25:2906:0:b0:dfb:b53:aaf3 with SMTP id 3f1490d57ef6-dfb0b53ad81mr7340584276.64.1718083793205;        Mon, 10 Jun 2024 22:29:53 -0700 (PDT)"
            },
            {
                "name": "ARC-Seal",
                "value": "i=1; a=rsa-sha256; t=1718083793; cv=none;        d=google.com; s=arc-20160816;        b=g5gWY7km4J7Qk4K2Ng3J80CR0aScnPwH3UNen6dZfkW4LM7IR1/50Xev18p76O1knP         C3Y9rYFFcQYhC6J0xgVQN5eQaqzpJEx4WhctGX8Kaou3x3cF5/zXIKXtrFuYb6cbYX0V         /FOro4lUu2/Y+n/Aw8QgoiWx8YPLqUSxu8/eO8x47NC8bucqYYSaqUZPg4HczOgPFGMT         36AGXaPx2/2/g/6LWCzdcd/Yov9NTtVIWNB4mmzyL89ZaQpHE2z6VYAjaqhQAltAtQWN         YakKZPPA+xknoo+M1FrkmfP9xcahDStFk7NT3gIyEAfdUvLFd/oqzKmuyk3sc/qBYVqJ         i3Vw=="
            },
            {
                "name": "ARC-Message-Signature",
                "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=content-transfer-encoding:mime-version:subject:message-id:to:from         :date:dkim-signature;        bh=o/Z8ehDeY87NkCyqhE1cCJ0nGG2yFdT9nKvCzyETLfY=;        fh=v/KvELVKqOxe64WCufNz0ag9lKebnOvY90URIqd027g=;        b=LbGAJObmtNWfw8mOtsvn7c8b5ExdTIAstf081q/Qo7MKLqkZVs2qW3riOC2hyx6U3b         j7rddZM4WZcsvWl+Er9ZGCLfHYnm0NI5Vz90wgp8fOA+pkzQpCadsR1EbUmf3qqPI1zE         zf/DZ5pBGqfec+C97H+n+/vy0UpM2qsCHuhhLhbidiFpYWfCAYXeqtt768qqNWjVAOCK         AoY9GiiEDBZNnUZ+ldDSysiHhyHHF9KhCZAiVKAfAjruKaFx38zmXI7Ls3W8048UUJEj         gLsYZ4MFZeWNkWWkFsJahmUgxcxF4FspK5/9Tpaq+dbOKlV8xOrrgI6jD5BiqMAmNIfW         FhLw==;        dara=google.com"
            },
            {
                "name": "ARC-Authentication-Results",
                "value": "i=1; mx.google.com;       dkim=pass header.i=@github.com header.s=pf2023 header.b=m2fbMC4K;       spf=pass (google.com: domain of noreply@github.com designates 192.30.252.201 as permitted sender) smtp.mailfrom=noreply@github.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=github.com"
            },
            {
                "name": "Return-Path",
                "value": "<noreply@github.com>"
            },
            {
                "name": "Received",
                "value": "from out-18.smtp.github.com (out-18.smtp.github.com. [192.30.252.201])        by mx.google.com with ESMTPS id 6a1803df08f44-6b06ad23b69si73123286d6.71.2024.06.10.22.29.53        for <gurjas2525@gmail.com>        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);        Mon, 10 Jun 2024 22:29:53 -0700 (PDT)"
            },
            {
                "name": "Received-SPF",
                "value": "pass (google.com: domain of noreply@github.com designates 192.30.252.201 as permitted sender) client-ip=192.30.252.201;"
            },
            {
                "name": "Authentication-Results",
                "value": "mx.google.com;       dkim=pass header.i=@github.com header.s=pf2023 header.b=m2fbMC4K;       spf=pass (google.com: domain of noreply@github.com designates 192.30.252.201 as permitted sender) smtp.mailfrom=noreply@github.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=github.com"
            },
            {
                "name": "Received",
                "value": "from github.com (hubbernetes-node-35a4d40.va3-iad.github.net [10.48.156.36]) by smtp.github.com (Postfix) with ESMTPA id C4058E0155 for <gurjas2525@gmail.com>; Mon, 10 Jun 2024 22:29:52 -0700 (PDT)"
            },
            {
                "name": "DKIM-Signature",
                "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=github.com; s=pf2023; t=1718083792; bh=o/Z8ehDeY87NkCyqhE1cCJ0nGG2yFdT9nKvCzyETLfY=; h=Date:From:To:Subject:From; b=m2fbMC4KPcHk/bdNgM9EJrZWJtqLbTCrRN7CUea0JltgRzfVw0vqJvSnYAmaX8CX0\\t EQJoGGHArfmMZOOWJx/6zyM9X4kwrCV8xaEIeK3xX7m4ElT+hdmZ7WEwhEcsRlUj1c\\t LqkHQnusE0vZwLj5nqopfAbdYAxHmMBC18FLqshA="
            },
            {
                "name": "Date",
                "value": "Mon, 10 Jun 2024 22:29:52 -0700"
            },
            {
                "name": "From",
                "value": "GitHub <noreply@github.com>"
            },
            {
                "name": "To",
                "value": "GURJAS KAUR <gurjas2525@gmail.com>"
            },
            {
                "name": "Message-ID",
                "value": "<6667e0d0c2b39_8d188897020@lowworker-64588bd4c-zfrlm.mail>"
            },
            {
                "name": "Subject",
                "value": "[GitHub] A third-party OAuth application has been added to your account"
            },
            {
                "name": "Mime-Version",
                "value": "1.0"
            },
            {
                "name": "Content-Type",
                "value": "text/plain; charset=UTF-8"
            },
            {
                "name": "Content-Transfer-Encoding",
                "value": "7bit"
            },
            {
                "name": "X-Auto-Response-Suppress",
                "value": "All"
            }
        ],
        "body": {
            "size": 478,
            "data": "SGV5IEdVUmphc2thdXIhDQoNCkEgdGhpcmQtcGFydHkgT0F1dGggYXBwbGljYXRpb24gKEFuYWNvbmRhKSB3aXRoIHJlYWQ6dXNlciBhbmQgdXNlcjplbWFpbCBzY29wZXMgd2FzIHJlY2VudGx5IGF1dGhvcml6ZWQgdG8gYWNjZXNzIHlvdXIgYWNjb3VudC4NClZpc2l0IGh0dHBzOi8vZ2l0aHViLmNvbS9zZXR0aW5ncy9jb25uZWN0aW9ucy9hcHBsaWNhdGlvbnMvMTZkZWJmNjIyNmU2MDMwNDcyZjIgZm9yIG1vcmUgaW5mb3JtYXRpb24uDQoNClRvIHNlZSB0aGlzIGFuZCBvdGhlciBzZWN1cml0eSBldmVudHMgZm9yIHlvdXIgYWNjb3VudCwgdmlzaXQgaHR0cHM6Ly9naXRodWIuY29tL3NldHRpbmdzL3NlY3VyaXR5LWxvZw0KDQpJZiB5b3UgcnVuIGludG8gcHJvYmxlbXMsIHBsZWFzZSBjb250YWN0IHN1cHBvcnQgYnkgdmlzaXRpbmcgaHR0cHM6Ly9naXRodWIuY29tL2NvbnRhY3QNCg0KVGhhbmtzLA0KVGhlIEdpdEh1YiBUZWFtDQoNCg=="
        }
    },
    "sizeEstimate": 4299,
    "historyId": "2042559",
    "internalDate": "1718083792000"
}'''

# Load JSON data
data = json.loads(json_data)

# Extract relevant date fields
headers = data["payload"]["headers"]

# Function to parse date and get day of the week
def get_day_of_week(date_str):
    try:
        date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
        return date.strftime('%A')
    except ValueError as e:
        return str(e)

# Find the "Date" header
for header in headers:
    if header["name"] == "Date":
        email_date = header["value"]
        day_of_week = get_day_of_week(email_date)
        print(f"Email Date: {email_date}\nDay of Week: {day_of_week}")

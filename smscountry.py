import requests

values = {
    "Text": "Sample text",
    "Number": "918013616447",
    "SenderId": "SMSCountry",
    "DRNotifyUrl": "https://www.domainname.com/notifyurl",
    "DRNotifyHttpMethod": "POST",
    "Tool": "API"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post('https://restapi.smscountry.com/v0.1/Accounts/authKey/SMSes/', json=values, headers=headers)

response_body = response.text
print(response_body)

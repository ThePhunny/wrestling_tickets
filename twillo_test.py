import requests

data = {
    'To': 'whatsapp:+18013616447',
    'From': 'whatsapp:+14155238886',
    'Body': 'ACK',
}

response = requests.post(
    'https://api.twilio.com/2010-04-01/Accounts/AC826462077781267f9a09026a207cf149/Messages.json',
    data=data,
    auth=('AC826462077781267f9a09026a207cf149', '461bb1bf23fc4598f9505f15eb9b45ee'),
)
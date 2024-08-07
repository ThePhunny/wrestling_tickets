#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import logging
import datetime
import os
from twilio.rest import Client

# Configure logging
logging.basicConfig(filename='tickets.log', level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# List of URLs to scrape
urls = [
	"https://www.allelitewrestling.com/aew-event/aew-wrestledream-2024",
	"https://www.allelitewrestling.com/aew-event/aew-full-gear-2024",
	"https://www.allelitewrestling.com/aew-event/aew-revolution-2024",
	"https://www.allelitewrestling.com/aew-event/aew-all-out-2024"
]
WA_FROM = 'whatsapp:+14155238886'
WA_TO = "whatsapp:+18013616447"

def ping_larold(message):
	# Send a text message to Larold
	# Find your Account SID and Auth Token at twilio.com/console
	# and set the environment variables. See http://twil.io/secure
	account_sid = os.environ["TWILIO_ACCOUNT_SID"]
	auth_token = os.environ["TWILIO_AUTH_TOKEN"]
	
	# auth = (account_sid, auth_token)
	
	data = {
			'To': WA_TO,
			'From': WA_FROM,
			'Body': message,
			}
	response = requests.post(twillo_url, data=data,auth=auth,)
	print(response.text)
def get_ticket_info(url):
	# Send a GET request to the URL
	response = requests.get(url)

	# Parse the HTML content
	soup = BeautifulSoup(response.content, "html.parser")

	# Search for the text "ON SALE: TBA"
	if soup.find_all(string="ON SALE: TBA"):
		logging.info(f"[TBA]	::	{url}")
	else:
		# Search for any link to "ticketmaster.com" or "seatgeek.com"
		ticket_links = soup.find_all("a", href=lambda href: href and ("ticketmaster.com" in href or "seatgeek.com" in href))
		if ticket_links:
			logging.info(f"[FOUND]	::	{ticket_links[0]['href']}")
			ping_larold(f"[FOUND]	::	{ticket_links[0]['href']}")
		else:
			logging.info(f"[NONE]	::	{url}")

for url in urls:
	get_ticket_info(url)
	

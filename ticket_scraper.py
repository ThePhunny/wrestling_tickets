#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
	"https://www.allelitewrestling.com/aew-event/aew-wrestledream-2024",
	"https://www.allelitewrestling.com/aew-event/aew-all-out-2024"
]

# Iterate over each URL
for url in urls:
	# Send a GET request to the URL
	response = requests.get(url)
	
	# Parse the HTML content
	soup = BeautifulSoup(response.content, "html.parser")
	
	# Search for the text "ON SALE: TBA"
	if soup.find_all(string="ON SALE: TBA"):
		print(f"Text 'ON SALE: TBA' found on the page: {url}")
	else:
		# Search for any link to "ticketmaster.com" or "seatgeek.com"
		ticket_links = soup.find_all("a", href=lambda href: href and ("ticketmaster.com" in href or "seatgeek.com" in href))
		if ticket_links:
			for link in ticket_links:
				print(f"Link to '{link['href']}' found on the page: {url}")
		else:
			print(f"Neither 'ON SALE: TBA' nor 'ticketmaster.com' or 'seatgeek.com' link found on the page: {url}")
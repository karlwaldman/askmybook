import requests
from bs4 import BeautifulSoup
import pdfkit
import time
from fake_useragent import UserAgent


# Construct the URL for the HTML page
urls = []
ua = UserAgent()

for year in range(1977, 2022):
    headers = {'User-Agent': ua.random}
    url = f"https://www.berkshirehathaway.com/letters/{year}.html"
    urls.append(url)
    print(urls)

    # Send a request to the URL and retrieve the page content
    response = requests.get(url, headers=headers)

    # Parse the page content into a BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the text from the BeautifulSoup object
    text = soup.get_text()

    

    # Write the text to a PDF file
    pdfkit.from_string(text, f"{year}.pdf")
    time.sleep(5)


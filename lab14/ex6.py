
# Exercise 6
# Get mortgage rates from Hawaii website

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

# Get the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the mortgage rate table
tables = soup.find_all("table")

for table in tables:
    if "Interest Rate" in table.get_text():
        rows = table.find_all("tr")

        # Print each bank and its rates
        for row in rows:
            columns = row.find_all(["th", "td"])
            data = [col.get_text(" ", strip=True) for col in columns]

            if data:
                print(" | ".join(data))

# Scrape names of ITM faculty and grad students
import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", itm_url)

itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, "html.parser")
print(soup.prettify()[:500])
# BeautifulSoup returns a BeautifulSoup object.
# It helps me find and extract information from HTML.

# Find all the faculty, which are in h2 tags with class="title"
# 3(b)
cards = soup.find_all("article")

print("Total People:", len(cards))

if cards:
    print("First Card:")
    print(cards[0].prettify())
# find_all("article") finds all the people cards.
# len(cards) counts the number of cards.
# cards[0] shows the HTML of the first card.


for card in cards:
    name = card.find("h2", class_="title")
    email = card.find("div", class_="field-email")

    if name:
        print("Name:", name.get_text(strip=True))

        if email:
            email_text = email.find("div", class_="field-item")
            print("Email:", email_text.get_text(strip=True))
        else:
            print("Email: Not available")

        print()
# This code goes through each people card.
# It finds the person's name and email address.
# It prints the name and email for each person.
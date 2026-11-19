# Scrape data from the City of Chicago's data portal 
# Print any line with a <title> tag in it
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

print("Retrieving", url)
response = urllib.request.urlopen(url)
print(response)
# The response is an HTTPResponse object.
# I can use it to read data from the website.
# The SSL setting helps avoid certificate errors.

for line in response:
    line = line.decode("utf-8").strip()
    if "<title>" in line:
        print(line)
# The website returns data as bytes.
# Decoding converts the bytes into readable text.
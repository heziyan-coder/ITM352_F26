# Exercise 5
# Get driver type data from Chicago

import pandas as pd
import requests

# 5(a) Get JSON data from the website
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

response = requests.get(url)
response_json = response.json()

print("Driver types and counts:")
print(response_json)
#The .json() method converts the JSON response into Python data, usually a list of dictionaries.

# 5(b) Convert JSON data to DataFrame
response_df = pd.DataFrame.from_records(response_json)

response_df = response_df[["driver_type", "count_license"]]
response_df.columns = ["driver_type", "count"]
response_df = response_df.set_index("driver_type")

print(response_df)
#This code converts the JSON data into a pandas DataFrame and uses driver_type as the index.
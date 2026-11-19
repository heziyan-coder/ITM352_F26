# Get public license data from City of Chicago's data portal
# Exercise 4
# Get public vehicle license data from Chicago

import pandas as pd
from sodapy import Socrata

# 4(a) Get 500 records and convert to DataFrame
client = Socrata("data.cityofchicago.org", None)

json_file = "rr23-ymwb"
results = client.get(json_file, limit=500)

results_df = pd.DataFrame.from_records(results)

print("First 5 records:")
print(results_df.head())
#This code gets 500 records from the Chicago data portal and converts them into a pandas DataFrame.

# 4(d) Print vehicle numbers and fuel sources
vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]

print("\nPublic vehicles and fuel sources:")
print(vehicles)
#This code displays the vehicle numbers and their fuel sources.

# 4(e) Count vehicles by fuel source
vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()

print("\nVehicles by fuel source:")
print(vehicles_by_fuel)
#This code groups the vehicles by fuel source and counts how many vehicles use each type.
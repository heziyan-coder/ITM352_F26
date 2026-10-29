import pandas as pd

# Read the JSON file into a DataFrame
results_df = pd.read_json("Taxi_trips.json")

# Display the first few rows of the DataFrame
print(results_df.head(6))

# Display basic statistics about the DataFrame
print(results_df.describe())

# Calculate the median fare
print(results_df.columns.tolist())

# median = results_df["Fare"].median()
# print("The median fare value is", median)
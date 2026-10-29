import pandas as pd

homes_data_file = "https://drive.google.com/uc?export=download&id=1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"

homes_df = pd.read_csv(homes_data_file)

print(homes_df.head(10))

#print the dimensions of the dataframe
shape = homes_df.shape
print("The dimensions of the dataframe are: ", shape)

df_big = homes_df[homes_df['units']>= 500]
print(df_big.head(10))
import pandas as pd

poke_df = pd.read_csv('pokemon_data.csv')

# Read the first 3 rows
print(poke_df.head(3))
print(" ")

# Read the column names
print(poke_df.columns)
print(" ")

# Read the columns: Name, Type 1 and HP only
print(poke_df[['Name', 'Type 1', 'HP']])
print(" ")

# Read Each Row
print(poke_df.iloc[0])

# Read a specific location

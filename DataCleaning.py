import pandas as pd

# Data Cleaning


df = pd.read_csv("data.csv")

# 1. drop irrelevant column

#df = df.drop(columns=["Legendary", "No"])


# 2. handle missing data

#df = df.dropna(subset=["Type2"])
#df = df.fillna({"Type2" : "None"})

# 3. Fix inconsistent values

#df["Type1"] = df["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE", "Water" : "WATER"})

# 4. Standartize text

#df["Name"] = df["Name"].str.lower()

# 5. fix datatypes

#df["Legendary"] = df["Legendary"].astype(bool)

# 6. remove dupe values

df = df.drop_duplicates()


print(df.to_string())
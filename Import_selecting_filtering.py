import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")
print(df)

#selection by column 

#print(df["Name"].to_string())

#print(df["Height"])

#print(df[["Weight", "Name", "Height"]])


#selection by rows

#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

# whole dataframe
 
#print(df.iloc[1:10:3])
#print(df.mean(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.sum(numeric_only=True))

#print(df.count())


# single column

#print(df["Height"].mean())
#print(df["Height"].max())
#print(df["Height"].min())


# grouping


group = df.groupby("Type1")

print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].sum())
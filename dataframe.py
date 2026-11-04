import pandas as pd

data = {
    "Name" : ["david", "elene", "vezdo", "giruxa", "beka"],
    "age" : [17, 15, 17, 17, 17]
}

df = pd.DataFrame(data=data)

#new column
df["job"] = ["AI", "N/A", "GYM", "EAT", "AI"]

#new row
new_rows = pd.DataFrame([{"Name" : "saba", "age" : 17, "job" : "tt scroll"}, {"Name" : "paxunia", "age" : 17, "job" : "rblx dev"}], index=[5, 6])
df = pd.concat([df, new_rows])

print(df)

data2 = {
    "games" : ["rblx", "fortnite", "minecraft", "doom", "CS2"],
    "coolness_scale" : [80, 90, 87, 30, 35]
}

df2 = pd.DataFrame(data=data2)



df2["bias_level"] = [95, 100, 80, 0, 5]

new_rows2 = pd.DataFrame([{"games" : "Candy crush", "coolness_scale" : 65, "bias_level": 50}, {"games" : "BrawlStars", "coolness_scale" : 86, "bias_level": 83}], index=[5, 6])
df2 = pd.concat([df2, new_rows2])

print(df2)
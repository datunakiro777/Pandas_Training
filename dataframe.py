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
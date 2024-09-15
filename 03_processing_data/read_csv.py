
import pandas as pd

df = pd.read_csv("fruit.csv")
print(df)

data = df.to_dict(orient="list")  # also try 'dict', 'series', 'records'
print(data)

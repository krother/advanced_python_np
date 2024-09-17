
import pandas as pd

data = [["apple", 3],
        ["banan", 7],
        ["cherry", 9],
        ]
df = pd.DataFrame(data, columns=["fruit", "number"])
df.to_csv("fruit.csv", index=False)

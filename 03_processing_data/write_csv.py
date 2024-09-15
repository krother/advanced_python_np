
import pandas as pd

df = pd.DataFrame({
    'fruit': ["apple", "banana", "cherry"],
    'amount': [4, 5, 6],
})

df.to_csv("fruit.csv", index=False)

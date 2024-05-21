import sys
import pandas as pd
from functools import reduce

labs = int(sys.argv[1])
try:
    exs = int(sys.argv[2])
except IndexError:
    exs = 3
    
directory = f"../Scores/Lab{labs}/"

dfs = []
for i in range(1, exs + 1):
    temp_df = pd.read_csv(directory+f"ex{labs}_{i}.csv")
    dfs.append(temp_df)

df_merged = reduce(lambda left, right: pd.merge(left, right, on=['STUDENT ID', 'SESSION NO'],
                                                how='outer'), dfs)

df = df_merged.iloc[:, [0, 1] + list(range(2, len(df_merged.columns), 2))]

df.to_csv(directory+f"Lab{labs}.csv", index=False)

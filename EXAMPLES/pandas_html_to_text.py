import pandas as pd

df_list = pd.read_html('https://www.wsj.com', header=0)

df = df_list[0]

print(df.head())

df.to_csv('money.csv', sep="|")


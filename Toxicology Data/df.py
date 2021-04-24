import pandas as pd

df = pd.read_csv("drugsPerAgencyTop10Drugs.csv")
print(df['Agency'].unique())
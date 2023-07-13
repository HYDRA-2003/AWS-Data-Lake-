import pandas as pd
 
df1 = pd.read_csv(r'F:\Software\danish\Alapex\Sectoral Data Changed Names\auto.csv')
df2 = pd.read_csv(r'F:\Software\danish\Alapex\Sectoral Data Changed Names\bank.csv')
df3 = pd.read_csv(r'F:\Software\danish\Alapex\Sectoral Data Changed Names\healthcare.csv')
df4 = pd.read_csv(r'F:\Software\danish\Alapex\Sectoral Data Changed Names\it.csv')
df5 = pd.read_csv(r'F:\Software\danish\Alapex\Sectoral Data Changed Names\pharma.csv')
df_merged = df1.merge(df2, how='outer')
df_merged = df_merged.merge(df3,  how='outer')
df_merged = df_merged.merge(df4, how='outer')
df_merged = df_merged.merge(df5, how='outer')

df_csv = df_merged.to_csv('F:/Software/danish/Alapex/Sectoral Merged/merged_csv.csv')

print(df_merged)

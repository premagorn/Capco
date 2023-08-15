import pandas as pd
xlsx = pd.ExcelFile('Analyze-Quantitative-Data.xlsx')
df = pd.read_excel(xlsx, 'Overview', header=3)
df_filled = df.fillna(method='ffill')
df_filter = df_filled.iloc[:, 1:]
df_group = df_filter.groupby(by=['Gender']).mean()
print(df_group)

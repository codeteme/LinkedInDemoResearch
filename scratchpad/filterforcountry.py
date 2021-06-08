# clean allpermutations_noexclude_USA.csv
import pandas as pd

df = pd.read_csv('intermediate/allpermutations_noexclude_USA.csv')
df.columns = ["Country", "Gender", "Company Industry", "Age Range", "Job seniority", "Company Size", "Count"]
is_USA = df['Country'] == 'USA'
df = df[is_USA]
# df.to_csv('intermediate/filtered_noexclude_USA.csv')
df_GBR = pd.read_csv('intermediate/allpermutations_noexclude_temp_3.csv')
df_GBR.columns =  ["Country", "Gender", "Company Industry", "Age Range", "Job seniority", "Company Size", "Count"]
is_GBR = df_GBR['Country'] == 'GBR'
df_GBR = df_GBR[is_GBR]
# df_GBR.to_csv('intermediate/filtered_noexclude_GBR.csv')

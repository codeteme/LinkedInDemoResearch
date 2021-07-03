import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('intermediate/rank_dataframe.py/df_rankorder.csv')
# df = pd.read_csv('intermediate/rank_dataframe.py/df_rankorder_1.csv')
# df = pd.read_csv('intermediate/rank_dataframe.py/df_rankorder_2.csv')
df = pd.read_csv('intermediate/rank_dataframe.py/df_rankorder_3.csv')

country_list = list(df['Country'].unique())
sector_list = list(df['Sector'].unique())
companysize_list = list(df['Company Size'].unique())

print(companysize_list)

# for country in country_list:
#     for sector in sector_list:
#         df_ctry_sctr = df[(df['Country'] == country) & (df['Sector'] == sector)]
#         grouped_df = df_ctry_sctr.groupby("Seniority")['Rank'].mean()
#         print('Country: ', country, '\n', 'Sector: ', sector)
#         # print(grouped_df)
#         print(df_ctry_sctr.groupby("Seniority")['Rank'].count())
#         # For each country-sector df, the sum of ranks should be 10, if ranks are computed, or 0, if ranks are not computed. 
#         assert (sum(grouped_df) == 10 or sum(grouped_df) == 0) 


for country in country_list:
    for sector in sector_list:
        for companysize in companysize_list:
            df_ctry_sctr = df[(df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == companysize)]
            grouped_df = df_ctry_sctr.groupby("Seniority")['Rank'].mean()
            print('Country: ', country, '\n', 'Sector: ', sector, '\n', 'Company Size: ', companysize)
            print(grouped_df)
            # print(df_ctry_sctr.groupby("Seniority")['Rank'].count())
            # For each country-sector df, the sum of ranks should be 10, if ranks are computed, or 0, if ranks are not computed. 
            assert (sum(grouped_df) == 10 or sum(grouped_df) == 0) 
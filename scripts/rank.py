import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('intermediate/rank_dataframe.py/df_rankorder.csv')

country_list = list(df['Country'].unique())
sector_list = list(df['Sector'].unique())

for country in country_list:
    for sector in sector_list:
        df_ctry_sctr = df[(df['Country'] == country) & (df['Sector'] == sector)]
        grouped_df = df_ctry_sctr.groupby("Seniority")['Rank'].mean()
        print('Country: ', country, '\n', 'Sector: ', sector)
        print(grouped_df)



# mean_df = grouped_df['Rank'].mean()
# mean_df = mean_df.drop('Any Job Seniority')
# mean_df.sort_values(ascending=True)
# print(mean_df)


# Sort the job seniorities
# sorting_dict = {'Unpaid': 0, 'Training': 1, 'Entry': 2, 'Senior': 3, 'Manager':4, 'Director': 5, 'VP': 6, 'CXO': 7, 'Partner': 8, 'Owner': 9, 'Any Job Security': 10}
# df_reshaped.sort_values(by=df_reshaped.index, key=lambda x: x.map(sorting_dict), inplace=True)
# mean_df = mean_df.sort_index(key=lambda x: x.map(sorting_dict))

# mean_df.plot()

# Program will only end when plt.show returns, which is after you closed all figures.
# plt.show(block=True)


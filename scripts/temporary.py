import pandas as pd

df = pd.read_csv('processed/data_collection_2/dataset.csv')
# drop the two irrelevant index columns added when building the cleaned dataset imported above

df.drop(df.columns[[0, 1]], axis = 1, inplace = True)


# rename the colums
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
# replace all 0s by 1 so as to avoid arithmetic errors
df['Count'].replace(to_replace=0, value = 1, inplace = True)

df.to_excel('intermediate/temporary/df.xlsx')
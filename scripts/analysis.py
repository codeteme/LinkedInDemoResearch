import pandas as pd
import numpy as np

df = pd.read_csv('intermediate/data_collection_2/temp_USA.csv')
# rename the column headers
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']


# select parameters
def df_specifier(df, country, sector): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == '10,001+ employees') & (df['Age Ranges'] == 'Any Age Range'))
    return df.loc[idx]



def filter_reshape_export(df, country, sector): 
    usa_it = df_specifier(df, country, sector) # USA, IT, Big Companies
    # split data to with connection and any connection
    df_with_connection = usa_it[usa_it['Connectivity Status'] == 'connected to big companies']
    df_any_connection = usa_it[usa_it['Connectivity Status'] == 'connected to any']

    df_with_connection = df_with_connection.groupby(["Job Seniority", "Gender"]).sum() # filter only job seniority and gender
    df_with_connection.reset_index(inplace=True) # Unstack the rows 
    df_with_connection = df_with_connection.pivot(index='Job Seniority', columns='Gender') # make values of Gender the columns headers
    # print(df_with_connection.head())

    df_any_connection = df_any_connection.groupby(["Job Seniority", "Gender"]).sum()
    df_any_connection.reset_index(inplace=True)
    df_any_connection = df_any_connection.pivot(index='Job Seniority', columns='Gender')
    # print(df_any_connection.head())


    df_usa_it_reshaped = pd.merge(df_with_connection, df_any_connection, on='Job Seniority', suffixes=('_with_connection', '_any_connection'))
    # print(df_usa_it_reshaped)
    # df_usa_it_reshaped.to_excel('processed/data_collection_2/US_IT_BigCompanies.xlsx')

filter_reshape_export(df, 'USA', 'IT')
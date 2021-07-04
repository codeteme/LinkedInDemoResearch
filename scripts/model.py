# This script computes the rank and produces a simple linear model to see what factors influence %female

import pandas as pd
import numpy as np

"""
    Current working director: 
    /Users/tmt0947/Development/workspaces/QCRI/LinkedInDemoResearch 
"""

df = pd.read_csv('processed/data_collection_2/dataset.csv')
df.drop(df.columns[[0, 1]], axis = 1, inplace = True)

# Drop all of the “any” age, “any” company size, “any” rank.
is_not_anycompanysize = df['Company Size'] != 'Any Company Size'
is_not_anyage = df['Age Ranges'] != 'Any Age Range'

df = (df[is_not_anycompanysize & is_not_anyage]).reset_index()

# Only consider the four least-sparse ranks: selected_seniorities are Entry, Senior, Manager, and Director
selected_seniorities =  ['Entry', 'Senior', 'Manager', 'Director']
is_selected_seniorities = df['Job Seniority'].apply(lambda x: x in selected_seniorities) 
df = (df[is_selected_seniorities]).reset_index()

# # Only consider US and UK for now (**or even just US**)
# is_USA = df['Country'] == 'USA'
# df = (df[is_USA]).reset_index(drop=True)

# Global Variables
df_rankorder = pd.DataFrame(columns = ['Country', 'Sector', 'Age Ranges','Company Size', 'Seniority', 'Rank', '%/female']) # dataframe that compute average rank value of each permutation


def condition_any_gender(df):
    if (df['Count_with_connection', 'Any Gender'] == 0) and (df['Count_any_connection', 'Any Gender'] > 3000):
        return 290 
    elif df['Count_with_connection', 'Any Gender'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Any Gender']

def condition_female(df):
    if (df['Count_with_connection', 'Female'] == 0) and (df['Count_any_connection', 'Female'] > 3000):
        return 290 
    elif df['Count_with_connection', 'Female'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Female']
    # return df['Count_with_connection', 'Female'] / df['Count_any_connection', 'Female']

def condition_male(df):
    if (df['Count_with_connection', 'Male'] == 0) and (df['Count_any_connection', 'Male'] > 3000):
        return 290 
    elif df['Count_with_connection', 'Male'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Male']

    
# select parameters
def df_specifier(df, country, sector, size, age): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == size) & (df['Age Ranges'] == age))
    return df.loc[idx]

def filter_reshape(df, country, sector, size, age): 
    # split data to with connection and any connection
    df_with_connection = df[df['Connectivity Status'] == 'connected to big companies']
    df_any_connection = df[df['Connectivity Status'] == 'connected to any']

    df_with_connection = df_with_connection.groupby(["Job Seniority", "Gender"]).sum() # filter only job seniority and gender
    df_with_connection.reset_index(inplace=True) # Unstack the rows 
    df_with_connection = df_with_connection.pivot(index='Job Seniority', columns='Gender') # make values of Gender the columns headers

    df_any_connection = df_any_connection.groupby(["Job Seniority", "Gender"]).sum()
    df_any_connection.reset_index(inplace=True)
    df_any_connection = df_any_connection.pivot(index='Job Seniority', columns='Gender')


    df_reshaped = pd.merge(df_with_connection, df_any_connection, on='Job Seniority', suffixes=('_with_connection', '_any_connection'))

    df_reshaped['Count_with_connection', 'Any Gender'] = df_reshaped.apply(condition_any_gender, axis=1)
    df_reshaped['Count_with_connection', 'Female'] = df_reshaped.apply(condition_female, axis=1)
    df_reshaped['Count_with_connection', 'Male'] = df_reshaped.apply(condition_male, axis=1)

    df_reshaped['with_:_any', 'Any Gender'] = df_reshaped['Count_with_connection', 'Any Gender'] / df_reshaped['Count_any_connection', 'Any Gender']
    df_reshaped['with_:_any', 'Female'] = df_reshaped['Count_with_connection', 'Female'] / df_reshaped['Count_any_connection', 'Female']
    df_reshaped['with_:_any', 'Male'] = df_reshaped['Count_with_connection', 'Male'] / df_reshaped['Count_any_connection', 'Male']

    df_reshaped['Gender Proportion', 'Female'] = df_reshaped['Count_any_connection', 'Female'] / df_reshaped['Count_any_connection', 'Any Gender']
    df_reshaped['Gender Proportion', 'Male'] = df_reshaped['Count_any_connection', 'Male'] / df_reshaped['Count_any_connection', 'Any Gender']
    df_reshaped['Female to Male', 'f:m'] = df_reshaped['with_:_any', 'Female'] / df_reshaped['with_:_any', 'Male']

    # Drop all Nan values
    # df_reshaped =  df_reshaped.dropna()

    # # Fill all Nan values with 0
    df_reshaped =  df_reshaped.fillna(value=0)


    # Sort the job seniorities
    sorting_dict = {'Entry': 0, 'Senior': 1, 'Manager':2, 'Director': 3}
    # df_reshaped.sort_values(by=df_reshaped.index, key=lambda x: x.map(sorting_dict), inplace=True)
    df_reshaped = df_reshaped.sort_index(key=lambda x: x.map(sorting_dict))

    # print(df_reshaped['Female to Male']['f:m'].values)
    # print(df_reshaped)

    return df_reshaped

def rank_order(df, country, sector, size, age):
    global df_rankorder
    print(country, sector, size, age)
    print(df)

    # Filter for the four seniority levels: Entry, Senior, Manager and Director
    df['seniority'] = df.index
    df['rank'] = df['Female to Male', 'f:m'].rank()
    
    for i in range(0, 4):
        row_value = [country, sector, size, age, df['seniority'].iloc[i], df['rank'].iloc[i], df['Gender Proportion', 'Female'].iloc[i]]
        # print(row_value)
        df_rankorder_len = len(df_rankorder)
        df_rankorder.loc[df_rankorder_len] = row_value

    print(df_rankorder)


def render(df, country, sector, size, age): 
    df = df_specifier(df, country, sector, size, age)
    df = filter_reshape(df, country, sector, size, age)
    rank_order(df, country, sector, size, age)

def main(): 
    global df_rankorder

    # countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
    countries = ['USA']
    sectors = ['IT', 'Finance']
    agerange_noany = ["18 to 24","25 to 34", "35 to 54", "55+"]
    company_sizes_noany = ['10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']

    df.drop(df.columns[[0, 1]], axis = 1, inplace = True)


    # render(df, 'USA', 'IT', '5001-10,000 employees', '18 to 24')

    for country in countries: 
        for sector in sectors: 
            for size in company_sizes_noany:
                for age in agerange_noany:
                    print(country, sector, size, age)
                    # render(df, country, sector, size, age)
                    # Some seniority levels may not data so they are dropped
                    try:
                        render(df, country, sector, size, age)
                        break
                    except:
                        if country not in df['Country'].unique(): print("country not found")
                        if sector not in df['Sector'].unique(): print("sector not found")
                        if size not in df['Company Size'].unique(): print("sector not found")
                        if age not in df['Age Ranges'].unique(): print("sector not found")
                        print("exception")

    
    save_path = f'intermediate/rank_dataframe/df_rankorder_model.csv'
    df_rankorder.to_csv(save_path)

main()
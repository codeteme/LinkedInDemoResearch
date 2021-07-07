# This script computes the rank and produces a simple linear model to see what factors influence %female

import pandas as pd
import numpy as np

# library
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression



"""
    Current working director: 
    /Users/tmt0947/Development/workspaces/QCRI/LinkedInDemoResearch 
"""

df = pd.read_csv('processed/data_collection_2/dataset.csv')
# Drop unnecessarily first columns
df.drop(df.columns[[0, 1]], axis = 1, inplace = True)
# Drop all of the “any” age, “any” company size, “any” rank.
is_not_anycompanysize = df['Company Size'] != 'Any Company Size'
is_not_anyage = df['Age Ranges'] != 'Any Age Range'
df = (df[is_not_anycompanysize & is_not_anyage]).reset_index()
# Only consider the four least-sparse ranks: selected_seniorities are Entry, Senior, Manager, and Director
selected_seniorities =  ['Entry', 'Senior', 'Manager', 'Director']
is_selected_seniorities = df['Job Seniority'].apply(lambda x: x in selected_seniorities) 
df = (df[is_selected_seniorities]).reset_index()

# Global Variables
df_rankorder = pd.DataFrame(columns = ['Country', 'Sector', 'Company Size', 'Age Ranges', 'Seniority', 'Rank', '%\Female']) # dataframe that compute average rank value of each permutation
counter_sparsity_treated = 0 # keeps track of modified data frames

def increment_counter(): # calculate the total number of modified plots
    global counter_sparsity_treated 
    counter_sparsity_treated += 1


def condition_any_gender(df):
    if (df['Count_with_connection', 'Any Gender'] == 0) and (df['Count_any_connection', 'Any Gender'] > 3000):
        increment_counter()
        return 290 
    elif df['Count_with_connection', 'Any Gender'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Any Gender']

def condition_female(df):
    if (df['Count_with_connection', 'Female'] == 0) and (df['Count_any_connection', 'Female'] > 3000):
        increment_counter()
        return 290 
    elif df['Count_with_connection', 'Female'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Female']
    # return df['Count_with_connection', 'Female'] / df['Count_any_connection', 'Female']

def condition_male(df):
    if (df['Count_with_connection', 'Male'] == 0) and (df['Count_any_connection', 'Male'] > 3000):
        increment_counter()
        return 290 
    elif df['Count_with_connection', 'Male'] == 0:
        return float('NaN')
    else:
        return df['Count_with_connection', 'Male']

    
# select parameters
def df_specifier(df, country, sector, size, age, connectivity_status): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == size) & (df['Age Ranges'] == age))
    return df.loc[idx]

def filter_reshape(df, country, sector, size, age, connectivity_status): 
    # Drop unnecessarily first columns
    df.drop(df.columns[[0, 1]], axis = 1, inplace = True)
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

def rank_order(df, country, sector, size, age, connectivity_status):
    global df_rankorder

    # Filter for the four seniority levels: Entry, Senior, Manager and Director
    df['seniority'] = df.index
    df['rank'] = df['Female to Male', 'f:m'].rank()
    
    for i in range(0, 4):
        row_value = [country, sector, size, age, df['seniority'].iloc[i], df['rank'].iloc[i], df['Gender Proportion', 'Female'].iloc[i]]
        # print(row_value)
        df_rankorder_len = len(df_rankorder)
        df_rankorder.loc[df_rankorder_len] = row_value


def render(df, country, sector, size, age, connectivity_status): 
    df = df_specifier(df, country, sector, size, age, connectivity_status)
    df = filter_reshape(df, country, sector, size, age, connectivity_status)
    rank_order(df, country, sector, size, age, connectivity_status)

def regression(): 
    global df_rankorder    
    cols_to_exclude = ['Rank', '%\Female']
    for col in df_rankorder.columns:
        if col not in cols_to_exclude:
            df_rankorder[col] = df_rankorder[col].astype('category')

    """
    The labelencoder assigned the following numbers to the selected categorical variables i.e. no country and no gender | code snippet:  print(labelencoder.classes_)
    Country: 
        {'USA', 1, 'GBR': 2', 'VNM': 3, 'IND': 4, 'PHL': 5}
    Sector: 
        {'Finance': 1, 'IT': 2}
    Age:
        {'18 to 24': 1, '25 to 34': 2, '35 to 54': 3, '55+': 4}
    Company Size: 
        {'Myself Only': 1, '2-10 employees': 2, '11-50 employees': 3, 
        '51-200 employees': 4, '201-500 employees': 5, '501-1000 employees': 6, 
        '1001-5000 employees': 7, '5001-10,000 employees': 8, '10,001+ employees': 9}
    Seniority: 
        {'Entry': 1, 'Senior': 2, 'Manager': 3, 'Director': 4}

    """

    # creating instance of labelencoder
    labelencoder = LabelEncoder()# Assigning numerical values and storing in another column
    # df_rankorder['Sector'] = labelencoder.fit_transform(df_rankorder['Sector'])
    # df_rankorder['Age Ranges'] = labelencoder.fit_transform(df_rankorder['Age Ranges'])
    # df_rankorder['Company Size'] = labelencoder.fit_transform(df_rankorder['Company Size'])
    # df_rankorder['Seniority'] = labelencoder.fit_transform(df_rankorder['Seniority'])
    dict_map_sector = {'Finance': 1, 'IT': 2}
    dict_map_ageranges = {'18 to 24': 1, '25 to 34': 2, '35 to 54': 3, '55+': 4}
    dict_map_companysize = {'Myself Only': 1, '2-10 employees': 2, '11-50 employees': 3, 
                            '51-200 employees': 4, '201-500 employees': 5, '501-1000 employees': 6, 
                            '1001-5000 employees': 7, '5001-10,000 employees': 8, '10,001+ employees': 9}
    dict_map_seniority = {'Entry': 1, 'Senior': 2, 'Manager': 3, 'Director': 4}

    df_rankorder = df_rankorder.replace({"Sector": dict_map_sector}) 
    df_rankorder = df_rankorder.replace({"Age Ranges": dict_map_ageranges}) 
    df_rankorder = df_rankorder.replace({"Company Size": dict_map_companysize})
    df_rankorder = df_rankorder.replace({"Seniority": dict_map_seniority})

    """
        Problem: Analyse correlation between each independent variable, bar Country, and the depedent variable %\Female.
        pairplot does not produce a good explanation since the all the indepedent variables, bar rank, are categorical.
        A boxplot maybe more appropriate in this case.
    """


    # For now, following variable(s) is(are) excluded: 
    df_rankorder = df_rankorder.drop(columns = 'Country')
    print(df_rankorder.columns)

    # Basic correlogram
    corr = df_rankorder.corr()
    corr.style.background_gradient(cmap='coolwarm')
    print(corr)

    # X = df_rankorder.drop(columns = '%\Female')
    # y = df_rankorder['%\Female']
    # # creating an object of LinearRegression class
    # LR = LinearRegression()
    # # fitting the training data
    # reg = LinearRegression().fit(X, y)
    # score = reg.score(X, y)
    # coefficient = reg.coef_
    # intercept = reg.intercept_

    # # print('score: ', score, 'coefficient', coefficient, 'intercept', intercept)

def main(): 
    global df
    global df_rankorder
    global counter_sparsity_treated # reminder: this variable keeps track of modified 

    countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
    # countries = ['USA']
    sectors = ['IT', 'Finance']
    # sectors = ['IT']

    company_sizes_noany = ['10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']
    agerange_noany = ["18 to 24", "25 to 34", "35 to 54", "55+"]
    connectivity_statuses = ['connected to big companies', 'connected to any']

    country_count_dict = dict() # key = country and value = [total count, sparsity treated count]
    
    for country in countries: 
        rows_computed = 0
        for sector in sectors: 
            for size in company_sizes_noany:
                for age in agerange_noany:
                    for connectivity_status in connectivity_statuses:
                        # Some seniority levels may not data so they are dropped
                        try:
                            rows_computed += 1
                            render(df, country, sector, size, age, connectivity_status)
                            break
                        except:
                            if country not in df['Country'].unique(): print("country not found")
                            if sector not in df['Sector'].unique(): print("sector not found")
                            if size not in df['Company Size'].unique(): print("sector not found")
                            if age not in df['Age Ranges'].unique(): print("sector not found")
                            if connectivity_status not in df['Connectivity Status'].unique(): print("connectivity status not found")
                            print("exception")
        country_count_dict[country] = [rows_computed, counter_sparsity_treated]


    # render(df, 'USA', 'IT', '5001-10,000 employees', '18 to 24')

    for country, total_sparisty in country_count_dict.items():
        print('Country: ', country, '| ',  'Total and sparsity counts: ', total_sparisty)


    # regression()
    # save_path = f'intermediate/rank_dataframe/df_rankorder_model.csv'
    # df_rankorder.to_csv(save_path)

main()
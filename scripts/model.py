# This script computes the rank and produces a simple linear model to see what factors influence %female

import pandas as pd
import numpy as np

# library
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

import streamlit as st


# Current working director: 
# /Users/tmt0947/Development/workspaces/QCRI/LinkedInDemoResearch 

df = pd.read_csv('processed/data_collection_2/dataset_transformed.csv')
print('Original shape of the imported dataset - dataset_transformed.csv: ', df.shape)
# Drop unnecessary first columns
df.drop(df.columns[0], axis = 1, inplace = True)
# Only consider the four least-sparse ranks: selected_seniorities are Entry, Senior, Manager, and Director
selected_seniorities =  ['Entry', 'Senior', 'Manager', 'Director']
is_selected_seniorities = df['Job Seniority'].apply(lambda x: x in selected_seniorities) 
df = df[is_selected_seniorities].reset_index()
print('Shape of dataframe after selected the four seniorities: ', df.shape)

# Global Variables
df_finalized = pd.DataFrame()

counter_sparsity_treated = 0 # keeps track of modified data frames
indices_to_drop = []

def increment_counter(): # calculate the total number of modified plots
    global counter_sparsity_treated 
    counter_sparsity_treated += 1
    
# select parameters
def df_specifier(df, country, sector, seniority, size, age): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Job Seniority'] == seniority) & (df['Company Size'] == size) & (df['Age Ranges'] == age))
    return df.loc[idx]

def filter_reshape(df, country, sector, seniority, size, age): 
    # the is_sparsity_treated column is initiliazed to False
    df['Is_sparsity_treated'] = False

    if df['Any_Gender_with'].values[0] == 0 and df['Any_Gender_any'].values[0] > 3000:
        increment_counter()
        df['Any_Gender_with'] = 290
        indices_to_drop.append(df.index.values[0])
        df['Is_sparsity_treated'] = True
    elif df['Any_Gender_with'].values[0] == 0: 
        df['Any_Gender_with'] = float('Nan')

    if df['Female_with'].values[0] == 0 and df['Female_any'].values[0] > 3000:
        increment_counter()
        df['Female_with'] = 290
        indices_to_drop.append(df.index.values[0])
        df['Is_sparsity_treated'] = True
    elif df['Female_with'].values[0] == 0: 
        df['Female_with'] = float('Nan')

    if df['Male_with'].values[0] == 0 and df['Male_any'].values[0] > 3000:
        increment_counter()
        df['Male_with'] = 290
        indices_to_drop.append(df.index.values[0])
        df['Is_sparsity_treated'] = True
    elif df['Male_with'].values[0] == 0: 
        df['Male_with'] = float('Nan')

    df['Any_Gender_with:any'] = df['Any_Gender_with'] / df['Any_Gender_any']
    df['Female_with:any'] = df['Female_with'] / df['Female_any']
    df['Male_with:any'] = df['Male_with'] / df['Male_any']

    df['female_any:any_any'] = df['Female_any'] / df['Any_Gender_any']
    df['male_any:any_any'] = df['Male_any'] / df['Any_Gender_any']
    df['Female to Male'] = df['Female_with:any'] / df['Male_with:any']

    # # Fill all Nan values with 0
    df =  df.fillna(value=0)

    return df

def render(df, country, sector, seniority, size, age): 
    global df_finalized
    df = df_specifier(df, country, sector, seniority, size, age)
    df = filter_reshape(df, country, sector, seniority, size, age)
    df_finalized = df_finalized.append(df, ignore_index=True)

def regression_prep(): 
    global df_finalized    
    # Drop the is_sparsity_fixed column
    # cols_to_exclude = ['Rank', '%\Female']
    # for col in df_finalized.columns:
    #     if col not in cols_to_exclude:
    #         df_finalized[col] = df_finalized[col].astype('category')

    """
    The labelencoder assigned the following numbers to the selected categorical variables i.e. no country and no gender | code snippet:  print(labelencoder.classes_)
    \n
    Country: 
        {'USA', 1, 'GBR': 2', 'VNM': 3, 'IND': 4, 'PHL': 5}
    \n
    Sector: 
        {'Finance': 1, 'IT': 2}
    \n
    Company Size: 
        {'Myself Only': 1, '2-10 employees': 2, '11-50 employees': 3, 
        '51-200 employees': 4, '201-500 employees': 5, '501-1000 employees': 6, 
        '1001-5000 employees': 7, '5001-10,000 employees': 8, '10,001+ employees': 9}
    \n
    Age:
        {'18 to 24': 1, '25 to 34': 2, '35 to 54': 3, '55+': 4}
    \n
    Seniority: 
        {'Entry': 1, 'Senior': 2, 'Manager': 3, 'Director': 4}
    \n

    """
    dict_map_country = {'USA': 1, 'GBR': 2, 'VNM': 3, 'IND': 4, 'PHL': 5}
    dict_map_sector = {'Finance': 1, 'IT': 2}
    dict_map_ageranges = {'18 to 24': 1, '25 to 34': 2, '35 to 54': 3, '55+': 4}
    dict_map_companysize = {'Myself Only': 1, '2-10 employees': 2, '11-50 employees': 3, '51-200 employees': 4, '201-500 employees': 5, '501-1000 employees': 6, '1001-5000 employees': 7, '5001-10,000 employees': 8, '10,001+ employees': 9}
    dict_map_seniority = {'Entry': 1, 'Senior': 2, 'Manager': 3, 'Director': 4}
    
    df_finalized = df_finalized.replace({"Country": dict_map_country}) 
    df_finalized = df_finalized.replace({"Sector": dict_map_sector}) 
    df_finalized = df_finalized.replace({"Age Ranges": dict_map_ageranges}) 
    df_finalized = df_finalized.replace({"Company Size": dict_map_companysize})
    df_finalized = df_finalized.replace({"Job Seniority": dict_map_seniority})

    # Specify and drop
    is_USA = df_finalized['Country'] == 1
    is_GBR = df_finalized['Country'] == 2
    is_VNM = df_finalized['Country'] == 3
    is_IND = df_finalized['Country'] == 4
    is_PHL = df_finalized['Country'] == 5

    is_Finance = df_finalized['Sector'] == 1
    is_IT = df_finalized['Sector'] == 2

    regression(df_finalized)
    
    # st.markdown('**USA, IT, NO Any Company Size, NO Any Age Range, each job seniority**')
    # regression(df_finalized[is_USA & is_IT].reset_index(drop = True))
    # st.markdown('**USA, Finance, NO Any Company Size, NO Any Age Range, each job seniority**')
    # regression(df_finalized[is_USA & is_Finance].reset_index(drop = True))
    # st.markdown('**GBR, IT, NO Any Company Size, NO Any Age Range, each job seniority**')
    # regression(df_finalized[is_GBR & is_IT].reset_index(drop = True))
    # st.markdown('**GBR, Finance, NO Any Company Size, NO Any Age Range, each job seniority**')
    # regression(df_finalized[is_GBR & is_Finance].reset_index(drop = True))

def regression(df_finalized): 

    # For now, following variable(s) is(are) excluded: 
    df_finalized = df_finalized.drop(columns = ['Country', 'Sector'])
    df_finalized = df_finalized.drop(columns = ['Any_Gender_any',
       'Male_any', 'Female_any', 'Any_Gender_with', 'Male_with', 'Female_with','Is_sparsity_treated', 'Any_Gender_with:any', 'Male_with:any','male_any:any_any', 'Female_with:any'])
    print(df_finalized.columns)
    print(df_finalized.dtypes)
    print(df_finalized['Job Seniority'].unique())
    st.write('Columns: ', list(df_finalized.columns))

    # Basic correlogram
    corr = df_finalized.corr()
    corr.style.background_gradient(cmap='coolwarm')
    print(corr)
    st.write(corr)

    # X = df_finalized.drop(columns = ['Any_Gender_any',
    #    'Male_any', 'Female_any', 'Any_Gender_with', 'Male_with', 'Female_with',
    #    'Is_sparsity_treated', 'Any_Gender_with:any', 'Female_with:any',
    #    'Male_with:any', 'female_any:any_any', 'male_any:any_any', 'Female to Male'])
    # y = df_finalized['female_any:any_any']
    # # creating an object of LinearRegression class
    # LR = LinearRegression()
    # # fitting the training data
    # reg = LinearRegression().fit(X, y)
    # score = reg.score(X, y)
    # coefficient = reg.coef_
    # intercept = reg.intercept_

    # print('score: ', score, 'coefficient', coefficient, 'intercept', intercept)

def main(): 
    global df_finalized
    global indices_to_drop
    global counter_sparsity_treated # reminder: this variable keeps track of modified 

    countries = df['Country'].unique()
    sectors = df['Sector'].unique()
    seniorities = df['Job Seniority'].unique()
    company_sizes = df['Company Size'].unique()
    company_sizes = np.delete(company_sizes, 0) # Remove Any Company Size
    age_ranges = df['Age Ranges'].unique()
    age_ranges = np.delete(age_ranges, 0) # Remove Any Age Range
    
    country_count_dict = dict() # key = country and value = [total count, sparsity treated count]

    total_rows_computed = 0

    for country in ['USA']: 
        rows_computed_ctry = 0
        for sector in ['IT']:
            for seniority in seniorities:  
                for size in ['Any Company Size']:
                    for age in age_ranges:
                        rows_computed_ctry += 1
                        total_rows_computed+=1
                        render(df, country, sector, seniority, size, age)

                            
    #     country_count_dict[country] = [rows_computed_ctry, counter_sparsity_treated]

    # render(df, 'GBR', 'Finance', 'Senior', '5001-10,000 employees', '25 to 34')
    # render(df, 'USA', 'IT', 'Director', '51-200 employees', '55+')
    
    print('total_rows_computed: ', total_rows_computed)

    df_finalized = df_finalized.set_index('index') # Set the orindinal index as the actual index
    indices_to_drop = list(set(indices_to_drop)) # Remove dupilicated indices
    assert df_finalized[df_finalized.index.duplicated()].shape[0] == 0 # Ensure there're no duplicates
    # print('len(indices_to_drop): ', len(indices_to_drop))
    # print('df_finalized shape before filter: ', df_finalized.shape)
    # is_not_treated = df_finalized['Is_sparsity_treated'] == False
    # df_finalized = df_finalized[is_not_treated]
    # # df_finalized = df_finalized[~df_finalized.index.isin(indices_to_drop)]
    # print('df_finalized shape after filter: ', df_finalized.shape)
    # print(df_finalized.columns)
    # print(df_finalized)


    for country, total_sparisty in country_count_dict.items():
        print('Country: ', country, '| ',  'Total and sparsity counts: ', total_sparisty)

    regression_prep()


    # save_path = f'intermediate/rank_dataframe/df_transformed_model.csv'
    # df_finalized.to_csv(save_path)

    

main()
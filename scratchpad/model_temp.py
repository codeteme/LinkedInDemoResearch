# This script computes the rank and produces a simple linear model to see what factors influence %female

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.compose import make_column_selector as col_selector

import streamlit as st



# Current working director: 
# /Users/tmt0947/Development/workspaces/QCRI/LinkedInDemoResearch 
df = pd.read_csv('processed/data_collection_2/dataset_transformed.csv')
# Drop unnecessary first columns
df.drop(df.columns[0], axis = 1, inplace = True)
# Only consider the four least-sparse ranks: selected_seniorities are Entry, Senior, Manager, and Director
selected_seniorities =  ['Entry', 'Senior', 'Manager', 'Director']
is_selected_seniorities = df['Job Seniority'].apply(lambda x: x in selected_seniorities) 
# df = df[is_selected_seniorities].reset_index()
st.write(df)

counter_sparsity_treated = 0 # keeps track of modified data frames
indices_to_drop = []

def increment_counter(): # calculate the total number of modified plots
    global counter_sparsity_treated 
    counter_sparsity_treated += 1

# select parameters
def df_specifier(df, country, sector): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector)) # Choose appropriate rows 
    return df.loc[idx]

def filter_reshape(df, country, sector): 
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

def df_column_encoder(df):
    # Choose all the non-numeric columns
    categorical_cols = col_selector(dtype_include=object)
    categorical_cols = categorical_cols(df)
    # Change all non-numerica columns to categorical columns 
    df[categorical_cols] = df[categorical_cols].astype('category')
    # Encode the values in each categorical column to integers
    df["Job Seniority"] = df["Job Seniority"].cat.codes
    df["Company Size"] = df["Company Size"].cat.codes
    df["Age Ranges"] = df["Age Ranges"].cat.codes

    return df

def makeCorrMatrix(df):
    
    df.drop(["Country","Sector"], axis=1, inplace = True) # Drop two specifier columns
    column_to_drop = ['Company Size', 'Any_Gender_any', 'Male_any', 'Female_any', 'Any_Gender_with', 'Male_with', 'Female_with','Is_sparsity_treated', 'Any_Gender_with:any', 'Male_with:any','male_any:any_any', 'Female_with:any']
    df = df.drop(columns = column_to_drop)
    fig, ax = plt.subplots()
    ax = df.corr()
    sns.heatmap(df.corr(), annot=True)
    st.pyplot(fig)
    
    return 

def render(df, country, sector): 
    df = df_specifier(df, country, sector)
    df = filter_reshape(df, country, sector)
    df = df_column_encoder(df)
    makeCorrMatrix(df)
    st.write(f'Country : {country}, Sector: {sector}')
    return 


def main(df):
    global counter_sparsity_treated # reminder: this variable keeps track of modified 

    countries = df['Country'].unique()
    sectors = df['Sector'].unique()

    counter = 0
    for country in countries: 
        for sector in sectors:
            counter += 1
            render(df, country, sector)
    
    assert(counter == 10) # There are 5 countries and 2 sectors so 5 * 2 = 10 matrices
main(df)
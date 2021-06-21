import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('processed/data_collection_2/dataset.csv')
# drop the two irrelevant index columns added when building the cleaned dataset imported above

df.drop(df.columns[[0, 1]], axis = 1, inplace = True)


# rename the colums
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
# replace all 0s by 1 so as to avoid arithmetic errors
df['Count'].replace(to_replace=0, value = 1, inplace = True)
# df['Count'].replace(to_replace=0, value = 290, inplace = True)

st.write(df)
# select parameters
def df_specifier(df, country, sector, size): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == size) & (df['Age Ranges'] == 'Any Age Range'))
    return df.loc[idx]


def filter_reshape(df, country, sector, size): 
    # split data to with connection and any connection
    df_with_connection = df[df['Connectivity Status'] == 'connected to big companies']
    df_any_connection = df[df['Connectivity Status'] == 'connected to any']

    df_with_connection = df_with_connection.groupby(["Job Seniority", "Gender"]).sum() # filter only job seniority and gender
    df_with_connection.reset_index(inplace=True) # Unstack the rows 
    df_with_connection = df_with_connection.pivot(index='Job Seniority', columns='Gender') # make values of Gender the columns headers
    # print(df_with_connection.head())

    df_any_connection = df_any_connection.groupby(["Job Seniority", "Gender"]).sum()
    df_any_connection.reset_index(inplace=True)
    df_any_connection = df_any_connection.pivot(index='Job Seniority', columns='Gender')
    # print(df_any_connection.head())


    df_reshaped = pd.merge(df_with_connection, df_any_connection, on='Job Seniority', suffixes=('_with_connection', '_any_connection'))

    df_reshaped['with_:_any', 'Any Gender'] = df_reshaped['Count_with_connection', 'Any Gender'] / df_reshaped['Count_any_connection', 'Any Gender']
    df_reshaped['with_:_any', 'Female'] = df_reshaped['Count_with_connection', 'Female'] / df_reshaped['Count_any_connection', 'Female']
    df_reshaped['with_:_any', 'Male'] = df_reshaped['Count_with_connection', 'Male'] / df_reshaped['Count_any_connection', 'Male']
    df_reshaped['Gender Proportion', 'Female'] = df_reshaped['Count_any_connection', 'Female'] / df_reshaped['Count_any_connection', 'Any Gender']
    df_reshaped['Gender Proportion', 'Male'] = df_reshaped['Count_any_connection', 'Male'] / df_reshaped['Count_any_connection', 'Any Gender']
    # df_reshaped['Male to Female', 'm:f'] = df_reshaped['with_:_any', 'Male'] / df_reshaped['with_:_any', 'Female']
    df_reshaped['Female to Male', 'f:m'] = df_reshaped['with_:_any', 'Female'] / df_reshaped['with_:_any', 'Male']


    # Sort the job seniorities
    sorting_dict = {'Unpaid': 0, 'Training': 1, 'Entry': 2, 'Senior': 3, 'Manager':4, 'Director': 5, 'VP': 6, 'CXO': 7, 'Partner': 8, 'Owner': 9, 'Any Job Security': 10}
    # df_reshaped.sort_values(by=df_reshaped.index, key=lambda x: x.map(sorting_dict), inplace=True)
    df_reshaped = df_reshaped.sort_index(key=lambda x: x.map(sorting_dict))

    return df_reshaped


def plotter(df): # plot
    # set the ticklabel font size globally (i.e. for all figures/subplots in a script) using rcParams:
    plt.rc('xtick',labelsize=8)
    plt.rc('ytick',labelsize=8)

    # df.index -> df['Job Seniorities']
    # df['Male to Female', 'm:f'] -> df['male:female']
    # df['Gender Proportion', 'Female'] -> df['female']

    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Job Seniorities')
    # ax1.set_ylabel('male:female', color=color)
    # ax1.plot(df.index, df['Male to Female', 'm:f'], color=color)
    ax1.set_ylabel('female:male', color=color)
    ax1.plot(df.index, df['Female to Male', 'f:m'], color=color)
    ax1.tick_params(axis='x', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('%\female', color=color)  # we already handled the x-label with ax1
    ax2.plot(df.index, df['Gender Proportion', 'Female'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


    # # Program will only end when plt.show returns, which is after you closed all figures.
    # plt.show(block=True)

    return fig

def filter_reshape_plot(df, country, sector, size):
    df = df_specifier(df, country, sector, size) # USA, IT, Big Companies
    df = filter_reshape(df, country, sector, size)
    fig = plotter(df)

    total_count = df.loc['Any Job Seniority':]['Count_any_connection', 'Any Gender'][0]
    fig_caption = f'Data aggregated for {country} {sector} {size} - {total_count}'
    plt.figtext(0.5, 0.0001, fig_caption, wrap=True, horizontalalignment='center', fontsize=12)

    st.write(fig)
    
    save_path = f'plots/plots_data_collection_2 2.1/_{country}_{sector}_{size}.png'
    # Uncomment to save figures
    fig.savefig(save_path)


def run_analysis():
    countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
    company_sizes = ['Any Company Size', '10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']
    sectors = ['IT', 'Finance']
    # filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')
    for country in countries: 
        for company_size in company_sizes:
            for sector in sectors: 
                filter_reshape_plot(df, country, sector, company_size)

    # filter_reshape_plot(df, 'GBR', 'Finance', 'Any Company Size')

    
run_analysis()

# filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')
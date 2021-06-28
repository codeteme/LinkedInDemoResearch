import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('processed/data_collection_2/dataset.csv')
# drop the two irrelevant index columns added when building the cleaned dataset imported above

df.drop(df.columns[[0, 1]], axis = 1, inplace = True)

# rename the colums
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']

st.write(df)

df_ratio = pd.DataFrame(columns = ['Country', 'Sector', 'Company Size', 'Ratio']) # dataframe for the ratio calculations of all permutations
df_rankorder = pd.DataFrame(columns = ['Country', 'Sector', 'Company Size', 'Seniority', 'Rank']) # dataframe that compute average rank value of each permutation
df_averagerank = pd.Series()
counter = 0 # keeps track of modified data frames

seniority_counter = 0
country_sector_permutation_counter = 0


def increment_counter(): # calculate the total number of modified plots
    global counter 
    counter += 1


# select parameters
def df_specifier(df, country, sector, size): 
    idx = np.where((df['Country'] == country) & (df['Sector'] == sector) & (df['Company Size'] == size) & (df['Age Ranges'] == 'Any Age Range'))
    return df.loc[idx]


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


def filter_reshape(df, country, sector, size): 
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
    df_reshaped =  df_reshaped.dropna()

    # Sort the job seniorities
    sorting_dict = {'Unpaid': 0, 'Training': 1, 'Entry': 2, 'Senior': 3, 'Manager':4, 'Director': 5, 'VP': 6, 'CXO': 7, 'Partner': 8, 'Owner': 9, 'Any Job Security': 10}
    # df_reshaped.sort_values(by=df_reshaped.index, key=lambda x: x.map(sorting_dict), inplace=True)
    df_reshaped = df_reshaped.sort_index(key=lambda x: x.map(sorting_dict))

    # print(df_reshaped['Female to Male']['f:m'].values)
    # print(df_reshaped)
    
    # Unpaid is a sparse data and is ignored completely
    global seniority_counter
    # if 'Unpaid' in df_reshaped.index: 
    #     seniority_counter += 1
    #     df_reshaped = df_reshaped.drop('Unpaid')
    # if 'Training' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'Entry' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'Senior' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'Manager' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'Director' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'VP' in df_reshaped.index: 
    #     seniority_counter += 1
    # if 'CXO' in df_reshaped.index: 
        # seniority_counter += 1
    # if 'Partner' in df_reshaped.index: 
        # seniority_counter += 1
    # if 'Owner' in df_reshaped.index: 
        # seniority_counter += 1
    # if 'Any Job Seniority' in df_reshaped.index: 
        # seniority_counter += 1

    # df_reshaped = df_reshaped.drop('Unpaid')
    # print(seniority_counter)
    return df_reshaped

def has_unpaid(df):
    return 'Unpaid' in df.index.values

def has_training(df):
    return 'Training' in df.index.values

def has_entry(df):
    return 'Entry' in df.index.values

def has_senior(df):
    return 'Senior' in df.index.values

def has_manager(df):
    return 'Manager' in df.index.values

def has_director(df):
    return 'Director' in df.index.values

def has_vp(df):
    return 'VP' in df.index.values

def has_cxo(df):
    return 'CXO' in df.index.values

def has_partner(df):
    return 'Partner' in df.index.values

def has_owner(df):
    return 'Owner' in df.index.values

def has_anyjobseniority(df):
    return 'Any Job Seniority' in df.index.values

def low_high_ratio(df, country, sector, size):
    
    if has_training(df) & has_entry(df): 
        training_fm = df.loc['Training']['Female to Male', 'f:m']
        entry_fm = df.loc['Entry']['Female to Male', 'f:m']
        numerator_ratio = min(training_fm, entry_fm)
        # print("Case 1")
    elif has_training(df): 
        training_fm = df.loc['Training']['Female to Male', 'f:m']
        numerator_ratio = training_fm
        # print("Case 2")
    elif has_entry(df): 
        entry_fm = df.loc['Entry']['Female to Male', 'f:m']
        numerator_ratio = entry_fm
        # print("Case 3")
    else: 
        numerator_ratio = np.nan
        # print("Case 4")


    if has_director(df) & has_vp(df):
        director_fm = df.loc['Director']['Female to Male', 'f:m']
        vp_fm = df.loc['VP']['Female to Male', 'f:m']
        denominator_ratio = max(director_fm, vp_fm)
        # print("Case 5")
    elif has_director(df):
        director_fm = df.loc['Director']['Female to Male', 'f:m']
        denominator_ratio = director_fm
        # print("Case 6")       
    elif has_vp(df):
        vp_fm = df.loc['VP']['Female to Male', 'f:m']
        denominator_ratio = vp_fm
        # print("Case 7")  
    else:
        denominator_ratio = np.nan
        # print("Case 8")
    
    
    ratio = numerator_ratio/denominator_ratio
    global df_ratio
    row_value = [country, sector, size, ratio]
    df_ratio_len = len(df_ratio)
    df_ratio.loc[df_ratio_len] = row_value

    # print(df_ratio)

    # save_path = f'intermediate/ratio_dataframes.py/df_ratio.csv'
    save_path = f'intermediate/ratio_dataframes.py/df_ratio.xlsx'

    # Uncomment to save df_ratio as a .csv file
    df_ratio.to_csv(save_path)
    df_ratio.to_excel(save_path)

    # print(df_ratio)

def rank_order(df, country, sector, size):
    global df_rankorder
    global df_averagerank
    global country_sector_permutation_counter

    df = df[df.index.isin(["Entry", "Senior", "Manager", "Director"])]

    # todo: Drop unpaid completely (for the analysis)
    # if has_unpaid(df) & has_training(df) & has_entry(df) & has_senior(df) & has_manager(df) & has_director(df) & has_vp(df) & has_cxo(df) & has_partner(df) & has_owner(df) & has_anyjobseniority(df):
    # if has_entry(df) & has_senior(df) & has_manager(df) & has_director(df) & has_vp(df) & has_cxo(df) & has_partner(df) & has_owner(df) & has_anyjobseniority(df):
    if has_entry(df) & has_senior(df) & has_manager(df) & has_director(df) :
        country_sector_permutation_counter += 1
        df['seniority'] = df.index
        df['rank'] = df['Female to Male', 'f:m'].rank()
        
        # for i in range(0, 11):
        # for i in range(0, 9):
        for i in range(0, 4):
            row_value = [country, sector, size, df['seniority'].iloc[i], df['rank'].iloc[i]]
            df_rankorder_len = len(df_rankorder)
            df_rankorder.loc[df_rankorder_len] = row_value
        
        print(country_sector_permutation_counter)

    # save_path = f'intermediate/rank_dataframe.py/df_rankorder.csv'
    # save_path = f'intermediate/rank_dataframe.py/df_rankorder.xlsx'
    # df_rankorder.to_csv(save_path)
    # df_rankorder.to_excel(save_path)

    # save_path = f'intermediate/rank_dataframe.py/df_rankorder_1.csv'
    save_path = f'intermediate/rank_dataframe.py/df_rankorder_2.csv'
    df_rankorder.to_csv(save_path)


def lenz(df):
    return len(df) == 0

def plotter(df):

    # Keep track of changes made and add note to the relevant plots
    is_sparsity_fix = False
    if(290 in df['Count_with_connection', 'Any Gender'].values):
        is_sparsity_fix = True
    if(290 in df['Count_with_connection', 'Female'].values):
        is_sparsity_fix = True
    if(290 in df['Count_with_connection', 'Male'].values):
        is_sparsity_fix = True
        
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
    ax1.set_ylim([0, 2])
    ax1.plot(df.index, df['Female to Male', 'f:m'], color=color, marker = "o")
    ax1.tick_params(axis='x', labelcolor=color)

    # print(sparsity_fix_counter)
    # print(is_sparsity_fix)
    if is_sparsity_fix == True: 
        ax1.text(0.5, -0.5, 'Changes have been made to this plot', horizontalalignment='center', verticalalignment='center')

    ## controls the extent of the plot.
    offset = 1.0 
    # ax1.set_xlim(min(x)-offset, max(x)+ offset)
    # ax1.set_ylim(min(df['Female to Male', 'f:m'])-offset, max(df['Female to Male', 'f:m'])+ offset)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('%\female', color=color)  # we already handled the x-label with ax1
    ax2.plot(df.index, df['Gender Proportion', 'Female'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


    # Program will only end when plt.show returns, which is after you closed all figures.
    # plt.show(block=True)

    return fig

def filter_reshape_plot(df, country, sector, size):
    df = df_specifier(df, country, sector, size) # USA, IT, Big Companies
    df = filter_reshape(df, country, sector, size)
    # low_high_ratio(df, country, sector, size)
    rank_order(df, country,sector,size)
    # fig = plotter(df)
    # total_count = 0
    # if lenz(df.loc['Any Job Seniority':]['Count_any_connection', 'Any Gender']):
    #     total_count == 0
    # else:
    #     total_count = df.loc['Any Job Seniority':]['Count_any_connection', 'Any Gender'][0]

    # fig_caption = f'Data aggregated for {country} {sector} {size} - {total_count}'
    # plt.figtext(0.5, 0.0001, fig_caption, wrap=True, horizontalalignment='center', fontsize=12)

    # st.write(fig)
    
    # save_path = f'plots/plots_data_collection_2 2.4/_{country}_{sector}_{size}.png'
    # # Uncomment to save figures
    # fig.savefig(save_path)


def run_analysis():

    global country_sector_permutation_counter

    countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
    company_sizes = ['Any Company Size', '10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']
    sectors = ['IT', 'Finance']

    
    # filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')

    # for country in countries: 
    #     for company_size in company_sizes:
    #         for sector in sectors: 
    #             filter_reshape_plot(df, country, sector, company_size)

    for country in countries: 
        for sector in sectors: 
            for company_size in company_sizes:
                filter_reshape_plot(df, country, sector, company_size)

    # for company_size in company_sizes:
    #     for sector in sectors: 
    #         filter_reshape_plot(df, 'USA', sector, company_size)

    # filter_reshape_plot(df, 'USA', 'Finance', 'Any Company Size')


    # print(country_sector_permutation_counter)

    global df_rankorder
    grouped_df = df_rankorder.groupby(['Country', 'Sector', 'Company Size']).count()
    print(grouped_df)

    st.write('Total Count of Modified Plots')
    st.write(counter)


run_analysis()

# filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')
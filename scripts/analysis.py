import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('intermediate/data_collection_2/temp_USA.csv')
# rename the column headers
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
print(df['Company Size'].unique())


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
    df_reshaped['Male to Female', 'm:f'] = df_reshaped['with_:_any', 'Male'] / df_reshaped['with_:_any', 'Female']

    # Sort the job seniorities
    sorting_dict = {'Unpaid': 0, 'Training': 1, 'Entry': 2, 'Senior': 3, 'Manager':4, 'Director': 5, 'VP': 6, 'CXO': 7, 'Partner': 8, 'Owner': 9, 'Any Job Security': 10}
    # df_reshaped.sort_values(by=df_reshaped.index, key=lambda x: x.map(sorting_dict), inplace=True)
    df_reshaped = df_reshaped.sort_index(key=lambda x: x.map(sorting_dict))


    return df_reshaped


def plotter(df): # plot
    # df = df.drop([0, 1])
    print(df.head())
    print(df.index)

    # df.index -> df['Job Seniorities']
    # df['Male to Female', 'm:f'] -> df['male:female']
    # df['Gender Proportion', 'Female'] -> df['female']

    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Job Seniorities')
    ax1.set_ylabel('male:female', color=color)
    ax1.plot(df.index, df['Male to Female', 'm:f'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

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
    df = filter_reshape(df, country, sector, size) # USA, IT, Big Companies)
    fig = plotter(df)
    
    save_path = f'plots/_{country}_{sector}_{size}.png'
    fig.savefig(save_path)


def run_analysis():
    company_sizes = ['Any Company Size', '10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']
    # filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')
    for company_size in company_sizes:
        filter_reshape_plot(df, 'USA', 'IT', company_size)
    
run_analysis()

# filter_reshape_plot(df, 'USA', 'IT', '10,001+ employees')
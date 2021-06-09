import pandas as pd
import numpy as np
"""
Replace 0s in Count column with np.nan; use df["Count"].replace({0: np.nan}, inplace=True)
Write functions that takes in a data frame and
→ drops the first column because all are US 
→ split the data frame into with_connection and any_connection based on the values of Company Industry. 
→ computes df.groupby(['Job Seniority', 'Gender']).sum()
Send the USA without exclusion files to the function. The expected outcome: 
**with_connection**
Unpaid | Female 
       | Male
       | Any Gender

concatenate the columns of with_connection and to any_connection if the multi-level index values of the two data frames matched.
→ df.set_index('key').join(other.set_index('key'))
add four additional columns: female, male, %-female, %-male, male/female. follow the computation on the shared Google Sheet.
"""
df = pd.read_csv("processed/filtered_noexclude_GBR.csv")


def grouper(df):
    return df.groupby(['Job Seniority','Gender'])['Count'].sum()

def clean(df):
    df.drop(df.columns[[0, 1]], axis = 1, inplace = True) # drop the redundant indexing columns and country values
    df["Count"].replace({0: np.nan}, inplace=True) # replace 0s with missing values
    with_any_connection = df[df['Company Industry'] == 'Any Company Industry']
    any_connection = df[df['Company Industry'] != 'Any Company Industry']
    with_any_connection = grouper(with_any_connection)
    any_connection = grouper(any_connection)
    # [] check the nature of index
    # df.reset_index(drop = True)
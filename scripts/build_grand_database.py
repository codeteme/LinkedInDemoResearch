"""
Countries: 5
Gender: 3
Sector: 2 
Job Seniority: 11
Company Size: 10
Age Ranges: 5
Recent Status: 4
Connectivity Status:2

For one country:    1 * 3 * 2 * 11 * 10 * 5 * 4 * 2 = 26,400
For all countries:  5 * 3 * 2 * 11 * 10 * 5 * 4 * 2= 132,000

"""

import pandas as pd
import glob

path = "intermediate/data_collection_2 _1" # parent folder
all_files = glob.glob(path + "/*.csv") # read all files ending with CSV

# Read and concatenate all csv files in the parent directory
df = pd.concat((pd.read_csv(f) for f in all_files)) 
assert(df.shape[0] == 132000) # There should be 132000 entries (26,400 * 5)

dict = {'0': 'Country',
        '1': 'Gender',
        '2': 'Sector',
        '3': 'Job Seniority',
        '4': 'Company Size',
        '5': 'Age Ranges',
        '6': 'Recent Status', 
        '7': 'Connectivity Status',
        '8': 'Count'}
  
# call rename () method
df.rename(columns=dict, inplace=True)

print(df.columns)
# It is a raw file as such it would be saved at raw folder
save_path = f'raw/dataset_2_1.xlsx'
df.to_excel(save_path, index=False)
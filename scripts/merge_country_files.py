# Removed unused imports
import pandas as pd
import os

# path to working directory
path = "intermediate/data_collection_2"
# files = [os.path.join(path, file) for file in os.listdir(path)]
# df = pd.concat((pd.read_csv(f) for f in files if f.endswith('csv')), ignore_index=True) # Remove index

df_IT = pd.read_csv(f'{path}/IT.csv')
df_IT =  df_IT.reset_index(drop=True)
df_Finance = pd.read_csv(f'{path}/Finance.csv')
df_Finance = df_Finance.reset_index(drop=True)

# rename column headers
df_IT.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
df_Finance.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']

# concatentate dataframes with sector IT and Finance
df = pd.concat([df_IT, df_Finance])

# export the final dataframe 
save_path = f'processed/data_collection_2/dataset.csv'
df.to_csv(save_path)
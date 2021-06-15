# Removed unused imports
import pandas as pd
import os

# path to working directory
path = "intermediate/data_collection_2 copy"
files = [os.path.join(path, file) for file in os.listdir(path)]
df = pd.concat((pd.read_csv(f) for f in files if f.endswith('csv')), ignore_index=True) # Remove index

# rename column headers
df.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']

# save_path = f'{path}/temp.csv'
# df.to_csv(save_path)
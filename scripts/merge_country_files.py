# Removed unused imports
import pandas as pd
import os

# df_extract_it = pd.read_csv('intermediate/data_collection_2 copy/temp_PHL.csv')
# df_extract_it.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
# df_extract_it = df_extract_it[df_extract_it['Sector'] == 'IT']
# df_extract_it = df_extract_it.reset_index(drop=True)
# # export the final dataframe 
# save_path = f'intermediate/data_collection_2/cleaned_IT.csv'
# df_extract_it.to_csv(save_path)

# df_extract_finance = pd.read_csv('intermediate/archive/archive_data_collection_2/data_collection_2 copy/temp_4.csv')
# df_extract_finance.columns = ['Country', 'Gender', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges', 'Connectivity Status', 'Count']
# df_extract_finance = df_extract_finance[df_extract_finance['Sector'] == 'Finance']
# df_extract_finance = df_extract_finance.reset_index(drop=True)
# # # export the final dataframe 
# save_path = f'intermediate/data_collection_2/cleaned_Finance.csv'
# df_extract_finance.to_csv(save_path)

# path to working directory
path = "intermediate/data_collection_2"
files = [os.path.join(path, file) for file in os.listdir(path)]
df = pd.concat((pd.read_csv(f) for f in files if f.endswith('csv')), ignore_index=True) # Remove index


# # export the final dataframe 
# save_path = f'processed/data_collection_2/dataset.csv'
# df.to_csv(save_path)

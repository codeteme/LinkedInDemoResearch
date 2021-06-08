# This script computes preliminary EDA. It output an html file 
import pandas as pd
import os
import glob
# from pandas_profiling import ProfileReport

path = os.getcwd()
# use glob to get all the csv files in the folder
csv_files = glob.glob(os.path.join(path, "processed", "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f)
    df = df.drop(df.columns[0], axis = 1) # Drop the redundant indexing columns
    print('File Name:', f.split("\\")[-1])
    print("shape: ", df.shape)
    print()


# df = pd.read_csv('../intermediate/output.csv')
# profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
# profile.to_file(output_file='preliminary_eda.html')
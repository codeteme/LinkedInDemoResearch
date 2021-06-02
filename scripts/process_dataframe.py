# This script computes preliminary EDA. It output an html file 

import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_csv('../intermediate/output.csv')
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file(output_file='preliminary_eda.html')
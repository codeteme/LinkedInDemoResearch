# clean allpermutations_noexclude_USA.csv
import pandas as pd

# df_USA = pd.read_csv('intermediate/allpermutations_noexclude_USA.csv')
# df_USA.columns = ["Country", "Gender", "Company Industry", "Age Range", "Job seniority", "Company Size", "Count"]
# is_USA = df_USA['Country'] == 'USA'
# df_USA = df_USA[is_USA]
# # df_USA.to_csv('processed/filtered_noexclude_USA.csv')
# df_GBR = pd.read_csv('intermediate/allpermutations_noexclude_temp_3.csv')
# df_GBR.columns =  ["Country", "Gender", "Company Industry", "Age Range", "Job seniority", "Company Size", "Count"]
# is_GBR = df_GBR['Country'] == 'GBR'
# df_GBR = df_GBR[is_GBR]
# # df_GBR.to_csv('processed/filtered_noexclude_GBR.csv')

df_VNM = pd.read_csv('intermediate/allpermutations_noexclude_temp_VNM.csv')
df_IND = pd.read_csv('intermediate/allpermutations_noexclude_temp_IND.csv')
df_PHL = pd.read_csv('intermediate/allpermutations_noexclude_temp_PHL.csv')
# A wrapper function that takes in a dataframe filter it by country
def filter_by_country(df, country):
    df.columns = ["Country", "Gender", "Company Industry", "Age Range", "Job seniority", "Company Size", "Count"]
    is_selected_cntry = df['Country'] == country
    df = df[is_selected_cntry]
    return df
# A helper function that takes in a filtered dataframe then extracts the specified
def df_to_csv(df):
    country = df['Country'][0]
    directory = f"processed/filtered_noexclude_{country}.csv"
    df.to_csv(directory)
    return 

def filter_and_export(df, country):
    filtered = filter_by_country(df, country)
    df_to_csv(filtered)

# Uncomment to filter and export the data generated through the api calls. 
# filter_and_export(df_VNM, 'VNM')
# filter_and_export(df_IND, 'IND')
# filter_and_export(df_PHL, 'PHL')
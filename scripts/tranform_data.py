import pandas as pd

df = pd.read_csv('processed/data_collection_2/dataset.csv')
# Drop unnecessarily first columns
df.drop(df.columns[[0, 1]], axis = 1, inplace = True)

df_transformed = pd.DataFrame()

print('Original shape of the imported dataset - dataset.csv: ', df.shape)
# Original shape of the imported dataset - dataset.csv:  (33000, 8)


def transform(df, country, sector, company_size, job_seniority, age_range): 
    global df_transformed

    assert (country in df['Country'].values)
    assert (sector in df['Sector'].values)
    assert (company_size in df['Company Size'].values)
    assert (job_seniority in df['Job Seniority'].values)
    assert (age_range in df['Age Ranges'].values)

    is_selected_country = df['Country'] == country
    is_selected_sector = df['Sector'] == sector
    is_selected_companysize = df['Company Size'] == company_size
    is_selected_job_seniority = df['Job Seniority'] == job_seniority
    is_selected_age_range = df['Age Ranges'] == age_range

    is_female_gender = df['Gender'] == 'Female'
    is_male_gender = df['Gender'] == 'Male'
    is_any_gender = df['Gender'] == 'Any Gender'

    is_connected_to_big = df['Connectivity Status'] == 'connected to big companies'
    is_connected_to_any = df['Connectivity Status'] == 'connected to any'

    # Filter data frame for given country, sector, company_size, job_seniority, age_range.
    df = df[is_selected_country & is_selected_sector & is_selected_companysize & is_selected_job_seniority & is_selected_age_range]

    # Initialize the 6 (3 gender * 2 connecitivty status) colums with 0 count
    df['Any_Gender_any'] = df[is_any_gender & is_connected_to_any]['Count']
    df['Male_any'] = df[is_male_gender & is_connected_to_any]['Count'] 
    df['Female_any'] = df[is_female_gender & is_connected_to_any]['Count']

    df['Any_Gender_with'] = (df[is_any_gender & is_connected_to_big])['Count']
    df['Male_with'] = df[is_male_gender & is_connected_to_big]['Count'] 
    df['Female_with'] = df[is_female_gender & is_connected_to_big]['Count']



    df = df.fillna(0)
    df = df.drop(['Gender', 'Count'], axis=1) # todo: drop count 

    # todo: 
    # Minor: maybe re-order the columns so that you have the three "*_any" values first. Later, you can then add more counts (e.g. by "willingness to relocate".
    # That way, you first have the three "baseline" values, followed by groups of three values for each thing we're considering.

    df = df.groupby(['Country', 'Sector', 'Job Seniority', 'Company Size', 'Age Ranges']).sum() # filter only job seniority and gender
    df.reset_index(inplace=True) # Unstack the rows 
    df_transformed = df_transformed.append(df)
    return df

def main(): # Create# For a given Country, Sector, Company Size, Job Seniority and Age Ranges.
    global df_transformed

    countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
    sectors = ['IT', 'Finance']
    company_sizes = ['Any Company Size', '10,001+ employees', '5001-10,000 employees',
                        '1001-5000 employees', '501-1000 employees', '201-500 employees',
                        '51-200 employees', '11-50 employees', '2-10 employees', 'Myself Only']
    job_seniorities = ['Any Job Seniority', 'Owner', 'Partner', 'CXO', 'VP', 'Director', 'Manager', 'Senior', 'Entry', 'Training', 'Unpaid']
    ageranges = ['Any Age Range', '18 to 24', '25 to 34', '35 to 54', '55+']
    connectivity_statuses = ['connected to big companies', 'connected to any']


    # country = 'USA'
    # sector  = 'IT'
    # company_size = '51-200 employees'
    # job_seniority = 'Manager'
    # age_range = '25 to 34'

    for country in countries:
        for sector in sectors:
            for company_size in company_sizes:
                for job_seniority in job_seniorities: 
                    for age_range in ageranges:
                        transform(df, country, sector, company_size, job_seniority, age_range)

    # transform(df, country, sector, company_size, job_seniority, age_range)
    df_transformed = df_transformed.reset_index(drop=True)
    print(df_transformed)

    print('Final shape of the transformed data - dataset_transformation.csv: ', df_transformed.shape)
    # Final shape of the transformed data - dataset_transformation.csv: 5500
    # save_path = f'processed/data_collection_2/dataset_transformed.csv'
    # df_transformed.to_csv(save_path)    

main()

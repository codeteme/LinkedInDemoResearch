# This page creates pandas dataframes out of the scripts
import pandas as pd
import pandas_profiling as pp 

discrepancy_in_number = pd.read_csv("../raw/IT Decision Makers - GCC - Discrepancy in number o 747a51891ac94016bb4df19a97a4efc9.csv", na_values=['(NA)']).fillna(0)
# dataframe name abbreviated for convinience
di_number = discrepancy_in_number
# pp.ProfileReport(di_number).to_file('../intermediate/profile_report_di_number.html') 


discrepancy_in_open_relocate = pd.read_csv("../raw/IT Decision Makers - GCC - Discrepancy in willingn c4e7801ef5994e97a518115dc70a4ee9.csv",  na_values=['(NA)']).fillna(0)
# dataframe name abbreviated for convinience
di_open_relocate = discrepancy_in_open_relocate
cols_di_open_relocate = di_open_relocate.columns.drop('Country')
di_open_relocate[cols_di_open_relocate] = di_open_relocate[cols_di_open_relocate].apply(pd.to_numeric, errors='coerce')

pp.ProfileReport(di_open_relocate).to_file('../intermediate/profile_report_di_open_relocate.html') 


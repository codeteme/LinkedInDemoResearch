import pandas as pd

df = pd.read_csv('../raw/countries_and_their_2 digit_codes.csv')

country_alpha2 = dict(zip(df['Name'], df['Code']))





# LinkedInDemoResearch
Using LinkedIn Campaign Manager audience count data to pursue social science research.

Users can specify the attributes for the following variables: 
- Interface locale (required)
- Location (required)
- Gender
- Age range 
- Job seniority
 
Users can also append multiple boolean arguments. The following three are supported.
- OR 
- AND
- NOT

User can choose among the following list of countries:

(['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'The Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Republic of the Congo', 'Congo (DRC)', 'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern and Antarctic Lands', 'Gabon', 'The Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Vatican City', 'Honduras', 'Hong Kong SAR', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'South Korea', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Macao SAR', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'French-Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Norway', 'Oman', 'Pakistan', 'Palestinian Authority', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Serbia', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthelemy', 'Saint Pierre and Miquelon', 'São Tomé and Príncipe', 'Saudi Arabia', 'Senegal', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and South Sandwich Islands', 'South Sudan', 'Spain', 'Sri Lanka', 'Suriname', 'Eswatini', 'Sweden', 'Switzerland', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'US Virgin Islands', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])



Users can specify from the avaiable attributes. Here are all the supported specifications. 

location: refer to list above
gender: female and male
age segments: 18 - 24, 25 to 34, 35 - 44, 55+
job seniority: 
company:

Users can also exclude any attributes. For example NO Men aged 55+ from Mali


In total, there were a total of three rounds of data collection. Each one builds on top of the other. For example, the last round contains all the variables in the previous round in addition to "recency status".

analysis.py reads in the processed data, produces plots and configures the streamlit app to view plots.

build_grand_database.py reads in all five files (each corresponding to the five countries) then merges them to build one grand file. 

get_alpha2_alpha3.py gets the country names with their respective two digit codes. 

merge_country_files.py finds and merges all files in a given directory.

model.py is probably the most important script. It reads in the processed data and generates a correlation matrix according with a regression model. 

parser.py was used to test the header file later used to send in the request string (the authentication segment). 

The query builder script contains the main code to build and send the request string. 
variables_dictionaries.py contains all the possible values for each of the inputs - location, gender, job seniorty, member behavior, company industry and company size. 

requester.py contans request sender and reponse parser. More specifically, you can copy and paste the request header from browser's network panel getHeadersFromFirefox converts the string that you can copy in the firefox developer tools (tab network, right click on 1 request -> copy request-header) to a header that can be used

temporary.py is a set up for debugging purposes and does not add any value. 

Sat 4, 2023 | test.py is the new script I added. It's a streamlit app. It takes in a user input. The input is a drop down list of supported countries. 
            The app then returns a table of 'spend', 'reach', 'cost per 1,000 member accounts reached', 'average frequency' of a day, week and month periods.
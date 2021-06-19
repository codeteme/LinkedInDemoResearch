import re # module to work with RegEx
import time # api request needs to be timed
#  Import all the API supported specifiable variables 
from variables_dictionaries import * # imports locationsegments, agerangesegments, etc ...
from requester import * # imports request sender and reponse parser

# TODO: Add %20 to name of every variable for example instead of Member Gender put in Member%20Gender


def linkedinEncodeURL(strout):
   strout = re.sub(r':li:((\w)+)+:',r'%3Ali%3A\1%3A',strout)
   strout = strout.replace('\n','')
   return strout
   
def encodeInner(strout):
   strout = strout.replace(' ', '%20')
   strout = strout.replace(':', '%3A')
   strout = strout.replace('\n', '')
   strout = strout.replace('(', '%28')
   strout = strout.replace(')', '%29')
   strout = strout.replace(',', '%2C')
   strout = strout.replace('&', '%26')
   
   return strout

# test if the encoding works
def encodeTest():
    testurl = '''urn:urn:li:seniority:8,name:CXO,facetUrn:urn:li:adTargetingFacet:seniorities),(urn:urn:li:seniority:10,name:Owner,facetUrn:urn:li:adTargetingFacet:seniorities),'''
    assert linkedinEncodeURL(testurl) =='urn:urn%3Ali%3Aseniority%3A8,name:CXO,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),(urn:urn%3Ali%3Aseniority%3A10,name:Owner,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),'

# Assume interface locale andlocation are dealt with
# tc = """q=targetingCriteria&cmTargetingCriteria= "

def locale_builder():
    req = "(or:List((facet:(urn:urn:li:adTargetingFacet:interfaceLocales,name:Interface%20Locales),segments:List((urn:urn:li:locale:en_US,name:English,facetUrn:urn:li:adTargetingFacet:interfaceLocales)))))"
    return req

def location_builder(locations):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:locations,name:Locations),segments:List("""
    for i,location in enumerate(locations):
    #(urn:urn:li:geo:101282230,name:Germany,facetUrn:urn:li:adTargetingFacet:locations)
        conc += "(urn:" + encodeInner(location['urn']) 
        conc += ",name:" + encodeInner(location["name"])
        conc += ",facetUrn:" + encodeInner(location['facetUrn']) 
        conc += ")"
        if i<len(locations)-1:
            conc +=","
    conc += """))))"""
    return conc


# Manually add the space string variant
def gender_builder(genders): 

    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:genders,name:Member%20Gender),segments:List("""
    for i,gender in enumerate(genders):
        #(urn:urn:li:locale:de_DE,name:German,facetUrn:urn:li:adTargetingFacet:interfaceLocales)
        conc += "(urn:" + encodeInner(gender['urn']) 
        conc += ",name:" + encodeInner(gender["name"])
        conc += ",facetUrn:" + encodeInner(gender['facetUrn']) 
        conc += ")"
        if i<len(genders)-1:
            conc +=","
    conc += """))))"""
    return conc

# Manually add the space string variant i.e. %20
def age_builder(ageranges): 
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:ageRanges,name:Member%20Age),segments:List("""
    for i,agerange in enumerate(ageranges):
        conc += "(urn:" + encodeInner(agerange['urn']) 
        conc += ",name:" + encodeInner(agerange["name"])
        conc += ",facetUrn:" + encodeInner(agerange['facetUrn']) 
        conc += ")"
        if i<len(ageranges)-1:
            conc +=","
    conc += """))))"""
    return conc



def jobseniority_builder(jobseniorities): 
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:seniorities,name:Job%20Seniorities),segments:List("""
    for i,jobseniority in enumerate(jobseniorities): 
        conc += "(urn:" + encodeInner(jobseniority['urn']) 
        conc += ",name:" + encodeInner(jobseniority["name"])
        conc += ",facetUrn:" + encodeInner(jobseniority['facetUrn']) 
        conc += ")"
        if i<len(jobseniorities)-1:
            conc +=","
    conc += """))))"""
    return conc

def employer_builder(employers):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:employers,name:Company%20Names),segments:List("""
    for i,employer in enumerate(employers): 
        conc += "(urn:" + encodeInner(employer['urn']) 
        conc += ",name:" + encodeInner(employer["name"])
        conc += ",facetUrn:" + encodeInner(employer['facetUrn']) 
        conc += ")"
        if i<len(employers)-1:
            conc +=","
    conc += """))))"""
    return conc

# memberbehavior
def memberbehavior_builder(memberbehaviors):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:memberBehaviors,name:Member%20Traits),segments:List("""
    for i, memberbehavior in enumerate(memberbehaviors): 
        conc += "(urn:" + encodeInner(memberbehavior['urn']) 
        conc += ",name:" + encodeInner(memberbehavior["name"])
        conc += ",facetUrn:" + encodeInner(memberbehavior['facetUrn']) 
        conc += ")"
        if i<len(memberbehaviors)-1:
            conc +=","
    conc += """))))"""
    return conc

def companyindustry_builder(companyindustries):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:industries,name:Company%20Industries),segments:List("""
    for i, companyindustry in enumerate(companyindustries): 
        conc += "(urn:" + encodeInner(companyindustry['urn']) 
        conc += ",name:" + encodeInner(companyindustry["name"])
        conc += ",facetUrn:" + encodeInner(companyindustry['facetUrn']) 
        conc += ")"
        if i<len(companyindustries)-1:
            conc +=","
    conc += """))))"""
    return conc

def companysize_builder(companysizes):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:staffCountRanges,name:Company%20Size),segments:List("""
    for i, companysize in enumerate(companysizes): 
        conc += "(urn:" + encodeInner(companysize['urn']) 
        conc += ",name:" + encodeInner(companysize["name"])
        conc += ",facetUrn:" + encodeInner(companysize['facetUrn']) 
        conc += ")"
        if i<len(companysizes)-1:
            conc +=","
    conc += """))))"""
    return conc

def exclude_builder(excludes):
    conc = """(or:List((facet:(urn:urn:li:adTargetingFacet:employers,name:Company%20Names),segments:List("""
    for i, exclude in enumerate(excludes): 
        conc += "(urn:" + encodeInner(exclude['urn']) 
        conc += ",name:" + encodeInner(exclude["name"])
        conc += ",facetUrn:" + encodeInner(exclude['facetUrn']) 
        conc += ")"
        if i<len(excludes)-1:
            conc +=","
    conc += """))))"""
    return conc

# returns OR concatenated query string 
def OR_builder(args):
    conc = "(or:List("
    for arg in args: 
        conc += str(arg)[9:-2]
        conc += ","
    conc = conc[:-1] # remove the last comma
    conc += "))"
    return conc
        
# concatenates with AND 
def AND_builder(args):
    answer = ""
    for arg in args: 
        answer += str(arg) + ","
    return answer[:-1] # removes the last comma 

# returns NOT concatenated query string
def NOT_builder(args): 
    if args == []: 
        return "exclude:(or:List())"
    conc = "exclude:"
    conc += OR_builder(args)
    return conc

# def exclusion_script(sector):
#     if sector == 'IT_info': 
#         return bigfive_exclusion_script
#     elif sector == 'Finance_info':
#         return bigbank_exclusion_script


# Concatenates all the different request string components
def include_all():
    print("chk pt. include_all() is executed")
    # output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + NOT_builder(exclude_list) + ")"
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + exclusion_script

    return linkedinEncodeURL(output)

# Calls the requesting function and parse the return count
def make_call():
    criteria = include_all()
    print(criteria)
    count = getCount(criteria)
    return count

# 5 countries * 3 genders * 2 sectors * 7 senioritis * 6 company sizes * 6 age groups * 2 connectivity status * 4 recent status| exclusion based on sector value

# Initialize an empty list to be populated by each item in segment (from library)
country_list = [] 
gender_list = [] 
companyindustry_list = []
jobseniority_list = [] 
companysize_list = []
agerange_list = [] 
recentstatus_list = ['any recent status', 'recently promoted', 'recently relocated', 'recently switched jobs']
print(type(recentstatus_list))
for elem in recentstatus_list:
    if elem == 'any recent status':
        print(elem)
    else:
        print('asd')
connection_list = ['connected to any', 'connected to big companies']

any_gender = 'Any Gender'
any_companyindustry = 'Any Company Industry'
any_jobseniority = 'Any Job Seniority'
any_companysize = 'Any Company Size'
any_agerange = 'Any Age Range'
any_companyconnection = 'Any Company Connection'
any_connection = 'connected to any'
any_recentstatus = 'any recent status'

selected_countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
# select any country or countries in the following manner
# selected_countries = ['USA']


IT_company_industry = ["Internet", "Information Technology & Services", "Computer Software", "Computer & Network Security", "Computer Hardware", "Computer Networking", "Wireless", "Telecommunications", "Semiconductors", "Nanotechnology", "Consumer Electronics"]
Finance_company_industry = ["Banking", "Capital Markets", "Financial Services", "Insurance", "Investment Banking", "Investment Management", "Venture Capital & Private Equity"]


# Generate IT and Finance query string ready to pass to arg_list
it_list = []
for companyindustry in IT_company_industry:
    companyindustry_info = companyindustrysegments.get(companyindustry)
    it_list.append(companyindustry_info)
finance_list = []
for companyindustry in Finance_company_industry:
    companyindustry_info = companyindustrysegments.get(companyindustry)
    finance_list.append(companyindustry_info)

company_industry_info_dict = dict()
# comment to exclude a sector
company_industry_info_dict['IT_info'] = it_list
company_industry_info_dict['Finance_info'] = finance_list


arg_list = [locale_builder()]

exclusion_script = []
bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
connection_script = []
bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"

recently_promoted_script =  "(or:List((facet:(urn:urn:li:adTargetingFacet:memberBehaviors,name:Member%20Traits),segments:List((urn:urn:li:memberBehavior:18,name:Recently%20Promoted,facetUrn:urn:li:adTargetingFacet:memberBehaviors)))))"
recently_relocated_script = "(or:List((facet:(urn:urn:li:adTargetingFacet:memberBehaviors,name:Member%20Traits),segments:List((urn:urn:li:memberBehavior:15,name:Recently%20Relocated,facetUrn:urn:li:adTargetingFacet:memberBehaviors)))))"
recently_switchedjobs_script = "(or:List((facet:(urn:urn:li:adTargetingFacet:memberBehaviors,name:Member%20Traits),segments:List((urn:urn:li:memberBehavior:20,name:Recently%20Switched%20Jobs,facetUrn:urn:li:adTargetingFacet:memberBehaviors)))))"

# Intialize an empty dataframe with only column names
df = pd.DataFrame()

for country in selected_countries:
    country_info = locationsegments.get(country)
    country_list.append(country_info)
    arg_list.append(location_builder(country_list))
    row_value = []
    row_value.append(country)

    for gender in gendersegments.keys():
        if gender != any_gender:
            gender_info = gendersegments.get(gender)
            gender_list.append(gender_info)
            arg_list.append(gender_builder(gender_list))
            row_value.append(gender)
        else:
            row_value.append(any_gender)
        
        for sector in company_industry_info_dict.keys():
            if sector == 'IT_info':
                # parameter passed to exclude_builder should be a list so I have put it in one
                sector_list = company_industry_info_dict.get(sector)
                arg_list.append(companyindustry_builder(sector_list))
                exclusion_script = bigfive_exclusion_script
                row_value.append('IT')
            elif sector == 'Finance_info':
                sector_list = company_industry_info_dict.get(sector)
                arg_list.append(companyindustry_builder(sector_list))
                exclusion_script = bigbank_exclusion_script
                row_value.append('Finance')
            
            for jobseniority in jobsenioritysegments.keys():
                if jobseniority != any_jobseniority:
                    jobseniority_info = jobsenioritysegments.get(jobseniority)
                    jobseniority_list.append(jobseniority_info)
                    arg_list.append(jobseniority_builder(jobseniority_list))
                    row_value.append(jobseniority)
                else: 
                    row_value.append(any_jobseniority)

                for companysize in companysizesegments.keys(): # iterate through segment and get name of element
                    if companysize != any_companysize:
                        companysize_info = companysizesegments.get(companysize) # extract the corresponding value of the element
                        companysize_list.append(companysize_info) # add element information to the list 
                        arg_list.append(companysize_builder(companysize_list)) # pass the processed list to build query 
                        row_value.append(companysize)
                    else: 
                        row_value.append(any_companysize)
                    
                    for agerange in agerangesegments.keys():
                        if agerange != any_agerange:
                            agerange_info = agerangesegments.get(agerange)
                            agerange_list.append(agerange_info)
                            arg_list.append(age_builder(agerange_list))
                            row_value.append(agerange) 
                        else: 
                            row_value.append(any_agerange)
                        
                        for recentstatus in recentstatus_list:
                            if recentstatus == any_recentstatus:
                                row_value.append(recentstatus)
                            elif recentstatus == 'recently promoted':
                                arg_list.append(recently_promoted_script)
                                row_value.append(recentstatus)
                            elif recentstatus == 'recently relocated':
                                arg_list.append(recently_relocated_script)
                                row_value.append(recentstatus)
                            elif recentstatus == 'recently switched jobs':
                                arg_list.append(recently_switchedjobs_script)
                                row_value.append(recentstatus)
                            else:
                                row_value.append('Unknown')

                            for connection in connection_list:
                                if connection == 'connected to any': 
                                    row_value.append(connection)
                                elif connection == 'connected to big companies' and sector == 'IT_info': 
                                    arg_list.append(bigfive_connection_script)
                                    row_value.append(connection)
                                elif connection == 'connected to big companies' and sector == 'Finance_info': 
                                    arg_list.append(bigbank_connection_script)
                                    row_value.append(connection)
                                    
                                count =  make_call() # makes the api call then parses and shows count
                                # # Handles ConnectionError exception that may be raised during execution 
                                # while True:
                                #     try:
                                #         count =  make_call() # makes the api call then parses and shows count
                                #         print("count is executed")
                                #         break
                                #     except:
                                #         # print("exception")
                                #         time.sleep(5) # Retry every five seconds

                                row_value.append(count)
                                row = pd.Series(row_value)
                                row_df = pd.DataFrame([row])
                                df = pd.concat([row_df, df], ignore_index=True)
                                print(df.head())
                                print("row value", row_value)

                                row_value.pop() # remove the count value
                                time.sleep(2)
                                save_path = f'intermediate/data_collection_3/temp_{country}.csv'
                                df.to_csv(save_path, index=False)

                                if connection != any_connection: 
                                    arg_list.pop() # reomve the last added query parameter which is the connectivity status variable 
                                row_value.pop() # remove the connectivity status value
                        
                            if recentstatus != any_recentstatus:
                                arg_list.pop() # reomve the last added query parameter which is the recent status variable 
                            row_value.pop()# remove the recent status value
            
                        if agerange != any_agerange:
                            arg_list.pop() # remove the last added query parameter which is the age range variable
                            agerange_list.pop() # empty the list to step to the next element in the list
                        row_value.pop() # remove the age range value
                    
                    if companysize != any_companysize:
                        arg_list.pop() # remove the last added query parameter which is the current variable
                        companysize_list.pop() # empty the list to step to the next element in the list
                    row_value.pop() # remove the company size value
            
                if jobseniority != any_jobseniority:
                    arg_list.pop() # remove the last added query parameter which is the job seniority variable
                    jobseniority_list.pop() # empty the list to step to the next element in the list
                row_value.pop() # remove the job seniority value

            # There is no list to append to or remove from + there 
            arg_list.pop() # remove the last added query parameter which is the sector variable
            row_value.pop() # remove the company size value

        if gender != any_gender: # If gender is specified
            arg_list.pop() # remove the last added query parameter which is the gender variable
            gender_list.pop() # empty the list to step to the next element in the list
        row_value.pop() # remove the gender value
             
    arg_list.pop() # remove the last added query parameter which is the location variable
    country_list.pop() # empty the list to step to the next element in the list
    row_value.clear() # remove the location value

df.columns = ["Country", "Gender", "Sector", "Job Seniority", "Company Size", "Age Ranges", "Recent Status", "Connectivity Status", "Count"]
df.to_csv('intermediate/data_collection_3/temp.csv', index=False)



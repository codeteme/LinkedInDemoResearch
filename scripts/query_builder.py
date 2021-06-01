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

# Concatenates all the different request string components
def include_all():
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + NOT_builder(exclude_list) + ")"
    return linkedinEncodeURL(output)

# Calls the requesting function and parse the return count
def make_call():
    criteria = include_all()
    count = getCount(criteria)
    return count

# Specify countries
selected_countries = ['USA']
country_list = []
for country in selected_countries:
    country_info = locationsegments.get(country)
    country_list.append(country_info)

# # Specify genders 
# selected_genders = ["Male"]
# gender_list = []
# for gender in selected_genders:
#     gender_info = gendersegments.get(gender)
#     gender_list.append(gender_info)

exclude_list = []

arg_list = [
    locale_builder(), 
    location_builder(country_list)]

# Intialize an empty dataframe with only column names
df = pd.DataFrame() 

gender_list = [] # Initialize an empty list to be populated by each item in segment (from library) 
jobseniority_list = [] # Initialize an empty list to be populate by each item in segment (from library)
employer_list = [] # Initialize an empty list to be populate by each item in segment (from library)

for gender in gendersegments.keys():
    print("*****************")
    print("*****************")
    gender_info = gendersegments.get(gender)
    gender_list.append(gender_info)
    arg_list.append(gender_builder(gender_list))
    row_value = ['US']
    row_value.append(gender) 
    
    for jobseniority in jobsenioritysegments.keys():
        jobseniority_info = jobsenioritysegments.get(jobseniority)
        jobseniority_list.append(jobseniority_info)
        arg_list.append(jobseniority_builder(jobseniority_list))
        row_value.append(jobseniority)

        for employer in employersegments.keys(): # iterate through segment and get name of element
            employer_info = employersegments.get(employer) # extract the corresponding value of the element
            employer_list.append(employer_info) # add element information to the list 
            arg_list.append(employer_builder(employer_list)) # pass the list to build query 
            row_value.append(employer)
            count =  make_call() # makes the api call and parses and prints count
            row_value.append(count)
            row = pd.Series(row_value)
            row_df = pd.DataFrame([row])
            df = pd.concat([row_df, df], ignore_index=True)
            print(df.head())
            arg_list.pop() # remove the last added query parameter which is the current variable
            employer_list.pop() # empty the list to step to the next element in the list
            row_value.pop() # remove the count value
            row_value.pop() # remove the employer value
            time.sleep(3) # set a timer so linkedin does not suspect a bot and block service
        
        arg_list.pop() # remove the last added query parameter which is the job seniority variable
        jobseniority_list.pop() # empty the list to step to the next element in the list
        row_value.pop() # remove the job seniority value

    arg_list.pop() # remove the last added query parameter which is the gender variable
    gender_list.pop() # empty the list to step to the next element in the list
    row_value.clear() # remove the gender value
        

df.columns = ["Country", "Gender", "Job seniority", "Employer", "Count"]
df.to_csv('../intermediate/output.csv', index=False)





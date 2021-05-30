import re
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

# Specify countries
selected_countries = ['USA']
country_list = []
for country in selected_countries:
    country_info = locationsegments.get(country)
    country_list.append(country_info)

# Specify genders 
selected_genders = ["Female"]
gender_list = []
for gender in selected_genders:
    gender_info = gendersegments.get(gender)
    gender_list.append(gender_info)

# Select age range
selected_ageranges = ["18 to 24"]
agerange_list = []
for agerange in selected_ageranges:
    agerange_info = agerangesegments.get(agerange)
    agerange_list.append(agerange_info)

# Select job seniority
selected_jobseniority = ["Owner"]
jobseniority_list = []
for jobseniority in selected_jobseniority:
    jobseniority_info = jobsenioritysegments.get(jobseniority)
    jobseniority_list.append(jobseniority_info)

# Select company
selected_employers = ["Facebook"]
employer_list = []
for employer in selected_employers:
    employer_info = employersegments.get(employer)
    employer_list.append(employer_info)

# Specify genders 
# selected_genders_1 = ["Female"]
# gender_list_1 = []
# for gender in selected_genders_1:
#     gender_info = gendersegments.get(gender)
#     gender_list_1.append(gender_info)

# # Specify genders 
# selected_genders_2 = ["Male"]
# gender_list_2 = []
# for gender in selected_genders_2:
#     gender_info = gendersegments.get(gender)
#     gender_list_2.append(gender_info)

# # Select age range
# selected_ageranges_1 = ["25 to 34"]
# agerange_list_1 = []
# for agerange in selected_ageranges_1:
#     agerange_info = agerangesegments.get(agerange)
#     agerange_list_1.append(agerange_info)

# selected_ageranges_2 = ["18 to 24"]
# agerange_list_2 = []
# for agerange in selected_ageranges_2:
#     agerange_info = agerangesegments.get(agerange)
#     agerange_list_2.append(agerange_info)

# # Lengthy or connected queries work
# or_connected_1 = OR_builder([gender_builder(gender_list_1), age_builder(agerange_list_1)])
# or_connected_2 = OR_builder([gender_builder(gender_list_2), age_builder(agerange_list_2)])
# or_connected_3 = OR_builder([or_connected_1, or_connected_2])

# or_connected
exclude_list = []
# exclude_list = [OR_builder([jobseniority_builder(seniority_list)])]

# arg_list = [locale_builder(), 
#             location_builder(country_list),
#             or_connected_3]

# arg_list = [locale_builder(), 
#             location_builder(country_list),
#             gender_builder(gender_list),
#             age_builder(agerange_list),
#             employer_builder(employer_list)]

arg_list = [
    locale_builder(), 
    location_builder(country_list),
    gender_builder(gender_list),
    jobseniority_builder(jobseniority_list),
    employer_builder(employer_list)
    ]

def include_all():
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + NOT_builder(exclude_list) + ")"
    return linkedinEncodeURL(output)

criteria = include_all()
count = getCount(criteria)
print(count)




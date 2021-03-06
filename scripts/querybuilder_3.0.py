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


# Concatenates all the different request string components
def include_all():
    print("chk pt. include_all() is executed")
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + exclusion_script

    return linkedinEncodeURL(output)

# Calls the requesting function and parse the return count
def make_call():
    criteria = include_all()
    print(criteria)
    count = getCount(criteria)
    return count

# 5 countries * 3 genders * 2 sectors * 7 senioritis * 2 connectivity status| exclusion based on sector value

# Initialize an empty list to be populated by each item in segment (from library)
country_list = [] 
gender_list = [] 
companyindustry_list = []
jobseniority_list = [] 

connection_list = ['connected to any', 'connected to big companies']

any_gender = 'Any Gender'
any_companyindustry = 'Any Company Industry'
any_jobseniority = 'Any Job Seniority'
any_companyconnection = 'Any Company Connection'
any_connection = 'connected to any'

selected_countries = ['USA', 'GBR', 'VNM', 'IND', 'PHL']
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
# company_industry_info_dict['IT_info'] = it_list
company_industry_info_dict['Finance_info'] = finance_list


arg_list = [locale_builder()]

exclusion_script = []
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Facebook
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Apple
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Amazon Web Services
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Microsoft
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Google
# bigfive_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"


# bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No JP Morgan
# bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No JP Asset Management
# bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No JP Morgan Chase & Co
# bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Chase
# bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"
# No Goldman Sachs
bigbank_exclusion_script = "exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))))"

connection_script = []
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No Facebook
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No Apple
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No Amazon Web Services
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No Microsoft
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1441,name:Google,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No Google
# bigfive_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A162479,name:Apple,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A2382910,name:Amazon%20Web%20Services%20%28AWS%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1035,name:Microsoft,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"

# bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No JP Morgan
# bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# JP Morgan Asset Management
# bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# JP Morgan Chase & Co
# bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# Chase
# bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1382,name:Goldman%20Sachs,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"
# No goldman Sachs
bigbank_connection_script = "(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies,name:Company%20Connections),segments:List((urn:urn%3Ali%3Acompany%3A1067,name:J.P.%20Morgan,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A3492416,name:J.P.%20Morgan%20Asset%20Management,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A1068,name:JPMorgan%20Chase%20%26%20Co.,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies),(urn:urn%3Ali%3Acompany%3A163001,name:Chase,facetUrn:urn%3Ali%3AadTargetingFacet%3AfirstDegreeConnectionCompanies)))))"




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

                for connection in connection_list:
                    if connection == 'connected to any': 
                        row_value.append(connection)
                    elif connection == 'connected to big companies' and sector == 'IT_info': 
                        arg_list.append(bigfive_connection_script)
                        row_value.append(connection)
                    elif connection == 'connected to big companies' and sector == 'Finance_info': 
                        arg_list.append(bigbank_connection_script)
                        row_value.append(connection)
                        
                    # count =  make_call() # makes the api call then parses and shows count
                    # Handles ConnectionError exception that may be raised during execution 
                    while True:
                        try:
                            count =  make_call() # makes the api call then parses and shows count
                            print("count is executed")
                            break
                        except:
                            # print("exception")
                            time.sleep(5) # Retry every five seconds

                    row_value.append(count)
                    row = pd.Series(row_value)
                    row_df = pd.DataFrame([row])
                    df = pd.concat([row_df, df], ignore_index=True)
                    print(df.head())
                    print("row value", row_value)

                    row_value.pop() # remove the count value
                    time.sleep(2)
                    save_path = f'intermediate/data_collection_3/{country}_NoGoldmanSachs_3.0.csv'
                    df.to_csv(save_path, index=False)

                    if connection != any_connection: 
                        arg_list.pop() # reomve the last added query parameter which is the connectivity status variable 
                    row_value.pop() # remove the connectivity status value
            
                if jobseniority != any_jobseniority:
                    arg_list.pop() # remove the last added query parameter which is the job seniority variable
                    jobseniority_list.pop() # empty the list to step to the next element in the list
                row_value.pop() # remove the job seniority value

            # There is no list to append to or remove from + there 
            arg_list.pop() # remove the last added query parameter which is the sector variable
            row_value.pop() # remove the company sector value

        if gender != any_gender: # If gender is specified
            arg_list.pop() # remove the last added query parameter which is the gender variable
            gender_list.pop() # empty the list to step to the next element in the list
        row_value.pop() # remove the gender value
             
    arg_list.pop() # remove the last added query parameter which is the location variable
    country_list.pop() # empty the list to step to the next element in the list
    row_value.clear() # remove the location value

df.columns = ["Country", "Gender", "Sector", "Job Seniority", "Connectivity Status", "Count"]
df.to_csv('intermediate/data_collection_3/dataset_NoGoldmanSachs_3.0.csv', index=False)



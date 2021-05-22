### Checklist 
# Add %20 to name 

from authentication import *

"""
A regular expression (or RE) specifies a set of strings that matches it; 
the functions in this module let you check if a particular string matches a given regular expression 
(or if a given regular expression matches a particular string, 
which comes down to the same thing).
"""

import re
def linkedinEncodeURL(strout):
    #strout = strout.replace(' ', '%20')
    #strout = strout.replace(':li:', '%3Ali%3A')
    strout = re.sub(r':li:((\w)+)+:',r'%3Ali%3A\1%3A',strout)
    strout = strout.replace('\n','')
    return strout
    
def encodeInner(strout):
    #strout = strout.replace('(18,24)', '%3A%2818%2C24%29')
    #strout = strout.replace('(25,34)', '%3A%2825%2C34%29')
    #strout = strout.replace('(35,54)', '%3A%2835%2C54%29')
    strout = strout.replace(' ', '%20')
    strout = strout.replace(':', '%3A')
    strout = strout.replace('\n', '')
    strout = strout.replace('(', '%28')
    strout = strout.replace(')', '%29')
    strout = strout.replace(',', '%2C')
    
    return strout

#test:
testurl = '''urn:urn:li:seniority:8,name:CXO,facetUrn:urn:li:adTargetingFacet:seniorities
),(urn:urn:li:seniority:10,name:Owner,facetUrn:urn:li:adTargetingFacet:seniorities),'''
# print(linkedinEncodeURL(testurl))
assert linkedinEncodeURL(testurl) =='urn:urn%3Ali%3Aseniority%3A8,name:CXO,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),(urn:urn%3Ali%3Aseniority%3A10,name:Owner,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),'

# Assume interface locale andlocation are dealt with
# tc = """q=targetingCriteria&cmTargetingCriteria= "

def locale_builder():
    req = "(or:List((facet:(urn:urn:li:adTargetingFacet:interfaceLocales,name:Interface%20Locales),segments:List((urn:urn:li:locale:en_US,name:English,facetUrn:urn:li:adTargetingFacet:interfaceLocales)))))"
    return req

# def location_builder(locations):
#     req = "(or:List((facet:(urn:urn:li:adTargetingFacet:locations,name:Locations),segments:List((urn:urn:li:geo:104170880,name:Qatar,facetUrn:urn:li:adTargetingFacet:locations)))))"
#     return req

# interface locale and 2 locations 
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

locationfacet = {"urn": "urn:li:adTargetingFacet:profileLocations","name": "Locations"}
locationsegments = [
    {"urn": "urn:li:geo:104170880", "name": "Qatar","facetUrn": "urn:li:adTargetingFacet:locations"}, 
    {"urn": "urn:li:geo:100459316", "name": "Saudi Arabia", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"} },
    {"urn": "urn:li:geo:103619019", "name": "Oman", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}},
    {"urn": "urn:li:geo:103239229", "name": "Kuwait", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}},
    {"urn": "urn:li:geo:104305776", "name": "United Arab Emirates", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}},
    {"urn": "urn:li:geo:100425729", "name": "Bahrain", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}}
]

answer = location_builder(locationsegments[0:2])
# print(answer)

# def gender_builder(genders): 
#     req = "(facet:(urn:urn:li:adTargetingFacet:genders,name:Member Gender),segments:List((urn:urn:li:gender:FEMALE,name:Female,facetUrn:urn:li:adTargetingFacet:genders)))"
#     return req

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

genderfacet = {"urn": "urn:li:adTargetingFacet:genders","name": "Member Gender"}
gendersegments = [ {"urn": "urn:li:gender:FEMALE","name": "Female","facetUrn": "urn:li:adTargetingFacet:genders"}, 
                   {"urn": "urn:li:gender:MALE","name": "Male","facetUrn": "urn:li:adTargetingFacet:genders"}]

answer = gender_builder(gendersegments[0:2])


# def age_builder(ageranges): 
#     req = "(facet:(urn:urn:li:adTargetingFacet:ageRanges,name:Member%20Age),segments:List((urn:urn:li:ageRange:(18,24),name:18 to 24,facetUrn:urn:li:adTargetingFacet:ageRanges)))"
#     return req

# Manually add the space string variant
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

agerangefacet = {"urn": "urn:li:adTargetingFacet:ageRanges","name": "Member Age"}
agerangesegments = [{"urn": "urn:li:ageRange:(18,24)","name": "18 to 24","facetUrn": "urn:li:adTargetingFacet:ageRanges"},
                    {"urn": "urn:li:ageRange:(25,34)","name": "25 to 34","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    {"urn": "urn:li:ageRange:(35,54)","name": "35 to 54","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    {"urn": "urn:li:ageRange:(55,2147483647)","name": "55+","facetUrn": "urn:li:adTargetingFacet:ageRanges"}]

answer = age_builder(agerangesegments[0:2])

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

jobseniorityfacet = {"urn" : "urn:li:adTargetingFacet:seniorities", "name": "Job Seniorities"}
jobsenioritysegments = [{ "urn": "urn:li:seniority:1", "name" : "Unpaid", "facetUrn": "urn:li:adTargetingFacet:seniorities"},  
                        { "urn": "urn:li:seniority:2", "name" : "Training",  "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        { "urn": "urn:li:seniority:3", "name" : "Entry", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        { "urn": "urn:li:seniority:4", "name" : "Senior", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        { "urn": "urn:li:seniority:5", "name" : "Manager", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        { "urn": "urn:li:seniority:6", "name" : "Director", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        { "urn": "urn:li:seniority:7", "name" : "VP", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        { "urn": "urn:li:seniority:8", "name" : "CXO", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        { "urn": "urn:li:seniority:9", "name" : "Partner", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        { "urn": "urn:li:seniority:10", "name" : "Owner", "facetUrn": "urn:li:adTargetingFacet:seniorities" }]

def exclude():
    return "exclude:(or:List())"
    
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

def NOT_builder(args): 
    if args == []: 
        return "exclude:(or:List())"
    conc = "exclude:"
    conc += OR_builder(args)
    return conc

# arg_list = [locale_builder(), 
            # location_builder(locationsegments[1:5]), 
            # OR_builder([gender_builder(gendersegments[0:1]), age_builder(agerangesegments[0:2])])]

arg_list = [locale_builder(), 
            location_builder(locationsegments[0:1])]

# exclude_list = []
exclude_list = [OR_builder([jobseniority_builder(jobsenioritysegments[0:3])])]

def include_all():
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + NOT_builder(exclude_list) + ")"
    return linkedinEncodeURL(output)

print(include_all())
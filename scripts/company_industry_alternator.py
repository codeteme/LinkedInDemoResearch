import re
from variables_dictionaries import * # imports locationsegments, agerangesegments, etc ...

any_companyindustry = 'Any Company Industry'

IT_company_industry = ["Internet", "Information Technology & Services", "Computer Software", "Computer & Network Security", "Computer Hardware", "Company Networking", "Wireless", "Telecommunications", "Semiconductors", "Nanotechnology", "Consumer Electronics"]
Finance_company_industry = ["Banking", "Capital Markets", "Financial Services", "Insurance", "Investment Banking", "Investment Management", "Venture Capital & Private Equity"]

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

def companyindustry_builder(companyindustries):
    print(type(companyindustries))
    print(companyindustries)
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

# Generate IT and Finance query string ready to pass to arg_list
it_list = []
for companyindustry in IT_company_industry:
    companyindustry_info = companyindustrysegments.get(companyindustry)
    it_list.append(companyindustry_info)
finance_list = []
for companyindustry in Finance_company_industry:
    companyindustry_info = companyindustrysegments.get(companyindustry)
    finance_list.append(companyindustry_info)
any_companyindustry_list = []

Company_industry_Info_list = it_list + finance_list + any_companyindustry_list
company_industry_info_dict = dict()
company_industry_info_dict['IT_info'] = Company_industry_Info_list[0]
company_industry_info_dict['Finance_info'] = Company_industry_Info_list[1]
company_industry_info_dict['Any Company Industry'] = Company_industry_Info_list[2]

arg_list = []

row_value = []

# Inner loop value
for an_info in company_industry_info_dict.keys():
    if an_info != any_companyindustry:
        # parameter passed to companyindustry_builder should be a list so I have put it in one
        value = company_industry_info_dict.get(an_info)
        # print(value)
        arg_list.append(companyindustry_builder(value))
        if an_info == 'IT_info':
            row_value.append('IT')
        elif an_info == 'Finance_info':
            row_value.append('Finance')
        else: 
            row_value.append('Neither IT nor Finance')
    else: 
        row_value.append(any_companyindustry)
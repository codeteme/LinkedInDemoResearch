
gendersegments = {"Female": {"urn": "urn:li:gender:FEMALE","name": "Female","facetUrn": "urn:li:adTargetingFacet:genders"}, 
                  "Male" : {"urn": "urn:li:gender:MALE","name": "Male","facetUrn": "urn:li:adTargetingFacet:genders"}}

target_gender_output = [{'urn': 'urn:li:gender:FEMALE', 'name': 'Female', 'facetUrn': 'urn:li:adTargetingFacet:genders'}, {'urn': 'urn:li:gender:MALE', 'name': 'Male', 'facetUrn': 'urn:li:adTargetingFacet:genders'}]

selected_genders = ["Female", "Male"]
gender_list = []
for gender in selected_genders:
    gender_info = gendersegments.get(gender)
    gender_list.append(gender_info)
assert(gender_list == target_gender_output)

locationsegments = {
    "Qatar": {"urn": "urn:li:geo:104170880", "name": "Qatar","facetUrn": "urn:li:adTargetingFacet:locations"}, 
    "Saudi Arabia": {"urn": "urn:li:geo:100459316", "name": "Saudi Arabia", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"} },
    "Oman": {"urn": "urn:li:geo:103619019", "name": "Oman", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}},
    "Kuwait":     {"urn": "urn:li:geo:103239229", "name": "Kuwait", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}}, 
    "UAE": {"urn": "urn:li:geo:104305776", "name": "United Arab Emirates", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}} ,
    "Bahrain":  {"urn": "urn:li:geo:100425729", "name": "Bahrain", "facetUrn": "urn:li:adTargetingFacet:locations", "ancestorUrns": {"urn:li:geo:102393603"}}
}

target_country_output = [{'urn': 'urn:li:geo:104305776', 'name': 'United Arab Emirates', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': {'urn:li:geo:102393603'}}]

# location_builder(locationsegments[0:1])

selected_countries = ['UAE']
country_list = []
for country in selected_countries:
    country_info = locationsegments.get(country)
    country_list.append(country_info)
assert(country_list == target_country_output)


jobsenioritysegments = {"Unpaid" : { "urn": "urn:li:seniority:1", "name" : "Unpaid", "facetUrn": "urn:li:adTargetingFacet:seniorities"},  
                        "Training" : { "urn": "urn:li:seniority:2", "name" : "Training",  "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        "Entry" : { "urn": "urn:li:seniority:3", "name" : "Entry", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        "Senior" : { "urn": "urn:li:seniority:4", "name" : "Senior", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        "Manager" : { "urn": "urn:li:seniority:5", "name" : "Manager", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        "Director" : { "urn": "urn:li:seniority:6", "name" : "Director", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        "VP" : { "urn": "urn:li:seniority:7", "name" : "VP", "facetUrn": "urn:li:adTargetingFacet:seniorities" },
                        "CXO" : { "urn": "urn:li:seniority:8", "name" : "CXO", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        "Partner" : { "urn": "urn:li:seniority:9", "name" : "Partner", "facetUrn": "urn:li:adTargetingFacet:seniorities" }, 
                        "Owner" :{ "urn": "urn:li:seniority:10", "name" : "Owner", "facetUrn": "urn:li:adTargetingFacet:seniorities" }}

selected_seniorities = ["Unpaid", "Training", "Entry"]
seniority_list = []
for seniority in selected_seniorities:
    seniority_info = jobsenioritysegments.get(seniority)
    seniority_list.append(seniority_info)

target_seniority_output = [{'urn': 'urn:li:seniority:1', 'name': 'Unpaid', 'facetUrn': 'urn:li:adTargetingFacet:seniorities'}, {'urn': 'urn:li:seniority:2', 'name': 'Training', 'facetUrn': 'urn:li:adTargetingFacet:seniorities'}, {'urn': 'urn:li:seniority:3', 'name': 'Entry', 'facetUrn': 'urn:li:adTargetingFacet:seniorities'}]
assert (seniority_list == target_seniority_output)

agerangesegments = {"18 to 24": {"urn": "urn:li:ageRange:(18,24)","name": "18 to 24","facetUrn": "urn:li:adTargetingFacet:ageRanges"},
                    "25 to 34": {"urn": "urn:li:ageRange:(25,34)","name": "25 to 34","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    "35 to 54": {"urn": "urn:li:ageRange:(35,54)","name": "35 to 54","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    "55+": {"urn": "urn:li:ageRange:(55,2147483647)","name": "55+","facetUrn": "urn:li:adTargetingFacet:ageRanges"}}

selected_ageranges = ["18 to 24", "25 to 34"]
agerange_list = []
for agerange in selected_ageranges:
    agerange_info = agerangesegments.get(agerange)
    agerange_list.append(agerange_info)

target_agerange_ouptput = [{'urn': 'urn:li:ageRange:(18,24)', 'name': '18 to 24', 'facetUrn': 'urn:li:adTargetingFacet:ageRanges'}, {'urn': 'urn:li:ageRange:(25,34)', 'name': '25 to 34', 'facetUrn': 'urn:li:adTargetingFacet:ageRanges'}]
assert (agerange_list == target_agerange_ouptput)
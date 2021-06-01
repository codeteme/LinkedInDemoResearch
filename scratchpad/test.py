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


arg_list = [
    locale_builder(), 
    location_builder(country_list),
    gender_builder(gender_list),
    jobseniority_builder(jobseniority_list),
    employer_builder(employer_list)
    ]


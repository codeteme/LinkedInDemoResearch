"""
q=targetingCriteria&cmTargetingCriteria=(include:(and:List(
    (or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))),
    (or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AMALE,name:Male,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),
    (or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A103644278,name:United%20States,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A102221843)))))),
    (or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aemployers,name:Company%20Names),segments:List((urn:urn%3Ali%3Acompany%3A10667,name:Facebook,facetUrn:urn%3Ali%3AadTargetingFacet%3Aemployers))))),
    (or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AmemberBehaviors,name:Member%20Traits),
        segments:List(
            (urn:urn%3Ali%3AmemberBehavior%3A20,name:Recently%20Switched%20Jobs,facetUrn:urn%3Ali%3AadTargetingFacet%3AmemberBehaviors),
            (urn:urn%3Ali%3AmemberBehavior%3A23,name:Open%20to%20Relocation%20%28International%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AmemberBehaviors,ancestorUrns:List(urn%3Ali%3AmemberBehavior%3A21)),
            (urn:urn%3Ali%3AmemberBehavior%3A22,name:Open%20to%20Relocation%20%28Domestic%29,facetUrn:urn%3Ali%3AadTargetingFacet%3AmemberBehaviors,ancestorUrns:List(urn%3Ali%3AmemberBehavior%3A21)))))))),
    exclude:(or:List()))&withValidation=true





cmTargetingCriteria: (include:(and:List(
    (or:List((facet:(urn:urn:li:adTargetingFacet:interfaceLocales,name:Interface Locales),segments:List((urn:urn:li:locale:en_US,name:English,facetUrn:urn:li:adTargetingFacet:interfaceLocales))))),
    (or:List((facet:(urn:urn:li:adTargetingFacet:genders,name:Member Gender),segments:List((urn:urn:li:gender:MALE,name:Male,facetUrn:urn:li:adTargetingFacet:genders))))),
    (or:List((facet:(urn:urn:li:adTargetingFacet:locations,name:Locations),segments:List((urn:urn:li:geo:103644278,name:United States,facetUrn:urn:li:adTargetingFacet:locations,ancestorUrns:List(urn:li:geo:102221843)))))),
    (or:List((facet:(urn:urn:li:adTargetingFacet:employers,name:Company Names),segments:List((urn:urn:li:company:10667,name:Facebook,facetUrn:urn:li:adTargetingFacet:employers))))),
    (or:List((facet:(urn:urn:li:adTargetingFacet:memberBehaviors,name:Member Traits),segments:List(
        (urn:urn:li:memberBehavior:20,name:Recently Switched Jobs,facetUrn:urn:li:adTargetingFacet:memberBehaviors),
        (urn:urn:li:memberBehavior:23,name:Open to Relocation (International),facetUrn:urn:li:adTargetingFacet:memberBehaviors,ancestorUrns:List(urn:li:memberBehavior:21)),
        (urn:urn:li:memberBehavior:22,name:Open to Relocation (Domestic),facetUrn:urn:li:adTargetingFacet:memberBehaviors,ancestorUrns:List(urn:li:memberBehavior:21))))))))
    ,exclude:(or:List()))
"""


arg_list = [
    locale_builder(), 
    location_builder(country_list),
    gender_builder(gender_list),
    jobseniority_builder(jobseniority_list),
    employer_builder(employer_list)
    ]


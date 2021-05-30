import re

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
    # print(linkedinEncodeURL(testurl))
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


locationfacet = {"urn": "urn:li:adTargetingFacet:profileLocations","name": "Locations"}
locationsegments = {'Afghanistan': {'urn': 'urn:li:geo:101240012', 'name': 'Afghanistan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Albania': {'urn': 'urn:li:geo:102845717', 'name': 'Albania', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Algeria': {'urn': 'urn:li:geo:106395874', 'name': 'Algeria', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Angola': {'urn': 'urn:li:geo:105371935', 'name': 'Angola', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Argentina': {'urn': 'urn:li:geo:100446943', 'name': 'Argentina', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Armenia': {'urn': 'urn:li:geo:103030111', 'name': 'Armenia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Australia': {'urn': 'urn:li:geo:101452733', 'name': 'Australia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506852))'}, 
                    'Austria': {'urn': 'urn:li:geo:103883259', 'name': 'Austria', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Azerbaijan': {'urn': 'urn:li:geo:103226548', 'name': 'Azerbaijan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'The Bahamas': {'urn': 'urn:li:geo:106662619', 'name': 'The Bahamas', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Bahrain': {'urn': 'urn:li:geo:100425729', 'name': 'Bahrain', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bangladesh': {'urn': 'urn:li:geo:106215326', 'name': 'Bangladesh', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Barbados': {'urn': 'urn:li:geo:102118611', 'name': 'Barbados', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Belarus': {'urn': 'urn:li:geo:101705918', 'name': 'Belarus', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Belgium': {'urn': 'urn:li:geo:100565514', 'name': 'Belgium', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Belize': {'urn': 'urn:li:geo:105912732', 'name': 'Belize', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Benin': {'urn': 'urn:li:geo:101519029', 'name': 'Benin', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Bhutan': {'urn': 'urn:li:geo:103613266', 'name': 'Bhutan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bolivia': {'urn': 'urn:li:geo:104379274', 'name': 'Bolivia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Bosnia and Herzegovina': {'urn': 'urn:li:geo:102869081', 'name': 'Bosnia and Herzegovina', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Botswana': {'urn': 'urn:li:geo:105698121', 'name': 'Botswana', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Bouvet Island': {'urn': 'urn:li:geo:102127336', 'name': 'Bouvet Island', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Brazil': {'urn': 'urn:li:geo:106057199', 'name': 'Brazil', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Brunei': {'urn': 'urn:li:geo:103809722', 'name': 'Brunei', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bulgaria': {'urn': 'urn:li:geo:105333783', 'name': 'Bulgaria', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Burkina Faso': {'urn': 'urn:li:geo:100587095', 'name': 'Burkina Faso', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Burundi': {'urn': 'urn:li:geo:100800406', 'name': 'Burundi', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Cambodia': {'urn': 'urn:li:geo:102500897', 'name': 'Cambodia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Cameroon': {'urn': 'urn:li:geo:105745966', 'name': 'Cameroon', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Canada': {'urn': 'urn:li:geo:101174742', 'name': 'Canada', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Cape Verde': {'urn': 'urn:li:geo:101679268', 'name': 'Cape Verde', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Central African Republic': {'urn': 'urn:li:geo:100134827', 'name': 'Central African Republic', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Chad': {'urn': 'urn:li:geo:104655384', 'name': 'Chad', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Chile': {'urn': 'urn:li:geo:104621616', 'name': 'Chile', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'China': {'urn': 'urn:li:geo:102890883', 'name': 'China', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Colombia': {'urn': 'urn:li:geo:100876405', 'name': 'Colombia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Comoros': {'urn': 'urn:li:geo:103069791', 'name': 'Comoros', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Republic of the Congo': {'urn': 'urn:li:geo:106796687', 'name': 'Republic of the Congo', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Congo (DRC)': {'urn': 'urn:li:geo:101271829', 'name': 'Congo (DRC)', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Costa Rica': {'urn': 'urn:li:geo:101739942', 'name': 'Costa Rica', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Côte d’Ivoire': {'urn': 'urn:li:geo:103295271', 'name': 'Côte d’Ivoire', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Croatia': {'urn': 'urn:li:geo:104688944', 'name': 'Croatia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Cyprus': {'urn': 'urn:li:geo:106774002', 'name': 'Cyprus', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Czechia': {'urn': 'urn:li:geo:104508036', 'name': 'Czechia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Denmark': {'urn': 'urn:li:geo:104514075', 'name': 'Denmark', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Djibouti': {'urn': 'urn:li:geo:100371290', 'name': 'Djibouti', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Dominican Republic': {'urn': 'urn:li:geo:105057336', 'name': 'Dominican Republic', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Ecuador': {'urn': 'urn:li:geo:106373116', 'name': 'Ecuador', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Egypt': {'urn': 'urn:li:geo:106155005', 'name': 'Egypt', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'El Salvador': {'urn': 'urn:li:geo:106522560', 'name': 'El Salvador', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Equatorial Guinea': {'urn': 'urn:li:geo:105141335', 'name': 'Equatorial Guinea', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Eritrea': {'urn': 'urn:li:geo:104219996', 'name': 'Eritrea', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Estonia': {'urn': 'urn:li:geo:102974008', 'name': 'Estonia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Ethiopia': {'urn': 'urn:li:geo:100212432', 'name': 'Ethiopia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Falkland Islands': {'urn': 'urn:li:geo:104961595', 'name': 'Falkland Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Fiji': {'urn': 'urn:li:geo:105733447', 'name': 'Fiji', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 'Finland': {'urn': 'urn:li:geo:100456013', 'name': 
                    'Finland', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'France': {'urn': 'urn:li:geo:105015875', 'name': 
                    'France', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'French Guiana': {'urn': 'urn:li:geo:105001561', 'name': 
                    'French Guiana', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 'French Polynesia': {'urn': 'urn:li:geo:102681285', 'name': 
                    'French Polynesia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 'French Southern and Antarctic Lands': {'urn': 'urn:li:geo:104827874', 'name': 
                    'French Southern and Antarctic Lands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 'Gabon': {'urn': 'urn:li:geo:104471338', 'name': 
                    'Gabon', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'The Gambia': {'urn': 'urn:li:geo:106100033', 'name': 
                    'The Gambia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Georgia': {'urn': 'urn:li:geo:106315325', 'name': 
                    'Georgia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 'Germany': {'urn': 'urn:li:geo:101282230', 'name': 
                    'Germany', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Ghana': {'urn': 'urn:li:geo:105769538', 'name': 
                    'Ghana', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Greece': {'urn': 'urn:li:geo:104677530', 'name': 
                    'Greece', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Grenada': {'urn': 'urn:li:geo:104579260', 'name': 
                    'Grenada', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 'Guatemala': {'urn': 'urn:li:geo:100877388', 'name': 
                    'Guatemala', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 'Guernsey': {'urn': 'urn:li:geo:104019891', 'name': 
                    'Guernsey', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Guinea': {'urn': 'urn:li:geo:100099594', 'name': 
                    'Guinea', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Guinea-Bissau': {'urn': 'urn:li:geo:100115557', 'name': 
                    'Guinea-Bissau', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Guyana': {'urn': 'urn:li:geo:105836293', 'name': 
                    'Guyana', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 'Haiti': {'urn': 'urn:li:geo:100993490', 'name': 
                    'Haiti', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Heard Island and McDonald Islands': {'urn': 'urn:li:geo:100737582', 'name': 'Heard Island and McDonald Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Vatican City': {'urn': 'urn:li:geo:107163060', 'name': 'Vatican City', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Honduras': {'urn': 'urn:li:geo:101937718', 'name': 'Honduras', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Hong Kong SAR': {'urn': 'urn:li:geo:103291313', 'name': 'Hong Kong SAR', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Hungary': {'urn': 'urn:li:geo:100288700', 'name': 'Hungary', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Iceland': {'urn': 'urn:li:geo:105238872', 'name': 'Iceland', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'India': {'urn': 'urn:li:geo:102713980', 'name': 'India', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Indonesia': {'urn': 'urn:li:geo:102478259', 'name': 'Indonesia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Iraq': {'urn': 'urn:li:geo:106725625', 'name': 'Iraq', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Ireland': {'urn': 'urn:li:geo:104738515', 'name': 'Ireland', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Israel': {'urn': 'urn:li:geo:101620260', 'name': 'Israel', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Italy': {'urn': 'urn:li:geo:103350119', 'name': 'Italy', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Jamaica': {'urn': 'urn:li:geo:105126983', 'name': 'Jamaica', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Japan': {'urn': 'urn:li:geo:101355337', 'name': 'Japan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Jersey': {'urn': 'urn:li:geo:102705533', 'name': 'Jersey', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Jordan': {'urn': 'urn:li:geo:103710677', 'name': 'Jordan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kazakhstan': {'urn': 'urn:li:geo:106049128', 'name': 'Kazakhstan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kenya': {'urn': 'urn:li:geo:100710459', 'name': 'Kenya', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Korea': {'urn': 'urn:li:geo:105149562', 'name': 'South Korea', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kosovo': {'urn': 'urn:li:geo:104640522', 'name': 'Kosovo', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Kuwait': {'urn': 'urn:li:geo:103239229', 'name': 'Kuwait', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kyrgyzstan': {'urn': 'urn:li:geo:103490790', 'name': 'Kyrgyzstan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Laos': {'urn': 'urn:li:geo:100664862', 'name': 'Laos', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Latvia': {'urn': 'urn:li:geo:104341318', 'name': 'Latvia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Lebanon': {'urn': 'urn:li:geo:101834488', 'name': 'Lebanon', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Lesotho': {'urn': 'urn:li:geo:103712797', 'name': 'Lesotho', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Liberia': {'urn': 'urn:li:geo:106579411', 'name': 'Liberia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Libya': {'urn': 'urn:li:geo:104036859', 'name': 'Libya', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Lithuania': {'urn': 'urn:li:geo:101464403', 'name': 'Lithuania', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Luxembourg': {'urn': 'urn:li:geo:104042105', 'name': 'Luxembourg', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Macao SAR': {'urn': 'urn:li:geo:101316508', 'name': 'Macao SAR', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'North Macedonia': {'urn': 'urn:li:geo:103420483', 'name': 'North Macedonia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Madagascar': {'urn': 'urn:li:geo:105587166', 'name': 'Madagascar', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malawi': {'urn': 'urn:li:geo:105992277', 'name': 'Malawi', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malaysia': {'urn': 'urn:li:geo:106808692', 'name': 'Malaysia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Maldives': {'urn': 'urn:li:geo:102161637', 'name': 'Maldives', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Mali': {'urn': 'urn:li:geo:100770782', 'name': 'Mali', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malta': {'urn': 'urn:li:geo:100961908', 'name': 'Malta', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Marshall Islands': {'urn': 'urn:li:geo:106516799', 'name': 'Marshall Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'French-Martinique': {'urn': 'urn:li:geo:103091690', 'name': 'French-Martinique', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Mauritania': {'urn': 'urn:li:geo:106950838', 'name': 'Mauritania', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mauritius': {'urn': 'urn:li:geo:106931611', 'name': 'Mauritius', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Mayotte': {'urn': 'urn:li:geo:104097939', 'name': 'Mayotte', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mexico': {'urn': 'urn:li:geo:103323778', 'name': 'Mexico', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Moldova': {'urn': 'urn:li:geo:106178099', 'name': 'Moldova', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Mongolia': {'urn': 'urn:li:geo:102396337', 'name': 'Mongolia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Montenegro': {'urn': 'urn:li:geo:100733275', 'name': 'Montenegro', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Montserrat': {'urn': 'urn:li:geo:101150476', 'name': 'Montserrat', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Morocco': {'urn': 'urn:li:geo:102787409', 'name': 'Morocco', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mozambique': {'urn': 'urn:li:geo:100474128', 'name': 'Mozambique', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Myanmar': {'urn': 'urn:li:geo:104136533', 'name': 'Myanmar', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Namibia': {'urn': 'urn:li:geo:106682822', 'name': 'Namibia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Nepal': {'urn': 'urn:li:geo:104630404', 'name': 'Nepal', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Netherlands': {'urn': 'urn:li:geo:102890719', 'name': 'Netherlands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'New Caledonia': {'urn': 'urn:li:geo:105535747', 'name': 'New Caledonia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'New Zealand': {'urn': 'urn:li:geo:105490917', 'name': 'New Zealand', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Nicaragua': {'urn': 'urn:li:geo:105517145', 'name': 'Nicaragua', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Niger': {'urn': 'urn:li:geo:103550069', 'name': 'Niger', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Nigeria': {'urn': 'urn:li:geo:105365761', 'name': 'Nigeria', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Niue': {'urn': 'urn:li:geo:102139488', 'name': 'Niue', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Norfolk Island': {'urn': 'urn:li:geo:100646662', 'name': 'Norfolk Island', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Norway': {'urn': 'urn:li:geo:103819153', 'name': 'Norway', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Oman': {'urn': 'urn:li:geo:103619019', 'name': 'Oman', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Pakistan': {'urn': 'urn:li:geo:101022442', 'name': 'Pakistan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Palestinian Authority': {'urn': 'urn:li:geo:93000000', 'name': 'Palestinian Authority', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Panama': {'urn': 'urn:li:geo:100808673', 'name': 'Panama', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Papua New Guinea': {'urn': 'urn:li:geo:100152180', 'name': 'Papua New Guinea', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Paraguay': {'urn': 'urn:li:geo:104065273', 'name': 'Paraguay', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Peru': {'urn': 'urn:li:geo:102927786', 'name': 'Peru', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Philippines': {'urn': 'urn:li:geo:103121230', 'name': 'Philippines', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Pitcairn Islands': {'urn': 'urn:li:geo:104322374', 'name': 'Pitcairn Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Poland': {'urn': 'urn:li:geo:105072130', 'name': 'Poland', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Portugal': {'urn': 'urn:li:geo:100364837', 'name': 'Portugal', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Puerto Rico': {'urn': 'urn:li:geo:105245958', 'name': 'Puerto Rico', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Qatar': {'urn': 'urn:li:geo:104170880', 'name': 'Qatar', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Serbia': {'urn': 'urn:li:geo:101855366', 'name': 'Serbia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Reunion': {'urn': 'urn:li:geo:104265812', 'name': 'Reunion', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Romania': {'urn': 'urn:li:geo:106670623', 'name': 'Romania', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Russia': {'urn': 'urn:li:geo:101728296', 'name': 'Russia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Rwanda': {'urn': 'urn:li:geo:103547315', 'name': 'Rwanda', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Saint Barthelemy': {'urn': 'urn:li:geo:100936035', 'name': 'Saint Barthelemy', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Saint Pierre and Miquelon': {'urn': 'urn:li:geo:102024132', 'name': 'Saint Pierre and Miquelon', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'São Tomé and Príncipe': {'urn': 'urn:li:geo:106867470', 'name': 'São Tomé and Príncipe', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Saudi Arabia': {'urn': 'urn:li:geo:100459316', 'name': 'Saudi Arabia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Senegal': {'urn': 'urn:li:geo:103587512', 'name': 'Senegal', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Singapore': {'urn': 'urn:li:geo:102454443', 'name': 'Singapore', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Slovakia': {'urn': 'urn:li:geo:103119917', 'name': 'Slovakia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Slovenia': {'urn': 'urn:li:geo:106137034', 'name': 'Slovenia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Solomon Islands': {'urn': 'urn:li:geo:104980134', 'name': 'Solomon Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Somalia': {'urn': 'urn:li:geo:104725424', 'name': 'Somalia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Africa': {'urn': 'urn:li:geo:104035573', 'name': 'South Africa', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Georgia and South Sandwich Islands': {'urn': 'urn:li:geo:103665423', 'name': 'South Georgia and South Sandwich Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'South Sudan': {'urn': 'urn:li:geo:103622308', 'name': 'South Sudan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Spain': {'urn': 'urn:li:geo:105646813', 'name': 'Spain', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Sri Lanka': {'urn': 'urn:li:geo:100446352', 'name': 'Sri Lanka', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Suriname': {'urn': 'urn:li:geo:105530931', 'name': 'Suriname', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Eswatini': {'urn': 'urn:li:geo:106768907', 'name': 'Eswatini', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Sweden': {'urn': 'urn:li:geo:105117694', 'name': 'Sweden', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Switzerland': {'urn': 'urn:li:geo:106693272', 'name': 'Switzerland', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Tajikistan': {'urn': 'urn:li:geo:105925962', 'name': 'Tajikistan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Tanzania': {'urn': 'urn:li:geo:104604145', 'name': 'Tanzania', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Thailand': {'urn': 'urn:li:geo:105146118', 'name': 'Thailand', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Timor-Leste': {'urn': 'urn:li:geo:101101678', 'name': 'Timor-Leste', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Togo': {'urn': 'urn:li:geo:103603395', 'name': 'Togo', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Tokelau': {'urn': 'urn:li:geo:100212364', 'name': 'Tokelau', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Trinidad and Tobago': {'urn': 'urn:li:geo:106947126', 'name': 'Trinidad and Tobago', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Tunisia': {'urn': 'urn:li:geo:102134353', 'name': 'Tunisia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Turkey': {'urn': 'urn:li:geo:102105699', 'name': 'Turkey', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Turkmenistan': {'urn': 'urn:li:geo:105449295', 'name': 'Turkmenistan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Turks and Caicos Islands': {'urn': 'urn:li:geo:100771715', 'name': 'Turks and Caicos Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Tuvalu': {'urn': 'urn:li:geo:103609605', 'name': 'Tuvalu', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Uganda': {'urn': 'urn:li:geo:106943612', 'name': 'Uganda', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Ukraine': {'urn': 'urn:li:geo:102264497', 'name': 'Ukraine', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'United Arab Emirates': {'urn': 'urn:li:geo:104305776', 'name': 'United Arab Emirates', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'United Kingdom': {'urn': 'urn:li:geo:101165590', 'name': 'United Kingdom', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'United States': {'urn': 'urn:li:geo:103644278', 'name': 'United States', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Uruguay': {'urn': 'urn:li:geo:100867946', 'name': 'Uruguay', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Uzbekistan': {'urn': 'urn:li:geo:107734735', 'name': 'Uzbekistan', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Vanuatu': {'urn': 'urn:li:geo:102185308', 'name': 'Vanuatu', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Venezuela': {'urn': 'urn:li:geo:101490751', 'name': 'Venezuela', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Vietnam': {'urn': 'urn:li:geo:104195383', 'name': 'Vietnam', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'US Virgin Islands': {'urn': 'urn:li:geo:102119762', 'name': 'US Virgin Islands', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Wallis and Futuna': {'urn': 'urn:li:geo:104246629', 'name': 'Wallis and Futuna', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List())'}, 
                    'Yemen': {'urn': 'urn:li:geo:105962095', 'name': 'Yemen', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Zambia': {'urn': 'urn:li:geo:102120260', 'name': 'Zambia', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Zimbabwe': {'urn': 'urn:li:geo:101367137', 'name': 'Zimbabwe', 'facetUrn': 'urn:li:adTargetingFacet:locations', 'ancestorUrns': 'List(urn:li:geo:103537801)'}}

# The function returns all the locations available
def getList(dict):
  return dict.keys()
getList(locationsegments)


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
gendersegments = {"Female": {"urn": "urn:li:gender:FEMALE","name": "Female","facetUrn": "urn:li:adTargetingFacet:genders"}, 
                  "Male" : {"urn": "urn:li:gender:MALE","name": "Male","facetUrn": "urn:li:adTargetingFacet:genders"}}


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

agerangefacet = {"urn": "urn:li:adTargetingFacet:ageRanges","name": "Member Age"}

agerangesegments = {"18 to 24": {"urn": "urn:li:ageRange:(18,24)","name": "18 to 24","facetUrn": "urn:li:adTargetingFacet:ageRanges"},
                    "25 to 34": {"urn": "urn:li:ageRange:(25,34)","name": "25 to 34","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    "35 to 54": {"urn": "urn:li:ageRange:(35,54)","name": "35 to 54","facetUrn": "urn:li:adTargetingFacet:ageRanges"}, 
                    "55+": {"urn": "urn:li:ageRange:(55,2147483647)","name": "55+","facetUrn": "urn:li:adTargetingFacet:ageRanges"}}

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
selected_countries = ['Algeria', 'The Gambia']
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
selected_ageranges = ["18 to 24", "25 to 34"]
agerange_list = []
for agerange in selected_ageranges:
    agerange_info = agerangesegments.get(agerange)
    agerange_list.append(agerange_info)

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

arg_list = [locale_builder(), 
            location_builder(country_list),
            gender_builder(gender_list),
            age_builder(agerange_list)]

def include_all():
    output =  "q=targetingCriteria&cmTargetingCriteria=(include:(and:List(" + AND_builder(arg_list) + ")" + ")" + "," + NOT_builder(exclude_list) + ")"
    return linkedinEncodeURL(output)

# include_all()
print(include_all())




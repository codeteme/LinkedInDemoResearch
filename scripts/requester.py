import requests
import json
import re

response = requests.get(
    'https://pypi.org/project/har2requests/',

    headers={'Host': 'pypi.org', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://www.google.com/', 'Connection': 'keep-alive', 'Cookie': 'session_id=QNqSBa8aTK8JPBuzF5bxDJO6lyFNH3gwkzxO2Fm_ePA.YIaoGA.6i3uhXxG_3cJ2tV8PRdLHcJF9PJF3ks8dY_y2KMkU0irgEsDsRLWu219SaGm64mooXuUFlQZLz8PDJGWfML--A; _ga=GA1.2.735785210.1619437594; _gid=GA1.2.1141903637.1619437594', 'Upgrade-Insecure-Requests': '1', 'If-None-Match': '"Ct27T19ykHNA4sVrkNSmeg"', 'Cache-Control': 'max-age=0'},
)

# Copy and paste the request header from browser's network panel
# getHeadersFromFirefox converts the string that you can copy in
# the firefox developer tools (tab network, right click on 1 request ->
# -> copy request-header) to a header that you can use here

testheaders="""
Host: www.linkedin.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Prefer: safe
Referer: https://www.linkedin.com/campaignmanager/accounts/507131805/campaigns/new/details?campaignGroupId=615557454
x-restli-protocol-version: 2.0.0
x-li-lang: en_US
x-li-track: {"clientVersion":"2.4.777","mpVersion":"2.4.777","osName":"web","timezoneOffset":3,"timezone":"Asia/Qatar","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":2,"displayWidth":3360,"displayHeight":2100}
x-li-page-instance: urn:li:page:d_campaign_details;nlsD8e5YS++fFsIHNHt2Yw==
csrf-token: ajax:5901664971532134280
x-http-method-override: GET
content-type: application/x-www-form-urlencoded
Content-Length: 1354
Origin: https://www.linkedin.com
Connection: keep-alive
Cookie: JSESSIONID="ajax:5901664971532134280"; bcookie="v=2&c5f27fc8-a995-4dfd-8c37-03810153ea44"; bscookie="v=1&20210504140158723c598c-f005-41c1-8b84-6421b12f6089AQFS-UeasGOrxz960bmdW19hEqvgLdJF"; _ga=GA1.2.1101044002.1620136918; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18761%7CMCMID%7C33440669679956594540176137054812188594%7CMCAAMLH-1621515256%7C6%7CMCAAMB-1621515256%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1620917656s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1529527004; li_rm=AQGbZvsvtq8xxAAAAXk3r43BIwOwUOJqrRMQoA-nXXBCc5Xlflp62qe6ftE4-iHYdKn0mrIeEvvlftV1T82_25ZKeJ468C0zTS02yHh9pUK42WY0_Rfzpvc6; _gcl_au=1.1.1049138754.1620136927; aam_uuid=33618448150752971410197855517193788537; g_state={"i_l":0}; li_at=AQEDATWfwXIBJ1RGAAABeWjIvSEAAAF5sxBqXk4AIz_18Nz9hSN_C_BkUAo05qdp2nNsSG7VlOjsLL-o7hqasKw79rRmrU4mgBr3F58LWqwFPvQqFQ3tN45izKWkf0JSVOj00fK2eY_OJXQzDu7mpYAT; liap=true; timezone=Asia/Qatar; _guid=d8116692-cff4-4116-bbd5-37609e1b4828; li_sugr=558bab07-f0ec-415c-90b8-0d9041dd1343; AnalyticsSyncHistory=AQITn3h8GvuvsQAAAXl1sEkZI7OnsFN2tG-AmigkHJjxkqYbaKtBk0q6H0mKIhvvW67Tk_n_pjm30Bxr44J0GA; lms_ads=AQERYsZwHQLQyQAAAXl1sEoj2z1YYHdF8keOI7fNAy57wn-Xy-IXIzhuHQageAAkZQuWe-9eUwDe94Zlc_XklbEJLB3Hd44U; lms_analytics=AQERYsZwHQLQyQAAAXl1sEoj2z1YYHdF8keOI7fNAy57wn-Xy-IXIzhuHQageAAkZQuWe-9eUwDe94Zlc_XklbEJLB3Hd44U; gpv_pn=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails; s_tslv=1620960622654; liveagent_oref=https://www.linkedin.com/care/embed/chat/cmtChat?useDefaultButton=false&hostApplicationName=undefined; liveagent_vc=2; liveagent_ptid=18843a9a-c4de-4a4e-afbd-581a77a3a6d5; VID=V_2021_05_13_12_608948; _gac_UA-62256447-1=1.1620910764.CjwKCAjwnPOEBhA0EiwA609ReTdS7ez2npmn2Itwq5CLvMPXFrqQBz--fCwaDV8KHiZjJV1H6wa5shoCEwgQAvD_BwE; mbox=session#5a777e17d30d4b2a95995d02ac77f687#1620912626|PC#5a777e17d30d4b2a95995d02ac77f687.37_0#1636463112; _gcl_aw=GCL.1620910766.CjwKCAjwnPOEBhA0EiwA609ReTdS7ez2npmn2Itwq5CLvMPXFrqQBz--fCwaDV8KHiZjJV1H6wa5shoCEwgQAvD_BwE; _gcl_dc=GCL.1620910766.CjwKCAjwnPOEBhA0EiwA609ReTdS7ez2npmn2Itwq5CLvMPXFrqQBz--fCwaDV8KHiZjJV1H6wa5shoCEwgQAvD_BwE; li_gc=MTswOzE2MjA5MTExMTA7MjswMjEpcmTLSZu3fJDVPJzfL58besDb12i6qNcL87iKStnHSQ==; UserMatchHistory=AQJlEKavHAj0_AAAAXl1sEkYChWZl9KnnRGjvaSkftt78hobqQezN3eUfOu86nkm4UOoUxXY55Jm-w; lang=v=2&lang=en-us; lidc="b=TB94:s=T:r=T:a=T:p=T:g=2687:u=9:i=1621602076:t=1621688468:v=2:sig=AQFyI0R2uviAbjG-us9TLLm0dfhd5qiq"
TE: Trailers
Pragma: no-cache
Cache-Control: no-cache
"""
def getHeadersFromFirefox(headers):
    headers1={}
    for line in headers.split("\n")[1:-1]:
        headers1[line.split(':')[0]]= line[line.find(':')+2:]
    return headers1
headers = getHeadersFromFirefox(testheaders)



# Test it with a copied targeting-criteria in data:
response = requests.post(
    'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
    headers=headers,
    data='q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A103644278,name:United%20States,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A102221843)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Ade_DE,name:German,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true',
)

# Execute to get the result
def get_response(testCriteria):
    response = requests.post(
        'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
        headers=headers,
        data=testCriteria
    )
    return response

# Functions accepts string, delimiter and nth occurence of the delimiter where string is split up. 
def split_at(s, delim, n):
    r = s.split(delim, n)[n]
    return s[:-len(r)-len(delim)], r

# Extracts only the count from the returned response string
def parse_response(response_string):
    temp_str_1 = split_at(response_string, ',', 1)[0]
    temp_str_2 = split_at(temp_str_1, ':', 2)[1][:-2] 
    return int(temp_str_2) # convert to number

# Accepts the query built by userand calls appropriate functions
def getCount(testCriteria):
    return parse_response(get_response(testCriteria).text)



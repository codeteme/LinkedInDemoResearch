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
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
x-restli-protocol-version: 2.0.0
x-li-lang: en_US
x-li-track: {"clientVersion":"2.4.1450","mpVersion":"2.4.1450","osName":"web","timezoneOffset":3,"timezone":"Asia/Riyadh","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":1,"displayWidth":1680,"displayHeight":1050}
x-li-page-instance: urn:li:page:d_campaign_details;lZdeHgKkSminK8lGJR4Ucw==
csrf-token: ajax:2093587861622909016
x-li-er-key: urn:li:sponsoredAccount:507131805
x-http-method-override: GET
content-type: application/x-www-form-urlencoded
Content-Length: 2691
Origin: https://www.linkedin.com
Connection: keep-alive
Referer: https://www.linkedin.com/campaignmanager/accounts/507131805/campaigns/new/details?campaignGroupId=615557454
Cookie: bcookie="v=2&12924590-f701-481b-85f7-c19b4542266d"; bscookie="v=1&20210605151237ae2ef469-025d-48ac-8628-cb7117040996AQEPTxcCAH5qpDBPxzyV-9d3SpqFoEf6"; li_rm=AQFriIKtZOttzAAAAXoNr-dxS_DF6A7jDSK0b6_2pA3XYF8baYr5AwLncQUDAd1arwbD7uFOP2CINH7Y6CHhif-HklHJdBuUecaT2OJ6KncOCCStFJjH10_Tl3dWU9f53B0XpDbSU6LAp51HSMCSKtbsnrQ8C985V9eFOpJZtonqYjoJxBp6OOyWr-lBXcUZQZE-ldLLRfRQ8xSKTSXbxVGnHPxgiK8oBzR7K0qF1ugvlPAGdvBQYpG9S6l6qkB3BUhU2gK1w4WPOYX_BJdi_ArWNBsHzOfDNHZh7LeuTL5YNb6LEibtpMQ9LdGZpnAjZENBa84hifegZ8nDuVc; _ga=GA1.2.212018236.1622906017; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18803%7CMCMID%7C06822997612877381543424692258512506413%7CMCAAMLH-1625222729%7C6%7CMCAAMB-1625222729%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1624625129s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1529527004; _gcl_au=1.1.138998113.1622906018; aam_uuid=07000757872865609933407496805101469158; JSESSIONID="ajax:2093587861622909016"; gpv_pn=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails; s_tslv=1624617938904; li_sugr=1bfe14c9-67c9-4f52-a88e-1ce3103bbf32; UserMatchHistory=AQKdCxTk_t8TgQAAAXo4h129onxgCSPPPZk5O1lDH0cPtnXvBsj9Jcfkb4JkCMJXU8avgi5QgLMxT6bTTO9jvMYb4Z13pY1YhErEgumvJXgsj4cuAS_TwlkkXQk5-e55FWfkqD10qMBY7_LFtKBsUQNaR4_TRcl3iDKlX6q2VJSIqU9aC38Obaam2VYR28hUGY0AEVzaWOcPWhqXPZpkIQMFZBPWVR7HO7aUzf2dbqcTP7tkdErFAreAianE6SqU6s_v1Hh2whQvSJNDUbp4EwGSxtn9qO9PKZL5pyw; AnalyticsSyncHistory=AQKi6Az6394jEgAAAXo4h1291GEF4X_xDohBkyfLs8Bz4fFi3UInUMurhIWhzTgXvFticDmy12NKlvz8ANUi5Q; lms_ads=AQE0ihx3eD-3pgAAAXo4h18hxX4dsSt36BiMmQ9P6TUPH-xFmXkJbFjkvZU3U4qNNsPbgod6vpsXJwBg6n87z1ljtk4cQ1-i; lms_analytics=AQE0ihx3eD-3pgAAAXo4h18hxX4dsSt36BiMmQ9P6TUPH-xFmXkJbFjkvZU3U4qNNsPbgod6vpsXJwBg6n87z1ljtk4cQ1-i; _guid=2ad3c301-26bf-4569-9497-1c5b62ae039b; liveagent_oref=https://www.linkedin.com/help/lms?lang=en; liveagent_vc=2; liveagent_ptid=da3012a4-4bdb-4c0a-9c03-7ef8f6b5e9a3; li_at=AQEDATWfwXIDdQimAAABejQpWggAAAF6WDXeCE4ARsUvxQJZog2xRxNhoK7auWWqGcVd3ghW3pJJiSIUi7NZzVvRt5Rux8gl-VGWuKqpsx9p7fKc6RtSlHz--pYtFXrjwKb4euRWSHKFGchVQYEUQBvT; liap=true; lidc="b=TB94:s=T:r=T:a=T:p=T:g=2695:u=30:i=1624617931:t=1624704331:v=2:sig=AQHDNnwSRIJTwH79rx62HQpb-1B-p505"; lang=v=2&lang=en-us; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; s_plt=1.81; s_pltp=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails; s_ppv=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails%2C34%2C28%2C1101%2C1%2C6; s_ips=897; s_tp=3228; s_cc=true; s_sq=%5B%5BB%5D%5D
TE: Trailers
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
    print("RESPONSE STRING")
    print(response_string)
    print("****")
    print("****")
    temp_str_1 = split_at(response_string, ',', 1)[0]
    temp_str_2 = split_at(temp_str_1, ':', 2)[1][:-2] 
    return int(temp_str_2) # convert to number

# Accepts the query built by userand calls appropriate functions
def getCount(testCriteria):
    return parse_response(get_response(testCriteria).text)




# %%
import requests
import json
import re
import harreplay


# %%
import requests
response = requests.get(
    'https://pypi.org/project/har2requests/',

    headers={'Host': 'pypi.org', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://www.google.com/', 'Connection': 'keep-alive', 'Cookie': 'session_id=QNqSBa8aTK8JPBuzF5bxDJO6lyFNH3gwkzxO2Fm_ePA.YIaoGA.6i3uhXxG_3cJ2tV8PRdLHcJF9PJF3ks8dY_y2KMkU0irgEsDsRLWu219SaGm64mooXuUFlQZLz8PDJGWfML--A; _ga=GA1.2.735785210.1619437594; _gid=GA1.2.1141903637.1619437594', 'Upgrade-Insecure-Requests': '1', 'If-None-Match': '"Ct27T19ykHNA4sVrkNSmeg"', 'Cache-Control': 'max-age=0'},
)


# %%
# getHeadersFromFirefox converts the string that you can copy in
# the firefox developer tools (tab network, right click on 1 request ->
# -> copy request-header) to a header that you can use here


# original test headers, presumably from Tom at MPIDR
# headers={'Host': 'www.linkedin.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 'Accept': '*/*', 'Accept-Language': 'en-GB,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://www.linkedin.com/campaignmanager/account/503555724/campaign-create?campaignGroupId=606948013', 'x-restli-protocol-version': '2.0.0', 'x-li-lang': 'en_US', 'x-li-track': '{"clientVersion":"1.2.*","osName":"web","timezoneOffset":1,"deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web"}', 'x-li-page-instance': 'urn:li:page:d_campaign_create;2Fb9oJkCQ7KZnlFxMFXQ1w==', 'csrf-token': 'ajax:-1643625846928934947', 'x-http-method-override': 'GET', 'content-type': 'application/x-www-form-urlencoded', 'Content-Length': '1243', 'Origin': 'https://www.linkedin.com', 'Connection': 'keep-alive', 'Cookie': 'bcookie=v=2&b68cc6db-50fa-4784-879d-13e021142e4b; bscookie=v=1&2019081911463503dcc346-7ca2-403d-80d8-2d6e517dcfa8AQGivif9o0rzGvgxL88A05mcAdjmk125; visit=v=1&M; VID=V_2019_10_09_05_3631396; utag_main=v_id:016deecf04e8001b038740bad1670004d003700d00bd0$_sn:3$_se:3$_ss:0$_st:1571747578495$ses_id:1571745765465%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:linkedin.com; sl="v=1&NzedF"; li_at=AQEDAS3W8qABEiRJAAABbfJK5JkAAAFwOWwS7E0AwOm8_Z4ydYPHmPQuPLDgwyZgYFXRdS0edhjenIoqWaO6uj2OfC_oLF7FNxkK4NJCq0bwGeEovTw75gShihAUH4tRwb2h8QEo4IIO27RsfxU2_hue; liap=true; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18298%7CMCMID%7C33582537304092631233337028826612196732%7CMCAAMLH-1581511362%7C6%7CMCAAMB-1581511362%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1580913762s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-1851911619; UserMatchHistory=AQIRuZOA68w-VgAAAXAVX67ZIQOGmZ2nQ-_4dPhZt0Zs_-EcfsZOOu-_F-TzV3HKfwox6ZZz5qg; aam_uuid=33387932488196597363350868566638827191; li_oatml=AQEndSdEwxPuVgAAAXAVX6-A4OKYoLSxiull2ZIXJ0ysojvWFMX_NrPePJMm1-B7UvttX5GfQO5cAGCLFMtREi9bPWjenpO3; _ga=GA1.2.811638982.1571835098; _lipt=CwEAAAFv7IRqzvW5BWe1MdZ8oSiZ3N4BfnsE1gSPwTLdy50cKR_FwicE1vWBnT8x_sAcvh1_UDRtwAPUyf5CzcSWbXI8NWIgQ1bCyi3Y76UR0e9mS2gjcSDlXyexJqmnPrBVHP-tflhVG06fMCjxbSP0g890RqTX4WPErh2rXk6KFToLlIkCZY7FwadrVKv9xbYns6I_YpJrCA_qZCPWvu3lBabw09B0PtOQQTX6ATVHm07JY5KpnJN--M-9ymOzI6wWFXWBggkLuDeTbnhnhDW-57LIY6zvlpI9z8UF151OBYKtlFY6uAipGoc3AlNA4f0rmlE5HA; lissc=1; JSESSIONID="ajax:-1643625846928934947"; lang=v=2&lang=en-US; lidc="b=VB36:g=2829:u=20:i=1580906559:t=1580992948:s=AQFatqoC6NJ0RPXiCrYoGH6g-Z7sHkJ6"; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiJiMTFlMmRmNi05YjNlLTQ3NjgtYWJlZi1kZmE0OTgxNzc0YTN8MTU4MDkwNjU1MSIsInJlY2VudGx5LXNlYXJjaGVkIjoiIiwicmVmZXJyYWwtdXJsIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2NhbXBhaWdubWFuYWdlci9hY2NvdW50cyIsIlJOVC1pZCI6InwwIiwicmVjZW50bHktdmlld2VkIjoiIiwiQ1BULWlkIjoiTTJKaU1ESTRPV0l0TXpaaE1DMDBNekJsTFdKak16QXROVEpqT1dSak4yRmxZbUZsIiwiZXhwZXJpZW5jZSI6IiIsIndoaXRlbGlzdCI6Int9IiwidHJrIjoiIn0sIm5iZiI6MTU4MDkwNjU1MSwiaWF0IjoxNTgwOTA2NTUxfQ.v1cs7PV70O2pQkc8Wf7lCgKfe2iKRQUDmDw4VuO7P0I; PLAY_LANG=en; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'TE': 'Trailers'},
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
# print(headers)


# %%
# Test it with a copied targeting-criteria in data:
response = requests.post(
    'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
    headers=headers,
    data='q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A103644278,name:United%20States,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A102221843)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Ade_DE,name:German,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true',
)
# print(response.text)

testCriteria = "q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A104170880,name:Qatar,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations))))))),exclude:(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Aseniorities,name:Job%20Seniorities),segments:List((urn:urn%3Ali%3Aseniority%3A1,name:Unpaid,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),(urn:urn%3Ali%3Aseniority%3A2,name:Training,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities),(urn:urn%3Ali%3Aseniority%3A3,name:Entry,facetUrn:urn%3Ali%3AadTargetingFacet%3Aseniorities))))))"
response = requests.post(
    'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
    headers=headers,#{'Host': 'www.linkedin.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 'Accept': '*/*', 'Accept-Language': 'en-GB,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://www.linkedin.com/campaignmanager/account/503555724/campaign-create?campaignGroupId=606948013', 'x-restli-protocol-version': '2.0.0', 'x-li-lang': 'en_US', 'x-li-track': '{"clientVersion":"1.2.*","osName":"web","timezoneOffset":1,"deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web"}', 'x-li-page-instance': 'urn:li:page:d_campaign_create;2Fb9oJkCQ7KZnlFxMFXQ1w==', 'csrf-token': 'ajax:-1643625846928934947', 'x-http-method-override': 'GET', 'content-type': 'application/x-www-form-urlencoded', 'Content-Length': '1243', 'Origin': 'https://www.linkedin.com', 'Connection': 'keep-alive', 'Cookie': 'bcookie=v=2&b68cc6db-50fa-4784-879d-13e021142e4b; bscookie=v=1&2019081911463503dcc346-7ca2-403d-80d8-2d6e517dcfa8AQGivif9o0rzGvgxL88A05mcAdjmk125; visit=v=1&M; VID=V_2019_10_09_05_3631396; utag_main=v_id:016deecf04e8001b038740bad1670004d003700d00bd0$_sn:3$_se:3$_ss:0$_st:1571747578495$ses_id:1571745765465%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:linkedin.com; sl="v=1&NzedF"; li_at=AQEDAS3W8qABEiRJAAABbfJK5JkAAAFwOWwS7E0AwOm8_Z4ydYPHmPQuPLDgwyZgYFXRdS0edhjenIoqWaO6uj2OfC_oLF7FNxkK4NJCq0bwGeEovTw75gShihAUH4tRwb2h8QEo4IIO27RsfxU2_hue; liap=true; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18298%7CMCMID%7C33582537304092631233337028826612196732%7CMCAAMLH-1581511362%7C6%7CMCAAMB-1581511362%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1580913762s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-1851911619; UserMatchHistory=AQIRuZOA68w-VgAAAXAVX67ZIQOGmZ2nQ-_4dPhZt0Zs_-EcfsZOOu-_F-TzV3HKfwox6ZZz5qg; aam_uuid=33387932488196597363350868566638827191; li_oatml=AQEndSdEwxPuVgAAAXAVX6-A4OKYoLSxiull2ZIXJ0ysojvWFMX_NrPePJMm1-B7UvttX5GfQO5cAGCLFMtREi9bPWjenpO3; _ga=GA1.2.811638982.1571835098; _lipt=CwEAAAFv7IRqzvW5BWe1MdZ8oSiZ3N4BfnsE1gSPwTLdy50cKR_FwicE1vWBnT8x_sAcvh1_UDRtwAPUyf5CzcSWbXI8NWIgQ1bCyi3Y76UR0e9mS2gjcSDlXyexJqmnPrBVHP-tflhVG06fMCjxbSP0g890RqTX4WPErh2rXk6KFToLlIkCZY7FwadrVKv9xbYns6I_YpJrCA_qZCPWvu3lBabw09B0PtOQQTX6ATVHm07JY5KpnJN--M-9ymOzI6wWFXWBggkLuDeTbnhnhDW-57LIY6zvlpI9z8UF151OBYKtlFY6uAipGoc3AlNA4f0rmlE5HA; lissc=1; JSESSIONID="ajax:-1643625846928934947"; lang=v=2&lang=en-US; lidc="b=VB36:g=2829:u=20:i=1580906559:t=1580992948:s=AQFatqoC6NJ0RPXiCrYoGH6g-Z7sHkJ6"; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiJiMTFlMmRmNi05YjNlLTQ3NjgtYWJlZi1kZmE0OTgxNzc0YTN8MTU4MDkwNjU1MSIsInJlY2VudGx5LXNlYXJjaGVkIjoiIiwicmVmZXJyYWwtdXJsIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2NhbXBhaWdubWFuYWdlci9hY2NvdW50cyIsIlJOVC1pZCI6InwwIiwicmVjZW50bHktdmlld2VkIjoiIiwiQ1BULWlkIjoiTTJKaU1ESTRPV0l0TXpaaE1DMDBNekJsTFdKak16QXROVEpqT1dSak4yRmxZbUZsIiwiZXhwZXJpZW5jZSI6IiIsIndoaXRlbGlzdCI6Int9IiwidHJrIjoiIn0sIm5iZiI6MTU4MDkwNjU1MSwiaWF0IjoxNTgwOTA2NTUxfQ.v1cs7PV70O2pQkc8Wf7lCgKfe2iKRQUDmDw4VuO7P0I; PLAY_LANG=en; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'TE': 'Trailers'},
    data=testCriteria#'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A103644278,name:United%20States,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A102221843)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Ade_DE,name:German,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true',
)
# print(response.content)
print(response.text)
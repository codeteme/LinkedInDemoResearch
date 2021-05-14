import requests 
import string
import random

testheaders="""Host: www.linkedin.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Prefer: safe
x-restli-protocol-version: 2.0.0
x-li-lang: en_US
x-li-track: {"clientVersion":"2.4.542","mpVersion":"2.4.542","osName":"web","timezoneOffset":3,"timezone":"Asia/Qatar","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":1.5789473684210527,"displayWidth":3360,"displayHeight":2100}
x-li-page-instance: urn:li:page:d_campaign_details;u/m+ZDY+TzmMEWe5xxvnTA==
csrf-token: ajax:5901664971532134280
x-http-method-override: GET
content-type: application/x-www-form-urlencoded
Content-Length: 548
Origin: https://www.linkedin.com
Connection: keep-alive
Referer: https://www.linkedin.com/campaignmanager/accounts/507131805/campaigns/new/details?campaignGroupId=615557454
Cookie: JSESSIONID="ajax:5901664971532134280"; bcookie="v=2&c5f27fc8-a995-4dfd-8c37-03810153ea44"; bscookie="v=1&20210504140158723c598c-f005-41c1-8b84-6421b12f6089AQFS-UeasGOrxz960bmdW19hEqvgLdJF"; _ga=GA1.2.1101044002.1620136918; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18757%7CMCMID%7C33440669679956594540176137054812188594%7CMCAAMLH-1621254949%7C7%7CMCAAMB-1621254949%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1620657349s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1529527004; li_rm=AQGbZvsvtq8xxAAAAXk3r43BIwOwUOJqrRMQoA-nXXBCc5Xlflp62qe6ftE4-iHYdKn0mrIeEvvlftV1T82_25ZKeJ468C0zTS02yHh9pUK42WY0_Rfzpvc6; _gcl_au=1.1.1049138754.1620136927; aam_uuid=33618448150752971410197855517193788537; g_state={"i_l":0}; li_at=AQEDATWfwXIEkeTKAAABeVZaNhwAAAF5ema6HE4AE5sTR51e0Ou_oD6PPp5lFN6hDytfhk7rekah2No2u7WImuCIsAIxo8K9U0bn_PwZIQLWx3TnNMSFi9mkR19hWGZ0RVsmxt2mx2bkuAsIQ5ljLOhQ; liap=true; timezone=Asia/Qatar; UserMatchHistory=AQJ2TMNgWUX3FwAAAXlWWkhi8w6W7CSSP1m_nK1i_L-0ShroIcBYWBHto1RvxgiumMLu_DY8z8sJhxhZSFFSYJmTOPumwzIjM1EyIqctnfehlludqw0mOevZt-X1X2q6VdnhVDtTKKhdr6wLuBWmEjlW4tEtsCeVfCv1eC_6ferW6ZML5fsNlZRWxD9fpZvnIM8ZPSN3-3JpeG5cpowGZ0P1ojpLEVXuUJ2PEczKQZZ5MqLRIDpf0U4Vj9G7gkilXK26RIyuBmgE_pSxqkAoUAHAIR2mN2zuMC3B2Wc; _guid=d8116692-cff4-4116-bbd5-37609e1b4828; li_sugr=558bab07-f0ec-415c-90b8-0d9041dd1343; AnalyticsSyncHistory=AQImlOqvdD7R_wAAAXlQfsjmOND6i1KbbkULcVdo6vFDW6tfbcwSpETpDfZRJDwRY4E6byuOrYvMY0lfXk2m-w; lms_ads=AQGP9Dw1WZNgBQAAAXlQfsnqkiPbHbuCrr3HEn2_llPGxdQATkojuAixWPTFoqCoWz7F9_mPwZR83fdst0tAHUuR_tNxYWyn; lms_analytics=AQGP9Dw1WZNgBQAAAXlQfsnqkiPbHbuCrr3HEn2_llPGxdQATkojuAixWPTFoqCoWz7F9_mPwZR83fdst0tAHUuR_tNxYWyn; gpv_pn=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails; s_tslv=1620654680638; lang=v=2&lang=en-US; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; s_plt=0.83; s_pltp=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails; s_ppv=www.linkedin.com%2Fcampaignmanager%2Faccounts%2F507131805%2Fcampaigns%2Fnew%2Fdetails%2C40%2C32%2C1089%2C1%2C5; s_ips=860; s_tp=2723; s_cc=true; s_sq=lnkdprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwww.linkedin.com%25252Fcampaignmanager%25252Faccounts%25252F507131805%25252Fcampaigns%25252Fnew%25252Fdetails%2526link%253DQatar%2526region%253Dember585%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwww.linkedin.com%25252Fcampaignmanager%25252Faccounts%25252F507131805%25252Fcampaigns%25252Fnew%25252Fdetails%2526pidt%253D1%2526oid%253D%252528...e%252529%25253D%25253E%25257Bvart%25253D%25257Btarget%25253As%25252Cargs%25253Ae%25252Clabel%25253A%252522%252540glimmer%25252Fclosure-action%252522%25257D%25253Breturn%2525280%25252Cf.flaggedInstrument%252529%252528%252522inter%2526oidt%253D2%2526ot%253DTEXT; PLAY_LANG=en; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiI5ZDRmNjFjYy1hZjY4LTQ3MjgtYjM0Yi1lNmZhMWJlM2M0OGF8MTYyMDY1MTE4MiIsInJlY2VudGx5LXNlYXJjaGVkIjoiIiwicmVmZXJyYWwtdXJsIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2NhbXBhaWdubWFuYWdlci9hY2NvdW50cy81MDcxMzE4MDUvY2FtcGFpZ25zL25ldy9kZXRhaWxzIiwiYWlkIjoiIiwiUk5ULWlkIjoifDAiLCJyZWNlbnRseS12aWV3ZWQiOiI0MTg5Mjl8NDEyNDM2IiwiQ1BULWlkIjoiVGNqKVx1MDAxQsKgQsOswplcdTAwMEXDgsKDw6vCslwiwroiLCJleHBlcmllbmNlIjoiZW50aXR5IiwiaXNfbmF0aXZlIjoiZmFsc2UiLCJ3aGl0ZWxpc3QiOiJ7XCJCdXNpbmVzcyBTZWdtZW50OlN0cmF0ZWdpY1wiOlwiZmFsc2VcIn0iLCJ0cmsiOiIifSwibmJmIjoxNjIwNjUxNDI4LCJpYXQiOjE2MjA2NTE0Mjh9.f015x8cYlDaA7thZCum8apTF-smMrUUPkBr4qu3RO8Q; liveagent_oref=https://www.linkedin.com/care/embed/chat/cmtChat?useDefaultButton=false&hostApplicationName=undefined; liveagent_vc=2; liveagent_sid=18843a9a-c4de-4a4e-afbd-581a77a3a6d5; liveagent_ptid=18843a9a-c4de-4a4e-afbd-581a77a3a6d5; lidc="b=TB94:s=T:r=T:a=T:p=T:g=2685:u=3:i=1620654652:t=1620719014:v=2:sig=AQE_NQNuYOm2IAYxYHbD8Pj3CM_VbDA1"; _gid=GA1.2.1078695488.1620650176
TE: Trailers
"""
def getHeadersFromFirefox(headers):
    headers1={}
    for line in headers.split("\n")[1:-1]:
        headers1[line.split(':')[0]]= line[line.find(':')+2:]
    return headers1
headers = getHeadersFromFirefox(testheaders)
# print(headers)


# Copy the client ID, secret, and redirect URI in the fields below
CLIENT_ID    = '789co3vxpoql46'
CLIENT_SECRET = 'HPbG1NGzo0BSrsfh'
REDIRECT_URI = 'http://127.0.0.1:8000'

# Generate a random string to protect against cross-site request forgery
letters = string.ascii_lowercase
CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))


# Request authentication URL
auth_params = {'response_type': 'code',
               'client_id': CLIENT_ID,
               'redirect_uri': REDIRECT_URI,
               'state': CSRF_TOKEN,
               'scope': 'r_liteprofile,r_emailaddress'}

html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
                    params = auth_params)

# Print the link to the approval page
# print(html.url)

# response = requests.get('https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state=foobar&scope=r_liteprofile%20r_emailaddress%20w_member_social')
# print(response.content)


AUTH_CODE = 'AQQc1e_CC9oGWnrfj7y-6mek_SkO2J_wja49llawKPf1g_jotAneUqnfOkk747hQpgNFEv9tgyVabn-k3A5PydegO9zVooJUh2Yet6p3chlHix247aJqRAr6XAeAsjQlxJcsAdeX4W9P_PMXkc--hNhs7BrhG_M7eolpOQ44ptXKkQrAC_7NxjcrsdzScWltv9jaO4e3t6FpvvpPK0k'

ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

qd = {'grant_type': 'authorization_code',
      'code': AUTH_CODE,
      'redirect_uri': REDIRECT_URI,
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET}

# response = requests.post(ACCESS_TOKEN_URL, data=qd, timeout=60)
# response = response.json()

access_token = 'AQVWgl3wm_pg8oP0engahUmR41pkKF4lM4eEl-u87vYqaqzu5y1ThEknaTpu5FdLBfNi51gNeIo2qgmkMl8yO7JFhMH7YgnhaSnXtxt2ZereaZD21xJMyGoRnBZU4BDiMhIP6dVSA2bPTnyfCeSbQdP83YC4nPa-cPkDnBt_o7PjC3sOzLpRn8MmsUbzFQReHvXMJGg7GBHS8MlB_tmbZYonqGJO54YGp9c9hSsG7AnITxMj16DsJyKglpzUe4iNaWGQQ1RgYTzRRNcpVeqn4hPP2Sfui-AgT7pjqWMGS3Ih0UpRCNJ6NeM2g2J2wi6HT1EO_vDhTZRcjap_o6lw8csqiHvIyg'
# print ("Access Token:", access_token)

import json

params = {'oauth2_access_token': access_token}
response = requests.get('https://api.linkedin.com/v2/me', params = params) # Gets all the information saved about me

print(json.dumps(response.json(), indent=1))
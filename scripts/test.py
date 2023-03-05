import requests
import streamlit as st
import json
import pandas as pd
import time

cookies = {
    'bcookie': '"v=2&f54ea59a-febc-4eac-8157-57571cd2cbed"',
    'li_sugr': '25af2cec-f7b4-42cd-a455-252fe29d88fa',
    'bscookie': '"v=1&202301261457100a8356de-01c6-4a82-8bc2-d8160ca97ceeAQE8-1eobzAAExtOshSl_ioTEoTbhM_Q"',
    'li_rm': 'AQHYWxGuOdO5SAAAAYYxcZlk4q4bzJm1XV17P3nGDDG4zHOi-6tg57721RvaSBl4wCikqYi7tv39dUZDxijhijwGZfa5ufu_2SYN-HSssl0rZ0yUcbfkFbVL',
    'G_ENABLED_IDPS': 'google',
    '_gcl_au': '1.1.1644285021.1675866777',
    'aam_uuid': '48882790355094900021244224630315210561',
    'g_state': '{"i_l":0}',
    'liap': 'true',
    'JSESSIONID': '"ajax:0008567153367595254"',
    'timezone': 'Asia/Qatar',
    'li_theme': 'light',
    'li_theme_set': 'app',
    '_guid': '388d4e77-7778-410d-b3fc-908db30b172f',
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    'li_at': 'AQEDASmeNNoEWnaDAAABhjIzt4MAAAGG0V3NKk0AJPH5uUWpzV-AY0MzMR3kSBq-A60xwlBCNQdrF93Ox7ZMm99RWHqh4rFd9U0jBwBDJXQb0C6o2Kwxdz2_Fm5Uxb9FJVlBM1x2cqM_4zhGyUyTcYFg',
    'PLAY_LANG': 'en',
    'lang': 'v=2&lang=en-US',
    'liveagent_oref': 'https://www.linkedin.com/campaignmanager/',
    'liveagent_ptid': '22a3ae00-51d1-4c0b-8059-f37dad0e43a2',
    'liveagent_sid': '9a6b4a70-4422-47ab-9ca6-5936c7d1c65c',
    'liveagent_vc': '3',
    'UserMatchHistory': 'AQITuRkhojYQFAAAAYatUuQLhkd-XrrgjvyrKJiZg-t8COUubcv-La6gVktG1zpXrQ8ZJ-buymQTpFxrm_DM3cNAT8gJqo-O1BdEkZws6G1dNiHWOZtnfq3-K1KZ4mCp82JrxX4dcPUOJN17IF5S7qa3CWr8RjzogPchqDmvxJKVw-6fJM2AfnGRj6QbFAk73ktjdR3pNmxi0IwZA3U2YEWSJ44mqeb6E59J2fbLd3uiy64rUDwuHKoLbj01P8-562TUj4A9tFbnFnjgMtyxBXAl12T6FKKuqEvsQyE',
    'AnalyticsSyncHistory': 'AQL96qJ4oScAxAAAAYatUuQLF4XXUv6-jZ9ljoPfOCklQNqPLrUdm1V8grNSZMowoNphNEU2ENTcu2XOTz2uTg',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19421%7CMCMID%7C48350461644134611451264227855098193034%7CMCAAMLH-1678549936%7C6%7CMCAAMB-1678549936%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1677952336s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C986299809',
    's_plt': '2.58',
    's_pltp': 'www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaign-groups',
    's_ips': '854',
    's_cc': 'true',
    'lms_ads': 'AQGztvyJe0Bb5gAAAYatUuWlaNwDV9s-n025pcRcyurGVQ2_dglzLWrdrIccLVlJLP4Y1gZz_Hm9m06uKYH-DMRljEPM4baf',
    'lms_analytics': 'AQGztvyJe0Bb5gAAAYatUuWlaNwDV9s-n025pcRcyurGVQ2_dglzLWrdrIccLVlJLP4Y1gZz_Hm9m06uKYH-DMRljEPM4baf',
    'lidc': '"b=VB74:s=V:r=V:a=O:p=V:g=3420:u=582:x=1:i=1677945186:t=1678031586:v=2:sig=AQECr6vd9xUQfj4dR1waoY_IUsvoJZ5x"',
    'gpv_pn': 'www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaigns%2Fnew%2Fdetails',
    's_ppv': 'www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaigns%2Fnew%2Fdetails%2C36%2C22%2C1412%2C1%2C4',
    's_tp': '3896',
    's_tslv': '1677945278211',
    's_sq': '%5B%5BB%5D%5D',
}

headers = {
    'authority': 'www.linkedin.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'bcookie="v=2&f54ea59a-febc-4eac-8157-57571cd2cbed"; li_sugr=25af2cec-f7b4-42cd-a455-252fe29d88fa; bscookie="v=1&202301261457100a8356de-01c6-4a82-8bc2-d8160ca97ceeAQE8-1eobzAAExtOshSl_ioTEoTbhM_Q"; li_rm=AQHYWxGuOdO5SAAAAYYxcZlk4q4bzJm1XV17P3nGDDG4zHOi-6tg57721RvaSBl4wCikqYi7tv39dUZDxijhijwGZfa5ufu_2SYN-HSssl0rZ0yUcbfkFbVL; G_ENABLED_IDPS=google; _gcl_au=1.1.1644285021.1675866777; aam_uuid=48882790355094900021244224630315210561; g_state={"i_l":0}; liap=true; JSESSIONID="ajax:0008567153367595254"; timezone=Asia/Qatar; li_theme=light; li_theme_set=app; _guid=388d4e77-7778-410d-b3fc-908db30b172f; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; li_at=AQEDASmeNNoEWnaDAAABhjIzt4MAAAGG0V3NKk0AJPH5uUWpzV-AY0MzMR3kSBq-A60xwlBCNQdrF93Ox7ZMm99RWHqh4rFd9U0jBwBDJXQb0C6o2Kwxdz2_Fm5Uxb9FJVlBM1x2cqM_4zhGyUyTcYFg; PLAY_LANG=en; lang=v=2&lang=en-US; liveagent_oref=https://www.linkedin.com/campaignmanager/; liveagent_ptid=22a3ae00-51d1-4c0b-8059-f37dad0e43a2; liveagent_sid=9a6b4a70-4422-47ab-9ca6-5936c7d1c65c; liveagent_vc=3; UserMatchHistory=AQITuRkhojYQFAAAAYatUuQLhkd-XrrgjvyrKJiZg-t8COUubcv-La6gVktG1zpXrQ8ZJ-buymQTpFxrm_DM3cNAT8gJqo-O1BdEkZws6G1dNiHWOZtnfq3-K1KZ4mCp82JrxX4dcPUOJN17IF5S7qa3CWr8RjzogPchqDmvxJKVw-6fJM2AfnGRj6QbFAk73ktjdR3pNmxi0IwZA3U2YEWSJ44mqeb6E59J2fbLd3uiy64rUDwuHKoLbj01P8-562TUj4A9tFbnFnjgMtyxBXAl12T6FKKuqEvsQyE; AnalyticsSyncHistory=AQL96qJ4oScAxAAAAYatUuQLF4XXUv6-jZ9ljoPfOCklQNqPLrUdm1V8grNSZMowoNphNEU2ENTcu2XOTz2uTg; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19421%7CMCMID%7C48350461644134611451264227855098193034%7CMCAAMLH-1678549936%7C6%7CMCAAMB-1678549936%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1677952336s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C986299809; s_plt=2.58; s_pltp=www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaign-groups; s_ips=854; s_cc=true; lms_ads=AQGztvyJe0Bb5gAAAYatUuWlaNwDV9s-n025pcRcyurGVQ2_dglzLWrdrIccLVlJLP4Y1gZz_Hm9m06uKYH-DMRljEPM4baf; lms_analytics=AQGztvyJe0Bb5gAAAYatUuWlaNwDV9s-n025pcRcyurGVQ2_dglzLWrdrIccLVlJLP4Y1gZz_Hm9m06uKYH-DMRljEPM4baf; lidc="b=VB74:s=V:r=V:a=O:p=V:g=3420:u=582:x=1:i=1677945186:t=1678031586:v=2:sig=AQECr6vd9xUQfj4dR1waoY_IUsvoJZ5x"; gpv_pn=www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaigns%2Fnew%2Fdetails; s_ppv=www.linkedin.com%2Fcampaignmanager%2Faccounts%2Fid-redacted%2Fcampaigns%2Fnew%2Fdetails%2C36%2C22%2C1412%2C1%2C4; s_tp=3896; s_tslv=1677945278211; s_sq=%5B%5BB%5D%5D',
    'csrf-token': 'ajax:0008567153367595254',
    'origin': 'https://www.linkedin.com',
    'referer': 'https://www.linkedin.com/campaignmanager/accounts/506462727/campaigns/new/details?campaignGroupId=604745784',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
    'x-http-method-override': 'GET',
    'x-li-er-key': 'urn:li:sponsoredAccount:506462727',
    'x-li-lang': 'en_US',
    'x-li-page-instance': 'urn:li:page:d_campaign_details;mbH0R48BQACdxuhtU9KKFA==',
    'x-li-track': '{"clientVersion":"2.24.1456","mpVersion":"2.24.1456","osName":"web","timezoneOffset":3,"timezone":"Asia/Qatar","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":2,"displayWidth":3360,"displayHeight":2100}',
    'x-restli-protocol-version': '2.0.0',
}


locationsegments = {'Afghanistan': {'urn': 'urn:li:geo:101240012', 'name': 'Afghanistan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Albania': {'urn': 'urn:li:geo:102845717', 'name': 'Albania', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Algeria': {'urn': 'urn:li:geo:106395874', 'name': 'Algeria', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Angola': {'urn': 'urn:li:geo:105371935', 'name': 'Angola', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Argentina': {'urn': 'urn:li:geo:100446943', 'name': 'Argentina', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Armenia': {'urn': 'urn:li:geo:103030111', 'name': 'Armenia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Australia': {'urn': 'urn:li:geo:101452733', 'name': 'Australia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506852))'}, 
                    'Austria': {'urn': 'urn:li:geo:103883259', 'name': 'Austria', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Azerbaijan': {'urn': 'urn:li:geo:103226548', 'name': 'Azerbaijan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'The Bahamas': {'urn': 'urn:li:geo:106662619', 'name': 'The Bahamas', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Bahrain': {'urn': 'urn:li:geo:100425729', 'name': 'Bahrain', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bangladesh': {'urn': 'urn:li:geo:106215326', 'name': 'Bangladesh', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Barbados': {'urn': 'urn:li:geo:102118611', 'name': 'Barbados', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Belarus': {'urn': 'urn:li:geo:101705918', 'name': 'Belarus', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Belgium': {'urn': 'urn:li:geo:100565514', 'name': 'Belgium', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Belize': {'urn': 'urn:li:geo:105912732', 'name': 'Belize', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Benin': {'urn': 'urn:li:geo:101519029', 'name': 'Benin', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Bhutan': {'urn': 'urn:li:geo:103613266', 'name': 'Bhutan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bolivia': {'urn': 'urn:li:geo:104379274', 'name': 'Bolivia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Bosnia and Herzegovina': {'urn': 'urn:li:geo:102869081', 'name': 'Bosnia and Herzegovina', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Botswana': {'urn': 'urn:li:geo:105698121', 'name': 'Botswana', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Bouvet Island': {'urn': 'urn:li:geo:102127336', 'name': 'Bouvet Island', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Brazil': {'urn': 'urn:li:geo:106057199', 'name': 'Brazil', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Brunei': {'urn': 'urn:li:geo:103809722', 'name': 'Brunei', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Bulgaria': {'urn': 'urn:li:geo:105333783', 'name': 'Bulgaria', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Burkina Faso': {'urn': 'urn:li:geo:100587095', 'name': 'Burkina Faso', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Burundi': {'urn': 'urn:li:geo:100800406', 'name': 'Burundi', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Cambodia': {'urn': 'urn:li:geo:102500897', 'name': 'Cambodia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Cameroon': {'urn': 'urn:li:geo:105745966', 'name': 'Cameroon', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Canada': {'urn': 'urn:li:geo:101174742', 'name': 'Canada', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Cape Verde': {'urn': 'urn:li:geo:101679268', 'name': 'Cape Verde', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Central African Republic': {'urn': 'urn:li:geo:100134827', 'name': 'Central African Republic', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Chad': {'urn': 'urn:li:geo:104655384', 'name': 'Chad', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Chile': {'urn': 'urn:li:geo:104621616', 'name': 'Chile', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'China': {'urn': 'urn:li:geo:102890883', 'name': 'China', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Colombia': {'urn': 'urn:li:geo:100876405', 'name': 'Colombia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Comoros': {'urn': 'urn:li:geo:103069791', 'name': 'Comoros', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Republic of the Congo': {'urn': 'urn:li:geo:106796687', 'name': 'Republic of the Congo', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Congo (DRC)': {'urn': 'urn:li:geo:101271829', 'name': 'Congo (DRC)', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Costa Rica': {'urn': 'urn:li:geo:101739942', 'name': 'Costa Rica', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Côte d’Ivoire': {'urn': 'urn:li:geo:103295271', 'name': 'Côte d’Ivoire', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Croatia': {'urn': 'urn:li:geo:104688944', 'name': 'Croatia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Cyprus': {'urn': 'urn:li:geo:106774002', 'name': 'Cyprus', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Czechia': {'urn': 'urn:li:geo:104508036', 'name': 'Czechia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Denmark': {'urn': 'urn:li:geo:104514075', 'name': 'Denmark', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Djibouti': {'urn': 'urn:li:geo:100371290', 'name': 'Djibouti', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Dominican Republic': {'urn': 'urn:li:geo:105057336', 'name': 'Dominican Republic', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Ecuador': {'urn': 'urn:li:geo:106373116', 'name': 'Ecuador', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Egypt': {'urn': 'urn:li:geo:106155005', 'name': 'Egypt', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'El Salvador': {'urn': 'urn:li:geo:106522560', 'name': 'El Salvador', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Equatorial Guinea': {'urn': 'urn:li:geo:105141335', 'name': 'Equatorial Guinea', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Eritrea': {'urn': 'urn:li:geo:104219996', 'name': 'Eritrea', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Estonia': {'urn': 'urn:li:geo:102974008', 'name': 'Estonia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Ethiopia': {'urn': 'urn:li:geo:100212432', 'name': 'Ethiopia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Falkland Islands': {'urn': 'urn:li:geo:104961595', 'name': 'Falkland Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Fiji': {'urn': 'urn:li:geo:105733447', 'name': 'Fiji', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 'Finland': {'urn': 'urn:li:geo:100456013', 'name': 
                    'Finland', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'France': {'urn': 'urn:li:geo:105015875', 'name': 
                    'France', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'French Guiana': {'urn': 'urn:li:geo:105001561', 'name': 
                    'French Guiana', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 'French Polynesia': {'urn': 'urn:li:geo:102681285', 'name': 
                    'French Polynesia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 'French Southern and Antarctic Lands': {'urn': 'urn:li:geo:104827874', 'name': 
                    'French Southern and Antarctic Lands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 'Gabon': {'urn': 'urn:li:geo:104471338', 'name': 
                    'Gabon', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'The Gambia': {'urn': 'urn:li:geo:106100033', 'name': 
                    'The Gambia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Georgia': {'urn': 'urn:li:geo:106315325', 'name': 
                    'Georgia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 'Germany': {'urn': 'urn:li:geo:101282230', 'name': 
                    'Germany', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Ghana': {'urn': 'urn:li:geo:105769538', 'name': 
                    'Ghana', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Greece': {'urn': 'urn:li:geo:104677530', 'name': 
                    'Greece', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Grenada': {'urn': 'urn:li:geo:104579260', 'name': 
                    'Grenada', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 'Guatemala': {'urn': 'urn:li:geo:100877388', 'name': 
                    'Guatemala', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 'Guernsey': {'urn': 'urn:li:geo:104019891', 'name': 
                    'Guernsey', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 'Guinea': {'urn': 'urn:li:geo:100099594', 'name': 
                    'Guinea', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Guinea-Bissau': {'urn': 'urn:li:geo:100115557', 'name': 
                    'Guinea-Bissau', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 'Guyana': {'urn': 'urn:li:geo:105836293', 'name': 
                    'Guyana', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 'Haiti': {'urn': 'urn:li:geo:100993490', 'name': 
                    'Haiti', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Heard Island and McDonald Islands': {'urn': 'urn:li:geo:100737582', 'name': 'Heard Island and McDonald Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Vatican City': {'urn': 'urn:li:geo:107163060', 'name': 'Vatican City', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Honduras': {'urn': 'urn:li:geo:101937718', 'name': 'Honduras', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Hong Kong SAR': {'urn': 'urn:li:geo:103291313', 'name': 'Hong Kong SAR', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Hungary': {'urn': 'urn:li:geo:100288700', 'name': 'Hungary', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Iceland': {'urn': 'urn:li:geo:105238872', 'name': 'Iceland', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'India': {'urn': 'urn:li:geo:102713980', 'name': 'India', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Indonesia': {'urn': 'urn:li:geo:102478259', 'name': 'Indonesia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Iraq': {'urn': 'urn:li:geo:106725625', 'name': 'Iraq', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Ireland': {'urn': 'urn:li:geo:104738515', 'name': 'Ireland', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Israel': {'urn': 'urn:li:geo:101620260', 'name': 'Israel', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Italy': {'urn': 'urn:li:geo:103350119', 'name': 'Italy', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Jamaica': {'urn': 'urn:li:geo:105126983', 'name': 'Jamaica', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Japan': {'urn': 'urn:li:geo:101355337', 'name': 'Japan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Jersey': {'urn': 'urn:li:geo:102705533', 'name': 'Jersey', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Jordan': {'urn': 'urn:li:geo:103710677', 'name': 'Jordan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kazakhstan': {'urn': 'urn:li:geo:106049128', 'name': 'Kazakhstan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kenya': {'urn': 'urn:li:geo:100710459', 'name': 'Kenya', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Korea': {'urn': 'urn:li:geo:105149562', 'name': 'South Korea', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kosovo': {'urn': 'urn:li:geo:104640522', 'name': 'Kosovo', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Kuwait': {'urn': 'urn:li:geo:103239229', 'name': 'Kuwait', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Kyrgyzstan': {'urn': 'urn:li:geo:103490790', 'name': 'Kyrgyzstan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Laos': {'urn': 'urn:li:geo:100664862', 'name': 'Laos', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Latvia': {'urn': 'urn:li:geo:104341318', 'name': 'Latvia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Lebanon': {'urn': 'urn:li:geo:101834488', 'name': 'Lebanon', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Lesotho': {'urn': 'urn:li:geo:103712797', 'name': 'Lesotho', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Liberia': {'urn': 'urn:li:geo:106579411', 'name': 'Liberia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Libya': {'urn': 'urn:li:geo:104036859', 'name': 'Libya', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Lithuania': {'urn': 'urn:li:geo:101464403', 'name': 'Lithuania', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Luxembourg': {'urn': 'urn:li:geo:104042105', 'name': 'Luxembourg', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Macao SAR': {'urn': 'urn:li:geo:101316508', 'name': 'Macao SAR', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'North Macedonia': {'urn': 'urn:li:geo:103420483', 'name': 'North Macedonia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Madagascar': {'urn': 'urn:li:geo:105587166', 'name': 'Madagascar', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malawi': {'urn': 'urn:li:geo:105992277', 'name': 'Malawi', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malaysia': {'urn': 'urn:li:geo:106808692', 'name': 'Malaysia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Maldives': {'urn': 'urn:li:geo:102161637', 'name': 'Maldives', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Mali': {'urn': 'urn:li:geo:100770782', 'name': 'Mali', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Malta': {'urn': 'urn:li:geo:100961908', 'name': 'Malta', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Marshall Islands': {'urn': 'urn:li:geo:106516799', 'name': 'Marshall Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'French-Martinique': {'urn': 'urn:li:geo:103091690', 'name': 'French-Martinique', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Mauritania': {'urn': 'urn:li:geo:106950838', 'name': 'Mauritania', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mauritius': {'urn': 'urn:li:geo:106931611', 'name': 'Mauritius', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Mayotte': {'urn': 'urn:li:geo:104097939', 'name': 'Mayotte', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mexico': {'urn': 'urn:li:geo:103323778', 'name': 'Mexico', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Moldova': {'urn': 'urn:li:geo:106178099', 'name': 'Moldova', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Mongolia': {'urn': 'urn:li:geo:102396337', 'name': 'Mongolia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Montenegro': {'urn': 'urn:li:geo:100733275', 'name': 'Montenegro', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Montserrat': {'urn': 'urn:li:geo:101150476', 'name': 'Montserrat', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Morocco': {'urn': 'urn:li:geo:102787409', 'name': 'Morocco', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Mozambique': {'urn': 'urn:li:geo:100474128', 'name': 'Mozambique', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Myanmar': {'urn': 'urn:li:geo:104136533', 'name': 'Myanmar', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Namibia': {'urn': 'urn:li:geo:106682822', 'name': 'Namibia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Nepal': {'urn': 'urn:li:geo:104630404', 'name': 'Nepal', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Netherlands': {'urn': 'urn:li:geo:102890719', 'name': 'Netherlands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'New Caledonia': {'urn': 'urn:li:geo:105535747', 'name': 'New Caledonia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'New Zealand': {'urn': 'urn:li:geo:105490917', 'name': 'New Zealand', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Nicaragua': {'urn': 'urn:li:geo:105517145', 'name': 'Nicaragua', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Niger': {'urn': 'urn:li:geo:103550069', 'name': 'Niger', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Nigeria': {'urn': 'urn:li:geo:105365761', 'name': 'Nigeria', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Niue': {'urn': 'urn:li:geo:102139488', 'name': 'Niue', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Norfolk Island': {'urn': 'urn:li:geo:100646662', 'name': 'Norfolk Island', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Norway': {'urn': 'urn:li:geo:103819153', 'name': 'Norway', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Oman': {'urn': 'urn:li:geo:103619019', 'name': 'Oman', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Pakistan': {'urn': 'urn:li:geo:101022442', 'name': 'Pakistan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Palestinian Authority': {'urn': 'urn:li:geo:93000000', 'name': 'Palestinian Authority', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Panama': {'urn': 'urn:li:geo:100808673', 'name': 'Panama', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Papua New Guinea': {'urn': 'urn:li:geo:100152180', 'name': 'Papua New Guinea', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Paraguay': {'urn': 'urn:li:geo:104065273', 'name': 'Paraguay', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Peru': {'urn': 'urn:li:geo:102927786', 'name': 'Peru', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Philippines': {'urn': 'urn:li:geo:103121230', 'name': 'Philippines', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Pitcairn Islands': {'urn': 'urn:li:geo:104322374', 'name': 'Pitcairn Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Poland': {'urn': 'urn:li:geo:105072130', 'name': 'Poland', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Portugal': {'urn': 'urn:li:geo:100364837', 'name': 'Portugal', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Puerto Rico': {'urn': 'urn:li:geo:105245958', 'name': 'Puerto Rico', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Qatar': {'urn': 'urn:li:geo:104170880', 'name': 'Qatar', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Serbia': {'urn': 'urn:li:geo:101855366', 'name': 'Serbia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Reunion': {'urn': 'urn:li:geo:104265812', 'name': 'Reunion', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Romania': {'urn': 'urn:li:geo:106670623', 'name': 'Romania', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Russia': {'urn': 'urn:li:geo:101728296', 'name': 'Russia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Rwanda': {'urn': 'urn:li:geo:103547315', 'name': 'Rwanda', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Saint Barthelemy': {'urn': 'urn:li:geo:100936035', 'name': 'Saint Barthelemy', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Saint Pierre and Miquelon': {'urn': 'urn:li:geo:102024132', 'name': 'Saint Pierre and Miquelon', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'São Tomé and Príncipe': {'urn': 'urn:li:geo:106867470', 'name': 'São Tomé and Príncipe', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Saudi Arabia': {'urn': 'urn:li:geo:100459316', 'name': 'Saudi Arabia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Senegal': {'urn': 'urn:li:geo:103587512', 'name': 'Senegal', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Singapore': {'urn': 'urn:li:geo:102454443', 'name': 'Singapore', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Slovakia': {'urn': 'urn:li:geo:103119917', 'name': 'Slovakia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Slovenia': {'urn': 'urn:li:geo:106137034', 'name': 'Slovenia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Solomon Islands': {'urn': 'urn:li:geo:104980134', 'name': 'Solomon Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Somalia': {'urn': 'urn:li:geo:104725424', 'name': 'Somalia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Africa': {'urn': 'urn:li:geo:104035573', 'name': 'South Africa', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'South Georgia and South Sandwich Islands': {'urn': 'urn:li:geo:103665423', 'name': 'South Georgia and South Sandwich Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'South Sudan': {'urn': 'urn:li:geo:103622308', 'name': 'South Sudan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Spain': {'urn': 'urn:li:geo:105646813', 'name': 'Spain', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Sri Lanka': {'urn': 'urn:li:geo:100446352', 'name': 'Sri Lanka', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Suriname': {'urn': 'urn:li:geo:105530931', 'name': 'Suriname', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Eswatini': {'urn': 'urn:li:geo:106768907', 'name': 'Eswatini', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Sweden': {'urn': 'urn:li:geo:105117694', 'name': 'Sweden', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Switzerland': {'urn': 'urn:li:geo:106693272', 'name': 'Switzerland', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'Tajikistan': {'urn': 'urn:li:geo:105925962', 'name': 'Tajikistan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Tanzania': {'urn': 'urn:li:geo:104604145', 'name': 'Tanzania', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Thailand': {'urn': 'urn:li:geo:105146118', 'name': 'Thailand', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Timor-Leste': {'urn': 'urn:li:geo:101101678', 'name': 'Timor-Leste', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Togo': {'urn': 'urn:li:geo:103603395', 'name': 'Togo', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Tokelau': {'urn': 'urn:li:geo:100212364', 'name': 'Tokelau', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Trinidad and Tobago': {'urn': 'urn:li:geo:106947126', 'name': 'Trinidad and Tobago', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Tunisia': {'urn': 'urn:li:geo:102134353', 'name': 'Tunisia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Turkey': {'urn': 'urn:li:geo:102105699', 'name': 'Turkey', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Turkmenistan': {'urn': 'urn:li:geo:105449295', 'name': 'Turkmenistan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Turks and Caicos Islands': {'urn': 'urn:li:geo:100771715', 'name': 'Turks and Caicos Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Tuvalu': {'urn': 'urn:li:geo:103609605', 'name': 'Tuvalu', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Uganda': {'urn': 'urn:li:geo:106943612', 'name': 'Uganda', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Ukraine': {'urn': 'urn:li:geo:102264497', 'name': 'Ukraine', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'United Arab Emirates': {'urn': 'urn:li:geo:104305776', 'name': 'United Arab Emirates', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'United Kingdom': {'urn': 'urn:li:geo:101165590', 'name': 'United Kingdom', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:100506914))'}, 
                    'United States': {'urn': 'urn:li:geo:103644278', 'name': 'United States', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Uruguay': {'urn': 'urn:li:geo:100867946', 'name': 'Uruguay', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Uzbekistan': {'urn': 'urn:li:geo:107734735', 'name': 'Uzbekistan', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Vanuatu': {'urn': 'urn:li:geo:102185308', 'name': 'Vanuatu', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Venezuela': {'urn': 'urn:li:geo:101490751', 'name': 'Venezuela', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:104514572))'}, 
                    'Vietnam': {'urn': 'urn:li:geo:104195383', 'name': 'Vietnam', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'US Virgin Islands': {'urn': 'urn:li:geo:102119762', 'name': 'US Virgin Islands', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102221843))'}, 
                    'Wallis and Futuna': {'urn': 'urn:li:geo:104246629', 'name': 'Wallis and Futuna', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List())'}, 
                    'Yemen': {'urn': 'urn:li:geo:105962095', 'name': 'Yemen', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:102393603))'}, 
                    'Zambia': {'urn': 'urn:li:geo:102120260', 'name': 'Zambia', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801))'}, 
                    'Zimbabwe': {'urn': 'urn:li:geo:101367137', 'name': 'Zimbabwe', 'facetUrn': 'urn:li:adTargetingFacet:profileLocations', 'ancestorUrns': 'List(urn:li:geo:103537801)'}}

original_dict = locationsegments

formatted_locationsegments = {}
for country, info in original_dict.items():
    geo_id = info['urn'].split(':')[-1]
    ancestor_geo_id = info['ancestorUrns'].split(':')[-1][:-2]
    new_key = country.replace(' ', '%20')
    new_value = [new_key, geo_id, ancestor_geo_id]
    formatted_locationsegments[country] = new_value

# Set author and date
st.write("""
## LinkedIn Ad Campaign Forecast Demo
#### by Temesgen Tewolde
###### Last Update: March 5, 2023
""")
         
st.caption('This is a demo application that allows users to select a country from a dropdown list and see the corresponding LinkedIn API request. The application provides four metrics: Spend, Reach, Cost per 1,000 member accounts reached, and Frequency, which are explained in a collapsible container that can be expanded and collapsed as needed. Additionally, the application displays the estimated target audience size for the selected country. The user can click the "Submit Request" button to retrieve data from LinkedIn\'s API and view the forecast for the selected country based on the chosen metrics.')

# Define the text to be displayed when the info button is clicked
# Define the content to show in the help section
help_text = """

**Spend**

Projected amount spent for your campaign. This number will vary based on your target audience, schedule, budget, and more.

**Reach**

The projected number of unique member accounts that are shown at least one ad in your campaign selected this time period. This number will vary based on your target audience, schedule, budget, member activity, auction dynamics, and more. For campaigns running on our Audience Network, some traffic is excluded from this metric, so it may be particularly approximate. 

**Cost per 1,000 member accounts reached**

The projected amount spent per 1,000 member accounts reached for your campaign. This number will vary based on target audience, schedule, budget, and more.

**Frequency**

The projected average number of times each member account is shown an ad in your campaign during selected time period. This number will vary based on your target audience, schedule, budget, member activity, auction dynamics, and more. For campaigns running on our Audience Network, some traffic is excluded from this metric, so it may be particularly approximate.

For more information: https://www.linkedin.com/help/lms/answer/a423317
"""

# Show the help text in a collapsible container
with st.expander("ℹ️ Help"):
    st.markdown(help_text)


st.write('Select a country from the dropdown list to see the corresponding LinkedIn API request.')



# Create the country dropdown list
selected_country = st.selectbox('Select a country', list(locationsegments.keys()))
if st.button("Submit Request"):
    # Get the location segments for the selected country
    target_country = selected_country
    new_key = formatted_locationsegments.get(target_country)[0]
    geo_id = formatted_locationsegments.get(target_country)[1]
    ancestor_geo_id = formatted_locationsegments.get(target_country)[2]

    # Define the LinkedIn API request data
    start_time = 1677974400000
    st.write(start_time)
    
    data_forecasting = 'q=criteria&accountId=506462727&adFormats=List(STANDARD_SPONSORED_CONTENT)&runSchedule=(start:{})&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A{},name:{},facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A{})))))))),exclude:(or:List()))&objectiveType=BRAND_AWARENESS&costType=CPM&unitCost=(amount:50.79,currencyCode:USD)&dailyBudget=(amount:100.0,currencyCode:USD)&optimizationTargetType=MAX_REACH&audienceExpansionEnabled=true&offsiteDeliveryEnabled=true'.format(start_time, geo_id, new_key, ancestor_geo_id)
    data_audiencecounts = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A{},name:{},facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A{})))))))),exclude:(or:List()))&withValidation=true'.format(geo_id, new_key, ancestor_geo_id)


    response_forecasting = requests.post(
        'https://www.linkedin.com/campaign-manager-api/campaignManagerForecasting',
        cookies=cookies,
        headers=headers,
        data=data_forecasting,
    )

    response_audiencecounts = requests.post(
        'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
        cookies=cookies,
        headers=headers,
        data=data_audiencecounts,
    )

    # Show the response
    st.write('LinkedIn API response:')
    # Extract the required information 
    parsed_data_forecasting = json.loads(response_forecasting.text)
    parsed_data_audiencecounts = json.loads(response_audiencecounts.text)

    count_value = parsed_data_audiencecounts['elements'][0]['count']
    st.write("Target audience size: ", count_value)


    monthly_data = parsed_data_forecasting['elements'][0]['monthly']
    month_spend = f"${monthly_data['spend']['lowEnd']:.2f} - ${monthly_data['spend']['highEnd']:.2f}"
    month_reach = f"{monthly_data['reach']['lowEnd']} - {monthly_data['reach']['highEnd']}"
    month_cost_per_1000 = f"${monthly_data['costPerKeyResult']['lowEnd']:.2f} - ${monthly_data['costPerKeyResult']['highEnd']:.2f}"
    month_avg_frequency = f"{monthly_data['frequencyPerReachedMember']['lowEnd']:.1f} - {monthly_data['frequencyPerReachedMember']['highEnd']:.1f}"

    # Extract the required information for week
    weekly_data = parsed_data_forecasting['elements'][0]['weekly']
    week_spend = f"${weekly_data['spend']['lowEnd']:.2f} - ${weekly_data['spend']['highEnd']:.2f}"
    week_reach = f"{weekly_data['reach']['lowEnd']} - {weekly_data['reach']['highEnd']}"
    week_cost_per_1000 = f"${weekly_data['costPerKeyResult']['lowEnd']:.2f} - ${weekly_data['costPerKeyResult']['highEnd']:.2f}"
    week_avg_frequency = f"{weekly_data['frequencyPerReachedMember']['lowEnd']:.1f} - {weekly_data['frequencyPerReachedMember']['highEnd']:.1f}"

    # Extract the required information for day
    daily_data = parsed_data_forecasting['elements'][0]['daily']
    day_spend = f"${daily_data['spend']['lowEnd']:.2f} - ${daily_data['spend']['highEnd']:.2f}"
    day_reach = f"{daily_data['reach']['lowEnd']} - {daily_data['reach']['highEnd']}"
    day_cost_per_1000 = f"${daily_data['costPerKeyResult']['lowEnd']:.2f} - ${daily_data['costPerKeyResult']['highEnd']:.2f}"
    day_avg_frequency = f"{daily_data['frequencyPerReachedMember']['lowEnd']:.1f} - {daily_data['frequencyPerReachedMember']['highEnd']:.1f}"

    # Extract the required information for custom
    custom_data = parsed_data_forecasting['elements'][0]['custom']
    custom_spend = f"${custom_data['spend']['lowEnd']:.2f} - ${custom_data['spend']['highEnd']:.2f}"
    custom_clicks = f"{custom_data['clicks']['lowEnd']} - {custom_data['clicks']['highEnd']}"
    custom_impressions = f"{custom_data['impressions']['lowEnd']} - {custom_data['impressions']['highEnd']}"


    # Create a DataFrame with the required columns and data
    data = {'Month': [month_spend, month_reach, month_cost_per_1000, month_avg_frequency],
            'Week': [week_spend, week_reach, week_cost_per_1000, week_avg_frequency],
            'Day': [day_spend, day_reach, day_cost_per_1000, day_avg_frequency]}
    df = pd.DataFrame(data=data, index=['spend', 'reach', 'cost per 1,000 member accounts reached', 'average frequency'])

    # Display the DataFrame in a table
    st.dataframe(df, use_container_width=True)

    data_as_csv= df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download table as CSV", 
        data_as_csv, 
        f"{selected_country}.csv",
        "text/csv",
        key="download-tools-csv",
    )

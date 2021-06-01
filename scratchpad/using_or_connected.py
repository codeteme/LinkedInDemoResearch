
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

# exclude_list = [OR_builder([jobseniority_builder(seniority_list)])]

# arg_list = [locale_builder(), 
#             location_builder(country_list),
#             or_connected_3]
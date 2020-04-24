import pickle

# dict1 = {
# 'calender_event': {'event_id': 1, 'date': -1, 'organiser_event_user': 1, 'priority': 1, 'event_type': -1, 'going': 1}, 
# 'event': {'Event_id': 1, 'Organiser_name': -1, 'Date': -1, 'Venue': -1, 'Time': -1, 'Dress_code': -1, 'Field': -1}, 
# 'event_id_people_invited': {'Person_id': 1}, 
# 'family_circle': {'Owner_ID': 1, 'Owner_name': -1, 'Circle_members': -1, 'Circle_members_id': 1}, 
# 'family_folder': {'event_id': 1, 'event_folder_url': -1}, 
# 'insurance_company': {'Person_id': 1, 'Policy_type': -1, 'Premium_amount': 1, 'Policy_term': 1, 'Sum_assured': 1, 'Policy_id': 1}, 
# 'medical_sercives': {'Person_id': 1, 'Hospital_name': -1, 'Consultant_name': -1, 'Total_fees': 1, 'Disease': -1, 'checkup_date': -1}, 
# 'relation': {'user_1_id': 1, 'user_2_id': 1, 'relation_type': -1, 'priority': 1}, 
# 'school': {'Person_id': 1, 'School': -1, 'Class': 1}, 
# 'social_media': {'Person_id': 1, 'Social_network_service': -1, 'Handle': -1}, 
# 'subscription': {'Person_id': 1, 'subscription_service': -1, 'Account_type': -1, 'Account_id': -1}, 
# 'user_data': {'Name': -1, 'Person_id': 1, 'Age': 1, 'Birthday': -1, 'contact_no': -1, 'email_id': -1, 'Anniversery': -1}}

dict1 = {
'calender_event': {'date': 3, 'event_id': 1, 'event_type': 2, 'going': 2, 'name': 2, 'organiser_event_user': 2, 'priority': 1, 'user_id': 1}, 
'event': {'Date': 3, 'Dress_code': 2, 'Event_id': 1, 'Event_name': 2, 'Organiser_id': 1, 'Organiser_name': 2, 'Time': 4, 'Venue': 2}, 
'event_id_people_invited': {'Event_id': 1, 'Person_id': 1}, 
'family_circle': {'Circle_members': 2, 'Circle_members_id': 1, 'Group_id': 1, 'Owner_ID': 1, 'Owner_name': 2}, 
'family_folder': {'event_folder_url': 2, 'event_id': 1, 'people_shared_id': 1}, 
'insurance': {'Person_id': 1, 'Policy_id': 1, 'policy_taken_date': 3, 'Policy_term': 1, 'Policy_type': 2, 'Premium_amount': 1, 'Sum_assured': 1}, 
'medical_sercives': {'checkup_date': 3, 'Consultant_name': 2, 'Disease': 2, 'Hospital_name': 2, 'Patient_id': 1, 'Person_id': 1, 'Total_fees': 1}, 
'relation': {'priority': 1, 'relation_type': 2, 'user_1_id': 1, 'user_2_id': 1}, 
'school': {'Class': 1, 'Person_id': 1, 'School': 2, 'School_id': 1}, 
'social_media': {'Handle': 2, 'Person_id': 1, 'Social_network_service': 2}, 
'subscription': {'Account_id': 2, 'Account_type': 2, 'Person_id': 1, 'subscription_service': 2}, 
'user_data': {'Age': 1, 'Anniversery': 3, 'Birthday': 3, 'contact_no': 2, 'email_id': 2, 'Name': 2, 'Person_id': 1, 'Premium': 2, 'Validity': 3}}

f = open('helper.pkl', 'wb')
pickle.dump(dict1, f)
f.close()


# dict1 = {}
# for i in range(len(result)):
#     dict1[result[i][0]] = {}
#     query = f"""select column_name from information_schema.columns where table_name = '{result[i][0]}'"""
#     # print(query)
#     cursor.execute(query);
#     result1 = cursor.fetchall()
#     for j in range(len(result1)):
#         dict1[result[i][0]][result1[j][0]] = -1

# print(dict1)
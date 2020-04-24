import pickle

dict1 = {
'calender_event': {'event_id': 1, 'date': -1, 'organiser_event_user': 1, 'priority': 1, 'event_type': -1, 'going': 1}, 
'event': {'Event_id': 1, 'Organiser_name': -1, 'Date': -1, 'Venue': -1, 'Time': -1, 'Dress_code': -1, 'Field': -1}, 
'event_id_people_invited': {'Person_id': 1}, 
'family_circle': {'Owner_ID': 1, 'Owner_name': -1, 'Circle_members': -1, 'Circle_members_id': 1}, 
'family_folder': {'event_id': 1, 'event_folder_url': -1}, 
'insurance_company': {'Person_id': 1, 'Policy_type': -1, 'Premium_amount': 1, 'Policy_term': 1, 'Sum_assured': 1, 'Policy_id': 1}, 
'medical_sercives': {'Person_id': 1, 'Hospital_name': -1, 'Consultant_name': -1, 'Total_fees': 1, 'Disease': -1, 'checkup_date': -1}, 
'relation': {'user_1_id': 1, 'user_2_id': 1, 'relation_type': -1, 'priority': 1}, 
'school': {'Person_id': 1, 'School': -1, 'Class': 1}, 
'social_media': {'Person_id': 1, 'Social_network_service': -1, 'Handle': -1}, 
'subscription': {'Person_id': 1, 'subscription_service': -1, 'Account_type': -1, 'Account_id': -1}, 
'user_data': {'Name': -1, 'Person_id': 1, 'Age': 1, 'Birthday': -1, 'contact_no': -1, 'email_id': -1, 'Anniversery': -1}}

f = open('helper.pkl', 'wb')
pickle.dump(dict1, f)
f.close()

#import dependencies
import pandas as pd
import os
import numpy as np
from datetime import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
import plotly
import plotly.offline as py
import plotly.graph_objs as go
from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px

######################################################STEP 1
# incorporate data into app
data_file_path = 'C:\\Users\\ssteffen\\University of Idaho\\Storage-Boise - ECHO\\Staff\\Sam\\Data\\Spreadsheets\\Email data\\email_data.csv'

# read the data into a dataframe
email_data_df = pd.read_csv(data_file_path)

#drop unnecessary columns
email_data_df = email_data_df.drop(['List',
                                    'Send Date-time',
                                    'Soft Bounces',
                                    'Hard Bounces',
                                    'Abuse Complaints',
                                    'Folder Id',
                                    'Unique Id',
                                    'Total Orders',
                                    'Total Gross Sales',
                                    'Total Revenue',
                                    'Analytics ROI',
                                    'Campaign Cost',
                                    'Revenue Created',
                                    'Goal Conversion Rate',
                                    'Per Visit Goal Value',
                                    'Transactions',
                                    'Ecommerce Conversion Rate',
                                    'Per Visit Value',
                                    'Average Value',
                                    'Time on Site'
                                   ], axis=1)

#replace the NaN values with 0 to proceed with the analysis
email_data_df['Total Bounces'] = email_data_df['Total Bounces'].fillna(0)
email_data_df['Times Forwarded'] = email_data_df['Times Forwarded'].fillna(0)
email_data_df['Forwarded Opens'] = email_data_df['Forwarded Opens'].fillna(0)
email_data_df['Times Liked on Facebook'] = email_data_df['Times Liked on Facebook'].fillna(0)
email_data_df['Visits'] = email_data_df['Visits'].fillna(0)
email_data_df['New Visits'] = email_data_df['New Visits'].fillna(0)
email_data_df['Pages/Visit'] = email_data_df['Pages/Visit'].fillna(0)
email_data_df['Bounce Rate'] = email_data_df['Bounce Rate'].fillna(0)

#rename the columns
email_data_df.rename(columns={'Send Date':'Date',
                     'Send Time (PT)':'Time',
                     'Send Weekday':'Weekday',
                     'Times Liked on Facebook':'FB Likes'},
                     inplace=True)

#reorder the columns
email_data_df = email_data_df[['Date','Weekday','Time','Series','Type','Title','Subject',    'Total Recipients','Successful Deliveries','Total Bounces','Times Forwarded','Forwarded Opens',    'Unique Opens', 'Open Rate', 'Total Opens', 'Unique Clicks','Click Rate', 'Total Clicks', 'Unsubscribes',    'FB Likes','Visits','New Visits','Pages/Visit','Bounce Rate']]

#change the data types of inappropriate datatypes, if necessary
email_data_df['Date'] = pd.to_datetime(email_data_df['Date'], format='%m/%d/%Y')
email_data_df['Total Recipients'] = pd.to_numeric(email_data_df['Total Recipients'])
email_data_df['Successful Deliveries'] = pd.to_numeric(email_data_df['Successful Deliveries'])
email_data_df['Total Bounces'] = pd.to_numeric(email_data_df['Total Bounces'])
email_data_df['Times Forwarded'] = pd.to_numeric(email_data_df['Times Forwarded'])
email_data_df['Forwarded Opens'] = pd.to_numeric(email_data_df['Forwarded Opens'])
email_data_df['Open Rate'] = pd.to_numeric(email_data_df['Open Rate'])
email_data_df['Click Rate'] = pd.to_numeric(email_data_df['Click Rate'])
email_data_df['Visits'] = pd.to_numeric(email_data_df['Visits'])
email_data_df['New Visits'] = pd.to_numeric(email_data_df['New Visits'])
email_data_df['Pages/Visit'] = pd.to_numeric(email_data_df['Pages/Visit'])
email_data_df['Bounce Rate'] = pd.to_numeric(email_data_df['Bounce Rate'])

#create a new dataframe that uses the series as the index
series_totals_df = email_data_df.groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count = email_data_df.groupby(['Series'])['Title'].count()
series_totals_df.insert(0, 'Email Count', email_count)

#arrange the data in descending order
series_totals_df = series_totals_df.sort_values(by='Email Count', ascending=False)

series_names = list(series_totals_df.index.values)

#create lists of the email counts and series
email_count_list = series_totals_df['Email Count']
series_names = list(series_totals_df.index.values)

# reset the index for series_totals_df
series_totals_df.reset_index(inplace=True)

#prep 2018 email campaign data for graphing
series_totals_2018_df = email_data_df.loc[(email_data_df['Date'] < '1/1/2019')].groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count_2018_list = email_data_df.loc[(email_data_df['Date'] < '1/1/2019')].groupby(['Series'])['Title'].count()
series_totals_2018_df.insert(0, 'Email Count', email_count_2018_list)

#arrange the data in descending order
series_totals_2018_df = series_totals_2018_df.sort_values(by='Email Count', ascending=False)

#create lists for axes
email_count_list_2018 = series_totals_2018_df['Email Count']
series_totals_2018_list = list(series_totals_2018_df.index.values)
# reset the index for series_totals_2018
series_totals_2018_df.reset_index(inplace=True)

#prep 2019 email campaign data for graphing
series_totals_2019_df = email_data_df.loc[email_data_df['Date'].between('12/31/2018', '1/1/2020')].groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count_2019_list = email_data_df.loc[(email_data_df['Date'].between('12/31/2018', '1/1/2020'))].groupby(['Series'])['Title'].count()
series_totals_2019_df.insert(0, 'Email Count', email_count_2019_list)

#arrange the data in descending order
series_totals_2019_df = series_totals_2019_df.sort_values(by='Email Count', ascending=False)

#visualize the 2019 data
email_count_2019_list = series_totals_2019_df['Email Count']
series_totals_2019_list = list(series_totals_2019_df.index.values)

# reset the index for series_totals_2019
series_totals_2019_df.reset_index(inplace=True)

#prepare email campaign data for 2020
series_totals_2020_df = email_data_df.loc[email_data_df['Date'].between('12/31/2019', '1/1/2021')].groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count_2020_list = email_data_df.loc[(email_data_df['Date'].between('12/31/2019', '1/1/2021'))].groupby(['Series'])['Title'].count()
series_totals_2020_df.insert(0, 'Email Count', email_count_2020_list)

#arrange the data in descending order
series_totals_2020_df = series_totals_2020_df.sort_values(by='Email Count', ascending=False)

#visualize the 2020 data
email_count_2020_list = series_totals_2020_df['Email Count']
series_2020_list = list(series_totals_2020_df.index.values)

# reset the index for series_totals_2020
series_totals_2020_df.reset_index(inplace=True)

#prepare email campaign data for 2021
series_totals_2021_df = email_data_df.loc[email_data_df['Date'].between('12/31/2020', '1/1/2022')].groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count_2021_list = email_data_df.loc[(email_data_df['Date'].between('12/31/2020', '1/1/2022'))].groupby(['Series'])['Title'].count()
series_totals_2021_df.insert(0, 'Email Count', email_count_2021_list)

#arrange the data in descending order
series_totals_2021_df = series_totals_2021_df.sort_values(by='Email Count', ascending=False)

#visualize the 2021 data
email_count_2021_list = series_totals_2021_df['Email Count']
series_2021_list = list(series_totals_2021_df.index.values)

# reset the index for series_totals_2021
series_totals_2021_df.reset_index(inplace=True)

#TABLE 3: A table of the total types of emails sent
#create a new dataframe that uses the email type as the index
email_type_totals_df = email_data_df.groupby(email_data_df['Type']).sum()

# add an additional column that counts the number of emails for each email type
email_type_count_list = email_data_df.groupby(['Type'])['Title'].count()
email_type_totals_df.insert(0, 'Email Count', email_type_count_list)

# # arrange the data in descending order
email_type_totals_df = email_type_totals_df.sort_values(by='Email Count', ascending=False)

# # show the table
email_type_totals_df

# TABLE 5: A table illustrating the TOD as bins and open/click data for each series
#create a new row in the email_data_df called "Times" that converts the "Time" column to a datetime data type
email_data_df['Times'] = pd.to_datetime(email_data_df['Time'], format='%H:%M:%S').dt.time

#name the filepath to the data
# former_file_path = "C:\\Users\\ssteffen\\Desktop\\Sam\\Email_data\\email_data.csv"
#to get the current file path, enter 'pwd' in GitBash terminal:
# /c/Users/ssteffen/University of Idaho/Storage-Boise - ECHO/Staff/Sam/Data
root_file_path = 'C:\\Users\\ssteffen\\University of Idaho\\Storage-Boise - ECHO\\Staff\\Sam\\Data\\Spreadsheets\\iECHO data\\' 
data_path_2018 = f'{root_file_path}2018_iECHO_data.csv' 
data_path_2019 = f'{root_file_path}2019_iECHO_data.csv' 
data_path_2020 = f'{root_file_path}2020_iECHO_data.csv' 
data_path_2021 = f'{root_file_path}2021_iECHO_data.csv' 
data_path_cumulative = f'{root_file_path}2018-2021_iECHO_attendance_data.csv'
data_path_zips = f'C:\\Users\\ssteffen\\University of Idaho\\Storage-Boise - ECHO\\Staff\\Sam\\Data\\Spreadsheets\\US_zip_codes.csv'

# read the 2018-2021 data into separate dataframes
iecho_data_2018 = pd.read_csv(data_path_2018)
iecho_data_2019 = pd.read_csv(data_path_2019)
iecho_data_2020 = pd.read_csv(data_path_2020)
iecho_data_2021 = pd.read_csv(data_path_2021)
iecho_data_cumulative = pd.read_csv(data_path_cumulative)

#read the zipcode database into a df
US_zip_codes_df = pd.read_csv(data_path_zips) 

#eliminate unnecessary columns
iecho_data_2018_df = iecho_data_2018.drop(['Date.1',
                                        'First Name',
                                        'Last Name',
                                        'Unnamed: 24',
                                        'Unnamed: 25',
                                        'Unique Series (3)',
                                        '# of Sessions',
                                        'Unique Attendance by Series',
                                        '# of People who attended 2+ sessions in same series',
                                        'of 29 people who attended +1 ECHO series',
                                        'Unique Part by County',
                                        '2018 total',
                                        'Unnamed: 33',
                                        '232 Unique Participants',
                                        'COUNTY',
                                        'Unnamed: 36',
                                        'Sessions Attended',
                                        'OPSUD',
                                        'BHPC',
                                        'XWAIV'
                                       ], axis=1)

iecho_data_2019_df = iecho_data_2019.drop(['Date.1',
                                        'First Name',
                                        'Last Name',
                                       ], axis=1)

iecho_data_2020_df = iecho_data_2020.drop(['Date.1',
                                        'First Name',
                                        'Last Name',
                                        'COPY',
                                        'COPY.1',
                                       ], axis=1)

#eliminate unnecessary columns
iecho_data_2021_df = iecho_data_2021.drop(['First Name',
                                        'Last Name',
                                        'COPY',
                                        'Unnamed: 24', 
                                        'Unnamed: 25', 
                                        'Unnamed: 26'
                                       ], axis=1)

#add the list to the .apply method to fill in missing data with NaNs
iecho_data_2018_df = iecho_data_2018_df[['Date', 'Clinic Name', 'Session Topic', 'Full Name', 'Attendee Type',
       'Job Title', 'Credentials', 'Specialty', 'Attendee Street Address',
       'Attendee City', 'Attendee State', 'Attendee Zip Code',
       'Attendee County', 'Attendee Email 1', 'Attendee Email 2',
       'Health Center Name', 'Health Center Street Address',
       'Health Center City', 'Health Center State', 'Health Center Zip Code',
       'Health Center County']].apply(lambda x: x.str.strip()).replace('', np.nan)

#add the list to the .apply method to fill in missing data with NaNs
iecho_data_2019_df = iecho_data_2019_df[['Date', 'Clinic Name', 'Session Topic', 'Full Name',
       'Attendee Type', 'Job Title', 'Credentials',
       'Specialty', 'Attendee Street Address', 'Attendee City',
       'Attendee State', 'Attendee Zip Code', 'Attendee County',
       'Attendee Email 1', 'Attendee Email 2', 'Health Center Name',
       'Health Center Street Address', 'Health Center City',
       'Health Center State', 'Health Center Zip Code',
       'Health Center County']].apply(lambda x: x.str.strip()).replace('', np.nan)

#add the list to the .apply method to fill in missing data with NaNs
iecho_data_2020_df = iecho_data_2020_df[['Date', 'Clinic Name', 'Session Topic', 'Full Name', 'Attendee Type',
       'Job Title', 'Credentials', 'Specialty', 'Attendee Street Address',
       'Attendee City', 'Attendee State', 'Attendee Zip Code',
       'Attendee County', 'Attendee Email 1', 'Attendee Email 2',
       'Health Center Name', 'Health Center Street Address',
       'Health Center City', 'Health Center State', 'Health Center Zip Code']].apply(lambda x: x.str.strip()).replace('', np.nan)

#add the list to the .apply method to fill in missing data with NaNs
iecho_data_2021_df = iecho_data_2021_df[['Date', 'Clinic Name', 'Session Topic', 'Full Name', 'Attendee Type',
       'Job Title', 'Credentials', 'Specialty', 'Attendee Street Address',
       'Attendee City', 'Attendee State', 'Attendee Zip Code',
       'Attendee County', 'Attendee Email 1', 'Attendee Email 2',
       'Health Center Name', 'Health Center Street Address',
       'Health Center City', 'Health Center State', 'Health Center Zip Code']].apply(lambda x: x.str.strip()).replace('', np.nan)

#change 'Opioids, Pain, and Substance Use Disorders' to 'OPSUD'
iecho_data_2018_df['Clinic Name'] = iecho_data_2018_df['Clinic Name'].apply(lambda x: x.strip()).replace('Opioids, Pain, and Substance Use Disorders', 'OPSUD')
#change 'Behavioral Health in Primary Care' to 'BH in PC'
iecho_data_2018_df['Clinic Name'] = iecho_data_2018_df['Clinic Name'].apply(lambda x: x.strip()).replace('Behavioral Health in Primary Care', 'BH in PC')
#change 'X-Waiver Training' to 'XWT'
iecho_data_2018_df['Clinic Name'] = iecho_data_2018_df['Clinic Name'].apply(lambda x: x.strip()).replace('X-Waiver Training', 'XWT')

iecho_data_2019_df['Clinic Name'] = iecho_data_2019_df['Clinic Name'].apply(lambda x: x.strip()).replace('Opioids, Pain, and Substance Use Disorders', 'OPSUD')
iecho_data_2019_df['Clinic Name'] = iecho_data_2019_df['Clinic Name'].apply(lambda x: x.strip()).replace('Behavioral Health in Primary Care', 'BH in PC')
iecho_data_2019_df['Clinic Name'] = iecho_data_2019_df['Clinic Name'].apply(lambda x: x.strip()).replace('X-Waiver Training', 'XWT')

iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19', 'COVID')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('Opioids, Pain, and Substance Use Disorders', 'OPSUD')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('Behavioral Health in Primary Care', 'BH in PC')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Nursing Home Safety- Tuesday Cohort', 'PALTC')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('Perinatal SUD', 'PSUD')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Ambulatory / Acute Care', 'COVID')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Nursing Home Safety- Friday Cohort', 'PALTC')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('X-Waiver Training', 'XWT')
iecho_data_2020_df['Clinic Name'] = iecho_data_2020_df['Clinic Name'].apply(lambda x: x.strip()).replace('Syphilis in Pregnancy', 'Syphilis')

iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Behavioral Health in Primary Care', 'BH in PC')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Opioids, Pain, and Substance Use Disorders', 'OPSUD')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Counseling Techniques for Substance Use Disorders', 'CTSUDs')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19', 'COVID')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Ambulatory / Acute Care', 'COVID')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Safety for Post-Acute and Long-Term Care', 'PALTC')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('COVID-19 Nursing Home Safety- Friday Cohort', 'PALTC')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Hepatitis C', 'VHLC')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Perinatal SUD', 'PSUD')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Pediatric Behavioral Health', 'PBH')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('X-Waiver Training', 'XWT')
iecho_data_2021_df['Clinic Name'] = iecho_data_2021_df['Clinic Name'].apply(lambda x: x.strip()).replace('Nursing Home COVID-19 Safety', 'PALTC')

#create a new df that shows each session topic by series, date, and attendance per session
session_topics_2018_df = iecho_data_2018_df[['Clinic Name', 'Session Topic', 'Full Name','Date']]
session_attendance_raw_list = session_topics_2018_df.groupby(['Clinic Name', 'Session Topic', 'Date'])['Full Name'].count()
session_attendance_2018_df = pd.DataFrame(session_attendance_raw_list)
#change the name of the 'Full Name' count to 'Attendance'
session_attendance_2018_df.rename(columns = {'Full Name':'Attendance'}, inplace=True)
#reset the index
session_attendance_2018_df.reset_index(inplace=True)

session_topics_2019_df = iecho_data_2019_df[['Clinic Name', 'Session Topic', 'Full Name','Date']]
session_attendance_raw_list = session_topics_2019_df.groupby(['Clinic Name', 'Session Topic', 'Date'])['Full Name'].count()
session_attendance_2019_df = pd.DataFrame(session_attendance_raw_list)
session_attendance_2019_df.rename(columns = {'Full Name':'Attendance'}, inplace=True)
session_attendance_2019_df.reset_index(inplace=True)

session_topics_2020_df = iecho_data_2020_df[['Clinic Name', 'Session Topic', 'Full Name','Date']]
session_attendance_raw_list = session_topics_2020_df.groupby(['Clinic Name', 'Session Topic', 'Date'])['Full Name'].count()
session_attendance_2020_df = pd.DataFrame(session_attendance_raw_list)
session_attendance_2020_df.rename(columns = {'Full Name':'Attendance'}, inplace=True)
session_attendance_2020_df.reset_index(inplace=True)

session_topics_2021_df = iecho_data_2021_df[['Clinic Name', 'Session Topic', 'Full Name','Date']]
session_attendance_raw_list = session_topics_2021_df.groupby(['Clinic Name', 'Session Topic', 'Date'])['Full Name'].count()
session_attendance_2021_df = pd.DataFrame(session_attendance_raw_list)
session_attendance_2021_df.rename(columns = {'Full Name':'Attendance'}, inplace=True)
session_attendance_2021_df.reset_index(inplace=True)

#change the data types of inappropriate datatypes, if necessary
# session_attendance_2018_df.dtypes
session_attendance_2018_df['Date'] = pd.to_datetime(session_attendance_2018_df['Date'], format='%m/%d/%Y')
#reorder the df
session_attendance_2018_df = session_attendance_2018_df.sort_values(by='Date')

session_attendance_2019_df['Date'] = pd.to_datetime(session_attendance_2019_df['Date'], format='%m/%d/%Y')
session_attendance_2019_df = session_attendance_2019_df.sort_values(by='Date')

session_attendance_2020_df['Date'] = pd.to_datetime(session_attendance_2020_df['Date'], format='%m/%d/%Y')
session_attendance_2020_df = session_attendance_2020_df.sort_values(by='Date')

session_attendance_2021_df['Date'] = pd.to_datetime(session_attendance_2021_df['Date'], format='%m/%d/%Y')
session_attendance_2021_df = session_attendance_2021_df.sort_values(by='Date')

#clean the US_zip_code data for merging
US_zip_codes_df = US_zip_codes_df[['zip', 'primary_city', 'state', 'county', 'latitude','longitude']]
US_zip_codes_df['zip'] = US_zip_codes_df['zip'].astype(str)
US_zip_codes_df['zip'] = '00' + US_zip_codes_df.zip
US_zip_codes_df['zip'] = US_zip_codes_df['zip'].str[-5:]

# create a df with attendance and address data for mapping for 2018, 2019, 2020, 2021
locations_2018_df = iecho_data_2018_df[['Date',
                                        'Clinic Name',
                                        'Session Topic',
                                        'Full Name',
                                        'Attendee Street Address',
                                        'Attendee City',
                                        'Attendee Zip Code',
                                        'Attendee County',
                                        'Health Center Name',
                                        'Health Center Street Address',
                                        'Health Center City',
                                        'Health Center State',
                                        'Health Center Zip Code',
                                        'Health Center County']]
locations_2018_df['County'] = locations_2018_df['Attendee County'].str.split(" / ", expand=True)[0]
locations_2018_df['Health District'] = locations_2018_df['Attendee County'].str.split(" / ", expand=True)[1]
locations_2018_df['Full Address'] = locations_2018_df['Attendee Street Address'] + ' ' + locations_2018_df['Attendee City'] + ', ' + locations_2018_df['Health Center State'] + ' ' + locations_2018_df['Attendee Zip Code']
locations_2018_df['zip'] = locations_2018_df['Attendee Zip Code'].str[:5]
locations_2018_df['Health Center Zip Code'] = locations_2018_df['Health Center Zip Code'].str[:5]
locations_2018_df = locations_2018_df.drop(columns=['Attendee County', 'Health Center County', 'Attendee Zip Code'])

locations_2019_df = iecho_data_2019_df[['Date',
                                        'Clinic Name',
                                        'Session Topic',
                                        'Full Name',
                                        'Attendee Street Address',
                                        'Attendee City',
                                        'Attendee Zip Code',
                                        'Attendee County',
                                        'Health Center Name',
                                        'Health Center Street Address',
                                        'Health Center City',
                                        'Health Center State',
                                        'Health Center Zip Code',
                                        'Health Center County']]
locations_2019_df['County'] = locations_2019_df['Attendee County'].str.split(" / ", expand=True)[0]
locations_2019_df['Health District'] = locations_2019_df['Attendee County'].str.split(" / ", expand=True)[1]
locations_2019_df['Full Address'] = locations_2019_df['Attendee Street Address'] + ' ' + locations_2019_df['Attendee City'] + ', ' + locations_2019_df['Health Center State'] + ' ' + locations_2019_df['Attendee Zip Code']
locations_2019_df['zip'] = locations_2019_df['Attendee Zip Code'].str[:5]
locations_2019_df['Health Center Zip Code'] = locations_2019_df['Health Center Zip Code'].str[:5]
locations_2019_df = locations_2019_df.drop(columns=['Attendee County', 'Health Center County', 'Attendee Zip Code'])

locations_2020_df = iecho_data_2020_df[['Date',
                                        'Clinic Name',
                                        'Session Topic',
                                        'Full Name',
                                        'Attendee Street Address',
                                        'Attendee City',
                                        'Attendee Zip Code',
                                        'Attendee County',
                                        'Health Center Name',
                                        'Health Center Street Address',
                                        'Health Center City',
                                        'Health Center State',
                                        'Health Center Zip Code']]
locations_2020_df['County'] = locations_2020_df['Attendee County'].str.split(" / ", expand=True)[0]
locations_2020_df['Health District'] = locations_2020_df['Attendee County'].str.split(" / ", expand=True)[1]
locations_2020_df['Full Address'] = locations_2020_df['Attendee Street Address'] + ' ' + locations_2020_df['Attendee City'] + ', ' + locations_2020_df['Health Center State'] + ' ' + locations_2020_df['Attendee Zip Code']
locations_2020_df['zip'] = locations_2020_df['Attendee Zip Code'].str[:5]
locations_2020_df['Health Center Zip Code'] = locations_2020_df['Health Center Zip Code'].str[:5]
locations_2020_df = locations_2020_df.drop(columns=['Attendee County', 'Attendee Zip Code'])

locations_2021_df = iecho_data_2021_df[['Date',
                                        'Clinic Name',
                                        'Session Topic',
                                        'Full Name',
                                        'Attendee Street Address',
                                        'Attendee City',
                                        'Attendee Zip Code',
                                        'Attendee County',
                                        'Health Center Name',
                                        'Health Center Street Address',
                                        'Health Center City',
                                        'Health Center State',
                                        'Health Center Zip Code']]
locations_2021_df['County'] = locations_2021_df['Attendee County'].str.split(" / ", expand=True)[0]
locations_2021_df['Health District'] = locations_2021_df['Attendee County'].str.split(" / ", expand=True)[1]
locations_2021_df['Full Address'] = locations_2021_df['Attendee Street Address'] + ' ' + locations_2021_df['Attendee City'] + ', ' + locations_2021_df['Health Center State'] + ' ' + locations_2021_df['Attendee Zip Code']
locations_2021_df['zip'] = locations_2021_df['Attendee Zip Code'].str[:5]
locations_2021_df['Health Center Zip Code'] = locations_2021_df['Health Center Zip Code'].str[:5]
locations_2021_df = locations_2021_df.drop(columns=['Attendee County', 'Attendee Zip Code'])

mappable_locations_2018_df = pd.merge(locations_2018_df, US_zip_codes_df, on='zip', how='left')
mappable_locations_2019_df = pd.merge(locations_2019_df, US_zip_codes_df, on='zip', how='left')
mappable_locations_2020_df = pd.merge(locations_2020_df, US_zip_codes_df, on='zip', how='left')
mappable_locations_2021_df = pd.merge(locations_2021_df, US_zip_codes_df, on='zip', how='left')

# merge the mappable data with the session attendance data on 'Session Topic' column
map_2018_data_df = pd.merge(mappable_locations_2018_df, session_attendance_2018_df, on=['Session Topic'], how='left')
#retitle columns and drop duplicate columns
map_2018_data_df = map_2018_data_df.rename(columns={'Date_x':'Date', 'Clinic Name_x':'Clinic Name', 'Attendnace':'Session Attendance'})
map_2018_data_df = map_2018_data_df.drop(columns=['Clinic Name_y','Date_y'])

map_2019_data_df = pd.merge(mappable_locations_2019_df, session_attendance_2019_df, on=['Session Topic'], how='left')
map_2019_data_df = map_2019_data_df.rename(columns={'Date_x':'Date', 'Clinic Name_x':'Clinic Name', 'Attendnace':'Session Attendance'})
map_2019_data_df = map_2019_data_df.drop(columns=['Clinic Name_y','Date_y'])

map_2020_data_df = pd.merge(mappable_locations_2020_df, session_attendance_2020_df, on=['Session Topic'], how='left')
map_2020_data_df = map_2020_data_df.rename(columns={'Date_x':'Date', 'Clinic Name_x':'Clinic Name', 'Attendnace':'Session Attendance'})
map_2020_data_df = map_2020_data_df.drop(columns=['Clinic Name_y','Date_y'])

map_2021_data_df = pd.merge(mappable_locations_2021_df, session_attendance_2021_df, on=['Session Topic'], how='left')
map_2021_data_df = map_2021_data_df.rename(columns={'Date_x':'Date', 'Clinic Name_x':'Clinic Name', 'Attendnace':'Session Attendance'})
map_2021_data_df = map_2021_data_df.drop(columns=['Clinic Name_y','Date_y'])

# create a mappable df to show unique participation by location, 2018, 2019, 2020, 2021
unique_attendees_by_city_2018_list = map_2018_data_df.groupby(['Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
unique_attendees_by_city_2018_df = pd.DataFrame(unique_attendees_by_city_2018_list)
unique_attendees_by_city_2018_df.reset_index(inplace=True)
unique_attendees_by_city_2018_df = unique_attendees_by_city_2018_df.rename(columns={'Full Name':'Unique Attendees Count'})
unique_attendees_by_city_2018_df = unique_attendees_by_city_2018_df.sort_values(by='Unique Attendees Count', ascending=False)
unique_attendees_by_city_2018_df.reset_index(inplace=True, drop=True)

unique_attendees_by_city_2019_list = map_2019_data_df.groupby(['Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
unique_attendees_by_city_2019_df = pd.DataFrame(unique_attendees_by_city_2019_list)
unique_attendees_by_city_2019_df.reset_index(inplace=True)
unique_attendees_by_city_2019_df = unique_attendees_by_city_2019_df.rename(columns={'Full Name':'Unique Attendees Count'})
unique_attendees_by_city_2019_df = unique_attendees_by_city_2019_df.sort_values(by='Unique Attendees Count', ascending=False)
unique_attendees_by_city_2019_df.reset_index(inplace=True, drop=True)

unique_attendees_by_city_2020_list = map_2020_data_df.groupby(['Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
unique_attendees_by_city_2020_df = pd.DataFrame(unique_attendees_by_city_2020_list)
unique_attendees_by_city_2020_df.reset_index(inplace=True)
unique_attendees_by_city_2020_df = unique_attendees_by_city_2020_df.rename(columns={'Full Name':'Unique Attendees Count'})
unique_attendees_by_city_2020_df = unique_attendees_by_city_2020_df.sort_values(by='Unique Attendees Count', ascending=False)
unique_attendees_by_city_2020_df.reset_index(inplace=True, drop=True)

unique_attendees_by_city_2021_list = map_2021_data_df.groupby(['Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
unique_attendees_by_city_2021_df = pd.DataFrame(unique_attendees_by_city_2021_list)
unique_attendees_by_city_2021_df.reset_index(inplace=True)
unique_attendees_by_city_2021_df = unique_attendees_by_city_2021_df.rename(columns={'Full Name':'Unique Attendees Count'})
unique_attendees_by_city_2021_df = unique_attendees_by_city_2021_df.sort_values(by='Unique Attendees Count', ascending=False)
unique_attendees_by_city_2021_df.reset_index(inplace=True, drop=True)

# create a mappable df to show annual unique participation by series by city
# merge session attendance data and location data for 2018
series_by_locations_2018_df = pd.merge(session_attendance_2018_df, map_2018_data_df, on="Session Topic", how="left")
series_by_locations_2018_list = series_by_locations_2018_df.groupby(['Clinic Name_x', 'Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
series_by_location_2018_df = pd.DataFrame(series_by_locations_2018_list)
series_by_location_2018_df.reset_index(inplace=True)
series_by_location_2018_df = series_by_location_2018_df.rename(columns={'Clinic Name_x':'Series',
                                                                       'Health Center State':'State',
                                                                       'Health Center Zip Code':'Zip',
                                                                       'Full Name':'Attendees per Zip'})

series_by_locations_2019_df = pd.merge(session_attendance_2019_df, map_2019_data_df, on="Session Topic", how="left")
series_by_locations_2019_list = series_by_locations_2019_df.groupby(['Clinic Name_x', 'Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
series_by_location_2019_df = pd.DataFrame(series_by_locations_2019_list)
series_by_location_2019_df.reset_index(inplace=True)
series_by_location_2019_df = series_by_location_2019_df.rename(columns={'Clinic Name_x':'Series',
                                                                       'Health Center State':'State',
                                                                       'Health Center Zip Code':'Zip',
                                                                       'Full Name':'Attendees per Zip'})

series_by_locations_2020_df = pd.merge(session_attendance_2020_df, map_2020_data_df, on="Session Topic", how="left")
series_by_locations_2020_list = series_by_locations_2020_df.groupby(['Clinic Name_x', 'Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
series_by_location_2020_df = pd.DataFrame(series_by_locations_2020_list)
series_by_location_2020_df.reset_index(inplace=True)
series_by_location_2020_df = series_by_location_2020_df.rename(columns={'Clinic Name_x':'Series',
                                                                       'Health Center State':'State',
                                                                       'Health Center Zip Code':'Zip',
                                                                       'Full Name':'Attendees per Zip'})

series_by_locations_2021_df = pd.merge(session_attendance_2021_df, map_2021_data_df, on="Session Topic", how="left")
series_by_locations_2021_list = series_by_locations_2021_df.groupby(['Clinic Name_x', 'Health Center City', 'Health Center State', 'Health Center Zip Code', 'County', 'Health District', 'latitude', 'longitude'])['Full Name'].count()
series_by_location_2021_df = pd.DataFrame(series_by_locations_2021_list)
series_by_location_2021_df.reset_index(inplace=True)
series_by_location_2021_df = series_by_location_2021_df.rename(columns={'Clinic Name_x':'Series',
                                                                       'Health Center State':'State',
                                                                       'Health Center Zip Code':'Zip',
                                                                       'Full Name':'Attendees per Zip'})

# create separate dfs for each series in 2018, for mapping
mappable_2018_BHPC_df = series_by_location_2018_df.loc[(series_by_location_2018_df['Series'] == 'BH in PC')]
mappable_2018_OPSUD_df = series_by_location_2018_df.loc[(series_by_location_2018_df['Series'] == 'OPSUD')]
mappable_2018_XWT_df = series_by_location_2018_df.loc[(series_by_location_2018_df['Series'] == 'XWT')]

# 2019 series
mappable_2019_BHPC_df = series_by_location_2019_df.loc[(series_by_location_2019_df['Series'] == 'BH in PC')]
mappable_2019_OPSUD_df = series_by_location_2019_df.loc[(series_by_location_2019_df['Series'] == 'OPSUD')]
mappable_2019_XWT_df = series_by_location_2019_df.loc[(series_by_location_2019_df['Series'] == 'XWT')]

# 2020 series
mappable_2020_BHPC_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'BH in PC')]
mappable_2020_OPSUD_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'OPSUD')]
mappable_2020_XWT_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'XWT')]
mappable_2020_COVID_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'COVID')]
mappable_2020_PALTC_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'PALTC')]
mappable_2020_Syphilis_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'Syphilis')]
mappable_2020_PSUD_df = series_by_location_2020_df.loc[(series_by_location_2020_df['Series'] == 'PSUD')]

# 2021 series
mappable_2021_BHPC_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'BH in PC')]
mappable_2021_OPSUD_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'OPSUD')]
mappable_2021_XWT_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'XWT')]
mappable_2021_COVID_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'COVID')]
mappable_2021_PALTC_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'PALTC')]
mappable_2021_PBH_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'PBH')]
mappable_2021_PSUD_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'PSUD')]
mappable_2021_CTSUDs_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'CTSUDs')]
mappable_2021_VHLC_df = series_by_location_2021_df.loc[(series_by_location_2021_df['Series'] == 'VHLC')]

#slice the 2018 df by series
BH_PC_attendance_2018_df = session_attendance_2018_df.loc[(session_attendance_2018_df['Clinic Name'] == 'BH in PC')]
bhpc_date_2018_list = BH_PC_attendance_2018_df['Date'].to_list()
bhpc_attendance_2018_list = BH_PC_attendance_2018_df['Attendance'].to_list()

OPSUD_attendance_2018_df = session_attendance_2018_df.loc[(session_attendance_2018_df['Clinic Name'] == 'OPSUD')]
OPSUD_date_2018_list = OPSUD_attendance_2018_df['Date'].to_list()
OPSUD_attendance_2018_list = OPSUD_attendance_2018_df['Attendance'].to_list()

XWT_attendance_2018_df = session_attendance_2018_df.loc[(session_attendance_2018_df['Clinic Name'] == 'XWT')]
XWT_date_2018_list = XWT_attendance_2018_df['Date'].to_list()
XWT_attendance_2018_list = XWT_attendance_2018_df['Attendance'].to_list()

non_XWT_attendance_2018_df = session_attendance_2018_df.loc[(session_attendance_2018_df['Clinic Name'] != 'XWT')]

#prep the 2019 data for graphing
BH_PC_attendance_2019_df = session_attendance_2019_df.loc[(session_attendance_2019_df['Clinic Name'] == 'BH in PC')]
bhpc_date_2019_list = BH_PC_attendance_2019_df['Date'].to_list()
bhpc_attendance_2019_list = BH_PC_attendance_2019_df['Attendance'].to_list()

OPSUD_attendance_2019_df = session_attendance_2019_df.loc[(session_attendance_2019_df['Clinic Name'] == 'OPSUD')]
OPSUD_date_2019_list = OPSUD_attendance_2019_df['Date'].to_list()
OPSUD_attendance_2019_list = OPSUD_attendance_2019_df['Attendance'].to_list()

non_XWT_attendance_2019 = session_attendance_2019_df.loc[(session_attendance_2019_df['Clinic Name']) != 'XWT']

XWT_attendance_2019_df = session_attendance_2019_df.loc[(session_attendance_2019_df['Clinic Name'] == 'XWT')]
XWT_date_2019_list = XWT_attendance_2019_df['Date'].to_list()
XWT_attendance_2019_list = XWT_attendance_2019_df['Attendance'].to_list()

#slice the 2020 df by series
BH_PC_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'BH in PC')]
bhpc_date_2020_list = BH_PC_attendance_2020_df['Date'].to_list()
bhpc_attendance_2020_list = BH_PC_attendance_2020_df['Attendance'].to_list()

OPSUD_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'OPSUD')]
OPSUD_date_2020_list = OPSUD_attendance_2020_df['Date'].to_list()
OPSUD_attendance_2020_list = OPSUD_attendance_2020_df['Attendance'].to_list()

XWT_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'XWT')]
XWT_date_2020_list = XWT_attendance_2020_df['Date'].to_list()
XWT_attendance_2020_list = XWT_attendance_2020_df['Attendance'].to_list()

COVID_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'COVID')]
COVID_date_2020_list = COVID_attendance_2020_df['Date'].to_list()
COVID_attendance_2020_list = COVID_attendance_2020_df['Attendance'].to_list()

PALTC_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'PALTC')]
PALTC_date_2020_list = PALTC_attendance_2020_df['Date'].to_list()
PALTC_attendance_2020_list = PALTC_attendance_2020_df['Attendance'].to_list()

PSUD_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'PSUD')]
PSUD_date_2020_list = PSUD_attendance_2020_df['Date'].to_list()
PSUD_attendance_2020_list = PSUD_attendance_2020_df['Attendance'].to_list()

syphilis_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] == 'Syphilis')]
syphilis_date_2020_list = syphilis_attendance_2020_df['Date'].to_list()
syphilis_attendance_2020_list = syphilis_attendance_2020_df['Attendance'].to_list()

non_XWT_attendance_2020_df = session_attendance_2020_df.loc[(session_attendance_2020_df['Clinic Name'] != 'XWT')]

#Drop the duplicate X-Waiver sessions and the COVID-19 session kickoff (outliar) and redraw the chart
session_attendance_sans_outliars_df = session_attendance_2020_df[session_attendance_2020_df['Attendance'] > 1]
session_attendance_sans_outliars_df = session_attendance_sans_outliars_df[session_attendance_sans_outliars_df['Attendance'] < 599]
#session_attendance_sans_outliars_df

#slice the 2020 df by series, using outliar-excluded data
BH_PC_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'BH in PC')]
bhpc_date_2020_list_SOL = BH_PC_attendance_2020_df_SOL['Date'].to_list()
bhpc_attendance_2020_list_SOL = BH_PC_attendance_2020_df_SOL['Attendance'].to_list()

OPSUD_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'OPSUD')]
OPSUD_date_2020_list_SOL = OPSUD_attendance_2020_df_SOL['Date'].to_list()
OPSUD_attendance_2020_list_SOL = OPSUD_attendance_2020_df_SOL['Attendance'].to_list()

XWT_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'XWT')]
XWT_date_2020_list_SOL = XWT_attendance_2020_df_SOL['Date'].to_list()
XWT_attendance_2020_list_SOL = XWT_attendance_2020_df_SOL['Attendance'].to_list()

COVID_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'COVID')]
COVID_date_2020_list_SOL = COVID_attendance_2020_df_SOL['Date'].to_list()
COVID_attendance_2020_list_SOL = COVID_attendance_2020_df_SOL['Attendance'].to_list()

PALTC_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'PALTC')]
PALTC_date_2020_list_SOL = PALTC_attendance_2020_df_SOL['Date'].to_list()
PALTC_attendance_2020_list_SOL = PALTC_attendance_2020_df_SOL['Attendance'].to_list()

PSUD_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'PSUD')]
PSUD_date_2020_list_SOL = PSUD_attendance_2020_df_SOL['Date'].to_list()
PSUD_attendance_2020_list_SOL = PSUD_attendance_2020_df_SOL['Attendance'].to_list()

syphilis_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] == 'Syphilis')]
syphilis_date_2020_list_SOL = syphilis_attendance_2020_df_SOL['Date'].to_list()
syphilis_attendance_2020_list_SOL = syphilis_attendance_2020_df_SOL['Attendance'].to_list()

non_XWT_attendance_2020_df_SOL = session_attendance_sans_outliars_df.loc[(session_attendance_sans_outliars_df['Clinic Name'] != 'XWT')]

#slice the 2021 df by series
COVID_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'COVID')]
COVID_date_2021_list = COVID_attendance_2021_df['Date'].to_list()
COVID_attendance_2021_list = COVID_attendance_2021_df['Attendance'].to_list()

BH_PC_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'BH in PC')]
bhpc_date_2021_list = BH_PC_attendance_2021_df['Date'].to_list()
bhpc_attendance_2021_list = BH_PC_attendance_2021_df['Attendance'].to_list()

OPSUD_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'OPSUD')]
OPSUD_date_2021_list = OPSUD_attendance_2021_df['Date'].to_list()
OPSUD_attendance_2021_list = OPSUD_attendance_2021_df['Attendance'].to_list()

CTSUDs_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'CTSUDs')]
CTSUDs_date_2021_list = CTSUDs_attendance_2021_df['Date'].to_list()
CTSUDs_attendance_2021_list = CTSUDs_attendance_2021_df['Attendance'].to_list()

PALTC_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'PALTC')]
PALTC_date_2021_list = PALTC_attendance_2021_df['Date'].to_list()
PALTC_attendance_2021_list = PALTC_attendance_2021_df['Attendance'].to_list()

VHLC_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'VHLC')]
VHLC_date_2021_list = VHLC_attendance_2021_df['Date'].to_list()
VHLC_attendance_2021_list = VHLC_attendance_2021_df['Attendance'].to_list()

PSUD_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'PSUD')]
PSUD_date_2021_list = PSUD_attendance_2021_df['Date'].to_list()
PSUD_attendance_2021_list = PSUD_attendance_2021_df['Attendance'].to_list()

PBH_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'PBH')]
PBH_date_2021_list = PBH_attendance_2021_df['Date'].to_list()
PBH_attendance_2021_list = PBH_attendance_2021_df['Attendance'].to_list()

XWT_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] == 'XWT')]
XWT_date_2021_list = XWT_attendance_2021_df['Date'].to_list()
XWT_attendance_2021_list = XWT_attendance_2021_df['Attendance'].to_list()

non_XWT_attendance_2021_df = session_attendance_2021_df.loc[(session_attendance_2021_df['Clinic Name'] != 'XWT')]

#change the data types of inappropriate datatypes, if necessary
# iecho_data_cumulative.dtypes
iecho_data_cumulative['Date'] = pd.to_datetime(iecho_data_cumulative['Date'], format='%m/%d/%Y')
# iecho_data_cumulative.dtypes

#reorder the df
iecho_data_cumulative_df = iecho_data_cumulative.sort_values(by='Date')

# get variables to plot cumulative attendance data, by series
cum_bh_pc_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'BH in PC')]
cum_bh_pc_dates_list = cum_bh_pc_attendance_df['Date'].to_list()
cum_bh_pc_attendees_list = cum_bh_pc_attendance_df['Attendance'].to_list()

cum_opsud_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'OPSUD')]
cum_opsud_dates_list = cum_opsud_attendance_df['Date'].to_list()
cum_opsud_attendees_list = cum_opsud_attendance_df['Attendance'].to_list()

cum_XWT_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'XWT')]
cum_XWT_dates_list = cum_XWT_attendance_df['Date'].to_list()
cum_XWT_attendees_list = cum_XWT_attendance_df['Attendance'].to_list()

cum_COVID_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'COVID')]
cum_COVID_dates_list = cum_COVID_attendance_df['Date'].to_list()
cum_COVID_attendees_list = cum_COVID_attendance_df['Attendance'].to_list()

cum_PALTC_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'PALTC')]
cum_PALTC_dates_list = cum_PALTC_attendance_df['Date'].to_list()
cum_PALTC_attendees_list = cum_PALTC_attendance_df['Attendance'].to_list()

cum_syphilis_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'Syphilis')]
cum_syphilis_dates_list = cum_syphilis_attendance_df['Date'].to_list()
cum_syphilis_attendees_list = cum_syphilis_attendance_df['Attendance'].to_list()

cum_PSUD_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'PSUD')]
cum_PSUD_dates_list = cum_PSUD_attendance_df['Date'].to_list()
cum_PSUD_attendees_list = cum_PSUD_attendance_df['Attendance'].to_list()

cum_PBH_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'PBH')]
cum_PBH_dates_list = cum_PBH_attendance_df['Date'].to_list()
cum_PBH_attendees_list = cum_PBH_attendance_df['Attendance'].to_list()

cum_VHLC_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'VHLC')]
cum_VHLC_dates_list = cum_VHLC_attendance_df['Date'].to_list()
cum_VHLC_attendees_list = cum_VHLC_attendance_df['Attendance'].to_list()

cum_CTSUDs_attendance_df = iecho_data_cumulative_df.loc[(iecho_data_cumulative_df['Clinic Name'] == 'CTSUDs')]
cum_CTSUDs_dates_list = cum_CTSUDs_attendance_df['Date'].to_list()
cum_CTSUDs_attendees_list = cum_CTSUDs_attendance_df['Attendance'].to_list()

#create a new df with only relevant info
cum_emails_df = email_data_df[['Date', 'Series', 'Type', 'Successful Deliveries', 'Times Forwarded', 'Unique Opens', 'Open Rate', 'Total Opens']]
cum_daily_emails_df = cum_emails_df[cum_emails_df['Type'] == 'Daily']

# get variables to plot cumulative email data, by year
daily_emails_2018_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Date'] < '2019-01-01')]
daily_emails_2019_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Date'] > '2019-01-01') & (cum_daily_emails_df['Date'] < '2019-12-31')]
daily_emails_2020_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Date'] > '2020-01-01') & (cum_daily_emails_df['Date'] < '2020-12-31')]
daily_emails_2021_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Date'] > '2021-01-01') & (cum_daily_emails_df['Date'] < '2021-12-31')]

# get variables to plot cumulative email data, by series
cum_bh_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'BH in PC')]
cum_bh_dailys_df = cum_bh_dailys_df.sort_values(by='Date')
cum_bh_email_date_list = cum_bh_dailys_df['Date'].to_list()
cum_bh_email_recips_list = cum_bh_dailys_df['Successful Deliveries'].to_list()

cum_opsud_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'OPSUD')]
cum_opsud_dailys_df = cum_opsud_dailys_df.sort_values(by='Date')
cum_opsud_email_date_list = cum_opsud_dailys_df['Date'].to_list()
cum_opsud_email_recips_list = cum_opsud_dailys_df['Successful Deliveries'].to_list()

#omit XWT from the list

cum_COVID_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'COVID')]
cum_COVID_dailys_df = cum_COVID_dailys_df.sort_values(by='Date')
cum_COVID_email_date_list = cum_COVID_dailys_df['Date'].to_list()
cum_COVID_email_recips_list = cum_COVID_dailys_df['Successful Deliveries'].to_list()

cum_PALTC_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'PALTC')]
cum_PALTC_dailys_df = cum_PALTC_dailys_df.sort_values(by='Date')
cum_PALTC_email_date_list = cum_PALTC_dailys_df['Date'].to_list()
cum_PALTC_email_recips_list = cum_PALTC_dailys_df['Successful Deliveries'].to_list()

cum_syphilis_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'Syphilis')]
cum_syphilis_dailys_df = cum_syphilis_dailys_df.sort_values(by='Date')
cum_syphilis_email_date_list = cum_syphilis_dailys_df['Date'].to_list()
cum_syphilis_email_recips_list = cum_syphilis_dailys_df['Successful Deliveries'].to_list()

cum_PSUD_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'PSUD')]
cum_PSUD_dailys_df = cum_PSUD_dailys_df.sort_values(by='Date')
cum_PSUD_email_date_list = cum_PSUD_dailys_df['Date'].to_list()
cum_PSUD_email_recips_list = cum_PSUD_dailys_df['Successful Deliveries'].to_list()

cum_PBH_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'PBH')]
cum_PBH_dailys_df = cum_PBH_dailys_df.sort_values(by='Date')
cum_PBH_email_date_list = cum_PBH_dailys_df['Date'].to_list()
cum_PBH_email_recips_list = cum_PBH_dailys_df['Successful Deliveries'].to_list()

cum_VHLC_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'VHLC')]
cum_VHLC_dailys_df = cum_VHLC_dailys_df.sort_values(by='Date')
cum_VHLC_email_date_list = cum_VHLC_dailys_df['Date'].to_list()
cum_VHLC_email_recips_list = cum_VHLC_dailys_df['Successful Deliveries'].to_list()

cum_CTSUDs_dailys_df = cum_daily_emails_df.loc[(cum_daily_emails_df['Series'] == 'CTSUDs')]
cum_CTSUDs_dailys_df = cum_CTSUDs_dailys_df.sort_values(by='Date')
cum_CTSUDs_email_date_list = cum_CTSUDs_dailys_df['Date'].to_list()
cum_CTSUDs_email_recips_list = cum_CTSUDs_dailys_df['Successful Deliveries'].to_list()

# get variables to plot cumulative email data, by series, per year
# prep 2018 EMAIL variables for plotting
bhpc_daily_2018_df = daily_emails_2018_df.loc[(daily_emails_2018_df['Series'] == 'BH in PC')]
bhpc_daily_2018_date_list = bhpc_daily_2018_df['Date'].to_list()
bhpc_daily_2018_recips_list = bhpc_daily_2018_df['Successful Deliveries'].to_list()
opsud_daily_2018_df = daily_emails_2018_df.loc[(daily_emails_2018_df['Series'] == 'OPSUD')]
opsud_daily_2018_date_list = opsud_daily_2018_df['Date'].to_list()
opsud_daily_2018_recips_list = opsud_daily_2018_df['Successful Deliveries'].to_list()
#omit XWT from email data

# prep 2019 EMAIL variables for plotting
bhpc_daily_2019_df = daily_emails_2019_df.loc[(daily_emails_2019_df['Series'] == 'BH in PC')]
bhpc_daily_2019_date_list = bhpc_daily_2019_df['Date'].to_list()
bhpc_daily_2019_recips_list = bhpc_daily_2019_df['Successful Deliveries'].to_list()
opsud_daily_2019_df = daily_emails_2019_df.loc[(daily_emails_2019_df['Series'] == 'OPSUD')]
opsud_daily_2019_date_list = opsud_daily_2019_df['Date'].to_list()
opsud_daily_2019_recips_list = opsud_daily_2019_df['Successful Deliveries'].to_list()
#omit XWT from email data

# prep 2020 EMAIL variables for plotting
bhpc_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'BH in PC')]
bhpc_daily_2020_date_list = bhpc_daily_2020_df['Date'].to_list()
bhpc_daily_2020_recips_list = bhpc_daily_2020_df['Successful Deliveries'].to_list()
opsud_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'OPSUD')]
opsud_daily_2020_date_list = opsud_daily_2020_df['Date'].to_list()
opsud_daily_2020_recips_list = opsud_daily_2020_df['Successful Deliveries'].to_list()
#omit XWT from email data
COVID_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'COVID')]
COVID_daily_2020_date_list = COVID_daily_2020_df['Date'].to_list()
COVID_daily_2020_recips_list = COVID_daily_2020_df['Successful Deliveries'].to_list()
PALTC_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'PALTC')]
PALTC_daily_2020_date_list = PALTC_daily_2020_df['Date'].to_list()
PALTC_daily_2020_recips_list = PALTC_daily_2020_df['Successful Deliveries'].to_list()
syphilis_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'Syphilis')]
syphilis_daily_2020_date_list = syphilis_daily_2020_df['Date'].to_list()
syphilis_daily_2020_recips_list = syphilis_daily_2020_df['Successful Deliveries'].to_list()
PSUD_daily_2020_df = daily_emails_2020_df.loc[(daily_emails_2020_df['Series'] == 'PSUD')]
PSUD_daily_2020_date_list = PSUD_daily_2020_df['Date'].to_list()
PSUD_daily_2020_recips_list = PSUD_daily_2020_df['Successful Deliveries'].to_list()

# prep 2021 EMAIL variables for plotting
bhpc_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'BH in PC')]
bhpc_daily_2021_date_list = bhpc_daily_2021_df['Date'].to_list()
bhpc_daily_2021_recips_list = bhpc_daily_2021_df['Successful Deliveries'].to_list()
opsud_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'OPSUD')]
opsud_daily_2021_date_list = opsud_daily_2021_df['Date'].to_list()
opsud_daily_2021_recips_list = opsud_daily_2021_df['Successful Deliveries'].to_list()
#omit XWT from email data
COVID_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'COVID')]
COVID_daily_2021_date_list = COVID_daily_2021_df['Date'].to_list()
COVID_daily_2021_recips_list = COVID_daily_2021_df['Successful Deliveries'].to_list()
PALTC_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'PALTC')]
PALTC_daily_2021_date_list = PALTC_daily_2021_df['Date'].to_list()
PALTC_daily_2021_recips_list = PALTC_daily_2021_df['Successful Deliveries'].to_list()
PBH_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'PBH')]
PBH_daily_2021_date_list = PBH_daily_2021_df['Date'].to_list()
PBH_daily_2021_recips_list = PBH_daily_2021_df['Successful Deliveries'].to_list()
PSUD_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'PSUD')]
PSUD_daily_2021_date_list = PSUD_daily_2021_df['Date'].to_list()
PSUD_daily_2021_recips_list = PSUD_daily_2021_df['Successful Deliveries'].to_list()
VHLC_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'VHLC')]
VHLC_daily_2021_date_list = VHLC_daily_2021_df['Date'].to_list()
VHLC_daily_2021_recips_list = VHLC_daily_2021_df['Successful Deliveries'].to_list()
CTSUDs_daily_2021_df = daily_emails_2021_df.loc[(daily_emails_2021_df['Series'] == 'CTSUDs')]
CTSUDs_daily_2021_date_list = CTSUDs_daily_2021_df['Date'].to_list()
CTSUDs_daily_2021_recips_list = CTSUDs_daily_2021_df['Successful Deliveries'].to_list()

#########################################################STEP 2
# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytitle = dcc.Markdown(children='# ECHO Idaho Email Attendance Data by Series')
# mytitle2 = dcc.Markdown(children='# ECHO Idaho Participation Data by Region')
mygraph = dcc.Graph(figure={})
# mygraph2 = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['All (2018-2021)','2018', '2019', '2020', '2021'],
                        value='All (2018-2021)',  # initial value displayed when page first loads
                        clearable=False)
# dropdown2 = dcc.Dropdown(options=['2018','2019'],
#                         value='2018',
#                         clearable=False)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=12)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=12)
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),
    # dbc.Row([
    #     dbc.Col([mytitle2], width=12)
    # ], justify='center'),
    # dbc.Row([
    #     dbc.Col([mygraph2], width=12)
    # ], justify='center'),
    # dbc.Row([
    #     dbc.Col([dropdown2], width=6)
    # ], justify='center'),
], fluid=True)

# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    # Output(mygraph2, component_property='figure'),
    Input(dropdown, component_property='value')
    # Input(dropdown2, component_property='value')
)

def update_graph(user_input):  # function arguments come from the component property of the Input
    if user_input == '2018':
        fig = px.scatter_geo(series_by_location_2018_df,
                    lat="latitude",
                    lon="longitude",
                    color="Series",
                    color_discrete_map={
                        "BH in PC":"blue",
                        "OPSUD":"gold",
                        "XWT":"orange"
                    },
                    hover_name="Health Center City", 
                    size="Attendees per Zip",
                    center=dict(lon=-114.15, lat=44.65)
                    )
        fig.update_layout(
            title = 'ECHO Idaho Cumulative Attendance Data (2018)',
            geo_scope='usa')

    elif user_input == '2019':
        fig = px.scatter_geo(series_by_location_2019_df,
                    lat="latitude",
                    lon="longitude",
                    color="Series",
                    color_discrete_map={
                        "BH in PC":"blue",
                        "OPSUD":"gold",
                        "XWT":"orange"
                    },
                    hover_name="Health Center City", 
                    size="Attendees per Zip",
                    center=dict(lon=-114.15, lat=44.65)
                    )
        fig.update_layout(
            title = 'ECHO Idaho Cumulative Attendance Data (2019)',
            geo_scope='usa')

    elif user_input == '2020':
        fig = px.scatter_geo(series_by_location_2020_df,
                    lat="latitude",
                    lon="longitude",
                    color="Series",
                    color_discrete_map={
                        "BH in PC":"blue",
                        "OPSUD":"gold",
                        "XWT":"orange",
                        "COVID":"gray",
                        "PALTC":"gainsboro",
                        "Syphilis":"silver",
                        "PSUD":"yellow"
                    },
                    hover_name="Health Center City", 
                    size="Attendees per Zip",
                    center=dict(lon=-114.15, lat=44.65)
                    )

        fig.update_layout(
                title = 'ECHO Idaho Cumulative Attendance Data (2020)',
                geo_scope='usa')

    elif user_input == '2021':
        fig = px.scatter_geo(series_by_location_2021_df,
                    lat="latitude",
                    lon="longitude",
                    color="Series",
                    color_discrete_map={
                        "BH in PC":"blue",
                        "OPSUD":"gold",
                        "XWT":"orange",
                        "COVID":"gray",
                        "PALTC":"gainsboro",
                        "PSUD":"yellow",
                        "PBH":"dodgerblue",
                        "VHLC":"mediumslateblue",
                        "CTSUDs":"olive"
                    },
                    hover_name="Health Center City", 
                    size="Attendees per Zip",
                    center=dict(lon=-114.15, lat=44.65)
                    )

        fig.update_layout(
                title = 'ECHO Idaho Cumulative Attendance Data (2021)',
                geo_scope='usa')

    return fig

# Run app
if __name__=='__main__':
    app.run_server(port=8053)
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

#show TABLE 1: Cleaned Data
# email_data_df

# TABLE 2: A table of the total emails sent for each series
#create a new dataframe that uses the series as the index
series_totals_df = email_data_df.groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count = email_data_df.groupby(['Series'])['Title'].count()
series_totals_df.insert(0, 'Email Count', email_count)

#arrange the data in descending order
series_totals_df = series_totals_df.sort_values(by='Email Count', ascending=False)

series = list(series_totals_df.index.values)

#Visualize Table #2 w/matplotlib for 2018-2022
email_count = series_totals_df['Email Count']
series = list(series_totals_df.index.values)

plt.barh(series, email_count, color=['indigo','gold','blue','grey','grey','grey','gold','gold','blue','gold','crimson','blue','crimson','gold','grey','black'])
plt.title("Email Campaigns by ECHO Series (2018-2022)")
plt.xlabel("Email Quantity")
plt.ylabel("ECHO Email Campaign")

#create a legend
indigo_patch = mpatches.Patch(color='indigo', label='Weekly')
gold_patch = mpatches.Patch(color='gold', label='Opioid-focused')
blue_patch = mpatches.Patch(color='blue', label='BH-focused')
gray_patch = mpatches.Patch(color='gray', label='Virus-focused')
crimson_patch = mpatches.Patch(color='crimson', label='Newsletter/Special')
black_patch = mpatches.Patch(color='black', label='Podcast')
plt.legend(handles=[indigo_patch, gold_patch, blue_patch, gray_patch, crimson_patch, black_patch])

# reset the index for series_totals_df
series_totals_df.reset_index(inplace=True)

#Visualize Table #2 w/ Plotly for 2018-2022
df = series_totals_df
# fig = px.bar(df, x='Email Count', y='Series',
#              hover_data=['Email Count', 'Series'], 
#              color='Series',
#              labels={'Series':'ECHO Email Campaign', 'Email Count':'Email Quantity'},
#              title='Email Campaigns by ECHO Series (2018-2022)',
#              category_orders={'Series': ['Podcast','Syphilis','MOUD','Special','PBH','Newsletter','XWT','PedsASD','PSUD','CTSUDs','PALTC','VHLC','COVID','BH in PC','OPSUD','Weekly']},
#              color_discrete_map={'Weekly':'indigo', 'OPSUD':'gold', 'BH in PC':'blue', 'COVID':'gray', 'VHLC':'gray', 'PALTC':'gray', 'CTSUDs':'gold', 'PSUD':'gold', 'PedsASD':'blue', 'XWT':'gold', 'Newsletter':'crimson', 'PBH':'blue', 'Special':'crimson', 'MOUD':'gold', 'Syphilis':'gray', 'Podcast':'black'},
#              height=600)
# fig.show()

series_totals_2018 = email_data_df.loc[(email_data_df['Date'] < '1/1/2019')].groupby(email_data_df['Series']).sum()

#add an additional column that counts the number of emails for each series
email_count_2018 = email_data_df.loc[(email_data_df['Date'] < '1/1/2019')].groupby(['Series'])['Title'].count()
series_totals_2018.insert(0, 'Email Count', email_count_2018)

#arrange the data in descending order
series_totals_2018 = series_totals_2018.sort_values(by='Email Count', ascending=False)

#visualize the 2018 data
email_count = series_totals_2018['Email Count']
series = list(series_totals_2018.index.values)

plt.barh(series, email_count, color=['indigo','gold','blue','gold'])
plt.title("Email Campaigns by ECHO Series (2018)")
plt.xlabel("Email Quantity")
plt.ylabel("ECHO Email Campaign")

#create a legend
indigo_patch = mpatches.Patch(color='indigo', label='Weekly')
gold_patch = mpatches.Patch(color='gold', label='Opioid-focused')
blue_patch = mpatches.Patch(color='blue', label='BH-focused')
plt.legend(handles=[indigo_patch, gold_patch, blue_patch])

# plt.show()

# reset the index for series_totals_2018
series_totals_2018.reset_index(inplace=True)

#Visualize Table #2 w/ Plotly for 2018 only
df = series_totals_2018
# fig = px.bar(df, x='Email Count', y='Series',
#              hover_data=['Email Count', 'Series'], 
#              color='Series',
#              labels={'Series':'ECHO Email Campaign', 'Email Count':'Email Quantity'},
#              title='Email Campaigns by ECHO Series (2018)',
#              category_orders={'Series': ['XWT','BH in PC','OPSUD','Weekly']},
#              color_discrete_map={'Weekly':'indigo', 'OPSUD':'gold', 'BH in PC':'blue', 'XWT':'gold'},
#              height=400)
# fig.show()

#########################################################STEP 2
# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytitle = dcc.Markdown(children='ECHO Idaho Participation Data')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Email Campaigns by ECHO Series (2018-2022)', 'Email Campaigns by ECHO Series (2018)'],
                        value='Email Campaigns by ECHO Series (2018-2022)',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([mytitle, mygraph, dropdown])

# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):  # function arguments come from the component property of the Input
    if user_input == 'Email Campaigns by ECHO Series (2018-2022)':
        fig = px.bar(df, x='Email Count', y='Series',
             hover_data=['Email Count', 'Series'], 
             color='Series',
             labels={'Series':'ECHO Email Campaign', 'Email Count':'Email Quantity'},
             title='Email Campaigns by ECHO Series (2018-2022)',
             category_orders={'Series': ['Podcast','Syphilis','MOUD','Special','PBH','Newsletter','XWT','PedsASD','PSUD','CTSUDs','PALTC','VHLC','COVID','BH in PC','OPSUD','Weekly']},
             color_discrete_map={'Weekly':'indigo', 'OPSUD':'gold', 'BH in PC':'blue', 'COVID':'gray', 'VHLC':'gray', 'PALTC':'gray', 'CTSUDs':'gold', 'PSUD':'gold', 'PedsASD':'blue', 'XWT':'gold', 'Newsletter':'crimson', 'PBH':'blue', 'Special':'crimson', 'MOUD':'gold', 'Syphilis':'gray', 'Podcast':'black'},
             height=600)

    elif user_input == 'Email Campaigns by ECHO Series (2018)':
        fig = px.bar(df, x='Email Count', y='Series',
             hover_data=['Email Count', 'Series'], 
             color='Series',
             labels={'Series':'ECHO Email Campaign', 'Email Count':'Email Quantity'},
             title='Email Campaigns by ECHO Series (2018)',
             category_orders={'Series': ['XWT','BH in PC','OPSUD','Weekly']},
             color_discrete_map={'Weekly':'indigo', 'OPSUD':'gold', 'BH in PC':'blue', 'XWT':'gold'},
             height=600)

    return fig  # returned objects are assigned to the component property of the Output

# Run app
if __name__=='__main__':
    app.run_server(port=8053)
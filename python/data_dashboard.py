#import dependencies
import pandas as pd
from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px

# incorporate data into app
# df = px.data.medals_long()
file_path = 'C:/Users/ssteffen/University of Idaho/Storage-Boise - ECHO/Staff/Sam/Data/Spreadsheets/iECHO data/2018-2021_iECHO_attendance_data.csv'
df = pd.read_csv(file_path)

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytitle = dcc.Markdown(children='ECHO Idaho Participation Data')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([mytitle, mygraph, dropdown])

# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):  # function arguments come from the component property of the Input
    if user_input == 'Bar Plot':
        fig = px.bar(data_frame=df, x="date", y="attendance", color="Clinic Name")

    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="date", y="attendance", color="Clinic Name",
                         symbol="Clinic Name")

    return fig  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8053)
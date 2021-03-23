import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import plotly.express as px

df = pd.read_csv("injuryByAgeGroup.csv")

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

###STYLESHEET

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server

test = df['Town'].unique()
options = [{'label': t, 'value': t} for t in test]
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Injuries by Age Group']),
        dcc.Dropdown(
            options=options,
            searchable=False,
            multi=False,
            clearable=False,
            style={"width": "40%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])


#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.bar(
            data_frame=dff,
            values= my_dropdown,
            names='Injury',
            x='Crashes',
            y='Injury Type'
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)
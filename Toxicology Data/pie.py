import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc 

df = pd.read_csv("DrugFatalTwoCollim30-4.csv")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.Div([
        html.Label(['NYC Calls for Animal Rescue']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[{'label':x, 'value':x}
                                  for x in df['Drug'].unique()
            ],
            #value='Ethanol',
            multi=False,
            clearable=False,
            style={"width": "50%"}
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

def update_graph(drug):
    dff = df
    mask = df["Drug"] == drug

    piechart=px.pie(
            data_frame=dff,
            names=['Fatal', 'Non-Fatal'],
            values = ['Fatal', 'Non-Fatal'],
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)




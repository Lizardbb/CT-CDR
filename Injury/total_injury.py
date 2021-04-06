import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import plotly.express as px

df = pd.read_csv("TransposedTownTotalcrashesFatalsInjuryNoinjury.csv")

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

###STYLESHEET

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server


options = [{'label': t, 'value': t} for t in df]
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Injuries by Town']),
        dcc.Dropdown(
            id='my_dropdown',
            options=options,
            value='Andover',
            searchable=False,
            multi=False,
            clearable=False,
            style={"width": "40%", 'color': colors['background']}
        )
        ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ])
])


#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.pie(
            data_frame=dff,
            labels=['Total','Fatal','Injury', 'No_Injury'],
            values=my_dropdown,
            names=['Total','Fatal','Injury', 'No_Injury'],
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True, port=5500)
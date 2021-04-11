import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go

#STORING DATA

covid_df = pd.read_csv("c19total.csv")


colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

#STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server

#options = [{'label': t, 'value': t} for t in town_df]


#COMPONENTS 

#Navbar 


#graph

fig = px.bar(covid_df, x="Stage", y="Total",
             color='Type', title = 'Covid Analytics',barmode='group',
             height=800)


fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})

app.layout = dbc.Container([
    ###hollistic bar graph and table 
    dbc.Row([
        dbc.Col(dcc.Graph(figure = fig), width = 12
        ),  
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8800)

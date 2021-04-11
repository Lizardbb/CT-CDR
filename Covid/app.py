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


#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

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

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=UCONN_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Connecticut Crash Data Repository ", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="darkblue",
    dark=True,
)


#graph

fig = px.bar(covid_df, x="Work_Zone_Relation", y="Total",
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
        dbc.Col(navbar,width = 12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure = fig), width = 12
        ),  
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8800)

import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go

#DATA
df = pd.read_csv("vehiclesPerMake.csv")

#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
###STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


#navbar 
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


app.layout=dbc.Container(
    [
    dbc.Row([
        dbc.Col(navbar,width = 12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='my_bar', figure={
             'data': [
                     {
                         "x": df["Vehicle Make"],
                         "y": df["Count"],
                         "type": "bar",
                         "height":00,
                     },
                 ],
                 "layout": {
                     "title":{
                         "text": "Cases Per Make",
                         "x": 0.05,
                         "xanchor": "left",
                     },
                     'paper_bgcolor':'rgba(0,0,0,0)',
                     'plot_bgcolor':'rgba(0,0,0,0)',
                     "colorway":["#7DF9FF"],
                     'font': {
                     'color': colors['text'],
                     'size': 12,
                 }
                 },
        }
        ),
        #style=CONTENT_STYLE,
        width =12,
        )
    ]),
    ])



if __name__ == '__main__':
    app.run_server(debug=True)
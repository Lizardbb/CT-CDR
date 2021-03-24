import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go


###STORING DATA
hollistic_df = pd.read_csv("drugcount-2.csv") #overview 
table_df = pd.DataFrame(
    {
        "Top 5 Drugs": ["Ethanol", "Cannabinoids","Cocaine","THC","Methadone"],
        "Number of Cases": ["774","354","179","176","137"],
    }
)
severity_df = pd.read_csv("drugbyFatalitysplitAll.csv")
severity2_df = pd.read_csv("DrugFatalTwoCollim30-4.csv")
age_df = pd.read_csv("drugByAgeGroupLinear.csv")
gender_df = pd.read_csv("drugBySex.csv")
#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
###STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#2B2D2F",

}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "9.5rem",
    "margin-right": "2rem",
    "padding": "0rem 1rem",
}
#SIDEBAR 
sidebar = html.Div(
    [
        html.H4("Toxicology Analytics", className="display-4"),
        html.Hr(),
        html.P(
            "Select a Drug Below to Learn More", className="lead"
        ),
        dbc.Nav(
            [
                dbc.RadioItems(
                    options=[{'label':x, 'value':x}
                                  for x in hollistic_df['Drug'].unique()
            ],
                    style={ "overflow-y":"scroll", "height": "400px",'display': 'inline-block'},
                    #labelStyle={'display': 'inline-block'},
                    value=1,
                    id="radioitems-input",
        ),
            ],
            vertical=True,
            pills=True,
            
        ),
    ],
    style=SIDEBAR_STYLE,
)
        

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

#content = html.Div(id="page-content", style=CONTENT_STYLE)
content = dbc.Container(
    [
    dbc.Row([
        dbc.Col(navbar,width = 12, style=CONTENT_STYLE)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='my_bar', figure={
             'data': [
                     {
                         "x": hollistic_df["Drug"],
                         "y": hollistic_df["Count"],
                         "type": "bar",
                         "height":00,
                     },
                 ],
                 "layout": {
                     "title":{
                         "text": "Cases Per Drug",
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
        style=CONTENT_STYLE,
        width =12,
        )
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='severity-fig', figure={}), style=CONTENT_STYLE, width=4
        ),
        #adding pie
        dbc.Col(
            dcc.Graph(id = "age-fig", figure ={}), width=6
        ),
        dbc.Col(
            dcc.Graph(id = "gender-fig", figure ={}), style = CONTENT_STYLE,width=4
        )
        
    ])
    ],
)


app.layout = html.Div([sidebar, content])


@app.callback(
    Output('severity-fig','figure'),
    [Input('radioitems-input','value')])

def update_bar_chart(drug):
    mask = severity_df["Drug"] == drug
    fig = px.bar(severity_df[mask], x="Severity", y="Count", #color = "Severity",
                 barmode="group")
    fig.update_layout({
        "title":{
                        "text": "Severity of Cases by Drug",
                        "x": 0.05,
                        "xanchor": "left",
                    },
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'colorway': ["#7DF9FF"],
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
        })
    return fig

@app.callback(
    Output('age-fig','figure'),
    [Input('radioitems-input','value')])

def update_age_chart(drug):
    mask = age_df["Drug"] == drug
    fig = px.bar(age_df[mask], y="Age_Group", x="Count",orientation = 'h', #color = "Severity",
                 barmode="group")
    fig.update_layout({
        "title":{
                        "text": "Age Group",
                        "x": 0.05,
                        "xanchor": "left",
                    },
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'colorway': ["#7DF9FF"],
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
        })
    return fig
    
@app.callback(
    Output('gender-fig','figure'),
    [Input('radioitems-input','value')])

def update_age_chart(drug):
    mask = gender_df["Drug"] == drug
    fig = px.bar(gender_df[mask], x="Sex", y="DrugByGender", #color = "Severity",
                 barmode="group")
    fig.update_layout({
        "title":{
                        "text": "Drug Use by Gender",
                        "x": 0.05,
                        "xanchor": "left",
                    },
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'colorway': ["#7DF9FF"],
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
        })
    return fig
    




# @app.callback(
#     Output('pie-chart','figure'),
#     [Input('radioitems-input','value')]
# )

# def update_pie_chart(drug):
#     mask = age_df["Drug"] == drug
#     fig = px.pie(age_df[mask], values = ['0-18','19-25','26-34'], names= ['0-18','19-25','26-34'])
#     return fig




if __name__ == '__main__':
    app.run_server(debug=True)
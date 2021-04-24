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
dropage_df = pd.read_csv("totaleddrugbyage.csv")
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
        #style=CONTENT_STYLE,
        width =12,
        )
    ]),


    dbc.Row([
        dbc.Col([
            html.P("Select Drug:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=False, value='Ethanol',
                         options=[{'label':x, 'value':x}
                                  for x in severity_df['Drug'].unique()],
                         ),
        #dcc.Graph(id ='severity-fig', figure={})
        ], 
        width = 4,
        )
        #dcc.Graph(id ="age-fig", figure ={}),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id ="age-fig", figure ={}),width = 4
            ),
        dbc.Col(
            dcc.Graph(id ='severity-fig', figure={}), width = 4
        ),
        
        dbc.Col(
            dcc.Graph(id = "gender-fig", figure ={}),width=4
        )
        
    ]),

    dbc.Row([
        dbc.Col([
            html.P("Select Age Group:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='dropdown_age', multi=False, value='0-18',
            options=[{'label': '0-18', 'value': '0-18'},
                     {'label': '19-25', 'value': '19-25'},
                     {'label': '26-34', 'value': '26-34'},
                     {'label': '35-54', 'value': '35-54'},
                     {'label': '55-64', 'value': '55-64'},
                     {'label': '65+', 'value': '65+'}
            ],
            ),
            
        #dcc.Graph(id ='severity-fig', figure={})
        ], 
        width = 4,
        ),
        #dcc.Graph(id ="age-fig", figure ={}),
    ]),

    dbc.Row([
        dcc.Graph(id='pie_chart')
    ]),

    ],
)



@app.callback(
    Output('severity-fig','figure'),
    [Input('my-dpdn','value')])

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
    [Input('my-dpdn','value')])

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
    [Input('my-dpdn','value')])

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
    
@app.callback(
    Output(component_id='pie_chart',component_property='figure'),
    [Input(component_id='dropdown_age',component_property='value')]
)  
def update_graph(dropdown_age):
    dff = dropage_df
    fig = px.pie(
        data_frame = dff,
        values = dropdown_age,
        names = 'Drug',
        hole = 0.3,
    )
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
    })

    
    return(fig)




if __name__ == '__main__':
    app.run_server(debug=True)
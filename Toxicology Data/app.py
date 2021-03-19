import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Inputpy
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
severity_df = pd.read_csv("Severe.csv")

#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
###STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

### Hollistic Data Card 
card_graph = dbc.Card(
        dcc.Graph(id='my_bar', figure={
            'data': [
                    {
                        "x": hollistic_df["Drug"],
                        "y": hollistic_df["Count"],
                        "type": "bar",
                        "height":00,
                        #'color': colors['text'],
                        #'fontColor': ["#FFFFFF"],
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
                    "colorway": ["#00e3ff"],
                    'font': {
                    'color': colors['text'],
                    'size': 11
                }
                },
            }),
            body=True, className= 'card border-primary mb-3',
            )
#Table
table = dbc.Table.from_dataframe(table_df, striped=True, bordered=True, hover=True, className = 'table-primary thread-dark')

#creating navbar 
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
        #dbc.Collapse(dbc.Nav, id="navbar-collapse", navbar=True),
    ],
    color="darkblue",
    dark=True,
)

#severity bar graph - CARD 
card_graph2 = dbc.Card(
        dcc.Graph(id='severity-fig', figure={}), body=True, className= 'card border-primary mb-3',
)

###LAYOUT 
app.layout = dbc.Container([
    #Navbar 
    dbc.Row([
        dbc.Col(navbar,width = 12)
    ]),

    #title 
    dbc.Row([
        dbc.Col(html.H2("Toxicology Dashboard",
                        className='text-center text-primary mb-4'),
                        width = 12)
    ]),
    ###hollistic bar graph and table 
    dbc.Row([
        dbc.Col(card_graph, width=11),
        dbc.Col(table, width= 1),
    ]),

    #fatal vs severe dropdown and graph
    dbc.Row([
        dbc.Col([
            html.P("Select Drug:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=False, value='Ethanol',
                         options=[{'label':x, 'value':x}
                                  for x in severity_df['Drug'].unique()],
                         ),
            card_graph2,
        #dcc.Graph(id ='severity-fig', figure={})
        ], 
        xs=10, sm=12, md=12, lg=5, xl=5
        ),
    ])
])

###CALLBACKS 

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
        'colorway': ["#00e3ff"],
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
        })
    return fig





if __name__ == '__main__':
<<<<<<< HEAD
    app.run_server(debug=True, port = 5500)
=======
    app.run_server(debug=True, port = 5501)
>>>>>>> 44b1d2fb624607996f4cefe2870608eccb5ae00f

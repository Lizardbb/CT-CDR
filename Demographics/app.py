import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go


###STORING DATA
hollistic_df = pd.read_csv("TownTotalcrashesFatalsInjuryNoinjury.csv") #overview 

##Top value finder
top_val = hollistic_df.nlargest(5, ['Crashes'])
top_town_list = top_val['Town'].values.tolist()
top_crash_list = top_val['Crashes'].values.tolist()


top_crashes_table_df = pd.DataFrame(
    {
        "Top 5 Most Crashes by Town": top_town_list,
        "Crashes": top_crash_list,
    }
)

##Bottom value finder
bottom_val = hollistic_df.nsmallest(5, ['Crashes'])
bottom_town_list = bottom_val['Town'].values.tolist()
bottom_crash_list = bottom_val['Crashes'].values.tolist()


bottom_crashes_table_df = pd.DataFrame(
    {
        "The 5 Least Crashes by Town": bottom_town_list,
        "Crashes": bottom_crash_list,
    }
)

##Severity list builder
town_list = hollistic_df['Town'].values.tolist()
Fatals_list = hollistic_df['Fatals'].values.tolist()
Injury_list = hollistic_df['Injury'].values.tolist()
Noinjury_list = hollistic_df['No_Injury'].values.tolist()

severity_town_list = []
severity_severe_list = []
severity_count_list = []

for i in range(len(town_list)):
    severity_town_list.append(town_list[i])
    severity_town_list.append(town_list[i])
    severity_town_list.append(town_list[i])
    
    severity_severe_list.append("Fatal")
    severity_severe_list.append("Injuries")
    severity_severe_list.append("No Injury")

    severity_count_list.append(Fatals_list[i])
    severity_count_list.append(Injury_list[i])
    severity_count_list.append(Noinjury_list[i])
    

severity_df = pd.DataFrame(
    {
        "Town": severity_town_list,
        "Severity": severity_severe_list,
        "Count": severity_count_list,
    }
)

#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
###STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server


### Hollistic Data Card 
card_graph = dbc.Card(
        dcc.Graph(id='my_bar', figure={
            'data': [
                    {
                        "x": hollistic_df["Town"],
                        "y": hollistic_df["Crashes"],
                        "type": "bar",
                        "height":00,
                        #'color': colors['text'],
                        #'fontColor': ["#FFFFFF"],
                    },
                ],
                "layout": {
                    "title":{
                        "text": "Crashes per Town",
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
#Tables
top_table = dbc.Table.from_dataframe(top_crashes_table_df, striped=True, bordered=True, hover=True, className = 'table-primary thread-dark')
bottom_table = dbc.Table.from_dataframe(bottom_crashes_table_df, striped=True, bordered=True, hover=True, className = 'table-primary thread-dark')


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
        dbc.Col(html.H2("Demographics Dashboard",
                        className='text-center text-primary mb-4'),
                        width = 12)
    ]),
    ###hollistic bar graph
    dbc.Row([
        dbc.Col(card_graph, width=12),
    ]),

    #fatal vs severe dropdown and graph
    dbc.Row([
        dbc.Col([
            html.P("Select Town:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=False, value='Andover',
                         options=[{'label':x, 'value':x}
                                  for x in severity_df['Town'].unique()],
                         ),
            card_graph2,
        ##dcc.Graph(id ='severity-fig', figure={})
        ], 
        xs=10, sm=12, md=12, lg=5, xl=5
        ),
        dbc.Col(top_table),
        dbc.Col(bottom_table),
    ]),
    
    html.Iframe(src=app.get_asset_url('ctmap.html'),
                style={"height": "1067px", "width": "100%"})
])



###CALLBACKS 

@app.callback(
    Output('severity-fig','figure'),
    [Input('my-dpdn','value')])

def update_bar_chart(Town):
    mask = severity_df["Town"] == Town
    fig = px.bar(severity_df[mask], x="Severity", y="Count", #color = "Severity",
                 barmode="group")
    fig.update_layout({
        "title":{
                        "text": "Severity of Cases by Town",
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
    app.run_server(debug=True, port = 8050)

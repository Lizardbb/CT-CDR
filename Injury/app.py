import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go

#STORING DATA
workzone_df = pd.read_csv("WorkzoneInjuries.csv") 
bus_df = pd.read_csv("BusCrashes.csv")
age_df = pd.read_csv("injuryByAgeGroup.csv")
town_df = pd.read_csv("TransposedTownTotalcrashesFatalsInjuryNoinjury.csv")


#STYLING EXTRAS
UCONN_LOGO = "https://production.wordpress.uconn.edu/techpark2018/wp-content/uploads/sites/2664/2018/12/uconn-wordmark-single-white.png"

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

#STYLESHEET
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server

options = [{'label': t, 'value': t} for t in town_df]


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

#Workzone Bar Chart 

fig = px.bar(workzone_df, x="Work_Zone_Relation", y="Total",
             color='Type', title = 'Workzone Crashes',barmode='group',
             height=400)


fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})

#Schoolbus Crashes

fig_2 = px.bar(bus_df, x="School_Bus_Relation", y="Total",
             color='Type', title = 'Schoolbus Crashes',barmode='group',
             height=480)


fig_2.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})

#LAYOUT
app.layout = dbc.Container([
    #Navbar 
    dbc.Row([
        dbc.Col(navbar,width = 12)
    ]),

    #title 
    dbc.Row([
        dbc.Col(html.H2("Injuries and Fatalities Dashboard",
                        className='text-center text-primary mb-4'),
                        width = 12)
    ]),
    ###hollistic bar graph and table 
    dbc.Row([
        dbc.Col(dcc.Graph(figure = fig), width = 6
        ),  
        dbc.Col(dcc.Graph(figure = fig_2), width = 6
        ),
    ]),
    dbc.Row([
        dbc.Col([html.Label(['Injuries by Age Group']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': '0-18', 'value': '0-18'},
                     {'label': '19-25', 'value': '19-25'},
                     {'label': '26-34', 'value': '26-34'},
                     {'label': '35-54', 'value': '35-54'},
                     {'label': '55-64', 'value': '55-64'},
                     {'label': '65+', 'value': '65+'},
            ],
            value='0-18',
            multi=False,
            clearable=False,
            style={"width": "40%"}
        ),
    ]),
    dbc.Col([html.Label(['Injuries by Town']),
        dcc.Dropdown(
            id='town_dropdown',
            options=options,
            value='Andover',
            searchable=False,
            multi=False,
            clearable=False,
            style={"width": "40%", 'color': colors['background']}
        ),
        ],
        width = 6,
        ),
        
        ]),
    

    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'the_graph'),
            #dcc.Graph(id = 'the_graph_2'),
        ],
        width = 6,
        ),
        dbc.Col([
            dcc.Graph(id = 'the_graph_2'),
        ],
        width = 6,
        ),
    ]),
        ])


#callbacks
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = age_df

    fig=px.pie(
            data_frame=dff,
            values= my_dropdown,
            names='Injury',
            hole=.3,
            )

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
    })

    return (fig)

    #pie graph 2
@app.callback(
    Output(component_id='the_graph_2', component_property='figure'),
    [Input(component_id='town_dropdown', component_property='value')])

def update_graph(town_dropdown):
    dff = town_df

    fig=px.pie(
            data_frame=dff,
            labels=['Total','Fatal','Injury', 'No_Injury'],
            values=town_dropdown,
            names=['Total','Fatal','Injury', 'No_Injury'],
            hole=.3,
            )

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'font': {
                    'color': colors['text'],
                    'size': 11
                }
    })

    return (fig)




if __name__ == '__main__':
    app.run_server(debug=True)


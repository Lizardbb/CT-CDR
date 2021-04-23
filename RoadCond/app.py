import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go

#STORING DATA
town_df = pd.read_csv("roadconsByTown (1).csv") 
hour_df = pd.read_csv("roadconByTimeHour.csv")
month_df = pd.read_csv("roadconByMonth.csv")
year_df = pd.read_csv("roadconByDateYear.csv")


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



#Year Bar Chart 

fig = px.bar(year_df, x="CrashDateYear", y="Count",
             color='Description', title = 'Road Conditions by Year',barmode='group',
             height=500)


fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})

#Month Crashes

fig_2 = px.bar(month_df, x="CrashDateMonth", y="Count",
             color='Description', title = 'Road Conditions by Month',barmode='group',
             height=500)


fig_2.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})

#Hour Crashes
the_graph = px.bar(hour_df, x="CrashTimeHour", y="Count",
             color='Description', title = 'Road Conditions by Hour',barmode='group',
             height=500)


the_graph.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
'font':{
    'color': 'antiquewhite'
}
})


#LAYOUT
app.layout = dbc.Container([
    ###hollistic bar graph and table 
    dbc.Row([
        dbc.Col(dcc.Graph(figure = fig), width = 11
        ),  
        dbc.Col(dcc.Graph(figure = fig_2), width = 11
        ),
    ]),
        
    

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure = the_graph),
        ],
        width = 11,
        )
    ]),
    dbc.Row([
        dbc.Col([html.Label(['Road Conditions by Town']),
        dcc.Dropdown(
            id='town_dropdown',
            options=options,
            value='Andover',
            searchable=True,
            multi=False,
            clearable=False,
            style={"width": "60%", 'color': colors['background']}
        ),
        ],
        width = 6,
        ),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'the_graph_2'),
        ],
        width = 10,
        ),
        ]),
    ])


#callbacks



    #pie graph 2
@app.callback(
    Output(component_id='the_graph_2', component_property='figure'),
    [Input(component_id='town_dropdown', component_property='value')])

def update_graph(town_dropdown):
    dff = town_df

    fig=px.pie(
            data_frame=dff,
            labels=['Dry','Standing Water','Wet','Snow', 'Slush','Ice / Frost', 'Moving Water', 'Sand', 'Mud', 'Dirt', 'Gravel', 'Oil', 'Other','Unknown'],
            values=town_dropdown,
            names=['Dry','Standing Water','Wet','Snow', 'Slush','Ice / Frost', 'Moving Water', 'Sand', 'Mud', 'Dirt', 'Gravel', 'Oil', 'Other','Unknown'],
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
    app.run_server(debug=True, port=5501)
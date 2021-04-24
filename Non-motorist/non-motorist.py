import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.express as px 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.graph_objects as go


###STORING DATA
hollistic_df = pd.read_csv("crashesTownFatalsInjuryNoinjury-Pedestrians.csv") #overview 

##Top value finder
top_val = hollistic_df.nlargest(5, ['Crashes'])
top_town_list = top_val['Town'].values.tolist()
top_crash_list = top_val['Crashes'].values.tolist()


top_crashes_table_df = pd.DataFrame(
    {
        "Top 5 Most Non-Motorist Crashes by Town": top_town_list,
        " Number of Crashes": top_crash_list,
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
    'text': '#FFFFFF',
    'drop': '#000000'
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
                    },
                ],
                "layout": {
                    "title":{
                        "text": "Total Non-Motorist Crashes per Town",
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



#severity bar graph - CARD 
card_graph2 = dbc.Card(
        dcc.Graph(id='severity-fig', figure={}), body=True, className= 'card border-primary mb-3',
)

###LAYOUT 
app.layout = dbc.Container([


    ###hollistic bar graph

    dbc.Row([
        dbc.Col(card_graph, width=12),
    ]),

    #fatal vs severe dropdown and graph
    dbc.Row([
        dbc.Col([
            html.P("Select Town:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=False, value='Ansonia',
                    style={'color':colors['drop']},
                         options=[{'label':x, 'value':x}
                                  for x in severity_df['Town'].unique()],
                         ),
            card_graph2,
        ##dcc.Graph(id ='severity-fig', figure={})
        ], 
        xs=10, sm=12, md=12, lg=5, xl=5
        ),
        dbc.Col(top_table),
    ])
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
                        "text": "Severity of Non-Motorist Crashes by Town",
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
    app.run_server(debug=True, port = 5501)

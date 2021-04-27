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

#
#Percent of crashes by pop

#population data
pop_data = pd.read_csv("2019censusdata.csv")

pop_list = pop_data["Population"].values.tolist()

crash_list = hollistic_df["Crashes"].values.tolist()

perc_list = []

for i in range(len(pop_list)):
    perc_list.append(round((crash_list[i]/pop_list[i]), 2))
    

perc_list_df = pd.DataFrame(
    {
        "Town": pop_data["Town"].values.tolist(),
        "Crashes divided by Pop": perc_list,
    }
)


perc_crashes_table_df = perc_list_df.nlargest(5, ['Crashes divided by Pop'])


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
    
    severity_severe_list.append("Fatals")
    severity_severe_list.append("Injures")
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

#age data frame

age_df = pd.read_csv("crashesTownByAges.csv")

zero_eighteen = age_df["0-18"].values.tolist()
nineteen_twentyfive = age_df["19-25"].values.tolist()
twentysix_thirtyfour = age_df["26-34"].values.tolist()
thirtyfive_fiftyfour = age_df["35-54"].values.tolist()
fiftyfive_sixtyfour = age_df["55-64"].values.tolist()
sixtyfive = age_df["65+"].values.tolist()


age_town_list = []
age_range_list = []
age_count_list = []

for i in range(len(town_list)-1):
    age_town_list.append(town_list[i])
    age_town_list.append(town_list[i])
    age_town_list.append(town_list[i])
    age_town_list.append(town_list[i])
    age_town_list.append(town_list[i])
    age_town_list.append(town_list[i])

    age_range_list.append("0-18")
    age_range_list.append("19-25")
    age_range_list.append("26-34")
    age_range_list.append("35-54")
    age_range_list.append("55-64")
    age_range_list.append("65+")

    age_count_list.append(zero_eighteen[i])
    age_count_list.append(nineteen_twentyfive[i])
    age_count_list.append(twentysix_thirtyfour[i])
    age_count_list.append(thirtyfive_fiftyfour[i])
    age_count_list.append(fiftyfive_sixtyfour[i])
    age_count_list.append(sixtyfive[i])


#Creation of age data frame
age_df = pd.DataFrame(
    {
        "Town": age_town_list,
        "Range": age_range_list,
        "Count": age_count_list,
    }
)

#state list builder

state_df = pd.read_csv("crashTownsByState.csv")

state_town_list = []
state_state_list = []
state_count_list = []
state_list = ['UT','NC','WI','ON','SI','MA','MI','NB','TN','NH','AK','OK','KY','OT','CO','NV','SD','PA','CH','WV','GA','RI','IN','MX','DC','BC','MD','OR','QC','CT','AR','MN','AL','ID','TX','NM','CU','NS','ND','ME','PR','IL','MO','SC','YT','DE','FL','TA','MP','CA','WY','HI','OH','NE','VT','NY','MS','NJ','AB','IA','KS','LA','WA','PE','MB','AZ','VA','MT']


for j in range(len(town_list)):
    for i in range(len(state_df.columns)-1):
        state_town_list.append(town_list[j])

for i in range(len(town_list)):
    state_state_list += state_list

state_count_list = state_df.loc[:,state_df.columns!="Town"].values.flatten().tolist()


state_df = pd.DataFrame(
    {
        "Town": state_town_list,
        "State": state_state_list,
        "Count": state_count_list,
    }
)

#creation of sex data frame

sex_df = pd.read_csv("crashTownsBySex.csv")

sex_town_list = []
sex_sex_list = []
sex_count_list = []

for i in range(len(town_list)):
    sex_town_list.append(town_list[i])
    sex_town_list.append(town_list[i])
    sex_sex_list += ['M', 'F']

sex_count_list = sex_df.loc[:,sex_df.columns!="Town"].values.flatten().tolist()



sex_df = pd.DataFrame(
    {
        "Town": sex_town_list,
        "Sex": sex_sex_list,
        "Count": sex_count_list,
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
total_table = dbc.Table.from_dataframe(top_crashes_table_df, striped=True, bordered=True, hover=True, className = 'table-primary thread-dark')
perc_table = dbc.Table.from_dataframe(perc_crashes_table_df, striped=True, bordered=True, hover=True, className = 'table-primary thread-dark')


#creating navbar 
navbar = dbc.Navbar(

)

#severity bar graph - CARD 
card_graph2 = dbc.Card(
        dcc.Graph(id='severity-fig', figure={}), body=True, className= 'card border-primary mb-3',
)

#Age group bar graph - CARD
card_graph3 = dbc.Card(
        dcc.Graph(id='age-fig', figure={}),body=True, className= 'card border-primary mb-3',
)

#State group bar graph - CARD
card_graph4 = dbc.Card(
        dcc.Graph(id='state-fig', figure={}),body=True, className= 'card border-primary mb-3',
)

#Sex group bar graph - CARD
card_graph5 = dbc.Card(
        dcc.Graph(id='sex-fig', figure={}),body=True, className= 'card border-primary mb-3',
)

###LAYOUT 
app.layout = dbc.Container([
    #Navbar 
 

   
    ###hollistic bar graph
    dbc.Row([
        dbc.Col(card_graph, width=12),
    ]),

    #fatal vs severe dropdown and graph
    dbc.Row([
        html.P("Select Town:  ",
                   style={"textDecoration": "underline"}),
            
    ]),

    dbc.Row([dcc.Dropdown(id='my-dpdn', multi=False, value='Andover', style={'height': '40px', 'width': "50%", 'padding': "-10px"},
                         options=[{'label':x, 'value':x}
                                  for x in severity_df['Town'].unique()],
                         )]),

    dbc.Row([
        dbc.Col(card_graph2, style={'height': "90%"}),
        dbc.Col(card_graph5, style={'height': "90%"}),
    ]),

    dbc.Row([
        dbc.Col(card_graph4, style={'height': "90%"}),
    ]),

    dbc.Row([
        dbc.Col(card_graph3, style={'height': "90%"}),
    ]),

    dbc.Row([
        dbc.Col(total_table),
        dbc.Col(perc_table),
    ])
])



###CALLBACKS 

@app.callback([
    Output('severity-fig','figure'),
    Output('age-fig', 'figure'),
    Output('state-fig', 'figure'),
    Output('sex-fig', 'figure')],
    [Input('my-dpdn','value')])

def update_bar_chart(Town):
    mask1 = severity_df["Town"] == Town
    fig1 = px.bar(severity_df[mask1], x="Severity", y="Count", #color = "Severity",
                 barmode="group")
    fig1.update_layout({
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

    mask2 = age_df["Town"] == Town
    fig2 = px.bar(age_df[mask2], x="Range", y="Count", #color = "Severity",
                 barmode="group")
    fig2.update_layout({
        "title":{
                        "text": "Age Range of Cases by Town",
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

    mask3 = state_df["Town"] == Town
    fig3 = px.bar(state_df[mask3], x="State", y="Count", #color = "Severity",
                 barmode="group")
    fig3.update_layout({
        "title":{
                        "text": "State Registration of Cases by Town",
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
    
    mask4 = sex_df["Town"] == Town
    fig4 = px.bar(sex_df[mask4], x="Sex", y="Count", #color = "Severity",
                 barmode="group")
    fig4.update_layout({
        "title":{
                        "text": "Sex of Cases by Town",
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
    return fig1, fig2, fig3, fig4



if __name__ == '__main__':
    app.run_server(debug=True, port = 8050)

# from jupyter_dash import JupyterDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import numpy as np






# Migration Dataset ######################################################################################
from flask import app

Migration_Data = pd.read_csv('https://raw.githubusercontent.com/erusto/Human-Migration-Reporting-System/main/20213101%20IOM%20SSD%20DTM%20MT%20R9_Baseline%20Area%20Dataset_September%202020.csv',encoding='windows-1252')
Migration_Data_1 = Migration_Data[["statname","a- IDP individuals","displ. Within","displ. Abroad","2014-2015","2016-2017","2018 pre R","2018 post R","2019","2020","conflict","Communial Conflict","Disasters","unknown","IDPs in camps ","IDPs in host community "," IDPs multiple displac ","host pop "," returnees present "," returnees internal ","abroad returnee ","H no damage ","H part damage ","H sev damaged ","House unknown","displaced and not returned to payam "," relocated pop in payam ",]].groupby("statname").sum()
Migration_Data_2 = Migration_Data_1.reset_index()

######################################### MAPS DF ###############
map1 = Migration_Data[["statname","0-county name","lat","lon","a- IDP individuals"]]
map2 = map1.dropna(how="all")
map3 = map2.pivot_table(index=["0-county name","statname"],values=["lat","lon","a- IDP individuals"],aggfunc={"a- IDP individuals":np.sum,"lat":np.mean,"lon":np.mean}).reset_index()

###################################### Reasons Why People Migrate ######################################################################################
ReasonForDisplacement = Migration_Data_2.pivot_table(index=["statname"],values=["conflict","Communial Conflict","Disasters","unknown",],aggfunc=np.sum,margins=True)
ReasonForDisplacement_1 = ReasonForDisplacement.transpose().reset_index()
ReasonForDisplacement_1.columns = ['Reason for Migration','Central Equatoria','Eastern Equatoria','Jonglei','Lakes','Northern Bahr el Ghazal','Unity','Upper Nile','Warrap','Western Bahr el Ghazal','Western Equatoria','Sum Reason for Migration']

###################################### Level of Damage on Houses ######################################################################################
LeveOfDamageOnHouse = Migration_Data_2.pivot_table(index=["statname"],values=["H no damage ","H part damage ","H sev damaged ","House unknown"],aggfunc=np.sum,margins=True)
LeveOfDamageOnHouse_1 = LeveOfDamageOnHouse.transpose().reset_index()
LeveOfDamageOnHouse_1.columns = ['Level of Damage on House','Central Equatoria','Eastern Equatoria','Jonglei','Lakes','Northern Bahr el Ghazal','Unity','Upper Nile','Warrap','Western Bahr el Ghazal','Western Equatoria','Sum House Damage']

###################################### Population Indicators ######################################################################################
Indicator = Migration_Data_2.pivot_table(index=["statname"],values=["IDPs in camps ","IDPs in host community "," IDPs multiple displac ","host pop "," returnees present "," returnees internal ","abroad returnee "],aggfunc=np.sum,margins=True)
Indicator_1 = Indicator.transpose().reset_index()
Indicator_1.columns = ['Indicator','Central Equatoria','Eastern Equatoria','Jonglei','Lakes','Northern Bahr el Ghazal','Unity','Upper Nile','Warrap','Western Bahr el Ghazal','Western Equatoria','CumulativeIndicator']

###################################### Migration Over the Years ######################################################################################
DisplacementOverTheYears = Migration_Data_2.pivot_table(index=["statname"],values=["2014-2015","2016-2017","2018 pre R","2018 post R","2019","2020"],aggfunc=np.sum,margins=True)
DisplacementOverTheYears_1 = DisplacementOverTheYears.transpose().reset_index()
DisplacementOverTheYears_1.columns = ['Year of Displacement','Central Equatoria','Eastern Equatoria','Jonglei','Lakes','Northern Bahr el Ghazal','Unity','Upper Nile','Warrap','Western Bahr el Ghazal','Western Equatoria','Total Displacement over years']

###################################### Detailed Datasets ########################################
Migration_Data = pd.read_csv('https://raw.githubusercontent.com/erusto/Human-Migration-Reporting-System/main/20213101%20IOM%20SSD%20DTM%20MT%20R9_Baseline%20Area%20Dataset_September%202020.csv',encoding='windows-1252')
pdfDwithinVsDabroad1 = Migration_Data[["0-county name","0-payam name","statname","a- IDP individuals","displ. Within","displ. Abroad","2014-2015","2016-2017","2018 pre R","2018 post R","2019","2020","conflict","Communial Conflict","Disasters","unknown","IDPs in camps ","IDPs in host community "," IDPs multiple displac ","host pop "," returnees present "," returnees internal ","abroad returnee ","H no damage ","H part damage ","H sev damaged ","House unknown","displaced and not returned to payam "," relocated pop in payam ",]]
pMigration_Data_2=pdfDwithinVsDabroad1.dropna(how="all")





###################################### HHDamageOvertheyearsinEachstate ######################################################################################
HHDamageOvertheyearsinEachstate=pd.read_csv('https://raw.githubusercontent.com/erusto/Human-Migration-Reporting-System/main/20213101%20IOM%20SSD%20DTM%20MT%20R9_Baseline%20Area%20Dataset_September%202020.csv',encoding='windows-1252')
HHDamageOvertheyearsinEachstate1 = HHDamageOvertheyearsinEachstate[["statname","a- IDP individuals","displ. Within","displ. Abroad","2014-2015","2016-2017","2018 pre R","2018 post R","2019","2020","pda-2016-2017 ","pda-2018 pre R","pda-2018 post R-ARCSS","pda-2019","pda-2020","2014-2015 Conflict","2014-2015  C - clashes","2014-2015 disaster","2014-2015 unknown","2016-2017 conflict","2016-2017  c-clashes","2016-2017 disaster","2016-2017  unknown ","2018 pre R conflict","2018 pre R C-clashes","2018 pre R disaster","2018 pre R unknown","2018 post R conflict","2018 post R C-clashes","2018 post R disaster","2018 post R unknown","2019 conflict","2019 C-clashes","2019 disaster","2019 unknown","2020 conflict","2020 C-clashes","2020 disaster","2020 unknown","i-2016-2017","i-2018 pre R","i-2018 post R","i-2019","i-2020 ","i-unknown","a-2016-2017","a-pre R 2018 ","a-post R 2018 ","a-2019","a-2020","a-unknown","conflict","Communial Conflict","Disasters","unknown","IDPs in camps ","IDPs in host community "," IDPs multiple displac ","host pop "," returnees present "," returnees internal ","abroad returnee ","H no damage ","H part damage ","H sev damaged ","House unknown","displaced and not returned to payam "," relocated pop in payam ",]].groupby("statname").sum()
HHDamageOvertheyearsinEachstate2 = HHDamageOvertheyearsinEachstate1.reset_index()
HHDamageOvertheyearsinEachstate3 = HHDamageOvertheyearsinEachstate2.pivot_table(index=["statname"],values=["2018 pre R conflict","2018 pre R C-clashes","2018 pre R disaster","2018 pre R unknown"],aggfunc=np.sum,margins=True)
HHDamageOvertheyearsinEachstate3 = HHDamageOvertheyearsinEachstate2.pivot_table(index=["statname"],values=["2018 pre R conflict","2018 pre R C-clashes","2018 pre R disaster","2018 pre R unknown"],aggfunc=np.sum,margins=True)
HHDamageOvertheyearsinEachstate4=HHDamageOvertheyearsinEachstate3.transpose().reset_index()
HHDamageOvertheyearsinEachstate4.columns = ['Year','Central Equatoria','Eastern Equatoria','Jonglei','Lakes','Northern Bahr el Ghazal','Unity','Upper Nile','Warrap','Western Bahr el Ghazal','Western Equatoria','Sum']

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
nav_STYLE = {
    'overflow': 'hidden',
  'position': 'fixed-top',
   "bottom": 0,
    "left": 0,
    "padding": "2rem 1rem",
    "width":"100%"

}



# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}




nav = html.Div(
    [

        #################NAV

                dbc.NavbarSimple(
                    [
                        dbc.NavItem(dbc.NavLink("Map",active="exact", href="/", external_link=True,)),
                        dbc.NavItem(dbc.NavLink("Agregated",active="exact", href="/page-1", external_link=True,)),
                         dbc.NavItem(dbc.NavLink("State_Analysis",active="exact", href="/page-2", external_link=True,)),
                         dbc.NavItem(dbc.NavLink("Payam Level",active="exact", href="/page-3", external_link=True,)),
                        dbc.NavItem(dbc.NavLink("Historical Analysis",active="exact", href="/page-4", external_link=True,)),

                        dbc.DropdownMenu(
                            [
                            dbc.DropdownMenuItem("Project Repo", href="https://github.com/erusto/Human-Migration-Reporting-System", active="exact",target="_blank", ),
                            dbc.DropdownMenuItem("Connect with me", href="https://www.linkedin.com/in/mogga-poul-erusto-015694171/", active="exact", target="_blank",)

                            ],
                            label="Select Category",
                            nav=True,
                            color="",

                        )
                    ],
                        brand="Human Migration Reporting System",
                        brand_href="/",
                        color="#5bc0de",
                        dark=True,
                )
        ###################


    ]

)


#####CONTENT STYLE


content = html.Div(id="page-content")
app.layout = html.Div([dcc.Location(id="url"), nav, content])



####CALLBACK
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return[


            ########################################## HOME 

                                dcc.Graph(id='ReturneesVsHostPop',
                                          #####################################
                                          figure = px.scatter_mapbox(
                                                    map3, lat="lat", lon="lon", hover_name="0-county name",size="a- IDP individuals",
                                                    hover_data=["statname","0-county name","a- IDP individuals"],
                                                    size_max=39,
                                                    height=660,
                                                    color="statname",
                                                    zoom=5.90,
                                                   ).update_layout(
                                                    mapbox_style="open-street-map",
                                                    margin={"r":0,"t":0,"l":0,"b":0},
                                                    autosize=True,
                                                    hovermode='closest',
                                                     mapbox=dict(
                                                         center= {'lon': 30.61238095, 'lat': 7.307798259 },
                                                         bearing=0,
                                                         pitch=25,),
                                                    legend=dict(
                                                        font = dict(size = 8),
                                                    )
                                          )
                                       #######################################
                                ,config={'displayModeBar': False})



        ]











    elif pathname == "/page-1":
        return[


              dbc.Container([


              html.Br(),

    dbc.Row([

         #################################
         dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees Present'),
                    html.H4(id='Returnees Present', children="1615765")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),

  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s In Host Population'),
                    html.H4(id='content-connections', children="1240920")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees Internal'),
                    html.H4(id='content-connections', children="1135894")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees from Abroad'),
                    html.H4(id='content-connections', children="538774")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),

  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s in Camps'),
                    html.H4(id='content-connections', children="374845")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s Multiply Displaced'),
                    html.H4(id='content-connections', children="97709")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        #################################



       ],
        className='mb-3'),







                   dbc.Row([
                       ##############################

                               dbc.Col([
            dbc.Card([
                dbc.CardBody

                ([
                     html.H5('Level of Damage on Houses'),
                               dcc.Graph(id='levelOfDamage',
                                         figure = go.Figure(go.Pie(
                                labels = LeveOfDamageOnHouse_1['Level of Damage on House'],
                                values = LeveOfDamageOnHouse_1['Sum House Damage'],
                                pull=[0,0,0,0.3],
                                         )
                                            ).update_layout(
                                   height=430,
                                   width=300,
                                 font =dict(size=14),
                                margin = dict(t=0, l=0, r=0, b=0),
                                legend=dict(title=None,
                                            font = dict(size = 8),
                                            orientation="h",
                                            y=0,
                                            yanchor="top",
                                            x=0,
                                            xanchor="left",))
                              ,config={'displayModeBar': False}
                    ),
                ])
            ],style={"height":"480px"}),
        ], width=3),

######################################################




        dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([
                     html.H5('Why Pepople choose to Migrate'),

                    dcc.Graph(id='HouseDamageLevel',
                              ##############
                               figure = px.pie(ReasonForDisplacement_1,
                                              values='Sum Reason for Migration',
                                              names='Reason for Migration',
                                              template='simple_white',
                                              hole=.6,
                                              height=400,
                                                ).update_layout(

                                font =dict(size=10),
                                  margin = dict(t=0, l=0, r=0, b=0),
                                  legend=dict(title=None,
                                            font = dict(size = 8),
                                            orientation="h",
                                            y=0,
                                            yanchor="top",
                                            x=0,
                                            xanchor="left",))

                              ####################################
                              ,config={'displayModeBar': False}
                    ),

                ])
            ], style={"height":"480px"}),
        ], width=3),





##################################################################################



 dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([
                    html.H5('Returnees over the Years'),
                       dcc.Graph(id='Indicators',
#######################################################################################################################3
                                figure = px.line(
                                DisplacementOverTheYears_1,
                                y=["2014-2015","2016-2017","2018 pre R","2018 post R","2019","2020"],
                                x='Total Displacement over years',
                                template='plotly_white',
                                height=410,
                                 width=280
                              ).update_traces(mode="lines+markers",
                                              line={'color':'rgb(91, 192, 222)'},
                                              marker_color='red',
                                             ).update_layout(
                            margin=dict(l=0, r=0, t=20, b=0),
                                showlegend=False,
                                #legend=dict(x=0.029, y=1.038, font_size=10),
                                font =dict(
                                size=10
                                ),
                                xaxis=dict(
                                    showgrid=False,
                                    showline=False,
                                    showticklabels=False,
                                    domain=[0, 0.85],
                                    title=' '),
                                yaxis=dict(
                                    title=None,
                                    showticklabels=True,
                                    domain=[0, 0.85],
                                    showline=True,
                                    type='category')
                                        )
#######################################################################################################################
                    ,config={'displayModeBar': False,}),
                ])
            ], style={"height":"480px"}),
        ], width=3),





##################################################################################
  dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([
                    html.H5('IDP,s in Each State'),
                       dcc.Graph(id='Indicators',
#######################################################################################################################3
                                  figure = px.bar(Migration_Data_2,
             x='a- IDP individuals',
             y='statname',
             color='statname',
             width=300,
            height=400,
             text='a- IDP individuals',
             template='simple_white',
        ).update_traces(
            #texttemplate='%{text:.2s}',
            #textposition='outside',
            textfont_color='black',
            textfont_size=8
        ).update_layout(
            uniformtext_minsize=13,
            uniformtext_mode='hide',
            showlegend=False,
            margin=dict(l=100, r=0, t=30, b=0),
    font =dict(size=10),
    yaxis=dict(
        {'categoryorder':'total ascending'},
        showticklabels=True,
        domain=[0, 0.85],
        title=' ', visible=True,
        tickfont = dict(size=10),
        showgrid=True,
        showline=True,
    ),
    xaxis=dict(
        showticklabels=False,
        domain=[0, 0.85],
        title=' ', visible=True,
        tickfont = dict(size=8),
        showgrid=False,
        showline=False,

    ),

        )
#######################################################################################################################
                    ,config={'displayModeBar': False,}),
                ])
            ], style={"height":"480px"}),
        ], width=3),























                       ##############################
                   ],
        className='mb-1'),


],fluid=True)

        ]

















    elif pathname == "/page-2":
        return[


              dbc.Container([


              html.Br(),





    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([
                    dcc.Graph(id='IDPsInEachState',

                              #############################################################

                              figure=px.scatter(Migration_Data_2,
               y=" IDPs multiple displac ",
               x='statname',
               template='plotly_white',
                #color="statname",
              # width=450,
                height=270,
               title="IDPs In Each state with Multiple Displacement",
               text='a- IDP individuals').update_traces(
                                  mode="lines+markers",
                                  fill='tozeroy',
                                  line={'color':'#FFC300 '},
                                 ).update_layout(

     uniformtext_minsize=13,

     showlegend=False,
     margin=dict(l=0, r=0, t=25, b=0),
     xaxis = dict(

            # {'categoryorder':'total ascending'},
          showticklabels=True,
           showgrid=True,
        showline=True,
         title='State Name',visible=True,
         tickfont = dict(size=8)

     ),

     yaxis = dict(

          title='',
         showticklabels=True,
        domain=[0, 0.8],
         showgrid=True,
        showline=True,
         tickfont = dict(size=8)
          ), )

                              ##############################################################

                    ,config={'displayModeBar': False})

                ])
            ]),
        ], width=7),





        dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([

                      dcc.Graph(id='DIsplaceInEachStateOverTheYears',

                    #################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                 figure=go.Figure(
                    go.Scatter(
                        x=Migration_Data_2['statname'],
                        y=Migration_Data_2['displaced and not returned to payam '],
                        name="Displaced not returned to Payam",


                    )).add_trace(
                    go.Bar(
                        x=Migration_Data_2['statname'],
                        y=Migration_Data_2[' relocated pop in payam '],
                        name='relocated pop in payam'
                    )).update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    title="IDP's Returned to Payam Vs IDP's Not Returned ",
                    margin = dict(t=30, l=0, r=0, b=0),
                    height=270,
                    xaxis = dict( tickfont = dict(size=8)),
                    yaxis = dict( tickfont = dict(size=8)),
                    legend=dict(
                    font = dict(size = 8),
                    #title=None, orientation="h",
                   # y=1, yanchor="bottom",
                  # x=0, xanchor="center"
                    )
                )

                    #################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


                                ,config={'displayModeBar': False}),


                ])
            ]),
        ], width=5),


    ],className='mb-2'),
###############################################################################################################


    dbc.Row([

          dbc.Col([
            dbc.Card([
                dbc.CardBody([



                      dcc.Graph(id='LevelOfDamageOnHoseInEachState',

                         #####################################

                figure=px.bar(
               Migration_Data_2,
               x='statname',
               template='plotly_white',
               y=["H no damage ","H part damage ","H sev damaged ","House unknown"],
               height=270,
                title="Level of Damage on Houses in Each State",

               barmode="group",).update_layout(

               margin=dict(l=20, r=20, t=30, b=20),
               xaxis = dict(
                   # {'categoryorder':'total ascending'},
                   title='', visible=True,
                   tickfont = dict(size=8)),
               yaxis = dict(
                   title='', visible=True,
                   tickfont = dict(size=8)),
               legend=dict(
                   font = dict(size = 8),
                #   title=None, orientation="h",
                 #  y=1, yanchor="bottom",
                  # x=0, xanchor="center"
               )
           )


                        #######################################


                                ,config={'displayModeBar': False}),




                ], style={'textAlign': 'center'})
            ]),
        ], width=7),


          dbc.Col([
            dbc.Card([
                dbc.CardBody
                ([

                      dcc.Graph(id='ReturneeInternalVsRetuneeAbroadVsHostCommunity ',

                                #################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                figure=go.Figure(
                    go.Scatter(
                        x=Migration_Data_2['statname'],
                        y=Migration_Data_2[" returnees internal "],
                         marker_color = 'red',
                        name="returnees internal",


                    )).add_trace(
                    go.Scatter(
                        x=Migration_Data_2['statname'],
                        y=Migration_Data_2["abroad returnee "],
                         marker_color = 'yellow',
                        name='abroad returnees'
                    )).add_trace(
                    go.Bar(
                        x=Migration_Data_2['statname'],
                        y=Migration_Data_2[" returnees present "],
                         #marker_color = 'green',
                        name='returnees present'
                    )).update_layout(
                      title="Returnee Internal Vs Returnee Abroad Vs Host Community ",
                    margin = dict(t=30, l=0, r=0, b=0),
                    #paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    height=270,
                    xaxis = dict( tickfont = dict(size=8)),
                    yaxis = dict( tickfont = dict(size=8)),
                     legend=dict(
                    font = dict(size = 8),
                    #title=None, orientation="h",
                    #y=1, yanchor="bottom",
                    #x=0, xanchor="center"
                     )
                    )

                    #################################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


                                ,config={'displayModeBar': False}),


                ])
            ]),
        ], width=5),











    ],className='mb-1'),






                   dbc.Row([
             dbc.Col([
            dbc.Card([
                dbc.CardBody([



                      dcc.Graph(id='DisplacedAndNotReturned',

                         #####################################

                figure=px.bar(
                            Migration_Data_2,
                            x='statname',
                            template='plotly_white',
                            y=["conflict","Communial Conflict","Disasters","unknown"],
                             title="Why People Choos to Migrate in Each State",
                            barmode="group",
                            height=270).update_layout(
                            margin=dict(l=0, r=0, t=30, b=0),
                            xaxis = dict(
                               # {'categoryorder':'total ascending'},
                                title='', visible=True,
                                tickfont = dict(size=8)),
                            yaxis = dict(

                                title='', visible=True,
                                tickfont = dict(size=8)),
                            legend=dict(
                                font = dict(size = 8),
                                title=None,
                                #orientation="h",
                                #y=1, yanchor="bottom",
                                #x=0, xanchor="center"
                            )
                        )

                        #######################################


                                ,config={'displayModeBar': False}),




                ], style={'textAlign': 'center'})
            ]),
        ], width=7),





        dbc.Col([
            dbc.Card([
                dbc.CardBody([



                      dcc.Graph(id='CampVsHostComm',

                         #####################################

                figure=px.bar(
                    Migration_Data_2,
                    x='statname',
                    template='plotly_white',
                    y=["IDPs in host community ","IDPs in camps "],

                     height=270).update_layout(
                    title="IDP's In Host Community Vs IDP's In Camp like Setting ",
                    margin = dict(t=30, l=0, r=0, b=0),

                    yaxis = dict(
                         title='', visible=True,
                        tickfont = dict(size=8)),
                    xaxis = dict(
                       # {'categoryorder':'total ascending'},
                        title='', visible=True,
                        tickfont = dict(size=8)),

                    legend=dict(
                        font = dict(size = 8),
                        title="",
                        orientation="h",
                        #y=1, yanchor="bottom",
                        #x=0, xanchor="center"
                    )
                        )



                        #######################################


                                ,config={'displayModeBar': False}),




                ], style={'textAlign': 'center'})
            ]),
        ], width=5),

    ],className='mb-1'),





###############################################################################################################





                   dbc.Row([


                         dbc.Col([
            dbc.Card([
                dbc.CardBody([



                      dcc.Graph(id='ReturneesVsHostPop',

                         #####################################
                        figure=go.Figure(
                            go.Bar(
                                x=Migration_Data_2['statname'],
                                y=Migration_Data_2[" returnees present "],

                                name="returnees present",



                            )).add_trace(
                            go.Scatter(
                                x=Migration_Data_2['statname'],
                                y=Migration_Data_2["host pop "],

                                name='host pop'
                            )).update_layout(
                            title="Returnees Present Vs Host Communities In Each State ",
                            margin = dict(t=30, l=0, r=0, b=0),
                            plot_bgcolor='rgba(0,0,0,0)',
                            height=270,
                            xaxis = dict( tickfont = dict(size=8)),
                            yaxis = dict( tickfont = dict(size=8)),
                            legend=dict(font = dict(size = 8),
                                          title=None,
                                         # orientation="h", y=1,
                                         # yanchor="bottom",
                                        #x=0, xanchor="center"
                                       )
                            )
                        #######################################


                                ,config={'displayModeBar': False}),




                ], style={'textAlign': 'center'})
            ]),
        ], width=12),


    ],className='mb-1'),





], style={'background-color': 'black'},fluid=True)









        ]

    elif pathname == "/page-3":
        return [

       dbc.Container([

           html.Br(),

                dbc.Row([

         #################################
         dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees Present'),
                    html.H4(id='Returnees Present', children="1615765")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),

  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s In Host Population'),
                    html.H4(id='content-connections', children="1240920")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees Internal'),
                    html.H4(id='content-connections', children="1135894")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('Returnees from Abroad'),
                    html.H4(id='content-connections', children="538774")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),

  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s in Camps'),
                    html.H4(id='content-connections', children="374845")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),


  dbc.Col([
            dbc.Card([

                dbc.CardBody([
                    html.H6('IDP,s Multiply Displaced'),
                    html.H4(id='content-connections', children="97709")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        #################################



       ],
        className='mb-3'),


    dbc.Row([
        dbc.Col([


                    dcc.Graph(id='bargraph',

                              ############################################################################
                              figure=px.treemap(
                                  pMigration_Data_2,
                                  path=["0-county name","0-payam name"],
                                  template='simple_white',
                                  values='a- IDP individuals',
                                  hover_data=['statname'],
                                  color="0-county name",
                                  height=550,

                              ).update_layout(
                                  margin=dict(l=0, r=0, t=0, b=0),)

                              ############################################################################
                              ,config={'displayModeBar': False}),

                          ], width=12),
                      ],className='mb-2'),
                  ], fluid=True)


        ]





    elif pathname == "/page-4":
        return[




                 dbc.Container([
                     dbc.Row([
                         dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################
  figure=px.line(HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2014-2015 Conflict","2014-2015  C - clashes","2014-2015 disaster","2014-2015 unknown"],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis = dict( tickfont = dict(size=8)),
                              yaxis = dict(
                                   showgrid=False,
                                  showline=False,
                                    showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont = dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),


                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                                  dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################
figure=px.line(HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2016-2017 conflict","2016-2017  c-clashes","2016-2017 disaster","2016-2017  unknown "],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis = dict( tickfont = dict(size=8)),
                              yaxis = dict(
                                  showline=False,
                                   showgrid=False,
                                    showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont = dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),
                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                     ],className='mb-1'),





                     dbc.Row([
                         dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################

figure=px.line(HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2018 pre R conflict","2018 pre R C-clashes","2018 pre R disaster","2018 pre R unknown"],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis = dict( tickfont = dict(size=8)),
                              yaxis = dict(
                                  showline=False,
                                   showgrid=False,
                                    showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont = dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),

                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                                  dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################
figure=px.line(HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2018 post R conflict","2018 post R C-clashes","2018 post R disaster","2018 post R unknown"],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis=dict(tickfont=dict(size=8)),
                              yaxis=dict(
                                  showline=False,
                                  showgrid=False,
                                  showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont=dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),


                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                     ],className='mb-1'),



                       dbc.Row([
                         dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################

figure=px.line(
    HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2019 conflict","2019 C-clashes","2019 disaster","2019 unknown"],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis = dict( tickfont = dict(size=8)),
                              yaxis = dict(
                                  showline=False,
                                   showgrid=False,
                                    showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont = dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),
                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                                  dbc.Col([
                             dbc.Card([
                                 dbc.CardBody
                                 ([
                                     dcc.Graph(id='bargraph',

                    #####################################################################################################
figure=px.line(
    HHDamageOvertheyearsinEachstate2,
                             x='statname',
                              template='plotly_white',
                              y=["2020 conflict","2020 C-clashes","2020 disaster","2020 unknown"],
                                height=180
                             ).update_layout(
                              margin=dict(l=20, r=20, t=30, b=20),
                              xaxis = dict( tickfont = dict(size=8)),
                              yaxis = dict(
                                  showgrid=False,
                                    showticklabels=False,
                                  domain=[0, 0.85],
                                  title=' ', visible=True,
                                  tickfont = dict(size=8)),
                              legend=dict(font = dict(size = 8),
                                          title=None,
                                          orientation="h", y=1,
                                          yanchor="bottom", x=0.5, xanchor="center" )),


                    #####################################################################################################



                               config={'displayModeBar': False}),
                                 ])
                             ]),
                         ], width=6),
                     ],className='mb-1'),




                ##############     
                 ], fluid=True)



        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=7887)

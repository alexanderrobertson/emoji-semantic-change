import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

app = dash.Dash(__name__,
                title='ESCOT',
                external_stylesheets=[dbc.themes.CYBORG],
                external_scripts=['https://www.googletagmanager.com/gtag/js?id=G-DXWSX353B6',],)
server = app.server


change_data = pd.read_csv('change.csv')
month_list = pd.read_csv('month_list.csv')
year_list = pd.read_csv('year_list.csv')

emoji_options = [{'label': f"{e} {n}", 'value': e} for e, n in change_data[['emoji', 'name']].drop_duplicates().values]

graph = dcc.Graph(id='emoji_graph',
                  config={'displayModeBar': False},
                  animate=True, style={'height':'600px'},
                  )
t_colors = px.colors.qualitative.G10

table_month = dash_table.DataTable(id='table_month',
                                   columns=[{"name": '', "id": 'emoji'}, {"name": 'Month', "id": 'month'},
                                            {"name": 'Most similar words', "id": 'top15'}],
                                   data=[],
                                   style_as_list_view=True,
                                   style_cell=dict(textAlign='left', whiteSpace='normal', height='auto', padding=10),
                                   style_header=dict(backgroundColor="black"),
                                   style_data=dict(backgroundColor="black"),
                                   style_data_conditional=[
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 0',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[0],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 1',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[1],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 2',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[2],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 3',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[3],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 4',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[4],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 5',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[5],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 6',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[6],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 7',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[7],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 8',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[8],
                                       },
                                       {
                                           'if': {
                                               'filter_query': '{grouper} = 9',
                                               'column_id': 'month',
                                           },
                                           'backgroundColor': px.colors.qualitative.G10[9],
                                       },

                                       # {
                                       #     'if': {
                                       #         'filter_query': '{grouper} is 999',
                                       #         'column_id': 'year',
                                       #     },
                                       #     'backgroundColor': next(t_colors)
                                       #
                                       # },
                                   ],
                                   )

table_year = dash_table.DataTable(id='table_year',
                                  columns=[{"name": '', "id": 'emoji'}, {"name": 'Year', "id": 'year'},
                                           {"name": 'Most similar words', "id": 'top15'}],
                                  data=[],
                                  style_as_list_view=True,
                                  style_cell=dict(textAlign='left', whiteSpace='normal', height='auto', padding=10),
                                  style_header=dict(backgroundColor="black"),
                                  style_data=dict(backgroundColor="black"),
                                  style_data_conditional=[
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 0',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[0],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 1',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[1],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 2',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[2],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 3',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[3],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 4',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[4],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 5',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[5],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 6',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[6],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 7',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[7],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 8',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[8],
                                      },
                                      {
                                          'if': {
                                              'filter_query': '{grouper} = 9',
                                              'column_id': 'year',
                                          },
                                          'backgroundColor': px.colors.qualitative.G10[9],
                                      },

                                      # {
                                      #     'if': {
                                      #         'filter_query': '{grouper} is 999',
                                      #         'column_id': 'year',
                                      #     },
                                      #     'backgroundColor': next(t_colors)
                                      #
                                      # },
                                  ],
                                  )


@app.callback((Output("table_year", "data"),
               Output("table_month", "data")),
              Input('emoji_picker', 'value'),
              )
def update_table(selected_dropdown_value):
    year = pd.DataFrame(year_list[year_list.emoji.isin(selected_dropdown_value)])
    month = pd.DataFrame(month_list[month_list.emoji.isin(selected_dropdown_value)])

    year['grouper'] = year.emoji.map({i: e for e, i in enumerate(selected_dropdown_value)})
    month['grouper'] = month.emoji.map({i: e for e, i in enumerate(selected_dropdown_value)})

    return [year.to_dict('records'), month.to_dict('records')]


@app.callback(Output('emoji_graph', 'figure'),
              [Input('emoji_picker', 'value')],
              )
def update_graph(selected_dropdown_value, data=change_data):
    trace = []
    df_sub = data

    for emoji in selected_dropdown_value:
        x_data = df_sub[df_sub['emoji'] == emoji]['date']
        trace.extend([go.Scatter(x=x_data,
                                 y=df_sub[df_sub['emoji'] == emoji]['change_smooth'],
                                 mode='lines',
                                 name=emoji,
                                 opacity=1.0,
                                 line=dict(width=4),
                                 textposition='bottom center'),
                      ])

    traces = [trace]

    figure = {'data': [val for sublist in traces for val in sublist],
              'layout': go.Layout(
                  colorway=px.colors.qualitative.G10,
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'t': 0, 'b':0, 'l':0, 'r':0},
                  hovermode='x',
                  autosize=True,
                  xaxis={'range': [data['date'].min(), data['date'].max()]},
              ),

              }

    return figure


dropdown1 = dcc.Dropdown(id='emoji_picker',
                         options=emoji_options,
                         multi=True,
                         value=['🐸', '💀', '🏀', '🎃', '🍁'],
                         style={'backgroundColor': '#1E1E1E', },
                         className='emoji_picker',
                         )

controls = dbc.Card(
    [
        html.H4("Emoji Semantic Change Over Time", className="card-title"),
        html.B(
            "CAUTION: This data was generated using Twitter data. It contains offensive language.",
            className="card-text",
        ),
        html.Br(),
        html.P(["Code and data ", html.A('on Github. ', href="https://github.com/alexanderrobertson/emoji-semantic-change"),
                "Paper ", html.A("on arXiv. ", href="https://arxiv.org/abs/2105.00846"),]),
        html.P(
            "Select an emoji from the drop-down, or start typing its name, to view how its semantics have changed over time.",
            className="card-text",
        ),
        dropdown1,
        html.Br(),
        html.P(
            "Chart shows semantic change over time, relative to first appearance in our dataset. Higher score = more semantic change. The most similar words each month/year are shown below the graph, by decreasing order of similarity.",
            className="card-text",
        ),

        html.Table(['Examples:', html.Tr([html.Th('Emoji'), html.Th('Pattern')]),
                    html.Tr([html.Td('🐸'), html.Td('Large sudden change in 2014')]),
                    html.Tr([html.Td('💀'), html.Td('Gradual change over time')]),
                    html.Tr([html.Td('🏀'), html.Td('Slight seasonality, linked to sports season')]),
                    html.Tr([html.Td('🎃'), html.Td('High seasonality, linked to holidays')]),
                    html.Tr([html.Td('🍁'), html.Td('Switches between two meanings throughout the year')])]),


       
    ],
    body=True, 
)


graph_card = dbc.Card(
    [
        graph,
    ],
    body=True,
)

app.layout = dbc.Container(
    [

        dbc.Row(
            [
                dbc.CardGroup([dbc.Col(controls, md=4),
                               dbc.Col(graph_card, md=8)],
                              ),
            ], 

        ),
        html.Hr(),
        dbc.Row(
            [dbc.Col(md=4),
             dbc.Col(table_month, md=4),
             dbc.Col(table_year, md=4),

             ],style={'margin-left':'10px',},

        ),
    ],
    fluid=True, style={'margin-top':"10px"}, 
)

if __name__ == '__main__':
    app.run_server(debug=True)

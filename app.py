import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.graph_objects as go

from itertools import cycle

import pandas as pd

# Initialise the app
app = dash.Dash(__name__)
server = app.server

data = pd.read_csv('nn_sim.csv')
change_data = pd.read_csv('change.csv')

# Creates a list of dictionaries, which have the keys 'label' and 'value'.

g1_colors = cycle(list(px.colors.qualitative.G10))
g2_colors = cycle(list(px.colors.qualitative.G10))


emoji_options = [{'label': f"{e} {n}", 'value': e} for e,n in data[['emoji', 'name']].drop_duplicates().values]

graph = dcc.Graph(id='emoji_graph',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(data.head(),
                         x='date',
                         y='mean',
                         color='emoji',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )

graph2 = dcc.Graph(id='emoji_graph2',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(change_data.head(),
                         x='date',
                         y='change',
                         color='emoji',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )


dropdown1 = dcc.Dropdown(id='emoji_picker',
                        options=emoji_options,
                        multi=True,
                        value=['🍊', '🍑'],
                        style={'backgroundColor': '#1E1E1E'},
                        className='emoji_picker',
                        )

user_controls = html.Div(className='four columns div-user-controls',
                         children = [html.H2('Emoji: semantic change over time'),
                                     html.H3('Something'),
                                     html.Br(),
                                     html.P('Choose one or more emoji from the dropdown below.'),
                                     dropdown1,
                                     ]
                         )



data_display = html.Div(className='eight columns div-for-charts bg-grey',
                        children = [html.Div(className='div-for-dropdown',
                                             children=[graph, graph2],
                                             style={'color': '#1E1E1E'}
                                             )]
                        )

@app.callback(Output('emoji_graph', 'figure'),
              [Input('emoji_picker', 'value')])
def update_graph(selected_dropdown_value, data=data):
    ''' Draw traces of the feature 'value' based one the currently selected emoji '''
    # STEP 1
    trace = []
    df_sub = data
    # STEP 2
    # Draw and append traces for each emojiemoji
    for emoji in selected_dropdown_value:
        x_data = df_sub[df_sub['emoji'] == emoji]['date']
        trace.extend([go.Scatter(x=x_data,
                                y=df_sub[df_sub['emoji'] == emoji]['mean'],
                                mode='lines',
                                name=emoji,
                                opacity=1.0,
                                line=dict(width=4),
                                textposition='bottom center'),
                     go.Scatter(x=x_data,
                                y=df_sub[df_sub['emoji'] == emoji]['upper'],
                                mode='lines',
                                line=dict(width=0),
                                hoverinfo='none',
                                showlegend=False),
                     go.Scatter(x=x_data,
                                y=df_sub[df_sub['emoji'] == emoji]['lower'],
                                mode='lines',
                                line=dict(width=0),
                                fill='tonexty',
                                hoverinfo='none',
                                fillcolor='rgba(68, 68, 68, 0.3)',
                                showlegend=False)]
                     )
    # STEP 3
    traces = [trace]
    # data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': [val for sublist in traces for val in sublist],
              'layout': go.Layout(
                  # colorway=px.colors.qualitative.G10,
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Semantic similarity to nearest neighbours over time', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub['date'].min(), df_sub['date'].max()]},
              ),

              }

    return figure

@app.callback(Output('emoji_graph2', 'figure'),
              [Input('emoji_picker', 'value')],
              )
def update_graph_categories(selected_dropdown_value, data=change_data):
    ''' Draw traces of the feature 'value' based one the currently selected emoji '''
    # STEP 1
    trace = []
    df_sub = data
    # STEP 2
    # Draw and append traces for each emoji


    for emoji in selected_dropdown_value:
        x_data = df_sub[df_sub['emoji'] == emoji]['date']
        trace.extend([go.Scatter(x=x_data,
                                y=df_sub[df_sub['emoji'] == emoji]['change'],
                                mode='lines',
                                name=emoji,
                                opacity=1.0,
                                line=dict(width=4),
                                textposition='bottom center'),
                     ])

    # STEP 3
    traces = [trace]
    # data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4

    figure = {'data': [val for sublist in traces for val in sublist],
              'layout': go.Layout(
                  # colorway=px.colors.qualitative.G10,
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Semantic change over time', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [data['date'].min(), data['date'].max()]},
              ),

              }

    return figure



app.layout = html.Div(children=[html.Div(className='row',
                                         children=[user_controls, data_display]
                                         )
                                ]
                      )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
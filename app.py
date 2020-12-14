import dash_core_components as dcc
import plotly.express as px
import dash
import dash_html_components as html

import pandas as pd



data = pd.read_csv('test_data.csv')

available_emoji = data.emoji.unique()

# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_emoji(list_emoji):
    dict_list = []
    for i in list_emoji:
        dict_list.append({'label': i, 'value': i})

    return dict_list

dropdown_selector = dcc.Dropdown(id='emoji_picker',
                           options=get_emoji(data['emoji'].unique()),
                           multi=True,
                           value=[data['emoji'].sort_values()[0]],
                           style={'backgroundColor': '#1E1E1E'},
                           className='emoji_picker')



graph = dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(data,
                         x='date',
                         y='mean',
                         color='emoji',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )

dropdown = dcc.Dropdown(id='emoji_picker',
                        options=get_emoji(data['emoji'].unique()),
                        multi=True,
                        value=[data['emoji'].sort_values()[0]],
                        style={'backgroundColor': '#1E1E1E'},
                        className='emoji_picker')






# Initialise the app
app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls', # Define the left element
                                           children = [html.H2('Emoji: semantic neighbour change over time'),
                                                       html.P('Select one or more emoji from the dropdown below.'),
                                                       dropdown,
                                                       ]
                                           ),
                                   html.Div(className='eight columns div-for-charts bg-grey', # Define the right element
                                            children = [html.Div(className='div-for-dropdown',
                                                                children=[graph],
                                                                style={'color': '#1E1E1E'}
         )]
                                            ),
                                  ])
                                ])







# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
import plotly.graph_objects as go
from dash import dcc
from dash import html

def render_tab(df):
    
    layout = html.Div([html.H1('Kanały sprzedaży', style={'text-align':'center'}),
                html.Div([html.Div([dcc.Graph(id='pie-weekday-sales')],
                                    style={'width':'50%'}),
                            html.Div([dcc.Dropdown(id='store_dropdown', options=[{'label':store_type, 'value':store_type} for store_type in df['Store_type'].unique()], value=df['Store_type'].unique()[0]),
                            dcc.Graph(id='barh-store-subcat')], style={'width':'50%'})], style={'display':'flex'}),
                            html.Div(id='temp-out')
                            ])
    
    return layout
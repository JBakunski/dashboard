import plotly.graph_objects as go
from dash import dcc
from dash import html

def render_tab(df):
    grouped = df[df['total_amt']>0].groupby('Store_type')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index, values=grouped.values)], layout=go.Layout(title='Udział poszczególnych kanałów w sprzedaży'))



    layout = html.Div([html.H1('Kanały sprzedaży', style={'text-align':'center'}),
                html.Div([html.Div([dcc.Graph(id='pie-prod-cat', figure=fig)],
                                    style={'width':'50%'}),
                            # html.Div([dcc.Dropdown(id='store_dropdown', options=[{'label':store_type, 'value':store_type} for store_type in df['store_type'].unique()], value=df['store_type'].unique()[0]),
                            # dcc.Graph(id='barh-prod-subcat')], style={'width':'50%'})], style={'display':'flex'}),
                            html.Div(id='temp-out')
                            ])])
    
    return layout
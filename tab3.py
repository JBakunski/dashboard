import plotly.graph_objects as go
from dash import dcc
from dash import html

def render_tab(df):
    # grouped = df[df['total_amt']>0].groupby('tran_date')['total_amt'].sum()
    # labels = grouped.index.weekday.sort_values().map({0: 'Poniedziałek',
    #                                                           1: 'Wtorek',
    #                                                           2: 'Środa',
    #                                                           3: 'Czwartek',
    #                                                           4: 'Piątek',
    #                                                           5: 'Sobota',
    #                                                           6: 'Niedziela'})
                                
    # fig = go.Figure(data=[go.Pie(labels=labels, values=grouped.values, sort=False)], layout=go.Layout(title='Udział poszczególnych kanałów w sprzedaży'))

    # print(grouped.head())
    # print(labels)

    layout = html.Div([html.H1('Kanały sprzedaży', style={'text-align':'center'}),
                html.Div([html.Div([dcc.Graph(id='pie-weekday-sales')],
                                    style={'width':'50%'}),
                            html.Div([dcc.Dropdown(id='store_dropdown', options=[{'label':store_type, 'value':store_type} for store_type in df['Store_type'].unique()], value=df['Store_type'].unique()[0]),
                            dcc.Graph(id='barh-store-subcat')], style={'width':'50%'})], style={'display':'flex'}),
                            html.Div(id='temp-out')
                            ])
    
    return layout
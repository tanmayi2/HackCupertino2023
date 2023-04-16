# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import json
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

app = Dash(__name__)

#read csv dataset into pandas dataframe
df = pd.read_csv("cuisine-32-hopefullyFinal3 - Sheet1.csv")

#map figure
fig = px.choropleth(df, locations="country",
                    color="nativeCuisine", 
                    hover_name="nativeCuisine", 
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.layout.plot_bgcolor = '#fff0d1'
fig.layout.paper_bgcolor = '#fff0d1'
fig.update_layout(
    margin=dict(l=20,r=20,t=20,b=20),
    dragmode=False,
)
fig.show()

#layout of the dashboard
app.layout = html.Div(children=[
    html.Div(id='rectangle1'),

    html.Div(
        children=html.Div([
            html.H1('I  N  F  U  S  E  D'),
        ])
    ),

    html.Div(
        children=html.Div([
            html.H2('______________'),
        ])
    ),

    html.Div(
        children=html.Div([
            html.H3('We hope to build stronger and closer communities by bringing people from different cultures together using our collective love for food.'),
        ])
    ),

    dcc.Graph(
        id='map',
        figure=fig,
        style={'width': '90vw', 'height': '70vh'},
    ),

    html.Br(),

    html.Div(
        id='output',
        children=html.Div([
        ]),
    ),
    html.Div(id='rectangle2'),
])

#callback for interactions with the map
@app.callback(
    Output('output', 'children'),
    Input('map', 'clickData'))
def display_click_data(clickData):
    if not clickData:
        return "Nothing selected"
    countryISO = json.dumps(clickData["points"][0]['location'])
    for ind in df.index:
        if df["country"][ind] == countryISO[1:-1] :
            return json.dumps(df["title"][ind] + ": " + df["instructions"][ind], indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)

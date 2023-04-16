# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("filtered_cuisines.csv")
# df = pd.read_excel("all_cuisines.xlsx", sheet_name='Sheet1', usecols=['title', 'nativeCuisine'])
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

fig = px.choropleth(df, locations="country",
                    color="nativeCuisine", # lifeExp is a column of gapminder
                    hover_name="nativeCuisine", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()

app.layout = html.Div(children=[
    html.H1(children='Dashboard Name'),

    html.Div(children='''
        We hope to build stronger communities by bringing people from different cultures together using our collective love for food.
    '''),

    dcc.Graph(
        id='map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

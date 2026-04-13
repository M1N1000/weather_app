import matplotlib.pyplot as plt
import dash
from dash import dcc, html
import plotly.express as px

# Dane
x = [1,2,3,4,5]
y1 = [10,15,13,20,17]
y2 = [3,7,4,9,6]

produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]

etykiety = ["Python","Java","C++","Javascript"]
wartosci = [40,25,15,20]

# Wykresy
fig_line = px.line(x=x, y=y1, title="Trend", markers=True)
fig_bar = px.bar(x=produkty, y=wyniki, title="Produkty")
fig_scatter = px.scatter(x=x, y=y2, title="Relacja")
fig_hist = px.histogram(x=oceny, nbins=4, title="Oceny")
fig_pie = px.pie(names=etykiety, values=wartosci, title="Języki")

# Dashboard
app = dash.Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Arial", "backgroundColor": "#f5f7fa"},
    children=[
        html.H1("Mój Dashboard", style={"textAlign": "center"}),

        html.Div([
            dcc.Graph(figure=fig_line),
            dcc.Graph(figure=fig_bar),
        ], style={"display": "flex"}),

        html.Div([
            dcc.Graph(figure=fig_scatter),
            dcc.Graph(figure=fig_hist),
        ], style={"display": "flex"}),

        html.Div([
            dcc.Graph(figure=fig_pie)
        ])
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
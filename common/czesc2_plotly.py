import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

x = [1,2,3,4,5]
y1 = [10,15,13,20,17]
y2 = [3,7,4,9,6]
godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]

produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]

etykiety = ["Python","Java","C++","Javascript"]
wartosci = [40,25,15,20]

# Tworzenie układu dashboardu
fig = make_subplots(
    rows=3, cols=2,
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "domain"}, None]  # pie chart
    ],
    subplot_titles=("Line", "Bar", "Scatter", "Histogram", "Pie")
)

# LINE
fig.add_trace(
    go.Scatter(x=x, y=y1, mode="lines+markers", name="Line"),
    row=1, col=1
)

# BAR
fig.add_trace(
    go.Bar(x=produkty, y=wyniki, orientation="h", name="Bar"),
    row=1, col=2
)

# SCATTER
fig.add_trace(
    go.Scatter(x=x, y=y2, mode="markers", name="Scatter"),
    row=2, col=1
)

# HISTOGRAM
fig.add_trace(
    go.Histogram(x=oceny, nbinsx=4, name="Histogram"),
    row=2, col=2
)

# PIE
fig.add_trace(
    go.Pie(labels=etykiety, values=wartosci, name="Pie"),
    row=3, col=1
)


# Layout
fig.update_layout(
    title="Dashboard Plotly",
    height=900,
    showlegend=False
)

fig.show()


#zad4
godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]

fig = px.scatter(x= godziny_nauki, y= wyniki,title="Godziny nauki a wyniki egazminu",
                 labels={"x":"godziny nauki","y":"wyniki"},)
fig.show()

#zad 5
jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
udzial = [35, 30, 15, 10, 10]

fig2 = px.pie(names=jezyki, values=udzial, title="Udzial")
fig2.show()

#zad6

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]
fig3 = px.line(x=dni, y=temperatura, title="Temperatura")
fig3.show()
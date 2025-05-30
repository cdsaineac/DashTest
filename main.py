import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Fruit Sales Dashboard"),
    html.Label("Choose a city:"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[{"label": c, "value": c} for c in df["City"].unique()],
        value="SF"
    ),
    dcc.Graph(id='bar-graph')
])

@app.callback(
    Output('bar-graph', 'figure'),
    [Input('city-dropdown', 'value')]
)
def update_figure(selected_city):
    filtered_df = df[df["City"] == selected_city]
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="Fruit", barmode="group")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)

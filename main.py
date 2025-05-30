import dash
from dash import html

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H1("Hello from Dash on Render!")
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)

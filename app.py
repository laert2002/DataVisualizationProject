from Phase_3 import app, df, current_price, starting_price, total_return, avg_volatility
import dash_bootstrap_components as dbc
from dash import dcc, html

# Hardcoded layout in this file to satisfy deployment structure
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("Bitcoin Price Analytics Dashboard", className="mb-0"),
                html.P("Interactive Analysis of Bitcoin Price Evolution (2010-Present)", 
                       className="text-muted")
            ], className="p-4")
        ])
    ], className="bg-light border-bottom mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Tabs(id="tabs", value="tab-1", children=[
                dcc.Tab(label=" Price Evolution", value="tab-1", children=[]),
                dcc.Tab(label=" Market Analysis", value="tab-2", children=[]),
                dcc.Tab(label=" Risk & Volatility", value="tab-3", children=[]),
            ])
        ])
    ], className="mb-4"),

    html.Div(id="page-content", className="mb-4"),

], fluid=True, className="py-4")

# Expose the Flask server for WSGI servers (gunicorn, etc.)
server = app.server

if __name__ == '__main__':
    print("Starting Dash app on http://localhost:8050/")
    app.run(debug=True, port=8050)

from dash import dcc, html
import dash_bootstrap_components as dbc
from Phase_3 import df

layout = dbc.Container([
	# Volatility Threshold Control
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Volatility Threshold (%)", className="fw-bold"),
					dcc.Slider(
						id='volatility-threshold-slider',
						min=0,
						max=10,
						step=0.5,
						value=3,
						marks={0: '0%', 5: '5%', 10: '10%'},
						tooltip={"placement": "bottom", "always_visible": True}
					)
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Statistical Summary", className="fw-bold"),
					html.Div(id='volatility-stats-text', className="mt-3")
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

	# Volatility Chart
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Daily Volatility Over Time", className="fw-bold mb-3"),
					dcc.Loading(
						id="loading-3",
						type="default",
						children=dcc.Graph(id='volatility-timeseries-chart', 
										 style={'height': '500px'})
					)
				])
			], className="shadow-sm")
		])
	], className="mb-4"),

	# Risk Analysis
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Risk Profile by Market Phase", className="fw-bold mb-3"),
					dcc.Graph(id='risk-profile-chart', style={'height': '450px'})
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Volatility Distribution", className="fw-bold mb-3"),
					dcc.Graph(id='volatility-distribution-chart', style={'height': '450px'})
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

], fluid=True)

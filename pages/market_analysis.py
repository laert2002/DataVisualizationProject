from dash import dcc, html
import dash_bootstrap_components as dbc
from Phase_3 import df

layout = dbc.Container([
	# Controls
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Moving Average Period:", className="fw-bold"),
					dcc.Slider(
						id='ma-period-slider',
						min=7,
						max=120,
						step=1,
						value=30,
						marks={7: '7', 30: '30', 60: '60', 120: '120'},
						tooltip={"placement": "bottom", "always_visible": True}
					)
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Volume Aggregation:", className="fw-bold"),
					dcc.Dropdown(
						id='volume-agg-dropdown',
						options=[
							{'label': 'Daily', 'value': 'daily'},
							{'label': 'Weekly', 'value': 'weekly'},
							{'label': 'Monthly', 'value': 'monthly'}
						],
						value='daily',
						clearable=False
					)
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

	# Volume and Price Chart
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Volume & Price Momentum", className="fw-bold mb-3"),
					dcc.Loading(
						id="loading-2",
						type="default",
						children=dcc.Graph(id='volume-price-chart', 
										 style={'height': '500px'})
					)
				])
			], className="shadow-sm")
		])
	], className="mb-4"),

	# Phase Analysis
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Market Phase Comparison", className="fw-bold mb-3"),
					dcc.Graph(id='phase-comparison-chart', style={'height': '450px'})
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Volatility Trends by Year", className="fw-bold mb-3"),
					dcc.Graph(id='volatility-by-year-chart', style={'height': '450px'})
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

], fluid=True)

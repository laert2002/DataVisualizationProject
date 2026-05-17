from dash import dcc, html
import dash_bootstrap_components as dbc
from Phase_3 import df, current_price, starting_price, total_return, avg_volatility, category_colors

layout = dbc.Container([
	# KPI Cards
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H6("Current Price", className="text-muted small"),
					html.H3(f"${current_price:,.2f}", className="text-primary fw-bold"),
					html.P(f"as of {df['Date'].iloc[-1].strftime('%Y-%m-%d')}", 
						   className="text-muted small mb-0")
				])
			], className="shadow-sm")
		], md=3),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H6("Total Return", className="text-muted small"),
					html.H3(f"{total_return:,.1f}%", 
						   className=f"fw-bold {'text-success' if total_return > 0 else 'text-danger'}"),
					html.P(f"from ${starting_price:.4f}", className="text-muted small mb-0")
				])
			], className="shadow-sm")
		], md=3),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H6("Avg Volatility", className="text-muted small"),
					html.H3(f"{avg_volatility:.2f}%", className="text-warning fw-bold"),
					html.P("30-day rolling average", className="text-muted small mb-0")
				])
			], className="shadow-sm")
		], md=3),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H6("Data Points", className="text-muted small"),
					html.H3(f"{len(df):,}", className="text-info fw-bold"),
					html.P(f"{(df['Date'].max() - df['Date'].min()).days} trading days", 
						   className="text-muted small mb-0")
				])
			], className="shadow-sm")
		], md=3),
	], className="mb-4"),

	# Controls
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Select Date Range:", className="fw-bold"),
					dcc.DatePickerRange(
						id='date-range-picker',
						start_date=df['Date'].min(),
						end_date=df['Date'].max(),
						display_format='YYYY-MM-DD',
						className="w-100"
					)
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.Label("Filter by Price Phase:", className="fw-bold"),
					dcc.Dropdown(
						id='phase-filter',
						options=[{'label': 'All Phases', 'value': 'all'}] + 
							   [{'label': phase, 'value': phase} 
								for phase in df['PriceCategory'].unique()],
						value='all',
						clearable=False
					)
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

	# Main Price Chart
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					dcc.Loading(
						id="loading-1",
						type="default",
						children=dcc.Graph(id='price-evolution-chart', 
										 style={'height': '500px'})
					)
				])
			], className="shadow-sm")
		])
	], className="mb-4"),

	# Additional Metrics
	dbc.Row([
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Price Statistics", className="fw-bold mb-3"),
					dcc.Graph(id='price-stats-chart', style={'height': '400px'})
				])
			], className="shadow-sm")
		], md=6),
		dbc.Col([
			dbc.Card([
				dbc.CardBody([
					html.H5("Daily Returns Distribution", className="fw-bold mb-3"),
					dcc.Graph(id='returns-distribution-chart', style={'height': '400px'})
				])
			], className="shadow-sm")
		], md=6),
	], className="mb-4"),

], fluid=True)

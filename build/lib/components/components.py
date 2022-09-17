from dash import html, dcc, Input, Output, callback
from datetime import datetime
import dash_bootstrap_components as dbc


def app_heading(heading):
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(heading,
                        className="app-heading fs1",
                         ), width=12,
            ),
        ]),
    ])


def page_heading(heading):
    return dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(heading, className="page-heading fs2"),
                width=12,
            ),
        ]),
    ])


def footer():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Span([
                    html.Span("date:", className="footer-constant"),
                    html.Span("", id="footer-date"),
                ])
            ], className="footer-column", width={"size": "4"}),
            dbc.Col([
                html.Span([
                    html.Span("status:", className="footer-constant"),
                    html.Span("", id="footer-status")
                ], className="status")
            ], className="footer-column", width={"size": "6"}),
        ], className="rounded footer"),
        dcc.Interval(
            id='interval-component',
            interval=1*1000*60,  # 1 minute in milliseconds
            n_intervals=0
        )
    ])


@callback(
    Output(component_id="footer-date", component_property="children"),
    Input(component_id="interval-component", component_property="n_intervals"))
def update_date_time(value):
    dt = datetime.now()
    current_time = dt.strftime("%m/%d/%Y %H:%M")
    return current_time

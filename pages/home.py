import dash
from dash import dcc, Output, Input, State, ctx
import dash_bootstrap_components as dbc
from datetime import date
import json
from components import components, utilities
import pages.home_fns

dash.register_page(__name__, path='/')

home = pages.home_fns.home

page_settings = utilities.get_page_settings(
    utilities.get_module_name(__file__))
layout = dbc.Container([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                components.page_heading(page_settings["page_heading"]),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Row(
                    dbc.Col(
                        dbc.Container(className="text-center", children=[
                            dcc.DatePickerSingle(
                                id='date_id',
                                min_date_allowed=date(2022, 1, 1),
                                max_date_allowed=date.today(),
                                initial_visible_month=utilities.get_start_date(),
                                date=utilities.get_start_date()
                            )]
                        ), width=12,
                    ),
                ),

                dbc.Row(
                    dbc.Col(
                        dcc.Loading(
                            children=[dcc.Graph(id="graph")],
                            color="#119DFF", type="dot", fullscreen=True
                        )
                    )
                ),
                dcc.Interval(
                    id='home-interval-component',
                    interval=2*1000*60,  # in milliseconds
                    n_intervals=0),
                components.footer("home"),
            ]),
        ]),
    ], className="page-frame rounded"),
])

# @dash.callback(
#     Output(component_id="session", component_property="data"),
#     Input(component_id="dummy", component_property="value")
# )
# def update_session(data, input_value):
#           return utilities.get_start_date()

# def update_table(data, input_value):
#    return data

@dash.callback(
    Output(component_id="graph", component_property="figure"),
    Output(component_id="session", component_property="data"),
    Output("footer-status", "children"),
    Output("footer-message", "children"),
    Input(component_id="date_id", component_property="date"),
    State(component_id="session", component_property="data"),
    Input(component_id="home-interval-component", component_property="n_intervals"))
def update_line_chart(value, session, interval):
    value = value.replace("-","")
    ctx_message  = json.dumps({
        "states": ctx.states,
        'triggered': ctx.triggered,
        "inputs": ctx.inputs,
    }, indent=2)

    print(ctx_message)
    home.start_date = value
    return home.update_line_chart(value, session, interval)

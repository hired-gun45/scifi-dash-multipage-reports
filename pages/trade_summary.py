import dash
from dash import html, dash_table, Output, Input, State, callback
import dash_bootstrap_components as dbc
from components import components, utilities

dash.register_page(__name__, path='/trade_summary')

page_settings = utilities.get_page_settings(
    utilities.get_module_name(__file__))
layout = dbc.Container([
    dbc.Row([
            dbc.Col(
                components.page_heading(page_settings["page_heading"]),
            ),
   ]),
    dbc.Row(
        dbc.Col(
            html.Div([
                dash_table.DataTable(
                    id='data_table',
                    style_table={
                        'fontSize':11,
                    },                )
            ]),className="text-center", width="auto"
        ),justify="center",
    ),
    dbc.Input(id="dummy", type="text",style={"display":"none"}),
    components.footer("trade_summary"),
])

@dash.callback(
    Output(component_id="data_table", component_property="data"),
    #Output(component_id="footer-status", component_property="children"),
    State(component_id="session", component_property="data"),
    Input(component_id="dummy", component_property="value")
)
# def update_table(data, input_value):
#      return data, "Ok"
def update_table(data, input_value):
   return data
from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from components import components, utilities
import os

app = Dash(__name__, external_stylesheets=[
           dbc.themes.JOURNAL], use_pages=True)
page_name = os.path.basename(__file__).replace(".py", "")
settings = utilities.get_settings()

app.layout = dbc.Container(children=[

    html.Div([
        dbc.Row(
            dbc.Col(
                html.Div([
                    components.app_heading(settings["app"]["app_heading"]),
                ]),
            ), style={"marginLeft":"15px","marginRight":"15px"}
        ),

        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        dcc.Link(
                            f"{page['name']}", href=page["relative_path"],
                            className="page-links",
                        )
                        for page in dash.page_registry.values()
                    ], className="page-links-container fw-bold"

                ),
            )
        ),
    ], className="head-container rounded"),
    dcc.Store(id="session", data=utilities.get_start_date(), storage_type='session'),
    dash.page_container
], style={"marginTop": "15px"})

if __name__ == '__main__':
    app.run_server(debug=True)

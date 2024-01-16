
import dash_ag_grid as dag
from dash import Dash, html, callback, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch-theme-change", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

app.layout = html.Div(
    [
        color_mode_switch,
        dag.AgGrid(
            id="grid-theme-change",
            columnDefs=[{"field": i} for i in df.columns],
            rowData=df.to_dict("records"),
        ),
    ],
)

@callback(
    Output("grid-theme-change", "className"),
    Input("switch-theme-change", "value")
)
def change_theme(value):
    if value:
        return "ag-theme-alpine"
    return "ag-theme-alpine-dark"


if __name__ == "__main__":
    app.run(debug=True)

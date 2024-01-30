
import dash_ag_grid as dag
from dash import Dash, html, callback, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")


heading = html.Div("My Cool App", className="bg-primary text-white p-2 h4")
color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch2"),
        dbc.Switch( id="switch-theme2", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch2"),
    ]
)

grid1 = dag.AgGrid(
    id="grid1",
    className="no-theme",
    columnDefs=[{"field": i} for i in df.columns],
    rowData=df.to_dict("records"),
)


grid2 = dag.AgGrid(
    id="grid2",
    className="no-theme my-5",
    columnDefs=[{"field": i} for i in df2.columns],
    rowData=df2.to_dict("records"),
)


app.layout = dbc.Container(
    [
        heading,
        color_mode_switch,
        grid1,
        grid2

    ],
    className="ag-theme-quartz",
    id="container"
)

@callback(
    Output("container", "className"),
    Input("switch-theme2", "value")
)
def change_theme(value):
    if value:
        return "ag-theme-quartz"
    return "ag-theme-quartz-dark"


if __name__ == "__main__":
    app.run(debug=True)

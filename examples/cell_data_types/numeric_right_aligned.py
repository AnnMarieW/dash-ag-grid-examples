import dash
import dash_ag_grid as dag
from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px

app = Dash(__name__)

datasets = {
    "gapminder": px.data.gapminder(),
    "tips": px.data.tips(),
    "iris": px.data.iris(),
    "stocks": px.data.stocks(),
}

dataTypeDefinitions = {
    "number": {
        "baseDataType": "number",
        "extendsDataType": "number",
        "columnTypes": "rightAligned",
        "appendColumnTypes": True
    },
}

app.layout = html.Div(
    [
        html.Label("Select Dataset:", htmlFor="select-cell-data-types-numeric"),
        dcc.Dropdown(list(datasets), value="gapminder", id="select-cell-data-types-numeric", className="mb-4"),
        dag.AgGrid(
            id="grid-cell-data-types-numeric",
            dashGridOptions={"dataTypeDefinitions":  dataTypeDefinitions},
            columnSize="sizeToFit",
            columnSizeOptions={'defaultMinWidth': 125}

        ),
    ],
)

@callback(
    Output("grid-cell-data-types-numeric", "rowData"),
    Output("grid-cell-data-types-numeric", "columnDefs"),
    Input("select-cell-data-types-numeric", "value"),
)
def update(value):
    if value is None:
        return dash.no_update
    rowData = datasets[value].to_dict("records")
    columnDefs = [{"field": i} for i in datasets[value].columns]
    return rowData, columnDefs


if __name__ == "__main__":
    app.run(debug=True)
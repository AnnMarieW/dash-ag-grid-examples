import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd
import plotly.express as px


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv"
)
df2 = px.data.gapminder()


app = Dash()


def make_grid(df, id="grid", columnDefs=None, editable=True):
    if columnDefs is None:
        columnDefs = [{"field": i} for i in df.columns]
    dataTypeDefinitions = {
        "number": {
            "baseDataType": "number",
            "extendsDataType": "number",
            "columnTypes": ["numberColumn", "rightAligned"],
            "appendColumnTypes": True,
            "valueFormatter": {
                "function": "params.value == null ? 'NaN' : String(params.value)"
            },
        },
        "money": {
            "baseDataType": "number",
            "extendsDataType": "number",
            "valueFormatter": {"function": "d3.format('($,.2f')(params.value)"},
        },
        "pct": {
            "baseDataType": "number",
            "extendsDataType": "number",
            "valueFormatter": {"function": "d3.format(',.1%')(params.value)"},
        },
    }

    return dag.AgGrid(
        id=id,
        rowData=df.to_dict("records"),
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        columnSizeOptions={"defaultMinWidth": 120},
        defaultColDef={
            "editable": editable,
            "filter": True,
            "filterParams": {
                "buttons": ["apply", "reset"],
                "closeOnApply": True,
            },
        },
        dashGridOptions={
            "dataTypeDefinitions": dataTypeDefinitions,
            "undoRedoCellEditing": True,
            "animateRows": False,
            "pagination": True,
            "columnTypes": {
                "numberColumn": {"cellEditorParams": {"showStepperButtons": True}}
            },
        },
    )


app.layout = html.Div(
    [
        make_grid(df),
        html.Div("Grid 2 with customized columns", className="mt-4"),
        make_grid(
            df2,
            id="grid2",
            columnDefs=[{"field": i} for i in ["country", "continent", "year", "lifeExp"]]
            + [{"field": "gdpPercap", "cellDataType": "money"}],
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

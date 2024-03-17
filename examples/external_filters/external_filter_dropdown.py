import dash_ag_grid as dag
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
years = sorted(df.year.unique())


app.layout = html.Div(
    [
        html.Label("Select Year"),
        dcc.Dropdown(
            years,
            value=years,
            multi=True,
            style={"marginBottom": 5},
            id="dd-external-filter",
        ),
        dag.AgGrid(
            columnDefs=[{"field": i} for i in ["year", "athlete", "country", "sport", "total"]],
            rowData=df.to_dict("records"),
            defaultColDef={"flex": 1, "minWidth": 150, "filter": True, "floatingFilter": True},
            id="grid-dd-external-filter",
        ),
    ]
)



@callback(
    Output("grid-dd-external-filter", "dashGridOptions"),
    Input("dd-external-filter", "value"),
)
def update_rows(value):
    return {
        "isExternalFilterPresent": {"function": "false" if value is None or value == [] else "true"},
        "doesExternalFilterPass": {"function": f"{value}.includes(params.data.year)"}
    }


if __name__ == "__main__":
    app.run(debug=True)

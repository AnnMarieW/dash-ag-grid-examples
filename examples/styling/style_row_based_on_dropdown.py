
from dash import Dash, html, dcc, callback, Input, Output
import dash_ag_grid as dag
import pandas as pd

rowData = [
    {"Firm": "Acme", "2022": 4},
    {"Firm": "Olive", "2022": 3},
    {"Firm": "Barnwood", "2022": 6},
    {"Firm": "Henrietta", "2022": -6},
]
df = pd.DataFrame(rowData)


app = Dash(__name__)

dropdown = dcc.Dropdown([1, 2, 3, 4, 15], id="dropdown", value=3)
grid = dag.AgGrid(
    id="grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": c} for c in df.columns],
    defaultColDef={"filter": True},
    columnSize="sizeToFit",
)

app.layout = html.Div(["Highlight values greater than:", dropdown, grid])


@callback(Output("grid", "getRowStyle"), Input("dropdown", "value"))
def update_style(X):
    return {
        "styleConditions": [
            {
                "condition": f"params.data['2022'] > {X}",
                "style": {"backgroundColor": "green"},
            },

        ],
    }


if __name__ == "__main__":
    app.run(debug=True)
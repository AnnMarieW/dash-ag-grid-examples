import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv"
)
df["original_company"] = df["company"]
df["original_mission"] = df["mission"]


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[
                {
                    "field": "company",
                    "tooltipValueGetter": {
                        "function": "params.data.company === params.data.original_company ? '' : 'original value: ' + params.data.original_company"
                    },
                    "editable": True,
                },
                {
                    "field": "mission",
                    "tooltipValueGetter": {
                        "function": "params.data.mission === params.data.original_mission ? '' : 'original value: ' + params.data.original_mission"
                    },
                    "editable": True,
                },
                {"field": "price"},
                {"field": "successful"},
            ],
            columnSize="sizeToFit",
            dashGridOptions={
                "tooltipShowDelay": 0,
                "tooltipInteraction": True,
                "undoRedoCellEditing": True,
            },
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)

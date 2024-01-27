
import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[
                {
                    "field": "company",
                    "headerTooltip": f"This is the Company column",
                    "tooltipValueGetter": {"function": "'Location: ' + params.data.location"}
                },
                {
                    "field": "mission",
                    "tooltipValueGetter": {"function": "(params.data.successful) ? 'Mission Successful!': ''"},
                },
                {
                    "field": "price",
                    "tooltipValueGetter": {"function": "d3.format('$,.0f')(params.value)"},
                },
                {
                    "field": "date",
                    "tooltipValueGetter": {"function": "'This is the mission date'"},
                },
                {
                    "field": "time",
                    "tooltipValueGetter": {"function": "params.value ? '' : 'No time provided'"},
                    "editable": True,
                },
                {
                    "field": "successful",
                    "editable": True,
                }
            ],

            dashGridOptions={
                "tooltipShowDelay":0,
                "tooltipInteraction": True,
            },
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)


import dash_ag_grid as dag
from dash import Dash, html, callback, Input, Output
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

# function to create a date object from  a date string "YYYY-MM-DD"
date_object = "d3.timeParse('%Y-%m-%d')(params.data.date)"

columnDefs = [
    {
      "field": "mission",
      "width": 150,
      "checkboxSelection": True,
      "lockPosition": "left"
    },
    {
      "field": "company",
      "width": 130,
      "cellRenderer": "CompanyLogoRenderer"
    },
    {
      "field": "location",
      "width": 225
    },
    {
      "field": "date",
      "valueFormatter": {"function": f"d3.timeFormat('%b %d, %Y')({date_object})"},
    },
    {
      "field": "price",
      "width": 130,
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('$,.0f')(params.value)"},
    },
    {
      "field": "successful",
      "width": 120,
    },
    { "field": "rocket" },
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="grid-v31-tutorial",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef={"filter": True, "editable": True},
            dashGridOptions={
                "rowSelection": "multiple",
                "suppressRowClickSelection": True,
                "animateRows": False,
                "pagination": True,

            },
        ),
        html.Div(id="container-v31-tutorial")
    ],
)


@callback(
    Output("container-v31-tutorial", "children"),
    Input("grid-v31-tutorial", "cellValueChanged"),
)
def output_selected_rows(changed):
    if not changed:
        return "No changes"
    return f"Changed: {changed}"


if __name__ == "__main__":
    app.run(debug=True)

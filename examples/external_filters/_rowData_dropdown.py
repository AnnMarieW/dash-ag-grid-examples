import dash_ag_grid as dag
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


app.layout = html.Div(
    [
        html.Label("Select Year"),
        dcc.Dropdown(
            sorted(df.year.unique()),
            value=sorted(df.year.unique()),
            multi=True,
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
    Output("grid-dd-external-filter", "rowData"),
    Input("dd-external-filter", "value"),
)
def update_rows(value):
    if value is None or value == []:
        return df.to_dict("records")

    dff = df[df['year'].isin(value)]
    return dff.to_dict("records")


if __name__ == "__main__":
    app.run(debug=True)

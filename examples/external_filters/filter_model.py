import dash_ag_grid as dag
from dash import Dash, dcc, html, callback, Input, Output, State
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
years = sorted(df.year.unique())


columnDefs = [
    {"field": "year", "filterParams": {"maxNumConditions": 7}}
] + [{"field": i} for i in ["athlete", "country", "sport", "total"]]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
    "floatingFilter": True
}

app.layout = html.Div(
    [
        html.Label("Select Year"),
        dcc.Dropdown(
            years,
            value=years,
            multi=True,
            clearable=False,
            id="dd-filter-model-multiple-conditions2",
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            id="grid-filter-model-multiple-conditions2",
            filterModel={},
        ),
    ]
)


@callback(
    Output("grid-filter-model-multiple-conditions2", "filterModel"),
    Input("dd-filter-model-multiple-conditions2", "value"),
    State("grid-filter-model-multiple-conditions2", "filterModel"),
)
def update_filter_model(selected_years, model):
    model["year"] = {
        "filterType": "number",
        "operator": "OR",
        "conditions": [
            {"filterType": "number", "type": "equals", "filter": year}
            for year in selected_years
        ],
    }
    return model


if __name__ == "__main__":
    app.run(debug=True)

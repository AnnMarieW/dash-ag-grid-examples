
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)


columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
    {"headerName": "Sale Price", "field": "sale", "hide": True},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000, "sale": 33000},
    {"make": "Ford", "model": "Mondeo", "price": 32000, "sale": 29000},
    {"make": "Porsche", "model": "Boxster", "price": 72000, "sale": 69000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Customizing CSV Exports with `shouldRowBeSkipped` and formatted with `processCellCallback` "
        ),
        html.Button("Download CSV", id="btn-csv-export-params", n_clicks=0),
        dag.AgGrid(
            id="grid-csv-export-params",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
            csvExportParams={
                "fileName": "ag_grid_test.csv",
                "shouldRowBeSkipped":{"function": "shouldRowBeSkipped(params)"},
                "processCellCallback": {"function": "processCellCallback(params)"}
            },
        ),
    ]
)


@app.callback(
    Output("grid-csv-export-params", "exportDataAsCsv"),
    Input("btn-csv-export-params", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True
    return False


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Add this to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


dagfuncs.shouldRowBeSkipped = (params) => {
    return params.node.data.make == "Ford"
}

dagfuncs.processCellCallback = (params) => {    
    return params.column.colDef.field == 'price'? '$' + params.value : params.value
}

"""

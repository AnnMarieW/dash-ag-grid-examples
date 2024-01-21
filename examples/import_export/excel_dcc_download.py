

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
df = df.head(10)

app.layout = dbc.Container(
    [
        dcc.Download(id="download-excel1"),

        dbc.Label("Excel File Name ", html_for="excel-file-name"),
        dbc.Input(id="excel-file-name", value="ag_grid_download.xlsx"),
        dbc.Button("Export to Excel", id="btn-excel-export1", className="my-2"),

        dag.AgGrid(
            id="grid-excel-export1",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": c} for c in df.columns],
        ),
    ], fluid=True
)

@app.callback(
    Output('download-excel1', 'data'),
    Input('btn-excel-export1', 'n_clicks'),
    State('excel-file-name', 'value'),
    State('grid-excel-export1', "virtualRowData"),
    prevent_initial_call=True
)
def export_data_to_excel(n, filename, data):
    dff = pd.DataFrame(data)
    return dcc.send_data_frame(dff.to_excel, filename, sheet_name="Sheet1")


if __name__ == "__main__":
    app.run(debug=True)

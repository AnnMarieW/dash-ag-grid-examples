

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd


app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
).head(50)

columnDefs = [
    {
        "headerName": "Athlete Details",
        "children": [
            {"field": "athlete", "width": 180},
            {"field": "age", "width": 90},
            {"field": "country", "width": 140},
        ],
    },
    {
        "headerName": "Sports Results",
        "children": [
            {"field": "sport", "width": 140},
            {"field": "total", "width": 100, "filter": "agNumberColumnFilter", "columnGroupShow": "closed"},
            {"field": "gold", "width": 100, "filter": "agNumberColumnFilter", "columnGroupShow": "open"},
            {"field": "silver", "width": 100, "filter": "agNumberColumnFilter", "columnGroupShow": "open"},
            {"field": "bronze", "width": 100, "filter": "agNumberColumnFilter", "columnGroupShow": "open"},
        ],
    },
]

app.layout = html.Div(
    [
        dcc.Download(id="download-excel3"),
        html.Button("Export to Excel", id="btn-excel-export3"),
        dag.AgGrid(
            id="grid-excel-export3",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={ "filter": True},
        ),
    ]
)

@app.callback(
    Output('download-excel3', 'data'),
    Input('btn-excel-export3', 'n_clicks'),
    State("grid-excel-export3", "virtualRowData"),
    prevent_initial_call=True
)
def export_data_to_excel(n, rows):
    dff=pd.DataFrame(rows)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('new_excel_file.xlsx')

    # Write each dataframe to a different worksheet.
    for sport in dff.sport.unique():
        dff1 =  dff[dff.sport==sport]
        dff1.to_excel(writer,sheet_name=sport)

    # Close the Pandas Excel writer and output the Excel file.
    writer.close()

    return dcc.send_file('new_excel_file.xlsx')


if __name__ == "__main__":
    app.run(debug=True)

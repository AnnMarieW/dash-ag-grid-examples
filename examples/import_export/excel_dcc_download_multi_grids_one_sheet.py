from dash import Dash, dcc, html, Input, Output, State
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

df1 = px.data.tips().head(10)
df2 = px.data.wind().head(10)

app = Dash(__name__)

grid1 = dag.AgGrid(
    id="grid-excel-export2a",
    rowData=df1.to_dict("records"),
    columnDefs=[{"field": c} for c in df1.columns],
    defaultColDef={"filter": True,  "editable": True},
    columnSize="sizeToFit",
)

grid2 = dag.AgGrid(
    id="grid-excel-export2b",
    rowData=df2.to_dict("records"),
    columnDefs=[{"field": c} for c in df2.columns],
    defaultColDef={"filter": True,  "editable": True},
    columnSize="sizeToFit",
)

app.layout = html.Div(
    [
        dcc.Download(id="download-excel2"),
        html.Button("Export grids to Excel", id="btn-excel-export2"),
        grid1, grid2
    ]
)


@app.callback(
    Output('download-excel2', 'data'),
    Input('btn-excel-export2', 'n_clicks'),
    State('grid-excel-export2a', 'virtualRowData'),
    State('grid-excel-export2b', 'virtualRowData'),
    prevent_initial_call=True
)
def export_data_to_excel(n,rowData1, rowData2):
    dff1 = pd.DataFrame(rowData1)
    dff2 = pd.DataFrame(rowData2)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('new_excel_file.xlsx')

    # Write each dataframe to the same sheet
    dff1.to_excel(writer,sheet_name="grids")
    dff2.to_excel(writer, sheet_name="grids", startrow=len(dff1) + 5)

    # Close the Pandas Excel writer and output the Excel file.
    writer.close()

    return dcc.send_file('new_excel_file.xlsx')


if __name__ == "__main__":
    app.run(debug=True)


import dash_ag_grid as dag
from dash import Dash, html, Input, Output, clientside_callback
import random
import pandas as pd

print("dash-ag-grid version: ", dag.__version__)
print("AG Grid version: ", dag.grid_version)

df = pd.DataFrame({
    'a': [random.randint(0, 10000) for _ in range(20)],
    'b': [random.randint(0, 10000) for _ in range(20)],
    'c': [random.randint(0, 10000) for _ in range(20)],
    'd': [0] * 20,
    'e': [0] * 20,
    'f': [0] * 20
})


app = Dash()

app.layout = html.Div(
    [
        html.Button("Update Some Data", id="btn-flash-update-custom"),
        html.Button("Flash Two Rows", id="btn-flash-rows-custom"),


        dag.AgGrid(
            id="grid-flash-cells-custom",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i } for i in df.columns],
            defaultColDef={"flex": 1,"cellClass": 'align-right', "enableCellChangeFlash": True},
            dashGridOptions={"cellFlashDelay": 2000, "cellFadeDelay": 500}

        )
    ], className="flash",
)

# Update some data
clientside_callback(
    """async (n) => {
        if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells-custom")

            var rowCount = gridApi.getDisplayedRowCount();        
            // pick 20 cells at random to update
            for (var i = 0; i < 20; i++) {
              var row = Math.floor(Math.random() * rowCount);
              var rowNode = gridApi.getDisplayedRowAtIndex(row);
              var col = ['a', 'b', 'c', 'd', 'e', 'f'][i % 6];
              rowNode.setDataValue(col, Math.floor(Math.random() * 10000));
            }        
        }
        return dash_clientside.no_update
    }""",
    Output("btn-flash-update-custom", "id"),
    Input("btn-flash-update-custom", "n_clicks"),
)


# Flash 2 rows
clientside_callback(
    """async  (n) =>  {
        if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells-custom")

            // pick row 4 and 5
            var rowNode1 = gridApi.getDisplayedRowAtIndex(4);
            var rowNode2 = gridApi.getDisplayedRowAtIndex(5);
            
            // flash whole row, so leave column selection out
            gridApi.flashCells({ 
              rowNodes: [rowNode1, rowNode2],  
              flashDelay: 3000,
              fadeDelay: 2000, 
            });
        }
        return dash_clientside.no_update
    }""",
    Output("btn-flash-rows-custom", "id"),
    Input("btn-flash-rows-custom", "n_clicks"),
)


if __name__ == "__main__":
    app.run(debug=True)
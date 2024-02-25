
import dash_ag_grid as dag
from dash import Dash, html, Input, Output, clientside_callback
import random
import pandas as pd


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
        html.Button("Update Some Data", id="btn-flash-update"),
        html.Button("Flash One Cell", id="btn-flash-cell"),
        html.Button("Flash Two Rows", id="btn-flash-rows"),
        html.Button("Flash Two Columns", id="btn-flash-cols"),

        dag.AgGrid(
            id="grid-flash-cells",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i } for i in df.columns],
            defaultColDef={"flex": 1,"cellClass": 'align-right', "enableCellChangeFlash": True}

        )
    ]
)

# Update some data
clientside_callback(
    """async (n) => {
        if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells")

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
    Output("btn-flash-update", "id"),
    Input("btn-flash-update", "n_clicks"),
)


# Flash cell
clientside_callback(
    """async  (n) => {
        if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells")
            
            // flash row 4 col 'c'
            var rowNode = gridApi.getDisplayedRowAtIndex(4);
            gridApi.flashCells({ rowNodes: [rowNode], columns: ['c'] });
        }
        return dash_clientside.no_update
    }""",
    Output("btn-flash-cell", "id"),
    Input("btn-flash-cell", "n_clicks"),
)

# Flash 2 rows
clientside_callback(
    """async (n) => {
        if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells")

            // pick row 4 and 5
            var rowNode1 = gridApi.getDisplayedRowAtIndex(4);
            var rowNode2 = gridApi.getDisplayedRowAtIndex(5);
            
            // flash whole row, so leave column selection out
            gridApi.flashCells({ rowNodes: [rowNode1, rowNode2] });
        }
        return dash_clientside.no_update
    }""",
    Output("btn-flash-rows", "id"),
    Input("btn-flash-rows", "n_clicks"),
)


# Flash 2 columns
clientside_callback(
    """async (n) => {
         if (n) {
           const gridApi = await dash_ag_grid.getApiAsync("grid-flash-cells");
           gridApi.flashCells({ columns: ['c', 'd'] });
        }
        return dash_clientside.no_update;
    }""",
    Output("btn-flash-cols", "id"),
    Input("btn-flash-cols", "n_clicks"),
)


if __name__ == "__main__":
    app.run(debug=True)
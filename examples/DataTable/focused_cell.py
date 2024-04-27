from dash import Dash, dcc, Input, Output, State, callback, clientside_callback
import dash_ag_grid as dag
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Store(id="focused_cell_store", data={}),
    dbc.Label('Click on cell or use keyboard to navigate'),
    dag.AgGrid(rowData=df.to_dict('records'), columnDefs=[{"field": i} for i in df.columns], id='focused_cell_grid'),
    dbc.Alert(id='focused_cell_container'),
])

@callback(Output('focused_cell_container', 'children'), Input('focused_cell_store', 'data'))
def update_graphs(focused_cell):
    return f"Focussed cell (or last focussed cell if the grid lost focus): {focused_cell}"



clientside_callback(
    """
    async function focusOnCell(id, storeId) {
        const gridApi = await dash_ag_grid.getApiAsync(id);
        gridApi.addEventListener("cellFocused", (e) => {        
            const row = e.api.getDisplayedRowAtIndex(e.rowIndex)
            const cellValue = e.api.getValue(e.column, row)            
            const focusData = {'value': cellValue, 'colId': e.column.colId, 'rowIndex': e.rowIndex}
            
             // Update dcc.Store with focusData
            dash_clientside.set_props(storeId, {data: focusData})           
        });
        return window.dash_clientside.no_update;
    }
    """,
    Output('focused_cell_grid', 'id'),
    Input('focused_cell_grid', 'id'),
    State("focused_cell_store", 'id')
)


if __name__ == "__main__":
    app.run(debug=True)
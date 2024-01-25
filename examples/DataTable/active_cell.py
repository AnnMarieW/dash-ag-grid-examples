from dash import Dash, Input, Output, callback, clientside_callback
import dash_ag_grid as dag
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dag.AgGrid(rowData=df.to_dict('records'), columnDefs=[{"field": i} for i in df.columns], id='grid2'),
    dbc.Alert(id='grid_out2'),
])

@callback(Output('grid_out2', 'children'), Input('grid2', 'cellClicked'))
def update_graphs(cell_clicked):
    return str(cell_clicked) if cell_clicked else "Click the grid"



clientside_callback(
    """
    async function focusOnCell(id) {
        const gridApi = await dash_ag_grid.getApiAsync(id);
        gridApi.addEventListener("cellFocused", (event) => {
            document.querySelector(`#${id} div.ag-cell-focus`).click();
        });
        return window.dash_clientside.no_update;
    }
    """,
    Output('grid2', 'id'),
    Input('grid2', 'id')
)


if __name__ == "__main__":
    app.run(debug=True)
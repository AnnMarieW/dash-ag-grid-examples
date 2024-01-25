from dash import Dash, Input, Output, callback
import dash_ag_grid as dag
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dag.AgGrid(rowData=df.to_dict('records'), columnDefs=[{"field": i} for i in df.columns], id='grid'),
    dbc.Alert(id='grid_out'),
])

@callback(Output('grid_out', 'children'), Input('grid', 'cellClicked'))
def update_graphs(cell_clicked):
    return str(cell_clicked) if cell_clicked else "Click the grid"

if __name__ == "__main__":
    app.run(debug=True)
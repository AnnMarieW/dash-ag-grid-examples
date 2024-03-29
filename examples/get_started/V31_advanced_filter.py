

import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")

app.layout = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"filter": True},
    dashGridOptions={"enableAdvancedFilter": True},
    enableEnterpriseModules=True,
   # licenseKey= enter your license key here
)


if __name__ == "__main__":
    app.run(debug=True)

from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

rowData = [
    {"Firm": "Acme",  "2021": 10, "2022": 14},
    {"Firm": "Olive", "2021": 13, "2022": 33},
    {"Firm": "Barnwood", "2021": 3, "2022": 1},
    {"Firm": "Henrietta", "2021": -5, "2022": -3},
]
df = pd.DataFrame(rowData)

getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.data['2022'] > params.data['2021']",
            "style": {"backgroundColor": "#3D9970"},
        },
        {
            "condition": "params.data['2022'] <= params.data['2021']",
            "style": {"backgroundColor": "#cd0200"},
        },
    ]
}


app = Dash(__name__)

grid = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{ 'field': c } for c in df.columns],
    getRowStyle=getRowStyle,
    columnSize="sizeToFit"
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
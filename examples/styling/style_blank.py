from dash import Dash, html
import pandas as pd
import numpy as np
import dash_ag_grid as dag

data_with_none = [
    {"Firm": "Acme", "2017": "", "2018": 5, "2019": 10, "2020": 4},
    {"Firm": "Olive", "2017": None, "2018": 3, "2019": 13, "2020": 3},
    {"Firm": "Barnwood", "2017": np.nan, "2018": 7, "2019": 3, "2020": 6},
    {"Firm": "Henrietta", "2017": 14, "2018": 1, "2019": 13, "2020": 1},
]
df = pd.DataFrame(data_with_none)

app = Dash(__name__)


cellStyle = {
    "styleConditions": [
        {
            "condition": "params.value === '' || params.value === null",
            "style": {"backgroundColor": "#FF4136"},
        }
    ]
}

app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[
                {
                    "field": i,
                }
                for i in df.columns
            ],
            defaultColDef={"cellStyle": cellStyle, "editable": True},
            columnSize="sizeToFit",
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

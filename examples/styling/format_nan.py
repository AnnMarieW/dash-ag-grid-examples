from dash import Dash,  html
import pandas as pd
import numpy as np
import dash_ag_grid as dag

data_with_none = [
    {'Firm': 'Acme', '2017': '', '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': None, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': np.NaN, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': "zero", '2018': 1, '2019': 13, '2020': 1},
]
df = pd.DataFrame(data_with_none)

app = Dash(__name__)

app.layout = html.Div([
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[
            {'field': "Firm" },
            {"field": '2017', "valueFormatter": {"function": "formatNaN(params.value)"}},
            {"field": "2018"}
        ],
        defaultColDef={"editable": True},
        columnSize="sizeToFit",
    )
])

if __name__ == '__main__':
    app.run(debug=True)


"""
Put the following in the dashAgGridFunctions.js file in /assets:

----------

dagfuncs.formatNaN = function (val) {
    return isNaN(val) ? 'N/A' : (val === '' ? 'None' : val);
};
"""
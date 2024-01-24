
from dash import Dash
import pandas as pd
import dash_ag_grid as dag


data = dict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("A", [1, -20, 3.512, 4, 10423, -441.2]),
        ("B", [10, 20, 30, 40, 50, 60]),
        ("C", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)
df = pd.DataFrame(data)


app = Dash(__name__)

app.layout = dag.AgGrid(
    rowData=df.to_dict('records'),
    columnDefs=[
        {"field": "Date"},
        {"field": "Region"},
        ] + [
        {
            "field": i,
            "cellClassRules":  {"max-value": "params.value == maxRowValue(params.data)"}
        } for i in ["A", "B", "C"]
    ],
    defaultColDef={"editable": True},
    columnSize="sizeToFit",
)

if __name__ == '__main__':
    app.run(debug=True)



"""
Put the following in a .css file in the /assets folder
------


.max-value {
    background-color: #3D9970;
}

"""


""""
Put the following in a the dashAgGridFunctions.js file in the /assets folder:
------


var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

// Returns the max value in a row
dagfuncs.maxRowValue = (obj) => {
    const numericValues = Object.values(obj).filter(value => typeof value === 'number' && !isNaN(value));
    return  Math.max(...numericValues)
}

"""
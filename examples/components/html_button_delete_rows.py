
import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
df=df.head(10)

columnDefs = [
    {
        "headerName": "",
        "cellRenderer": "DeleteButton",
        "lockPosition":'left',
        "maxWidth":35,
        "filter": False,
        'cellStyle': {'paddingRight': 0, 'paddingLeft': 0},
    },
    {"field": "athlete", "checkboxSelection": True, "headerCheckboxSelection": True},
    {"field": "age", "maxWidth": 100},
    {"field": "country"},
    {"field": "year", "maxWidth": 120},
    {"field": "sport"},
    {"field": "total"},
]


app.layout = html.Div(
    [
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True},
        ),
    ],

)

if __name__ == "__main__":
    app.run(debug=True)

"""

Place the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.DeleteButton = function (props) {
    function onClick() {
          props.api.applyTransaction({ remove: [props.node.data] })
    }
    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
            },
        },
        React.createElement(
            'button',
            {
                onClick,
                style: {borderWidth: '1px', height: '95%'},
            },
            "X"
        )
    );
};



"""

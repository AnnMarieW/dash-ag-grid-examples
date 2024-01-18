

import dash_ag_grid as dag
from dash import Dash
import pandas as pd
import dash_bootstrap_components as dbc

data = {
    "id": [1,2,3,4,5],
    "item1": [None for _ in range(5)],
    "item2": [None for _ in range(5)],
    "item3": [None for _ in range(5)],
    "item4": [None for _ in range(5)],

}
df = pd.DataFrame(data)

columnDefs = [
    {"field": "id"},
    {
        "field": "item1",
        "cellRenderer": "DBC_Spinner",
        "cellRendererParams": {"color": "danger"},
    },
   {
        "field": "item2",
        "cellRenderer": "DBC_Spinner",
        "cellRendererParams": {"color": "info"},
    },
    {
        "field": "item3",
        "cellRenderer": "DBC_Spinner",
        "cellRendererParams": {"size": "sm", "color": "success"},
    },
    {
        "field": "item4",
        "cellRenderer": "DBC_Spinner",
        "cellRendererParams": {"type": "grow", "color": "warning"},
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    dashGridOptions={"rowHeight": 48, "suppressRowHoverHighlight":True},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(grid)


if __name__ == "__main__":
    app.run_server(debug=True)


"""

Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

// use for making dbc.Spinner
dagcomponentfuncs.DBC_Spinner = function (props) {
    if (props.value !== undefined) {
        return props.value;
    } else {  
        return React.createElement(
            window.dash_bootstrap_components.Spinner,
            {           
                color: props.color,           
                size: props.size,
                type: props.type,
                style: {
                    margin: props.margin,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                },           
            },      
        );
    }
};


"""
import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [{"field": i} for i in ["make", "model", "price", "changes"]]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

cellStyle = {
    "styleConditions": [
        {"condition": "highlightEdits(params)", "style": {"backgroundColor": "#0074D9"}},
    ]
}

defaultColDef = {
    "valueSetter": {"function": "addEdits(params)"},
    "editable": True,
    "cellStyle": cellStyle,
}

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            This example adds a "Changes" column to track which fields in the row were edited.
            The cell background color is based on the "Changes" column.
            
            """
        ),

        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef=defaultColDef,
            columnSize="sizeToFit",
            id="style_edits_grid",
        ),

    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run(debug=True)


"""
Add the following to the dashAgGridFunctions.js file in the assets folder
-----------


var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.addEdits = function (params) {
    if (params.data.changes) {
        var newList = JSON.parse(params.data.changes)
        newList.push(params.colDef.field)
        params.data.changes = JSON.stringify(newList)
    } else {
        params.data.changes = JSON.stringify([params.colDef.field])
    }
    params.data[params.colDef.field] = params.newValue
    return true;
}

dagfuncs.highlightEdits = function (params) {
    if (params.data.changes) {
        if (JSON.parse(params.data.changes).includes(params.colDef.field)) {
            return true
        }
    }
    return false;
}


"""
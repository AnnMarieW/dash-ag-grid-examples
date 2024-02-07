"""
Updating rowData with a valueGetter

"""

import dash_ag_grid as dag
from dash import Dash, Input, Output, State, html, callback, dcc

app = Dash(__name__)

columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
    {
        "headerName": "Comments",
        "valueGetter": {"function": "commentsValueGetter(params)"},
        "editable": False
    }
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

app.layout = html.Div(
    [
        dcc.Markdown("Demo of accessing grid data after sort and filter, including column with a valueGetter"),
        html.Button("get data", id="btn"),
        dag.AgGrid(
            id="virtualRowData-grid",
            columnSize="sizeToFit",
            rowData=rowData,
            columnDefs=columnDefs,
            defaultColDef={"filter": True, "floatingFilter": True, "editable": True},
        ),
        html.Div(id="virtualRowData-output"),
    ]
)


@callback(
    Output("virtualRowData-output", "children"),
    Input("btn", "n_clicks"),
    State("virtualRowData-grid", "virtualRowData"),
    prevent_initial_call=True
)
def get_data(n, virtual_data):
    return str(virtual_data)


if __name__ == "__main__":
    app.run(debug=True)

"""
Add the following to the dashAgGridFunctions.js file in the assets folder
-----------

var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});


dagfuncs.commentsValueGetter = (params) => {
   const newComment = "The " + params.data.model + "Sold for $" + params.data.price
   
   // save the calculated data to `rowData` in the  "comments" column
   params.data.comments = newComment
   
   return newComment
}


"""

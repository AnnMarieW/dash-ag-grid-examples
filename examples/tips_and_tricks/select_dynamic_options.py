import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

options = {
    "United States": ["Boston", "Seattle", "Chicago"],
    "Canada": ["Vancouver", "Montreal", "Toronto"]
}

columnDefs = [
    {"field": "country"},
    {
        "headerName": "Select Editor",
        "field": "city",
        "editable": True,
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {"function": f"dynamicOptions(params, {options})"},
    },

]

rowData = [
    {"country": "United States", "city": "Boston"},
    {"country": "Canada", "city": "Montreal"},
    {"country": "Canada", "city": "Vancouver"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="cell-editors-dynamic",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": False},
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

"""
Put the following in the `dashAgGridFunctions.js file in the assets foler:
-----

var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.dynamicOptions = function (params, options) {
    return {values: options[params.data.country]}
};

"""

import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

items = [f"Product Number  {i}" for i in range(15)]


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=[{"items": i} for i in items],
            columnDefs=[
                {
                    "field": "items",
                    "cellEditor": {"function": "DMC_Select"},
                    "cellEditorParams": {"options": items,   "shadow": "xl",},
                    "cellEditorPopup": True,
                    "editable": True,
                }
            ],
            style={"height": 200},
            dashGridOptions={"popupParent": {"function": "setBody()"}},
        )
    ],
)


if __name__ == "__main__":
    app.run(debug=True)

"""
Add this to the dashAgGridFunctions.js file in the assets folder


Note:  This uses the same DMC_Select component as the example above.
----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.setBody = () => {
    return document.querySelector('body')
}



"""
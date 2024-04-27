"""
based on the docs
https://dash.plotly.com/dash-ag-grid/provided-cell-editors
https://dash.plotly.com/dash-ag-grid/styling-rows#conditional-row-classes

"""

import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

rowClassRules = {
    "priority-1": "params.data.priority == 'High'",
    "priority-2": "params.data.priority == 'Medium'",
    "priority-3": "params.data.priority == 'Low'",
}

columnDefs = [
    {
        "headerName": "Set Priority",
        "field": "priority",
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {
            "values": ["Low", "Medium", "High"],
        },
    },
    {
        "headerName": "Large Text Editor",
        "field": "description",
        "cellEditorPopup": True,
        "cellEditor": "agLargeTextCellEditor",
        "cellEditorParams": {
            "maxLength": 250,
            "rows": 10,
            "cols": 50,
        },
        "flex": 1,
    },
]


rowData = [
    {"priority": "High", "description": "Enter task description"},
    { "priority": "Medium", "description": "Enter task description"},
    { "priority": "Low", "description": "Enter task description"},
    {"priority": "High", "description": "Enter task description"},
    {"priority": "Medium", "description": "Enter task description"},
    {"priority": "Low", "description": "Enter task description"},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Row color changes based on the priority column"
        ),
        dag.AgGrid(

            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={"editable": True, "sortable": True},
            rowClassRules=rowClassRules,
            columnSize="sizeToFit",
        ),

    ],
)


if __name__ == "__main__":
    app.run(debug=True)


"""

add to a .css file in the /assets folder

------------------
.priority-1 {
    background-color: #0074D9 !important;
}
.priority-2 {
    background-color: #3D9970 !important;
}
.priority-3 {
    background-color: #cd0200; !important;
}

"""
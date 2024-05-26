
import dash_ag_grid as dag
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

data = [
    {"type": "Social Media", "links": "Links"},
    {"type": "Development", "links": "Links"}
]

columnDefs = [
    {
        "field": "type",
        "headerName": "Link Type",
    },
    {
        "field": "links",
        "headerName": "",
        "cellRenderer": "DropdownLinks",
        "cellStyle": {"overflow": "visible"}
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=data,
    columnSize="autoSize",
    dashGridOptions={"rowHeight": 48}
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom dash-bootstrap-components DropdownMenu "),
        grid
    ]
)

if __name__ == "__main__":
    app.run(debug=True)


"""


dagcomponentfuncs.DropdownLinks = function (props) {
    return  React.createElement(
        window.dash_bootstrap_components.DropdownMenu,
        {label: props.value},
        [
          React.createElement(window.dash_bootstrap_components.DropdownMenuItem, { href: #/action-1"}, "Item 1"),
          React.createElement(window.dash_bootstrap_components.DropdownMenuItem, { href: "#/action-2" }, "Item 2"),
          React.createElement(window.dash_bootstrap_components.DropdownMenuItem, { href: "#/action-3"}, "Item 3")
        ]
      )
};

------------
Add the following to a .css file in assets folder.  It makes the focused row have a
lower z-index so the menu is displayed when the button is clicked

.ag-row-focus {
    z-index: 999;
}

"""
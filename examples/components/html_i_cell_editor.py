
import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd


app = Dash(__name__, external_stylesheets=["https://use.fontawesome.com/releases/v5.15.4/css/all.css"])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

columnDefs = [
    {
        "field": "company",
        "cellRenderer": "cellEditorIcon",
        "cellRendererParams": {
            "icon": "fas fa-caret-down",
        },
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {
            "values": df["company"].unique(),
        }
    },
    {"field": "mission"},
    {
        "field": "date",
        "cellRenderer": "cellEditorIcon",
        "cellRendererParams": {
            "icon": "far fa-calendar",
        },
    },
    {"field": "successful"}
]

app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={"flex":1, "editable":True},
            dashGridOptions = {"singleClickEdit": True}

        ),
    ],
)



"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


// adds a right aligned icon to a cell
dagcomponentfuncs.cellEditorIcon = function (props) {
  return React.createElement(
    'span',
    {
      style: {
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
      },
    },
    props.value,
    React.createElement('i', {
      className: props.icon,
      style: { marginLeft: 'auto' },
    })
  );
}


"""


if __name__ == "__main__":
    app.run(debug=True)

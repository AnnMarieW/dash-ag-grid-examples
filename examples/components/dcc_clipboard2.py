import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "",
        "cellRenderer": "CopyRow",
        "lockPosition": "left",
        "maxWidth": 25,
        "filter": False,
        "cellStyle": {"paddingLeft": 5},
    },
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
    },
    {"headerName": "Company", "field": "company", "filter": True},
    {
        "headerName": "Last Close Price",
        "type": "rightAligned",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
    },
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
}


grid = dag.AgGrid(
    id="grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSize",
    defaultColDef=defaultColDef,
    dashGridOptions={"rowHeight": 48},
)


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom dcc.Clipboard"),
        grid,
        dcc.Textarea(style={"width": 600}),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.CopyRow = function (props) {
  return React.createElement("div", {}, [
    React.createElement(window.dash_core_components.Clipboard, {
      content: JSON.stringify(props.data),
      title: "Copy Row",
      style: {
        display: "inline-block",
        verticalAlign: "top",
        paddingLeft: 3,
        cursor: "pointer",
      },
      setProps: () => {},
    }),
  ]);
};

"""
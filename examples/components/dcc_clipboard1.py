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

    {"headerName": "Company", "field": "company", "filter": True},
    {
        "headerName": "Last Close Price",
        "type": "rightAligned",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
    },
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "cellRenderer": "DCC_Clipboard",
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSize",
    dashGridOptions={"rowHeight": 48},
)


app = Dash(__name__)

app.layout = html.Div(grid)

if __name__ == "__main__":
    app.run(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.DCC_Clipboard = function (props) {
  return React.createElement("div", {}, [
    props.value,
    React.createElement(window.dash_core_components.Clipboard, {
      content: props.value,
      title: "Copy cell",
      style: {
        display: "inline-block",
        verticalAlign: "top",
        paddingLeft: 10,
        cursor: "pointer",
      },
      setProps: () => {},
    }),
  ]);
};
"""
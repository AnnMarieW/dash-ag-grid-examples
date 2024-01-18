import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import dash_bootstrap_components as dbc



data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
    "buy": [False, True, True, True],
}
df = pd.DataFrame(data)

columnDefs = [
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
    {
        "field": "buy",
        "cellRenderer": "DBC_Switch",
        "cellRendererParams": {"color": "success"},
    },
]


grid = dag.AgGrid(
    id="dbc-switch-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSize",
    dashGridOptions={"rowHeight": 48},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom dash-bootstrap-components Switch "),
        grid,
        html.Div(id="dbc-switch-value-changed"),
    ],
    style={"margin": 20},
)


@callback(
    Output("dbc-switch-value-changed", "children"),
    Input("dbc-switch-grid", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


// custom component to display boolean data as a DBC Switch
dagcomponentfuncs.DBC_Switch = function (props) {
    const {setData, value} = props;

    // updated the dbc component
    setProps = ({value}) => {
       // update the grid
        props.node.setDataValue(props.column.colId, value);
        // update to trigger a dash callback
        setData(value)
    }

    return React.createElement(
        window.dash_bootstrap_components.Switch, {
            value: value,
            checked: value,
            setProps,
            style: {"paddingTop": 6},
        }
    )
};


"""

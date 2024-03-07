import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import dash_mantine_components as dmc

rowData = [
    {"example": 1, "option": "A", "order": "buy"},
    {"example": 2, "option": "B", "order": "sell"},
    {"example": 3, "option": "B", "order": "buy"},
    {"example": 4, "option": "C", "order": "sell"},
]


columnDefs = [
    {"field": "example"},
    {
        "field": "option",
        "minWidth": 300,
        "cellRenderer": "DMC_RadioGroup",
        "cellRendererParams": {
            "children": [
                {
                    "label": "A",
                    "value": "A",
                    "color": "green",
                    "disabled": False,
                },
                {
                    "label": "B",
                    "value": "B",
                    "color": "yellow",
                    "disabled": False,
                },
                {
                    "label": "C",
                    "value": "C",
                    "color": "red",
                    "disabled": False,
                },
            ]
        },
    },
    {
        "headerName": "Buy/Sell (disabled)",
        "field": "buy-sell",
        "cellRenderer": "DMC_RadioGroup",
        "cellRendererParams": {
            "children": [
                {
                    "label": "buy",
                    "value": "buy",
                    "color": "green",
                    "disabled": True,
                },
                {
                    "label": "sell",
                    "value": "sell",
                    "color": "red",
                    "disabled": True,
                },
            ],
        },
    },
]


grid = dag.AgGrid(
    id="grid-dmc-radiogroup",
    columnDefs=columnDefs,
    rowData=rowData,
    columnSize="autoSize",
)


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with dash-mantine-components RadioGroup"),
        grid,
        html.Div(id="dmc-radiogroup-value-changed"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("dmc-radiogroup-value-changed", "children"),
    Input("grid-dmc-radiogroup", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run_server(debug=True)


"""


var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

// DMC RadioGroup component
dagcomponentfuncs.DMC_RadioGroup = function (props) {
    const { setData, value } = props;

    const setProps = ({ value }) => {
        props.node.setDataValue(props.column.colId, value);
        setData(value);
    };

    const dataList = props.children;
    const children = dataList.map(item => {
        const { label, value, color, disabled } = item;

        return React.createElement(window.dash_mantine_components.Radio, {
            label: label,
            value: value,
            color: color,
            disabled: disabled,
        });
    });

    return React.createElement(
        window.dash_mantine_components.RadioGroup,
        {
            children: children,
            value: value,
            setProps: setProps,
        },
    );
};


dagcomponentfuncs.CustomTooltipImage = function (props) {
  return React.createElement(
    'img',
    {
      style: props.style || {
        width: '100%',
        maxWidth: '400px',
        height: 'auto',
        border: '2px solid grey',
        pointerEvents: 'none',
      },
      src: props.value
    },
  );
};


"""

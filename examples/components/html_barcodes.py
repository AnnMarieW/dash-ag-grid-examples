import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "country"},
    {"field": "athlete"},
    {"field": "year"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {
        "field": "sport",
        "headerName": "Barcode (sport)",
        "cellRenderer": "ValueToBarcode",
        "suppressSizeToFit": True,
        "minWidth": 250,
    },
]

app.layout = html.Div(
    [
        dcc.Markdown("Example of adding barcodes to grid with a cell renderer"),
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"rowHeight": 100},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)


"""
Put the following in the app.py file. More info on https://github.com/lindell/JsBarcode

-----------

#.js for custom html components - barcodes
js_custom_html_barcodes = ["https://cdn.jsdelivr.net/npm/jsbarcode@3.11.0/dist/JsBarcode.all.min.js"]

app = Dash(...,external_scripts=... + js_custom_html_barcodes)

-----------

Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


// Barcode generator
dagcomponentfuncs.ValueToBarcode = function (props) {
    const { value } = props;

    const canvas = document.createElement('canvas');
    JsBarcode(canvas, value, {
        format: "CODE128",
        displayValue: true,
    });

    const barcodeDataUrl = canvas.toDataURL();

    return React.createElement(
        'img',
        {
            src: barcodeDataUrl,
            style: { width: '100%', height: '95%' },
        }
    );
};


"""

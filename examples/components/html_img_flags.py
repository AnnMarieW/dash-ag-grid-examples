"""
Add country flag with a cell renderer
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


COUNTRY_CODES = {
    "Ireland": "ie",
    "Luxembourg": "lu",
    "Belgium": "be",
    "Spain": "es",
    "France": "fr",
    "Germany": "de",
    "Sweden": "se",
    "Italy": "it",
    "Greece": "gr",
    "Iceland": "is",
    "Portugal": "pt",
    "Malta": "mt",
    "Norway": "no",
    "Brazil": "br",
    "Argentina": "ar",
    "Colombia": "co",
    "Peru": "pe",
    "Venezuela": "ve",
    "Uruguay": "uy",
}

df = df[df.country.isin(COUNTRY_CODES)]
df["country_code"] = df.country.apply(lambda x: COUNTRY_CODES[x])


app = Dash(__name__)


columnDefs = [
    {"field": "country", "cellRenderer": "FlagsCellRenderer"},
    {"field": "athlete"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Example of adding flags to the Country column with a cell renderer"
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={
                "filter": True,
                "minWidth": 100,
            },
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.FlagsCellRenderer = function (props) {  

   // for more info see https://flagpedia.net/
    const url = `https://flagcdn.com/h20/${props.data.country_code}.png`;

    return React.createElement('span', {}, [
        React.createElement(
            'img',
            {
                style: {height: '10px'},
                src: url
            },

        ),
        React.createElement(
            'span',
            {
                style: {paddingLeft: '4px'},
            },
            props.value
        ),
    ]);
};



"""
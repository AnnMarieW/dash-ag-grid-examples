import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "country", },
    {"field": "athlete",  "headerTooltip": 'Olympic Athlete', "tooltipField": 'athlete',},
    {"field": "year"},
    {"field": "sport"},
    {"field": "gold",  "headerTooltip": 'gold',  "tooltipComponent":  "CustomHeaderTooltip"},
    {"field": "silver", "headerTooltip": 'silver', "tooltipComponent": "CustomHeaderTooltip"},
    {"field": "bronze", "headerTooltip": 'bronz', "tooltipComponent": "CustomHeaderTooltip"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"tooltipShowDelay": 100},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)



"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.CustomHeaderTooltip = function(props) {
  return React.createElement(
    "span",
    { className: "p-2 bg-secondary text-white" },
    [
      React.createElement("i", { className: "fa-solid fa-medal p-2" }),
      React.createElement("span", null, `${props.value} medal`),
    ]
  );
}


"""
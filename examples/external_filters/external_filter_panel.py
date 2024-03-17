from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc

import dash_ag_grid as dag

df = px.data.gapminder()
years = df.year.unique()
continents = df.continent.unique()

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])


columnDefs = [
    {"headerName": "Continent", "field": "continent"},
    {"headerName": "Year", "field": "year"},
    {"headerName": "Country", "field": "country"},
    {
        "headerName": "Life Expectancy",
        "field": "lifeExp",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('.1f')(params.value)"},
    },
    {
        "headerName": "Population",
        "field": "pop",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format(',.0f')(params.value)"},
    },
    {
        "headerName": "GDP per Capita",
        "field": "gdpPercap",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('$,.1f')(params.value)"},
    },
]

grid = dag.AgGrid(
    id="grid-panel",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    defaultColDef={"flex": 1, "minWidth": 100, "filter": True}
)

checklist = html.Div(
    [
        dbc.Label("Select Continents"),
        dbc.Checklist(
            id="continents-panel",
            options=continents,
            value=["Europe"],
            inline=True,
        ),
    ],
    className="mb-4",
)

slider = html.Div(
    [
        dbc.Label("Select Years"),
        dcc.RangeSlider(
            years[0],
            years[-1],
            5,
            id="years-panel",
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
            value=[years[2], years[-2]],
            className="p-0",
        ),
    ],
    className="mb-4",
)

heading = html.H4("AG Grid External Filter Demo", className="bg-primary text-white p-2 mb-2 text-center")

controls = dbc.Card(
    [checklist, slider],
    body=True,
)

app.layout = dbc.Container(
    [
        heading,
        dbc.Row([dbc.Col(controls, md=4),dbc.Col(grid, md=8)]),
    ],
    fluid=True,
)


@callback(
    Output("grid-panel", "dashGridOptions"),
    Input("continents-panel", "value"),
    Input("years-panel", "value"),
)
def update(continent, yrs):
    my_filter = f"{continent}.includes(params.data.continent) && params.data.year >= {yrs[0]} && params.data.year <= {yrs[1]}"

    return {
        "isExternalFilterPresent": {"function": "true"},
        "doesExternalFilterPass": {"function": my_filter},
    }


if __name__ == "__main__":
    app.run_server(debug=True)

import dash_ag_grid as dag
from dash import Dash, html

import plotly.express as px

app = Dash(__name__)


def make_country_figure(df, country):
    filter_df = df[df["country"] == country]
    fig = px.line(filter_df, x="year", y="lifeExp", title=country, width=400, height=200)
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="LightSteelBlue"
    )
    return fig

df = px.data.gapminder().query("continent=='Europe'")
df2 = df.groupby("country")[["lifeExp", "gdpPercap", "pop"]].mean().reset_index()

# define the figure in the "graph" column.  This is he data for the tooltip
df2["graph"] = df2["country"].apply(lambda country: make_country_figure(df, country))


columnDefs = [
    {"field": "country"},
    {
        "field": "lifeExp",
        "headerName": "Avg. Life Expectancy (1952-2007)",
        "valueFormatter": {"function": 'd3.format("(,.2f")(params.value)'},
        "tooltipField": "graph",
        "tooltipComponent": "CustomTooltipGraph",
    },
]

app.layout = html.Div(
    [
        html.H4("See the custom tooltip component in the Avg Life Expectancy column"),
        dag.AgGrid(
            rowData=df2.to_dict("records"),
            columnSize="autoSize",
            columnDefs=columnDefs,
            dashGridOptions={"tooltipShowDelay": 100, "tooltipInteraction": True},
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)



"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.CustomTooltipGraph = function (props) {
    return React.createElement(
        window.dash_core_components.Graph, {
            figure: props.value,
        })
};




"""
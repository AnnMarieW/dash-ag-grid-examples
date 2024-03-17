
from dash import Dash, dcc, html, Input, Output, callback, no_update
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag

app =  Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k-multi-year.csv")

fig = px.scatter_mapbox(
    df[df.year==2018],
    lat="lat", lon="lon",
    hover_data=["City", "State"],
    size="Population",  color="Population",
    zoom=4,
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

app.layout = html.Div(
    [
        html.H3("Population 2018"),
        html.H4("Filter the grid by hovering on the map"),
        dcc.Graph(id="graph-external-filter", figure=fig),
        dag.AgGrid(
            id="grid-graph-external-filter",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in ["City", "State", "Population", "year"]],
            defaultColDef={"flex": 1, "filter": True},
        ),
    ], style={"padding": 24}
)


@callback(
    Output("grid-graph-external-filter", "dashGridOptions"),
    Input("graph-external-filter", "hoverData"),
)
def generate_chart(hoverdata):
    if not hoverdata:
        return no_update

    city = hoverdata["points"][0]["customdata"][0]
    state = hoverdata["points"][0]["customdata"][1]

    return {
        "isExternalFilterPresent": {"function": "true"},
        "doesExternalFilterPass": {"function": f"params.data.City === '{city}' && params.data.State === '{state}'"}
    }


if __name__ == "__main__":
    app.run(debug=True)


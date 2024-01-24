
from dash import Dash, html
import pandas as pd
import dash_ag_grid as dag


df_gapminder = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = df_gapminder[:500]

app = Dash(__name__)


def data_bars(df, column):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    ranges = [
        ((df[column].max() - df[column].min()) * i) + df[column].min() for i in bounds
    ]
    styles = []

    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100
        styles.append(
            {
                "condition": f"params.value >= {min_bound}"
                             + (
                                 f" && params.value < {max_bound}"
                                 if (i < len(bounds) - 1)
                                 else ""
                             ),
                "style": {
                        "background":
                            f"""
                                linear-gradient(90deg,
                                #83C7AF 0%,
                                #83C7AF {max_bound_percentage}%,
                                white {max_bound_percentage}%,
                                white 100%)
                            """,
                        "color": "transparent",

                    }
            }
        )
    return styles

app.layout = html.Div(
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[
            {'field': "country"},
            {"field": "year"},
            {"field": "lifeExp"},
            {"field": "gdpPercap", "width": 75},
            {
                "field": "gdpPercap",
                "cellStyle": {"styleConditions": data_bars(df, 'gdpPercap')}
            },
        ],
        columnSize="sizeToFit",
    style={"height": 700}
))


if __name__ == '__main__':
    app.run(debug=True)

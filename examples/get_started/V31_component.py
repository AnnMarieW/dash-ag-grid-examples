
import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": "mission",},
                {"field": "company",  "cellRenderer": "CompanyLogoRenderer"},
                {"field": "price",  "valueFormatter": {"function": "d3.format('$,.0f')(params.value)"}},
                {"field": "successful"}
            ],
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)


import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i, "tooltipField": i} for i in df.columns],
            defaultColDef={"initialWidth": 110},
            dashGridOptions={
                "tooltipShowDelay":0,  # Makes tooltip show immediately.  Default 2000ms
                "tooltipHideDelay": 3000, # Hides tooltip after 3000ms
                "tooltipInteraction": True, # Won't hide when hover on toolip.  Can select and copy content.
               # "tooltipMouseTrack": True # tooltips follows the cursor - don't use when tooltipInteraction = True
            },
            style={"ag-tooltip-background-color": "red"}
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)

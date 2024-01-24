
from dash import Dash
import pandas as pd
import dash_ag_grid as dag


data = dict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("A", [1, -20, 3.512, 4, 10423, -441.2]),
        ("B", [10, 20, 30, 40, 50, 60]),
        ("C", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)
df = pd.DataFrame(data)



bottom3 = df['C'].nsmallest(3).tolist()
style_bottom3 =  {
    "styleConditions": [
        {
            "condition": f"{bottom3}.includes(params.value)",
            "style": {'backgroundColor': '#7FDBFF', "color": "white"}
        }
    ]
}


top3 = df['A'].nlargest(3).tolist()
style_top3 =  {
    "styleConditions": [
        {
            "condition": f"{top3}.includes(params.value)",
            "style": {'backgroundColor': '#0074D9', "color": "white"}
        }
    ]
}


app = Dash(__name__)
app.layout = dag.AgGrid(
    rowData=df.to_dict('records'),
    columnDefs=[
        {"field": "Date"},
        {"field": "Region"},
        {"field": "A", "cellStyle": style_top3},
        {"filed": "B"},
        {"field": "C", "cellStyle": style_bottom3}
    ],
    columnSize="sizeToFit",
)

if __name__ == '__main__':
    app.run(debug=True)

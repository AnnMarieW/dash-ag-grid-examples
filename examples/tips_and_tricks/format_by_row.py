from dash import html, Dash
import dash_ag_grid as dag
import pandas as pd

list_of_vals = [
    {
        "Val ID": "9729",
        "Year": "2017",
        "Hours": 1253.0,
        "Value": 31950000.0,
    },
    {
        "Val ID": "9733",
        "Year": "2016",
        "Hours": 2541.0,
        "Value": 29995000.0,
    },
    {"Val ID": "9837", "Year": "2019", "Hours": 566.0, "Value": 34900000.0},
    {
        "Val ID": "9507",
        "Year": "2013",
        "Hours": 2732.0,
        "Value": 26000000.0,
    },
    {
        "Val ID": "9805",
        "Year": "2018",
        "Hours": 1543.0,
        "Value": 31500000.0,
    },
]

df = pd.DataFrame(list_of_vals)
# transpose df
df = df.set_index("Val ID").T
df = df.reset_index().rename(columns={"index": "Val ID"})
data_list = [item for item in df.to_dict(orient="records")]
columns_list = list(df.columns)

app = Dash()

app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=data_list,
            columnDefs=[{"field": "Val ID", "editable": False}]
            + [
                {
                    "field": c,
                    "valueFormatter": {"function": "FormatNumbersByRow(params)"},
                    "type": "numericColumn",
                    "cellDataType": "number",
                    "editable": {"function": "params.data['Val ID'] != 'Year'"},
                }
                for c in columns_list
                if c != "Val ID"
            ],
            defaultColDef={"editable": True, "flex": 1},
            dashGridOptions={
                "undoRedoCellEditing": True,
                "undoRedoCellEditingLimit": 20,
            },
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.Intl = Intl;

dagfuncs.FormatNumbersByRow = function(params) {   
    if (params.data["Val ID"] == "Hours") {
        return Intl.NumberFormat("en-US").format(params.value);
    }
    if (params.data["Val ID"] == "Value") {
        return Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
          }).format(params.value);
    }
}

"""
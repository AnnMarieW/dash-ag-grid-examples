import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv").head(20)

# Add column with the formatted markdown info to show in the company column tooltip
df["company_md"] = df.apply(lambda row: f"""

    ## Mission Data for: {row['company']}
    -------------
    ### {row['location']}   
    #### {row['date']}
    
""", axis=1)

webb_carina = "https://user-images.githubusercontent.com/72614349/179115673-15eaccb9-d17d-4667-84fb-e0a46fd444e8.jpg"

columnDefs = [
    {
        "field": "company",
        "tooltipField": "company_md",
        "tooltipComponent": "CustomTooltipMarkdown",
        "tooltipComponentParams": {
            "style": {
                "backgroundColor": "var(--ag-card-shadow)",
                "color": "white",
                "padding": 20,
                "backgroundImage": f"url('{webb_carina}')",
                "boxShadow": "var(--ag-card-shadow)",
            }
        },
    },
    {"field": "mission"},
    {"field": "successful"}
]

app.layout = html.Div(
    [
        html.H4("See the custom tooltip component in the Company column"),
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            dashGridOptions={"tooltipShowDelay": 0},
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)



"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.CustomTooltipMarkdown = function (props) {
    return React.createElement(
        window.dash_core_components.Markdown, {
            children: props.value,
            className: props.className,
            style: props.style,
            dangerously_allow_html : props.dangerously_allow_html | false,
            link_target: props.link_target,
            mathjax: props.mathjax
        })
};





"""
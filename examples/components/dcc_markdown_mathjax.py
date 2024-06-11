import dash_ag_grid as dag
from dash import Dash, html, dcc

data = [
    {"formula": "$E=mc^2$", "inventor": "Einstein", "symbols": "$E,m,c$", "year": 1905},
    {"formula": "$y=mx+b$", "inventor": "Salmon", "symbols": "$y,m,x,b$", "year": None},
    {"formula": "$x=\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$", "inventor": "Brahmagupta", "symbols": "$x,a,b,c$", "year": 1607},
    {"formula": "$a^2+b^2=c^2$", "inventor": "Pythagoras", "symbols": "$a,b,c$", "year": "1800 BC"}
]

columnDefs = [
    {
        "field": "formula",
        "cellRenderer": "DccMarkdown",
        "cellRendererParams": {"mathjax": True, "className":"markdown"},

    },
    {"field": "inventor"},
    {

        "field": "symbols",
        "cellRenderer": "DccMarkdown",
        "cellRendererParams": {"mathjax": True,  "className":"markdown"},

    },
    {"field": "year",  'cellDataType': 'text'}
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=data,
    columnSize="sizeToFit",

)


app = Dash(__name__)

app.layout = html.Div(
    [dcc.Markdown("Example of formating data with MathJax"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run(debug=True)




"""
Put the following in the dashAgGridComponentFunctions.js file in /assets

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.DccMarkdown = function (props) {
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

"""
Put the following in a .css file in /assets

Note: The dcc.Markdown component wraps the content in a p element which can mess with the alignment when it's used
in the grid.  The following css will remove the extra margin.


.markdown p {
   margin: 0
}



"""
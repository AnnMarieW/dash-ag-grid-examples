import dash
from dash import dcc, html, Dash, Input, Output, State
import dash_ag_grid as dag

app = Dash(__name__)

upload = dcc.Upload(
    id="upload-image",
    children=html.Div(["Drag and Drop or ", html.A("Select Image Files")]),
    style={
        "width": "100%",
        "height": "60px",
        "lineHeight": "60px",
        "borderWidth": "1px",
        "borderStyle": "dashed",
        "borderRadius": "5px",
        "textAlign": "center",
        "margin": "10px",
    },
    multiple=True,
)

grid = dag.AgGrid(
    id="site-photo-grid",
    rowData=[
        {
            "Photo_id": 1,
            "Filename": "default.jpg",
            "Location": "Location",
            "Remarks": "Remarks",
            "Image": "",
        }
    ],
    columnDefs=[
        {"field": "Photo_id", "width": 50},
        {
            "field": "Filename",
            "tooltipComponent": "CustomTooltipImage",
            "tooltipField": "Image",
            # Can change the  CustomTooltipImage style here:
            # "tooltipComponentParams": {"style": {}},
        },

        {"field": "Location"},
        {"field": "Remarks"},
    ],
    defaultColDef={"editable": True},
    dashGridOptions={"tooltipShowDelay": 100},
    columnSize="sizeToFit",
)

app.layout = html.Div([upload, grid])


@app.callback(
    Output("site-photo-grid", "rowData"),
    Input("upload-image", "contents"),
    State("upload-image", "filename"),
    prevent_initial_call=True,
)
def update_output(contents, filename):
    if not contents:
        return dash.no_update

    data = [
        {
            "Photo_id": i+1,
            "Filename": f"{filename[i]}",
            "Location": "",
            "Remarks": "",
            "Image": contents[i],
        }
        for i in (range(len(contents)))
    ]
    return data

if __name__ == "__main__":
    app.run_server(debug=True)

"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.CustomTooltipImage = function (props) {
  return React.createElement('img', {
    style: props.style || {
      width: '100%',
      maxWidth: '400px',
      height: 'auto',
      border: '2px solid grey',
      pointerEvents: 'none',
    },
    src: props.value,
  });
};

"""
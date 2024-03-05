
import dash
from dash import Dash, html, dcc, Input, Output, State, clientside_callback
import dash_bootstrap_components as dbc
from utils.nav import navbar
from utils.utils import example_apps

# need these two imports for the custom components
import dash_mantine_components
import dash_iconify


# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# for the custom datepicker example
jquery_external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js",
    ]
jquery_external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css"
    ]

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.SPACELAB,
        dbc.icons.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        dbc_css,
        dark_hljs,
    ] + jquery_external_stylesheets,
    suppress_callback_exceptions=True,
    external_scripts=jquery_external_scripts,
    # the following is required in dash >=2.16 for apps where certain libraries are only used in
    # custom cell renderers
    # preloaded_libraries=['dash_iconify', 'dash_mantine_components', 'dash_core_components']
)


for k in example_apps:
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)
print("step 4")

app.layout = html.Div(
    [
        navbar,
        dbc.Container(dash.page_container, className="p-2"),

    ],
    className="mb-4 dbc dbc-ag-grid",

)


clientside_callback(
    """ 
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)

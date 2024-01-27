from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: dcc components", path=links.components_dcc
)


text1 = """
# Custom Components Examples

Here are some examples of using Dash Core Components in Dash AG Grid cells.  

For more information, please see the [Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section of the Dash AG Grid docs.
 
## dcc.Clipboard - copy cell

See this [forum post](https://community.plotly.com/t/ag-grid-with-dcc-clipboard/80357) for a tutorial 
"""

text2 = """
## dcc.Clipboard copy row

See this [forum post](https://community.plotly.com/t/ag-grid-with-dcc-clipboard/80357) for a tutorial 
"""

text3 = """
## dcc.Graph in a custom tooltip

__Try hovering over the Avg life expectancy column!__
"""

text4 = """
### dcc.Markdown in a custom tooltip

__Try hovering over the Company column!__
"""

text5 = """
## `dcc.RadioItems` as a custom filter component in header

This example was adapted from [React Data Grid: Filter Component](https://www.ag-grid.com/react-data-grid/component-filter/)

Try filtering the Year column and you will see the `dcc.RadioItems` component instead of the default number filter.
"""


next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.dcc_clipboard1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.dcc_clipboard2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.dcc_graph_in_tooltip", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.dcc_markdown_in_tooltip", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.dcc_radioitems_header", make_layout=make_tabs),
        up_next()
    ],
)

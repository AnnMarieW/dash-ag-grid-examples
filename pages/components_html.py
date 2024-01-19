from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: html components", path=links.components_html
)


text1 = """
# Custom Components Examples

Here are some examples adding custom components to cells in the Dash AG Grid component using regular HTML components.

For more information, please see the [Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section of the Dash AG Grid docs.
 

## HTML img component

Here is an example of adding country flags to the cells in the grid.  For more information see
 this [forum post](https://community.plotly.com/t/ag-grid-country-flags-cell-renderer/75932) for a tutorial.

"""

text2 = """
## HTML i component Add icons

This app uses a custom componenet in the header tooltiop.  It adds icons to the tooltip in the Gold Silver and Bronze columns.
Note that the Athlete column uses the default tooltip.
"""


text3 = """

"""

text4 = """
"""


next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.html_img_flags", make_layout=make_tabs),
         make_md(text2),
        example_app("examples.components.html_i_tooltip_header", make_layout=make_tabs),
        # make_md(text3),
        # example_app("examples.components.dmc_select_popupparent", make_layout=make_tabs),
        # make_md(text4),
        # example_app("examples.components.dmc_select_labels_and_vals", make_layout=make_tabs),
        up_next()
    ],
)

from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: dmc components", path=links.components_dmc
)


text1 = """
# Custom Components Examples

Here are some examples of using Dash Mantine Components in Dash AG Grid cells.  

For more information, please see the [Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section of the Dash AG Grid docs.
 

## dmc.Button

"""

text2 = """
## dmc.Select

"""


text3 = """
## dmc.Select with Popup Parent

Under most scenarios, the menu will fit inside the grid. However if the grid is small and / or the menu is very large, then the menu will not fit inside the grid and it will be clipped. This will lead to a bad user experience.

This example shows how to set the popup parent to allow the options menu to overflow the grid.

"""

text4 = """
## dmc.Select with grouping
- The "City" column uses both labels and values in the dropdown.
- The "Things To Do" column has dropdown options  grouped in different categories.

"""


next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.dmc_button", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.dmc_select", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.dmc_select_popupparent", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.dmc_select_labels_and_vals", make_layout=make_tabs),
        up_next()
    ],
)

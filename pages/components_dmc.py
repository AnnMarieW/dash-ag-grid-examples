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

## dmc.Button

"""

text2 = """
## dmc.Select

"""

text3 = """
## dmc.Select with grouping

"""


next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.dmc_button", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.dmc_select", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.dmc_select_labels_and_vals", make_layout=make_tabs),
        up_next()
    ],
)

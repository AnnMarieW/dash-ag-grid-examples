from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Cell Data Types", path=links.cell_data_types
)


text1 = """
# Dash AG Grid Cell Data Types

> This page is under construction


In this example, note that the numeric columns are automatically right aligned for all datasets selected in the dropdown.
"""




text2 = f"""

## Next Steps

 - Check out the <dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" /> to learn more about the key concepts of AG Grid, including filtering, editing,
  formatting data, adding custom components and using callbacks.

- See the [Dash docs]({links.dag_docs}) and the [AG Grid docs]({links.ag_grid_docs}) for details on all the features.

- Have questions?  Ask them on the [Dash Community Form]({links.forum})

Happy Coding!

"""

next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),

        example_app("examples.cell_data_types.numeric_right_aligned", make_layout=make_tabs),
        make_md(text2),
        up_next(next)
    ],
)

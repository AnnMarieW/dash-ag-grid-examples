from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__,
    description=app_description,
    title="Dash AG Grid Examples: html components",
    path=links.components_html,
)


text1 = """
# Custom Components Examples

Here are some examples adding custom components to cells in the Dash AG Grid component using regular HTML components.

For more information, please see the [Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section of the Dash AG Grid docs.
 

## HTML `img` component

This app adds flags in the cells in the country column.  See  this [forum post](https://community.plotly.com/t/ag-grid-country-flags-cell-renderer/75932) for a tutorial.

"""

text2 = """
## HTML `i` component (for icons)

This example shows how to use a custom component in the header tooltip. See the tooltip with icons in the Gold Silver and Bronze columns.
Note that the Athlete column uses the default tooltip.
"""

text2b = """
## HTML `i` component (for cell icons)

This example adds a right aligned icon to indicate a cell is editable. This demo uses the [provided cell editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors),
but it can be used with custom cell editors (like the dmc.Select) component as well.
 
The same cell render is used to add icons to both the Company column and the Date column.  You can specify the icon using the  "icon" prop in the `cellRendererParams`:

```
columnDefs = [
   {
        "field": "date",
        "cellRenderer": "cellEditorIcon",
        "cellRendererParams": {
            "icon": "far fa-calendar",
        },
    },
]
```

"""


text3 = """
## HTML `button` component

This example shows how to add a delete button in each row.  For more information on deleting rows, see this [tutorial](https://community.plotly.com/t/deleting-rows-in-dash-ag-grid/78700) on the Dash forum.

"""

text4 = """
## Upload image files and display them in a tooltip

"""

text5 = """
## Barcodes (HTML `canvas` component + HTML `img` component)

"""


next = f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.html_img_flags", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.html_i_tooltip_header", make_layout=make_tabs),
        make_md(text2b),
        example_app("examples.components.html_i_cell_editor", make_layout=make_tabs),
        make_md(text3),
        example_app(
            "examples.components.html_button_delete_rows", make_layout=make_tabs
        ),
        make_md(text4),
        example_app("examples.components.html_img_upload", make_layout=make_tabs),
        make_feature_card(links.upload_image_files_tooltip_gif, "## After upload"),
        make_md(text5),
        example_app("examples.components.html_barcodes", make_layout=make_tabs),
        up_next(),
    ],
)

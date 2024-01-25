from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Migrating from Dash DataTable", path=links.migrating_DataTable
)


text1 = f"""
# From Dash DataTable to Dash AG Grid
### A Migration guide
 
 
--------------

` `  
` ` 
## Getting Started

 - Check out the <dccLink href="{links.get_started_V31}" children="Getting Started with V31" /> for an overview of the basic grid features.
 
## Conditional Formatting
 
 - See examples of  <dccLink href="{links.styling}" children="conditional formatting" /> based on the DataTable Dash docs.
 

## Deleting Rows
Here is an example of how to delete a row by clicking on a button like in DataTable.  

See a this tutorial on [deleting rows in Dash Ag Grid](https://community.plotly.com/t/deleting-rows-in-dash-ag-grid/78700) on the Dash community forum.
 
"""

text2 = """

### Trigger callbacks with `cellClicked` prop

Use `cellClicked` or `cellDoubleClicked` in a callback rather than the DataTable `active_cell` prop.

Note that the callback is triggered only when the cell is clicked.  If you need to trigger the callback based on the
 active (ie focused cell), see the next example.
"""

text3="""

### Trigger callbacks on focused cell

Currently, there is no prop in Dash AG Grid to trigger a Dash callback based on which cell is focused (and not clicked).
The example below is a workaround for apps where it's necessary to trigger a callback when a user navigates around the
 grid with the keyboard.   

A clientside callback adds an event listener to the grid, so that when the cell is  focused, it triggers a click on the
 focused cell. This works, but it is not an ideal solution since the grid will   respond as if the user clicked a cell. 
   This could be an issue in certain cases, such as when "one click editing" is    enabled in the grid, or if you have
    buttons in the grid that would get triggered just because a user navigates to (or over) the cell with the button.
    

Try navigating by either clicking on the cells or using the keyboard arrow keys:
"""




next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.html_button_delete_rows", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.DataTable.cell_clicked", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.DataTable.active_cell", make_layout=make_tabs),
        make_md("### More content coming soon..."),

        up_next(next)
    ],
)

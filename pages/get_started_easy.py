from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Quickstart", path=links.get_started_easy
)


text1 = """
# Dash AG Grid Quickstart


Add a beautiful data grid to your Dash app with 3 lines of code!  

The `rowData` defines the data and the `columnDefs` control how the data is displayed. In this example, the data is in
 a Pandas dataframe.
 
```python
dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],    
)
```
"""

text1a = """

Features available by default:
- Alpine theme is applied to style the grid
- The columns are resizable (drag on the vertical handle in the header)
- The rows are sortable (click on the header to sort. shift-click the header to sort by multiple columns)
- Note the row animation when sorting
- Boolean values are rendered as a checkbox 
- Reorder the columns by dragging the column header
- Pin a column to the right or left side of the grid

"""

text2 = f"""

Congratulations! You've  built your first grid. 

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
        make_feature_card(links.get_started_easy_gif, text1a),
        make_md("Now give it a try here!"),
        example_app("examples.get_started.V31_quickstart", make_layout=make_tabs),
        make_md(text2),
        up_next(next)
    ],
)

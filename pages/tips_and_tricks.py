from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Tips & Tricsk", path=links.tips_and_tricks
)


text1 = """
# Tips and Tricks


### Overview
This section contains sample apps to illustrate a variety of topics and address frequently asked questions.

- How to make a grid with less code  -- by using functions to create a grid with all your favorite features.
- How to access data created with a `valueGetter` in a callback
- How to have different dropdown option in different rows of the same column
- How to have different value formatters in different rows of the same column




## 1. Low code grid

The grid is very configurable, and you will likely want to include all your favorite features with every grid.  To
 reduce the amount of boilerplate code in your apps, you can create a function that returns a grid to include in your layout.
 
Below is an example with some of my favorite features.  I keep this function in a utility folder, then use it like this:

```
from utils import make_grid

app.layout = ([
    make_grid(df)
])
``` 
Along with the features available by default, grids made with this function will also have:

 - Right aligned numeric fields
 - Ability to format currency columns with `{"cellDataType": "money"}`
 - Ability to format percentage columns with  `{"cellDataType": "pct"}`
 - The stepper buttons in the number cell editor
 - Apply and Reset buttons included in the filter
 - The filter menu closes when the Apply or Reset buttons are clicked
 - Pagination
 - Column size to fit with the initial minimum width of 120px
 - Ability to undo and redo cell editing with ctrl-z and ctrl-y
 - Row animation suppressed
 
Check out the second grid.  It uses the same function with a different data set.  
"""

text2 = """

## 2. Accessing ValueGetter data in a callback.

One of the cool features of the grid is the ability to create cell content with `valueGetters`.  This allows you
 to do things like add calculated fields like a a spreadsheet. See more info in the Dash docs [Value Getters](https://dash.plotly.com/dash-ag-grid/value-getters).
 
In this example, we'll show you how to get the data that was calculated by the `valueGetter` in a Dash callback.  

There are three tricks demonstrated here:
 - Getting only the sorted and filtered data using `virtualRowData`
 - Triggering the callback with the button to ensure you get the most up-to-date data
 - Saving the calculated columns in `rowData` so it's accessible in the callback

"""

text3 = """
## 3. Dynamic Select Options Using Built-in Select Component 

This example demonstrates dynamic options based on the value of a different column. For each country listed in the
 "Country" column, the dropdown in the "Cities" column can display different cities.

The JavaScript function receives a dictionary containing countries and their corresponding cities from the app by
 setting the cellEditorParams.

"""

text4 = """

## 4. Formatting Cells by Row and Conditional editing

This example demonstrates how to have different [Value Formatters](https://dash.plotly.com/dash-ag-grid/custom-functions-value-formatters) in cells of the same column. It also illustrates how to
 specify which cells are editable. Additionally, it has the [Undo and Redo Cell Edits](https://dash.plotly.com/dash-ag-grid/undo-redo-edits) feature enabled.

Note the following:
 - The first column is not editable
 - The "Year" row is not editable. See [Conditional Editing](https://dash.plotly.com/dash-ag-grid/cell-editing)
 - The "Hours" row uses a comma for thousands seperator
 - The "Value" row uses a currency format without decimal places.

"""




next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.tips_and_tricks.dag_utilities", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.tips_and_tricks.updating_rowData_with_ValueGetter", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.tips_and_tricks.select_dynamic_options", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.tips_and_tricks.format_by_row", make_layout=make_tabs),
        up_next()
    ],
)

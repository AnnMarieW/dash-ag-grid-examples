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
 
This section is organized like the DataTable Dash docs to make it easier to find similar features in the Dash AG Grid docs.
 
--------------

` `  
` ` 
## Overview Quickstart 

 - Check out the <dccLink href="{links.get_started_V31}" children="Getting Started with V31" /> for an overview of the basic grid features.
 
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


text4 = f"""

## User Guide

### Reference  

See a list of Dash AG Grid props in the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section.  Note that
 AG Grid has hundreds of props that are usable in Dash AG Grid with the `dashGridOptions` prop or accessing the grid's
  API in a clientside callback.  It's necessary to also use the upstream [AG Grid docs]({links.ag_grid_docs}) as reference.

### Grid Height

By default the grid height is set to 400px.  It automatically includes vertical scroll, virtualization and fixed headers.
See:
- [Grid Size](https://dash.plotly.com/dash-ag-grid/grid-size)
- [Pagination](https://dash.plotly.com/dash-ag-grid/pagination)

### Grid Width and Column Width
The grid automatically adds horizontal scroll bars if the grid width is wider than it's container.  

The column width can be adjusted by the user by dragging the handle in the column headers.  It is also highly customizable.
  See the [Column Sizing](https://dash.plotly.com/dash-ag-grid/column-sizing) section.
  
See the [Column Pinning](https://dash.plotly.com/dash-ag-grid/column-pinning) section for info on Fixed Columns.  The user can
 pin one or more columns right or left by dragging the columns.  The column pinning can also be specified in the app and locked in position.
 
If the cell content is wider than the column, the cell content is overflowing into ellipses by default. To set row height
 and word wrapping, see the [Row Height](https://dash.plotly.com/dash-ag-grid/row-height) and [Column Headers](https://dash.plotly.com/dash-ag-grid/column-headers) sections.

### Styling

The style of the Dash AG Grid is highly customizable - see the Layout and Styling section, plus:
- Displaying multiple rows of headers -- see [Grouping Columns](https://dash.plotly.com/dash-ag-grid/column-definitions#grouping-columns)
- Text alignment - By default the data is left aligned.  This can be changed by setting the  [Column Types](https://dash.plotly.com/dash-ag-grid/column-definitions#column-types) or by using CSS in the `cellClass`, `cellStyle` or `headerClass` props.
- Styling the table as a list view - this is the grid default.
- Changing the colors (including a dark theme) - The grid has several themes in both light and dark.  See the [Themes](https://dash.plotly.com/dash-ag-grid/styling-themes) section.

### Conditional Formatting

See:
- [Styling Rows](https://dash.plotly.com/dash-ag-grid/styling-rows)
- [Styling Cells](https://dash.plotly.com/dash-ag-grid/styling-cells)
- <dccLink href="{links.styling}" children="Styling Examples"/> on this site for a Dash AG Grid version of all the conditional styling receipies from the DataTable docs.

### Number Formatting

To see how to format numbers and dates, see:

- [Vale Formatter](https://dash.plotly.com/dash-ag-grid/value-formatters) 
- [D3 Value Formatters](https://dash.plotly.com/dash-ag-grid/d3-value-formatters)
- [Cell Data Types](https://dash.plotly.com/dash-ag-grid/cell-data-types)


### Sorting, Filtering, Selecting, and Paging Natively

- [Cross Filter Example](https://dash.plotly.com/dash-ag-grid/crossfilter) - See a Dash AG Grid version of the app from this section.
- [Filtering](https://dash.plotly.com/dash-ag-grid/column-filters) - Extensive filtering docs.
- [Sorting](https://dash.plotly.com/dash-ag-grid/row-sorting)
- [Row Selection](https://dash.plotly.com/dash-ag-grid/checkbox-row-selection)
- Deleting rows with a button - see the <dccLink href="{links.components_html}" children="Custom Component Gallery"/>



### Tooltips

See the <dccLink href="{links.tooltips}" children="Tooltips Tutorial"/> for displaying tooltips on data and header rows, conditional tooltips, define tooltips for each cell, customize behavior.

### Python-Driven Filtering, Paging, Sorting

See the [Server Side Infinite Row Model](https://dash.plotly.com/dash-ag-grid/infinite-row-model) section.

### Editing

See the [Editing ](https://dash.plotly.com/dash-ag-grid/cell-editing) section
- Determining which cell has changed in  [Editing and Callbacks](https://dash.plotly.com/dash-ag-grid/editing-and-callbacks)
- Adding or removing rows 
    - See forum post[](https://community.plotly.com/t/deleting-rows-in-dash-ag-grid/78700) and Deleting rows with a button - see the <dccLink href="{links.components_html}" children="Custom Component Gallery"/>
    - [Row Transactions](https://dash.plotly.com/dash-ag-grid/client-side)

- Running Python computations on certain columns or cells - See [Value Getters](https://dash.plotly.com/dash-ag-grid/value-getters)
- [Exporting to CSV](https://dash.plotly.com/dash-ag-grid/export-data-csv)
- <dccLink href="{links.import_export}" children="Exporting to Excel with dcc.Download"/>
- [Exporting to Excel with AG Grid Enterprise](https://www.ag-grid.com/react-data-grid/excel-export/)


### Typing and User Input Processing
- See [Cell Data Types](https://dash.plotly.com/dash-ag-grid/cell-data-types)

### Dropdowns Inside DataTable

- [Provided Cell Editor Components](https://dash.plotly.com/dash-ag-grid/provided-cell-editors) - Select component.
- <dccLink href="{links.components_dmc}" children="Custom Components dmc.Select"/>

### Virtualization

Dash AG Grid uses virtualization by default.  See [AG Grid docs](https://www.ag-grid.com/react-data-grid/dom-virtualisation/)


### Filtering Syntax

- [Filtering](https://dash.plotly.com/dash-ag-grid/column-filters) - Extensive filtering docs.



"""

next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        make_md(text4),
       # example_app("examples.components.html_button_delete_rows", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.DataTable.cell_clicked", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.DataTable.active_cell", make_layout=make_tabs),
        up_next(next)
    ],
)

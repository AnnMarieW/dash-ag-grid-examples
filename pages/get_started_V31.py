from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_nav_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Get started with V31", path=links.get_started_V31
)


text1 = """
# Getting Started with Dash AG Grid V31

An introduction to the key concepts of Dash AG Grid and some of the new features available in V31.

This tutorial is based on [Creating a Basic Grid](https://ag-grid.com/javascript-data-grid/deep-dive/) in the AG Grid docs.

## Overview  

Once complete, you'll have an interactive grid, with custom components and formatted data - Try it out for yourself by __sorting, filtering, resizing, selecting, or editing__ data in the grid:
"""

text2 = """
## Create a Basic Grid

Add a beautiful data grid to your Dash app with 3 lines of code!  Simply define the rows and columns:

```python
dag.AgGrid(
    columnDefs=[{"field": i} for i in df.columns],
    rowData=df.to_dict("records"),
)
```
Features available by default:
- Alpine theme is applied to style the grid
- The columns are resizable (drag on the vertical handle in the header)
- The rows are sortable (click on the header to sort. shift-click the header to sort by multiple columns)
- Note the row animation when sorting
- Boolean values are rendered as a checkbox 
- Reorder the columns by dragging the column header


If you are upgrading from dash-ag-grid 2.4, you will notice that a bunch of features are now enabled by default. 
If you prefer to disable these features, see the [Migration Guide](https://dash.plotly.com/dash-ag-grid/migration-guide) in the dash docs.

"""

text3 = """
## Configure Columns

Now that we have a basic grid with some arbitrary data, we can start to configure the grid with Column Properties.

Column Properties can be added to one or more columns to enable/disable column-specific features. Let's try this by adding the `filter: True` property to the 'mission' column:

```python
columnDefs: [
  { "field": "mission", "filter": True },
]
```
We should now be able to filter the 'mission' column - you can test this by filtering for the 'Apollo' missions:

Note: Column properties can be used to configure a wide-range of features; refer to our [Column Properties](https://dash.plotly.com/dash-ag-grid/column-definitions) docs for a full list of features.
"""

text4 = """
## Default Column Definitions

The example above demonstrates how to configure a single column. To apply this configuration across all columns we can use Default Column Definitions instead. Let's make all of our columns filterable by adding the `defaultColDef` property, and setting `filter: True`:

```python
defaultColDef: {
    "filter": True
}
```
Note: Column Definitions take precedence over Default Column Definitions

The grid should now allow filtering on all columns:


"""
text5 = """
## Grid Options

So far we've covered creating a grid, updating the data within the grid, and configuring columns. This section introduces Grid Options, which control functionality that extends across both rows & columns, such as Pagination and Row Selection.

AG Grid is highly customizable and has hundreds of properties. Only a subset of these are defined in the Dash AgGrid
 component. Valid grid-level properties that are not listed in the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section can be used by passing them to the dashGridOptions property on the Dash AgGrid component.

Let's try this by adding `pagination: True` to our `dashGridOptions`:

```python
dag.AgGrid(
    dashGridOptions = {"pagination": True}
)
```

We should now see Pagination has been enabled on the grid:

Note that the `Page Size` control is a new feature enabled by default in V31.

"""

text6 = """
## Format Cell Values
The data supplied to the grid usually requires some degree of formatting. For basic text formatting we can use [Value Formatters.](https://dash.plotly.com/dash-ag-grid/value-formatters)

Value Formatters are basic functions which take the value of the cell, apply some basic formatting, and return a new value to be displayed by the grid. Let's try this by adding the `valueFormatter property` to our 'price' column and returning the formatted value:

In dash-ag-grid, the [d3 format](https://dash.plotly.com/dash-ag-grid/d3-value-formatters) functions are included.  This makes it even easier to formant numbers and dates.

```python
columnDefs = [
  {
    field: "price",
    # Return formatted value
    "valueFormatter": {"function": "d3.format('$,.0f')(params.value)"},
  },
]
```

The grid should now show the formatted value in the 'price' column:
"""

text7 = """
## Custom Cell Components

Value Formatters are useful for basic formatting, but for more advanced use-cases we can use Cell Renderers instead.

Cell Renderers allow you add custom HTML, JavaScript and other Dash components within cells. To use a Cell Renderer, set
 the `cellRenderer` prop on a column, with the value as the name of your Cell Renderer.
 
If you are new to JavaScript see:
 - [Adding Your Own CSS and JS to Dash Apps](https://dash.plotly.com/external-resources)
 - [JavaScript and Dash AG Grid](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid)
 - [Cell Renderer Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components)
 

Let's try this by creating a new component to display the company logo in the 'company' column.

Add the following into a the `dashAgGridComponentFunctions.js` file in the `/assets` folder:

```
var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.CompanyLogoRenderer = function (props) {
  const url = `https://www.ag-grid.com/example-assets/space-company-logos/${props.data.company.toLowerCase()}.png`

  return React.createElement("span", {}, [
    React.createElement("img", {
      style: { width: "25px", height: "auto", filter: "brightness(1.1)" },
      src: url,
    }),
    React.createElement(
      "span",
      {
        style: { paddingLeft: "4px" },
      },
      props.value
    ),
  ]);
};
```

If you aren't very familiar with JavaScript and React, the component can look intimidating.  However, when you see a
 few examples, the syntax starts to make sense.  The above code is a function that returns a component.  Here's what it
 would look like in Python: 
 
```
def company_logo_renderer(company):
    url = f"https://www.ag-grid.com/example-assets/space-company-logos/{company.lower()}.png"
    return html.Span([
        html.Img(src=url, style={ "width": "25px", "height": "auto", "filter": "brightness(1.1)" }),
        html.Span(company, { "paddingLeft": "4px" })
    ])

``` 
"""

text8="""
## Editing and Provided Cell Editors

The grid comes with some [cell editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors) provided out of the box (no need to write your own custom component):

- Text Cell Editor
- Large Text Cell Editor
- Select Cell Editor
- Rich Select Cell Editor (Enterprise only)

New in V31 are some additional cell editors that are generally used with [Cell Data Types](https://dash.plotly.com/dash-ag-grid/cell-data-types):

- Number Cell Editor
- Date Cell Editor
- Checkbox Cell Editor

In the grid below, we have filter and editing enabled.  The Cell Data Types are inferred and the following features
 are enabled automatically!

- The **Text** columns has a `text` data type. It uses a text editor and the values are sorted and filtered as strings.
- The **Number** columns has a `number` data type. It uses a number editor and number filter.
- The **dateString** column has a `dateString` data type. The date editor, date filter and sort works automatically if
  the date is in the format yyyy-mm-dd.
- The **Boolean** column has a `boolean` data type. The value renders as a checkbox and it uses a checkbox filter.
"""

text9="""
## With callbacks

Certain props will trigger calback in Dash.  See the full list in the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section of the Dash docs.

In this example, we will track what data was changed in a callback.

Note that in V31, the `cellValueChanged` prop is a list of dicts rather than a dict.  If you are upgrading from V2.x, please see the Migration guide for more info.
See also the [Editing and Callbacks](https://dash.plotly.com/dash-ag-grid/editing-and-callbacks) section of the Dash docs.

This last example has a few more features:
 - Multiple Rows are selectable.  For more info see [Selection](https://dash.plotly.com/dash-ag-grid/checkbox-row-selection) section.
 - The row animation is disabled when you sort, filter or move columns
 - The date is formatted using the D3 functions
 - Numeric columns are right aligned
 
"""

text10 = """
## Summary
Congratulations! You've completed the tutorial and built your first grid. By now, you should be familiar with the key concepts of AG Grid:

- __Row Data__: Your data, in JSON format, that you want the grid to display.

- __Column Definitions__: Define your columns and control column-specific functionality, like sorting and filtering.

- __Default Column Definitions__: Similar to Column Definitions, but applies configurations to all columns.

-  __Grid Options__: Configure functionality which extends across the entire grid.

- __Value Formatters__: Functions used for basic text formatting

- __Cell Renderers__: Add your own components to cells

- __Editing__:  Editing cells with provided text, number, date and checkbox editors

- __Callbacks__ : Events that trigger Dash callbacks, typically as a result of user interaction.

## Next Steps
- See more features in the Dash docs and the AG Grid docs

Happy Coding!

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.get_started.V31_tutorial", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.get_started.V31_quickstart", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.get_started.V31_columns", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.get_started.V31_defaultcoldef", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.get_started.V31_pagination", make_layout=make_tabs),
        make_md(text6),
        example_app("examples.get_started.V31_format", make_layout=make_tabs),
        make_md(text7),
        example_app("examples.get_started.V31_component", make_layout=make_tabs),
        make_md(text8),
        example_app("examples.get_started.V31_editable", make_layout=make_tabs),
        make_md(text9),
        example_app("examples.get_started.V31_tutorial_callbacks", make_layout=make_tabs),
        make_md(text10),
        up_next()
    ],
)

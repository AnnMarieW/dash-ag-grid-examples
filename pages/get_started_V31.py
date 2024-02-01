from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
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

Add a beautiful data grid to your Dash app with 3 lines of code!  

The `rowData` defines the data and the `columnDefs` control how the data is displayed. In this example, the data is in
 a Pandas dataframe.

```python
dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],    
)
```

- Alpine theme is applied to style the grid
- The columns are resizable (drag on the vertical handle in the header)
- The rows are sortable (click on the header to sort. shift-click the header to sort by multiple columns)
- Note the row animation when sorting
- Boolean values are rendered as a checkbox 
- Reorder the columns by dragging the column header
- Pin a column to the right or left side of the grid


Features available by default:
- Alpine theme is applied to style the grid.
- The columns are resizable by dragging on the vertical handle in the header.  (Resizing coluns is enabled by default in V31)
- The rows are sortable.  Click click on the header to sort. shift-click the header to sort by multiple columns. (Sorting is enabled by default in V31)
- There is row animation when sorting (This is enabled by default in V31)
- Boolean values are rendered as a checkbox. (Cool new default in V31)
- Reorder the columns by dragging the column header
- Pin a column to the right or left side of the grid by dragging the column header and holding near the grid edge until the pin icon appears.


If you are upgrading from dash-ag-grid 2.4, you will notice that a bunch of features are now enabled by default. 
If you prefer to disable these features, see the [Migration Guide](https://dash.plotly.com/dash-ag-grid/migration-guide) in the dash docs.

"""

text3 = """
## Configure Columns

Now that we have a basic grid with some data, we can start to configure the grid with Column Properties.

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

The grid should now allow filtering on all columns.  Note that the filters are different based on the type of data.
- The Success column has a dropdown that displays True and False
- The Price has a number filter
- The date has a date filter with a date picker component
- The other columns have a text filter.

New in V31: The data type is inferred by default.  See more information in the [Cell Data Type](https://dash.plotly.com/dash-ag-grid/cell-data-type) section.


"""
text5 = """
## Grid Options

So far we've covered creating a grid, updating the data within the grid, and configuring columns. This section introduces Grid Options, which control functionality that extends across both rows & columns, such as Pagination and Row Selection.

AG Grid is highly customizable and has msny properties. Only a subset of these are defined in the Dash AG Grid
 component. Valid grid-level properties that are not listed in the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section can be used by passing them to the dashGridOptions property on the Dash AgGrid component.

Let's try this by setting `pagination=True` in `dashGridOptions`:

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

Value Formatters are basic functions which take the value of the cell, apply some basic formatting, and return a new value to be displayed by the grid. 
In Dash, it's not possible to have functions as props.  Instead we use a dictionary with `"function"` as the key and the value is the javascript function to execute.
You can find more information the  [Dash docs](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid).

In dash-ag-grid, the [d3 format](https://dash.plotly.com/dash-ag-grid/d3-value-formatters) functions are included.  This makes it even easier to formant numbers and dates.

Let's try this by adding the `valueFormatter property` to our 'price' column.

```python
columnDefs = [
  {
    field: "price",
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
 

If you are new to JavaScript see the Dash Docs:
 - [Adding Your Own CSS and JS to Dash Apps](https://dash.plotly.com/external-resources)
 - [JavaScript and Dash AG Grid](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid)
 - [Dash AG Grid Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components)
 

Let's try this by creating a new component to display the company logo in the 'company' column.

If you don't have one already, add a folder called `assets` in the same folder as your app.  Dash automatically
 serves the files in this folder.

```
- app.py
- assets/
    |-- dashAgGridComponentFunctions.js   
```

`dashAgGridComponentFunctions.js`
```js
var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});
  
dagcomponentfuncs.CompanyLogoRenderer = function (props) {
  var url = "https://www.ag-grid.com/example-assets/space-company-logos/" + props.value.toLowerCase() + ".png";
  return React.createElement(
    "span",
    null,
    React.createElement("img", { src: url, style: { width: "25px", height: "auto", filter: "brightness(1.1)" } }),
    React.createElement("span", { style: { paddingLeft: "4px" } }, props.value)
  );
}
```

Let's take a closer look at this file.  The first two lines defines a JavaScript variable  `dagcomponentfuncs`.  It defines
an object in the global window namespace.  Variables defined in this namespace are registered as custom components in Dash AG Grid.

Next we add our component called `CompanyLogoRenderer` to the `dagcompoentfuncs` object. For those familiar with React,
 you will see that the `CompanyLogoRenderer` is a function that returns a [React element without  using JSX](https://react.dev/reference/react/createElement#creating-an-element-without-jsx). 
 
To make this look a little more familiar to Python coders, let's translate it to Python.  This is a funtion that returns
 a component using Dash html components.  (Don't use this Python function - it's just for illustration.)
 
```python
def company_logo_renderer(company):
    url = f"https://www.ag-grid.com/example-assets/space-company-logos/{company.lower()}.png"
    return html.Span([
        html.Img(src=url, style={ "width": "25px", "height": "auto", "filter": "brightness(1.1)" }),
        html.Span(company, { "paddingLeft": "4px" })
    ])
``` 

Now we can use the `CompanyLogoRenderer` in our app like this:

```python
columnDefs = [   
    {
      "field": "company",    
      "cellRenderer": "CompanyLogoRenderer"
    },
    #... 
]
```

Be sure to check out the dash docs [Cell Renderer](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section for more details and examples.  Plus check out all the components in the  <dccLink href="/" children="Dash AG Grid Custom Component Gallery" /> 

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

text10 = f"""
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

- See the [Dash docs]({links.dag_docs}) and the [AG Grid docs]({links.ag_grid_docs}) for details on all the features.

- Have questions?  Ask them on the [Dash Community Form]({links.forum})

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

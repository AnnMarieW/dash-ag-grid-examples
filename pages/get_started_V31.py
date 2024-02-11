from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc

import utils.links
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Getting started with V31", path=links.get_started_V31
)


text1 = """
# Getting Started with Dash AG Grid V31

An introduction to the key concepts of Dash AG Grid and some of the new features available in V31.

This tutorial is based on [Creating a Basic Grid](https://ag-grid.com/javascript-data-grid/deep-dive/) in the AG Grid docs.

## Overview  

Once complete, you'll have an interactive grid, with custom components and formatted data - Try it out for yourself by __sorting, filtering, resizing, selecting, or editing__ data in the grid:
"""

text2 = """

## Quick Start

Make your first grid in less than 5 minutes!  


```python

import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

app.layout = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

app.run(debug=True)

```

__Basic grid features enabled by default in Dash AG Grid V31:__

- __Alpine Theme Styling__: The grid comes styled with the Alpine theme, available in both light and dark modes.
- __Column Resizing__: Resize columns by dragging the vertical handle in the header.
- __Sorting Rows__: Click on the header to sort rows; use shift-click for sorting by multiple columns. 
- __Animation__: See the smooth row animation during sorting and filtering.
- __Boolean Values as Checkboxes__: Boolean values are automatically rendered as checkboxes.
- __Column Reordering__: Change the order of the columns by dragging the column header.
- __Column Pinning__: Pin a column to the right or left side of the grid by dragging the column header.

The V31 release has many grid features enabled by default, which means  __more features with less code__.   If
 you've used previous versions of Dash AG Grid, please see the [Migration Guide](https://dash.plotly.com/dash-ag-grid/migration-guide) to help you upgrade to the latest release.
"""

text3 = """
## Configure Columns

Now that we have a basic grid with some data, we can start to configure the grid with Column Properties.

Column Properties can be added to one or more columns to enable/disable column-specific features. Let's try this by adding the `filter: True` property to the 'mission' column:


```python
columnDefs=[
  {"field": "mission", "filter": True},
  {"field": "company"},
  #... other columns
]
```
You'll now be able to filter the "mission" column -- give it a try by filtering for the "Apollo" missions.

Note: Column properties can be used to configure a wide-range of features; refer to the [Column Properties](https://dash.plotly.com/dash-ag-grid/column-definitions) docs for a full list of features.
"""

text4 = """
## Default Column Definitions
The example above demonstrates how to configure a single column. To apply this configuration across all columns we can
use Default Column Definitions instead. Let's make all of our columns filterable by adding the `defaultColDef` property,
and setting `filter=True`:

```python
dag.AgGrid(
    defaultColDef={"filter": True}
)
```


The grid will now allow filtering on all columns. Note that the Column Definitions take precedence over Default Column Definitions.

In the example below you'll see different types of filters used based on the [Cell Data Type](https://dash.plotly.com/dash-ag-grid/cell-data-types). 
This is one of the great new features available in this release.

- The "Successful" column, with boolean data, has a dropdown filter with True and False selections
- The "Price" has a [Number Filter](https://dash.plotly.com/dash-ag-grid/number-filters)
- The "Date" has a [Date Filter](https://dash.plotly.com/dash-ag-grid/date-filters) with a date picker component
- The other columns have the default [Text Filter](https://dash.plotly.com/dash-ag-grid/text-filters).

"""

text4b = """

### Cell Data Types and Automatic Type Inference  

In this release, Dash AG Grid introduces built-in cell data types featuring automatic type inference from column data. Beyond
 just filtering, as demonstrated in the above example, the grid can now automatically configure columns for rendering,
  editing, row grouping (an Enterprise feature), and Import & Export based on the data type. You have the flexibility 
  to override predefined cell data types and even create fully custom data types for handling complex objects, such
   as dicts or lists within cells.

This means that tasks that previously required manual column configuration can now be automated by the grid. This is
 another new low code feature in this latest release.

See more information in the [Cell Data Types](https://dash.plotly.com/dash-ag-grid/cell-data-types) section of the Dash Docs.

"""

text5 = """
## Grid Options
So far we've covered creating a grid and configuring columns. This section introduces Grid Options, which control
functionality that extends across both rows & columns, such as Pagination and Row Selection.

AG Grid is highly customizable and has many props -- only a subset of these are defined as separate props in the Dash AG Grid component.
Valid grid-level properties that are not listed in the [reference]() section in the Dash docs can be used by passing
them to the `dashGridOptions` property on the Dash AG Grid component.

Let's try this by setting `pagination=True` in the `dashGridOptions` prop:

```python
dag.AgGrid(
    dashGridOptions={"pagination": True}
)
```
You'll now see Pagination is enabled on the grid.  Note that the Page Size control is a new feature enabled by default
in Dash AG Grid V31.

"""

text6 = """
## Format Cell Values
The data supplied to the grid usually requires some degree of formatting. For basic text formatting we can use [Value Formatters.](https://dash.plotly.com/dash-ag-grid/value-formatters)

Value Formatters are functions which take the value of the cell, apply some formatting, and return a new value to be displayed by the grid. 
In Dash, it's not possible to have functions as props.  Instead we use a dictionary with `"function"` as the key and the value is the JavaScript function to execute.
You can find more information the  [Dash docs](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid).

In Dash AG Grid, the [d3 format](https://dash.plotly.com/dash-ag-grid/d3-value-formatters) functions are included.  This makes it even easier to formant numbers and dates.

Let's try this by adding the `valueFormatter property` to our "price" column.

```python
columnDefs = [
  {
    field: "price",
    "valueFormatter": {"function": "d3.format('$,.0f')(params.value)"},
  },
]
```

The grid now shows the formatted value in the "price" column:
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
 
To make this look a little more familiar to Python coders, let's translate it to Python.  This is a function that returns
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

The grid provides several built-in [cell editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors), eliminating the need to create custom components for the following:

- __Text Cell Editor__: The default editor, is a standard HTML `input` component
- __Large Text Cell Editor__: is an HTML `textarea` component
- __Select Cell Editor__: is an HTML `select` component
- __Rich Select Cell Editor__ (Enterprise only): A custom dropdown component
- __Number Cell Editor__*: is an HTML number `input` 
- __Date Cell Editor__*:  is an HTML date `input`
- __Checkbox Cell Editor__*: is an HTML checkbox `input`

`*` New components available in V31

Let's try this by making all the data editable.  We do this by adding `editable=True` to the `defaultColDef` prop:


```python
dag.AgGrid(
    defaultColDef={"editable": True, "filter":True}
)
```
The grid automatically uses the appropriate cell editors based on the Cell Data Type, just as it selects filters according to data type.

See the new number, date and checkbox editor in action!:
- The "Successful" column uses the Checkbox Cell Editor
- The "Price" uses the Number Cell Editor
- The "Date" uses the  Date Cell Editor
- The other columns use the Text Cell Editor.

"""

text8b = """

## Configuring the Provided Cell editors

You can configure the provided cell editors by passing parameters to the `cellEditorParams` prop. See the option for each
component in the  [Provieded Cell Editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors) documentation.

In the example above, we've configured the number editor to:

- Display stepper buttons within the component.
- Restrict entry to positive numbers by setting `min=0`.
- Ensure whole numbers only by setting `precision=0`.

```python
columnDefs = [
    {
       "field": "price",     
       "cellEditorParams": {"showStepperButtons": True, "min": 0, "precision": 0}
    },
]
```
"""

text9="""
## With callbacks

Certain props will trigger callbacks in Dash.  See the full list in the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section of the Dash docs.

In this example, we will track what data was changed in a callback.

Note that in V31, the `cellValueChanged` prop is a list of dicts rather than a dict.  If you are upgrading from V2.x, please see the Migration guide for more info.
See also the [Editing and Callbacks](https://dash.plotly.com/dash-ag-grid/editing-and-callbacks) section of the Dash docs.

This last example has a few more features:
 - Multiple Rows are selectable.  For more info see [Selection](https://dash.plotly.com/dash-ag-grid/checkbox-row-selection) section.
 - The row animation is disabled when you sort, filter or move columns
 - The date is formatted using the D3 functions
 - Numeric columns are right aligned 
"""

text10= """

## AG Grid Enterprise Features

Explore additional features with AG Grid Enterprise. A license is required; check [AG Grid docs for pricing details.](https://www.ag-grid.com/license-pricing/)

In AG Grid Enterprise, unlock functionalities like Grouping, Aggregation, Advanced Filtering, Hierarchical Data Support
& Tree View, Data Export to Excel, Excel-like Pivoting, Copy/Paste, Sparklines and more.

The Enterprise section in Dash Grid docs provides only a few examples, so please refer to the AG Grid documentation for details.


Here's a new Enterprise feature in Dash AG Grid V31.  You won't find this in the Dash Docs yet, but it's available in this release.

### Advanced Filter (AG Grid Enterprise license required)

The Advanced Filter allows for complex filter conditions to be entered across columns in a single type-ahead input, as well as within a hierarchical visual builder.

See this app live in the [AG Grid Docs](https://www.ag-grid.com/react-data-grid/filter-advanced/)


"""

text11 = f"""
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
        make_md(text4b),
        make_md(text5),
        example_app("examples.get_started.V31_pagination", make_layout=make_tabs),
        make_md(text6),
        example_app("examples.get_started.V31_format", make_layout=make_tabs),
        make_md(text7),
        example_app("examples.get_started.V31_component", make_layout=make_tabs),
        make_md(text8),
        example_app("examples.get_started.V31_editable", make_layout=make_tabs),
        make_md(text8b),
        make_md(text9),
        example_app("examples.get_started.V31_tutorial_callbacks", make_layout=make_tabs),
        make_md(text10),
       # example_app("examples.get_started.V31_advanced_filter", make_layout=make_tabs),
        make_feature_card(utils.links.advanced_filter_dark_gif, ""),
        make_md(text11),
        up_next()
    ],
)

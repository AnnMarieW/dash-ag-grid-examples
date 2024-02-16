

# Getting Started with Dash AG Grid V31

Elevate your Dash app's data visualization capabilities with [Dash AG Grid](https://dash.plotly.com/dash-ag-grid), a high-performance and highly customizable Dash component that wraps [AG Grid](https://ag-grid.com/): "The best JavaScript grid in the world."

I'm thrilled to announce the recent release of Dash AG Grid V31.0.0, aligning with AG Grid V31.0.3 and encompassing all its cutting-edge features. If you haven't tried Dash AG Grid yet, this is a great time to take it for a spin. The V31 release has many  grid features enabled by default, which means  __more features with less code__.  You'll be amazed at how easy it is to add this beautiful, feature rich data grid to your Dash app. If you've used previous versions of Dash AG Grid, please see this [Migration Guide](https://dash.plotly.com/dash-ag-grid/migration-guide) to help you upgrade to the latest release.

I've been a member of the Dash community team contributing to the development of Dash AG Grid since Plotly's decision to [open source this component last year](https://medium.com/plotly/announcing-dash-ag-grid-fbb4a1c83e62). My main focus has been on testing and documentation. Bryan Schroeder has taken the lead in developing the component, while Sébastien Didier has played a pivotal role in enhancing the documentation. Throughout this project, we've received invaluable mentorship from Alex Johnson, Plotly's CTO, and Liam Conners from the technical writing team. This project has been a great learning experience, and I'm excited to be part of the team working to make AG Grid available to all Dash users.

This article draws inspiration from the AG Grid documentation's ["Creating a Basic Grid" tutorial](https://www.ag-grid.com/javascript-data-grid/deep-dive/). I'll walk you through getting started with Dash AG Grid, focusing on the **free** AG Grid Community features, then touch on some of the advanced features you can unlock with an AG Grid Enterprise license.

## Quick Start


AG Grid is a powerful and feature-rich JavaScript datagrid library for creating interactive and customizable tables in web applications. Dash AG Grid extends its functionality to Python developers within the Dash framework, providing a seamless integration for creating dynamic data tables in Python-based web apps.

Create a Dash app to display data with AG Grid in less than five minutes!  

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

![ag-grid-v31a](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/74fe86e1-eb54-4dec-915f-d692f2c8cead)

__Basic grid features enabled by default in Dash AG Grid V31:__

- __Alpine Theme Styling__: The grid comes styled with the Alpine theme, available in both light and dark modes.
- __Column Resizing__: Resize columns by dragging the vertical handle in the header.
- __Sorting Rows__: Click on the header to sort rows; use shift-click for sorting by multiple columns. 
- __Animation__: See the smooth row animation during sorting and filtering.
- __Boolean Values as Checkboxes__: Boolean values are automatically rendered as checkboxes.
- __Column Reordering__: Change the order of the columns by dragging the column header.
- __Column Pinning__: Pin a column to the right or left side of the grid by dragging the column header.

If you just want to add a basic grid to your app, you can stop here.  But if you'd like to explore advanced capabilities, I'll show you how to filter, edit, format, and select the data in the next section.  I'll also demonstrate how to add pagination, custom components, and 
interaction with the grid in Dash callbacks.  

Access live examples and full code for each app featured in this article at the [Dash AG Grid Examples](https://dashaggridexamples.pythonanywhere.com/get-started-v31) site. There, you'll also  find additional tutorials, examples, and a gallery of custom components.


## Configure Columns

Now that we have a basic grid with some data, let's configure the grid using Column Properties. Use Column Properties to configure a wide range of features; check out the [Columns documentation](https://dash.plotly.com/dash-ag-grid/column-definitions) for a complete list of options.


Add Column Properties to enable/disable column-specific features in one or more columns. Try this by setting`filter=True` in the "mission" column.

```python
columnDefs=[
  {"field": "mission", "filter": True},
  {"field": "company"},
  #... other columns
]
```
You'll now be able to filter the "mission" column --- give it a try by filtering for the "Apollo" missions.


## Default Column Definitions
The example above demonstrates how to configure a single column. To apply this configuration across all columns, we can use Default Column Definitions instead. Let's make all of our columns filterable by adding the `defaultColDef` property, and setting `filter=True`:

```python
dag.AgGrid(
    defaultColDef={"filter": True}
)
```


The grid will now allow filtering on all columns. Note that the Column Definitions take precedence over Default Column Definitions.

In the example below, you'll see different types of filters used based on the [Cell Data Type](https://dash.plotly.com/dash-ag-grid/cell-data-types). 
This is one of the great new features available in this release.

- The "Successful" column, with boolean data, has a dropdown filter with True and False selections
- The "Price" has a [Number Filter](https://dash.plotly.com/dash-ag-grid/number-filters)
- The "Date" has a [Date Filter](https://dash.plotly.com/dash-ag-grid/date-filters) with a date picker component
- The other columns have the default [Text Filter](https://dash.plotly.com/dash-ag-grid/text-filters).


![ag-grid-v31b](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/549968be-faf3-4e5d-b123-f10f43ff54f7)

### Cell Data Types and Automatic Type Inference
In this release, Dash AG Grid introduces built-in cell data types featuring automatic type inference from column data. 
Beyond just filtering, as demonstrated in the above example, the grid can now automatically configure columns for rendering, editing, row grouping (an Enterprise feature), and Import & Export based on the data type. You have the flexibility to override predefined cell data types and even create fully custom data types for handling complex objects, such as dicts or lists within cells.

This means that tasks that previously required manual column configuration can now be automated by the grid. This is another new low code feature in this latest release.

See more information in the [Cell Data Types](https://dash.plotly.com/dash-ag-grid/cell-data-types) section of the Dash Docs.



## Grid Options
So far, I've covered creating a grid and configuring columns. This section introduces Grid Options, which control functionality that extends across both rows & columns, such as Pagination and Row Selection.

AG Grid is highly customizable and has many props --- only a subset of these are defined as separate props in the Dash AG Grid component. Valid grid-level properties that are not listed in the [reference](https://dash.plotly.com/dash-ag-grid/reference) section in the Dash docs can be used by passing them to the `dashGridOptions` property on the Dash AG Grid component.

Let's try this by setting `pagination=True` in the `dashGridOptions` prop:

```python
dag.AgGrid(
    dashGridOptions={"pagination": True}
)
```
You'll now see Pagination is enabled on the grid.  Note that the Page Size control is a new feature enabled by default in Dash AG Grid V31.


![image](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/e9b5c003-2257-477c-bf74-e503d0e1bd79)

## Format Cell Values
The data supplied to the grid usually requires some degree of formatting. For basic text formatting we can use [Value Formatters](https://dash.plotly.com/dash-ag-grid/value-formatters).

Value Formatters are functions which take the value of the cell, apply some formatting, and return a new value to be displayed by the grid. In Dash, it is not possible to have functions as props. Instead we use a dictionary with "function" as the key and the value is the JavaScript function to execute. You can find more information in the [Dash docs](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid).

In Dash AG Grid, the [d3 format functions](https://dash.plotly.com/dash-ag-grid/d3-value-formatters) are included. This makes it even easier to formant numbers and dates.

Let's try this by adding the `valueFormatter` property to our "price" column.

```python
columnDefs = [
  {
    "field": "price",
    "valueFormatter": {"function": "d3.format('$,.0f')(params.value)"},
  },
]
```
The grid now shows the formatted value in the "price" column:


![formatted_price](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/bf968528-1e33-40f5-ad23-034381a75b78)


## Custom Cell Components

Value Formatters are useful for basic formatting, but for more advanced use-cases we can use [Cell Renderer Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) instead.

Cell Renderers allow you to add custom HTML, JavaScript and other Dash components within cells. To use a Cell Renderer, set the `cellRenderer` prop on a column, with the value as the name of your Cell Renderer.
 

If you are new to JavaScript see the Dash Docs:
 - [Adding Your Own CSS and JS to Dash Apps](https://dash.plotly.com/external-resources)
 - [JavaScript and Dash AG Grid](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid)
 - [Dash AG Grid Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components)
 

Let's try this by creating a new component to display the company logo in the "company" column.

If you don't have one already, add a folder called `assets` in the same folder as your app.  Dash automatically serves the files in this folder.

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

Now we can use the `CompanyLogoRenderer` in our app like this:

```python
columnDefs=[   
    {
      "field": "company",    
      "cellRenderer": "CompanyLogoRenderer"
    },    
]
```

Be sure to check out the dash docs [Cell Renderer](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section for more details and examples.  Also, check out all the components in the  [Dash AG Grid Custom Component Gallery](https://dashaggridexamples.pythonanywhere.com/)

![cell_renderer](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/d8e0f837-bfb3-4496-92a4-4a13553d468c)

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

See the new number, date and checkbox editor in action:
- The "Successful" column uses the Checkbox Cell Editor
- The "Price" uses the Number Cell Editor
- The "Date" uses the  Date Cell Editor
- The other columns use the Text Cell Editor.

![ag-grid-v31c](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/99e525ec-3019-4b8a-8293-5fa124012b61)

## Configuring the Provided Cell editors

You can configure the provided cell editors by passing parameters to the `cellEditorParams` prop. See the option for each component in the  [Provided Cell Editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors) documentation.

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
## With callbacks
Certain properties in Dash AG Grid can trigger Dash callbacks. Please refer to the [Reference](https://dash.plotly.com/dash-ag-grid/reference) section of the Dash documentation.

In the following example, I'll show how to track changes in data using a callback.

This example includes several more features:
 - Multiple Rows are selectable.  For more info see [Selection](https://dash.plotly.com/dash-ag-grid/checkbox-row-selection) section.
 - The row animation is disabled when you sort, filter or move columns
 - The date is formatted using the D3 functions
 - Numeric columns are right aligned

Be sure to try it out for yourself in the live version at [Dash AG Grid Examples](https://dashaggridexamples.pythonanywhere.com/get-started-v31)


![ag-grid-callback](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/266afdbb-cabe-41dc-b850-41c6a07a2d89)


## AG Grid Enterprise Features

Explore additional features with AG Grid Enterprise. A license is required; check [AG Grid docs for pricing details.](https://www.ag-grid.com/license-pricing/)

In AG Grid Enterprise, unlock functionalities like Grouping, Aggregation, Advanced Filtering, Hierarchical Data Support & Tree View, Data Export to Excel, Excel-like Pivoting, Copy/Paste, Sparklines and more.

The Enterprise section in Dash Grid docs provides only a few examples, so please refer to the AG Grid documentation for details.


Here's a new Enterprise feature in Dash AG Grid V31.  You won't find this in the Dash Docs yet, but it's available in this release.

### Advanced Filter (AG Grid Enterprise license required)

The Advanced Filter allows for complex filter conditions to be entered across columns in a single type-ahead input, as well as within a hierarchical visual builder.

```python
import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv")

app.layout = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"filter": True},
    dashGridOptions={"enableAdvancedFilter": True},
    enableEnterpriseModules=True,
   # licenseKey= enter your license key here
)

app.run(debug=True)
```

See this app live in the [AG Grid Docs](https://www.ag-grid.com/react-data-grid/filter-advanced/)
![ag-grid-advanced-filter-light](https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/c0fb4069-2dcb-485a-af61-1d9fda724e31)

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

- See the [Dash docs](https://dash.plotly.com/dash-ag-grid) and the [AG Grid docs](https://ag-grid.com/) for details on all the features.

- Have questions?  Ask them on the [Dash Community Form](https://community.plotly.com/)

Happy Coding!







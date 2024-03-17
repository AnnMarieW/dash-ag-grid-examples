from dash import html, dcc, register_page

from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: External Filters", path=links.external_filters
)

text1 = """
# How to use external filters with Dash AG Grid 

Understanding when to use external filters in Dash AG Grid can greatly enhance your data filtering options. While the 
built-in [Column Filters](https://dash.plotly.com/dash-ag-grid/column-filters) are the easiest way to filter data in the grid, there are times when using other Dash 
components for filtering can be helpful.

The external filters allows you to blend your custom filtering logic with the grid's built-in features,
 providing a flexible approach to data filtering. 
 
In this tutorial, I'll show how to use the grid's External Filter API and discuss alternatives such as updating the
 `rowData` or the Filter Model in a callback.


## When to use External Filters

Below you will find two use-cases for using external components to filter the data in the grid:

1. Using  `dcc.Graph` features such as hover data or click data to filter data in the grid.
2. Using a side panel for multi-component filtering.  Use Dash components to filter not just the grid, but also update other components on the page.

### Example 1: Using a graph to filter the grid
"""

text1a = """
### Example 2: Using multiple Dash components to filter the grid
"""

text2="""

## How to use External Filters  

You can use callbacks to filter the data in the grid based on external Dash components. Here are 3 ways:

1. Using the [External Filter API](https://dash.plotly.com/dash-ag-grid/external-filter)
2.  Updating `rowData`
3. Updating the [Filter Model](https://dash.plotly.com/dash-ag-grid/callback-filters)

Please be sure to see the Dash AG Grid docs [Filtering](https://dash.plotly.com/dash-ag-grid/filtering-overview) sections for all the details.


### 1. External Filter

The [External Filter API](https://dash.plotly.com/dash-ag-grid/external-filter) allows you to mix your own filtering logic with the grid's built-in filtering.

In a callback, simply update the `dashGridOptions` with these two methods:

- `isExternalFilterPresent` (function) Set to "true" is there is an external filter, else "false"
- `doesExternalFilterPass` (function) A JavaScript function to filter the data

This example uses the value of the dropdown to filter the grid's "year" column.  Here's the callback.

```
@callback(
    Output("grid", "dashGridOptions"),
    Input("dropdown", "value"),
)
def update_rows(value):
    return {
        "isExternalFilterPresent": {"function": "false" if value is None or value == [] else "true"},
        "doesExternalFilterPass": {"function": f"{value}.includes(params.data.year)"}
    }
```

Note that you simply provide the function to filter the grid, rather than sending all the filtered data to the grid in the callback.
The grid uses the function to filter the data on the clientside. 

Note also that you will not see the dropdown selections shown in the  grid's built-in filters. You can still use the
 grid's filters -- try entering values in the column filters.
"""

text3 = """

### 2. Update `rowData`

For comparison, you could get the same result by updating the `rowData` in a callback.  However this is much
less efficient because a lot of data is being passed between the server and the client. 

Here's what the callback would look like: 


```python
@callback(
    Output("grid", "rowData"),
    Input("dropdown", "value"),
)
def update_rows(value):
    if value is None or value == []:
        return df.to_dict("records")

    dff = df[df['year'].isin(value)]
    return dff.to_dict("records")
```


Note that if the grid was editable, you would also need to include the `rowData` as a `State` in the callback to capture
 the edited data. This step would not be necessary when using the External Filter.
 
"""



text4 = """

### 3. Filter Model

Another way to filter grid data with external components is to update the [Filter Model](https://dash.plotly.com/dash-ag-grid/callback-filters) in a callback.  

When the user interacts with the built-in column filters, the grid keeps track of what was entered in the Filter Model.
When you update the Filter Model in a callback, it works as if the user made the selections from the column filter.

See more information in the [Column Filters](https://dash.plotly.com/dash-ag-grid/column-filters) section of the Dash docs,


Here's the same example, but we now use the Filter Model.  Note that unlike when you filter the data
by updating `rowData` or using the External Filter, you can see the grid's column filter is updated too.


"""

text5="""

## Hide Column Filters

When using external filters, it enhances the user experience to hide the column filter for columns with external filters.
 
In this example, note that the "year" column does not have a floating filter, and the icon to interact with the column filters is hidden.

 
 ```python
 columnDefs = [
    {"field": "year", "suppressMenu": True, "floatingFilter": False} 
 ]
 ``` 

"""

text6 = """
## Summary

This tutorial discussed three ways to use external components to filter data in the grid.  Here's when to use each:

External Filter
 - Filters data by providing a JavaScript function in a callback
 - Easy to use and fast.  Only available when using the Clientside Row Model
 
Filter Model
 - Filters data using the built-in column filter by updating the Filter Model in a callback. 
 - Good for large data sets. Can be used with both Clientside Row Models and Infinite Row Model.
 - Updating the Filter Model does not require any JavaScript.

Updating rowData
 - Filters data by updating the `rowData` in a callback.
 - OK to use with small data sets, but this method is not recommended.

"""



text_next = f"""
## Next Steps


- If you've found Dash AG Grid valuable, show your support by starring us on [GitHub](https://github.com/plotly/dash-ag-grid)! 🌟.
- Have questions or want to join the conversation? Head over to the [Dash Community Forum](https://community.plotly.com/). 

Happy Coding!

"""

next = f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.external_filters.external_filter_graph", make_layout=make_tabs),
        make_md(text1a),
        example_app("examples.external_filters.external_filter_panel", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.external_filters.external_filter_dropdown", make_layout=make_tabs),
        make_md(text3),
        make_md(text4),
        example_app("examples.external_filters.filter_model", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.external_filters.filter_model2", make_layout=make_tabs),
        make_md(text6),
        make_md(text_next),
        up_next()
    ],
)

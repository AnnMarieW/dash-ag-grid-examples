from dash import html, dcc, register_page

from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Accessing the Grid's API", path=links.grid_api
)

text1 = """

# How to use the AG Grid API with Dash 

## Overview
In this tutorial, I'll cover:
- Accessing the Grid's API in a Dash Clientside Callback
- Determining the Correct AG Grid Docs Version for Dash AG Grid
- Examples: Flashing Cells using the Grid's API
- Differentiating Between Dash AG Grid Functions: `getApiAsync` and `getApi`


## Using the Grid API
The grid is highly configurable and has an [extensive API]( https://www.ag-grid.com/react-data-grid/reference/). Not all
AG Grid props and methods are defined as Dash props, but you can still use them.

Many advanced features require using the Grid's API.  You can access the grid's API in Dash using `getApi` or 
`getApiAsync` in a clientside callback.   I'll use `getApiAsync` in the next couple examples, then later explain the 
difference between the functions.


## Determining the Correct AG Grid Docs Version for Dash AG Grid

Note that not all the grid's features are included in the Dash Docs, so it's necessary to also refer to AG Grid docs. 
Given AG Grid's frequent releases, you may often find it necessary to use an archived version of their docs.

Starting with Dash AG Grid V31.0.0, you can find your grid version by using `dag.grid_version`

```python
import dash_ag_grid as dag 

print("dash-ag-grid version: ", dag.__version__)
print("AG Grid version: ", dag.grid_version)
```

Now, navigate to the  [AG Grid docs archive](https://www.ag-grid.com/archive/)  to find the appropriate documentation
link. If you can't locate an exact match, use the version one minor step lower.  

In the following examples, I'll show how to use the grid's API to flash cells (a feature that is not yet in the Dash docs, but coming soon!).
It's important to use the archived version of AG Grid docs, because the in a later version, AG Grid changed some prop names.

In this tutorial I'm using Dash AG Grid V31.0.1 which uses grid version 31.0.3.

> Please follow along using the AG Grid docs for Flashing Cells https://www.ag-grid.com/archive/31.0.2/react-data-grid/flashing-cells/

## Example 1: Flashing Cells using the Grid's API

The grid can flash cells to highlight data changes. This is a great visual indicator to users of the grid who want data changes to be noticed.



Here I'm just going to provide a Dash version of the examples from the AG Grid docs.  Please refer to the [AG Grid docs]( https://www.ag-grid.com/archive/31.0.2/react-data-grid/flashing-cells/)
for all the details about the `flashCells` method.

"""

text2 = """

Let's take a closer look at the callback function to flash the columns.

In the AG Grid docs (React), they get the grid's API using `gridRef.current.api`:
```
const onFlashTwoColumns = useCallback(() => {
    // flash whole column, so leave row selection out
    gridRef.current.api.flashCells({ columns: ['c', 'd'] });
  }, []);

```

In the Dash app above, `getApiAsync` is used to get the grid API. Note that you need to provide the id of grid.  In this app the id is  `"grid-flash-cells"`  
```
const gridApi = await dash_ag_grid.getApiAsync("grid-flash-cells")
```

Here's one of the callbacks:
```
clientside_callback(
    \"\"\"async (n) => {
         if (n) {
            const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells")
            // flash whole column, so leave row selection out
            gridApi.flashCells({ columns: ['c', 'd'] });
         }
        return dash_clientside.no_update
    }\"\"\",
    Output("btn-flash-cols", "id"),
    Input("btn-flash-cols", "n_clicks"),
)
```

Once you have defined the `gridApi`, you'll have access to all the grid API methods in the Dash clientside callback.  

Here's an example of how to flash the 'c' and 'd' columns:
```
gridApi.flashCells({ columns: ['c', 'd'] });
```

This will get row number 4.  See how this is used in other clientside callbacks in the app above.
```
gridApi.getDisplayedRowAtIndex(4);
```


## Example 2 How Flashing Works

> See details about this example in the [AG Grid docs](https://www.ag-grid.com/archive/31.0.2/react-data-grid/flashing-cells/#how-flashing-works)

This example shows how to further configure the flashing by changing the flash background color with CSS and adjusting
the length of the flash in the grid's `flashCells` API.  

This also shows how important it is to use the correct version of the docs.  In AG Grid V31.1.0 they changed the prop names
from `flashDelay` to `flashDuration` and from `fadeDelay` to `fadeDuration`. However, those new props aren't available in our
version (31.0.3), so we need to continue to use the old prop names.

Here's the CSS to change the flash background color:
```
.flash .ag-theme-alpine,
.flash .ag-theme-alpine-dark {
  --ag-value-change-value-highlight-background-color: #cc222244;
}
```
"""

text3 = """


## Understanding `getApi` and `getApiAsync` in Dash AG Grid

In Dash AG Grid, there are two function for retrieving the grid API: `getApi` and `getApiAsync`.

Since most of us use Python more than JavaScript, here are some great articles from MDN on the difference between synchronous and asynchronous functions in JavaScript:

- [Introducing asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)

- [How to use Promises, async and await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises#async_and_await)


`getApi` Method:  

You can use `getApi` with a regular (synchronous) JavaScript function. It simply checks one time if the grid is ready and returns either the grid's API or an error. This means that if the Dash callback is triggered when the app starts and the grid is not ready, you will get the error.


Here's an example to illustrate.  This callback will be triggered when the app starts and the grid won't be ready.


```
# This uses getApi before the grid is ready and it  won't work:
clientside_callback(
    \"\"\" () => {
        const gridApi = dash_ag_grid.getApi("grid-flash-cells")
        gridApi.flashCells({ columns: ['c', 'd'] });
        return dash_clientside.no_update
    }\"\"\",
    Output("btn-flash-cols", "id"),
    Input("btn-flash-cols", "n_clicks"),
)
```

`getApiAsync` Method:  

The `getApiAsync` function is asynchronous and returns a promise.  It uses a timeout and will wait for up to 2 minutes for the grid to be ready before it sends an error. (If it takes longer than 2 minutes to load the grid, you should probably be using background callbacks). 

Here's some info from the MDN article:

>The [`async`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) keyword gives you a simpler way to work with asynchronous promise-based code. Adding `async` at the start of a function makes it an async function.
>
>Inside an async function, you can use the `await` keyword before a call to a function that returns a promise. This makes the code wait at that point until the promise is settled, at which point the fulfilled value of the promise is treated as a return value, or the rejected value is thrown.

>This enables you to write code that uses asynchronous functions but looks like synchronous code.


This is the same function as above, but it uses `getApiAsync`.  In this example, even though the callback is triggered  when the app starts, it will wait for the grid to render and you are unlikely to see an error.



```
# Flash 2 columns when the app starts using getApiAsync
clientside_callback(
    \"\"\"async () => {
        const gridApi =  await dash_ag_grid.getApiAsync("grid-flash-cells")
        gridApi.flashCells({ columns: ['c', 'd'] });
        return dash_clientside.no_update
    }\"\"\",
    Output("btn-flash-cols", "id"),
    Input("btn-flash-cols", "n_clicks"),
)

```



"""



text_next = f"""
## Next Steps

- When migrating to future version of Dash AG Grid, be sure to update the prop names in the `flashCells` API
- If you've found Dash AG Grid valuable, show your support by starring us on [GitHub](https://github.com/plotly/dash-ag-grid)! 🌟.
- Have questions or want to join the conversation? Head over to the [Dash Community Forum](https://community.plotly.com/). 

Happy Coding!

"""

next = f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.grid_api.getapi_flash_cells", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.grid_api.getapi_flash_cells2", make_layout=make_tabs),
        make_md(text3),
        make_md(text_next),
        up_next()
    ],
)

from dash import  html, dcc, register_page

from utils.code_and_show import example_app, make_tabs
from utils.utils import app_description
from utils.other_components import  up_next, make_md
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Theme Switch", path=links.theme_switch
)


text1 = """
# Dash AG Grid with light and dark themes

In this tutorial you'll learn how to style the grid for an app that switches between light and dark themes.

To learn all about AG Grid themes see Dash AG Grid docs [Layout and Styles](https://dash.plotly.com/dash-ag-grid/styling-themes) section.
"""

text2="""

## Change Grid Theme in a Callback

The grid has several themes to choose from, including light and dark modes of each theme.  The theme is set in the
 `className` prop, and the default theme in Dash is `ag-theme-alpine`.  
 
In this example we update the `className` prop in a callback based on the value of switch component. We switch between
 the  `"ag-theme-quartz"` and the `"ag-theme-quartz-dark"` theme.
 
  
"""

text3 = """

## Change theme of multiple grids in a callback

If you have many grids in your app, you can update the grid theme of all the grids at once by updating the `className` on
 the  app's container.  
 
In order for this work, it's necessary to remove the default theme, which Dash sets as `className="ag-theme-alpine"`.
  To remove the default theme, you could  set `className=""` on the grid.  However, it's more self-documenting to
   use something more descriptive such as `className="no-default-theme"`
 
Here's an example:

```python
app.layout = html.Div(
    [
        dag.AgGrid(
           className="no-default-theme"
           id="grid1"
           #... other props        
        )
        dag.AgGrid(
           className="no-default-theme"
           id="grid2"   
           #... other props     
        )
    ],
    id="outer-div"
    className="ag-theme-quartz"    # updated this prop in the callback
)
```
"""




text4 = """

## Change grid theme without using a callback

If you are using Dash Bootstrap Components with Bootstrap Color Modes, it's possible to style the grid with CSS variables -- No callbacks required!

Simply add the following CSS to a `.css` file in the `assets` folder.  Or use the external stylesheet as shown in the
 AG Grid section of [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/adding-themes/ag-grid).  Then
  add `className="dbc-ag-grid"` to the outer container of your app.
 
```
.dbc-ag-grid .ag-theme-alpine {
  --ag-alpine-active-color: var(--bs-primary);
  --ag-selected-row-background-color: rgba(var(--bs-primary-rgb), 0.3);
  --ag-row-hover-color: rgba(var(--bs-primary-rgb), 0.1);
  --ag-column-hover-color: rgba(var(--bs-primary-rgb), 0.1);
  --ag-input-focus-border-color: rgba(var(--bs-primary-rgb), 0.4);
  --ag-range-selection-background-color: rgba(var(--bs-primary-rgb), 0.2);
  --ag-range-selection-background-color-2: rgba(var(--bs-primary-rgb), 0.36);
  --ag-range-selection-background-color-3: rgba(var(--bs-primary-rgb), 0.49);
  --ag-range-selection-background-color-4: rgba(var(--bs-primary-rgb), 0.59);
  --ag-background-color: var(--bs-body-bg);
  --ag-foreground-color: var(--bs-body-color);
  --ag-border-color:  rgba(173,181,189, 0.40);
  --ag-cell-horizontal-border:  rgba(173,181,189, 0.20);
  --ag-secondary-border-color:  rgba(173,181,189, 0.20);
  --ag-header-background-color:  rgba(173,181,189, 0.20);
  --ag-odd-row-background-color:  rgba(173,181,189, 0.05);
  --ag-control-panel-background-color: var(--bs-body-bg);
  --ag-subheader-background-color:  var(--bs-body-bg);
  --ag-invalid-color: var(--bs-form-invalid-color);
  --ag-font-family: var(--bs-font-family);
}



```

This site uses the Bootstrap Spacelab theme with a light and dark color mode switch.  Note that all the grids in this
 site automatically use the light or dark mode based on the app's theme. Try changing the theme with switch in the
  header at the top of the page.  You will see the app below will automatically change to the light theme.
 
Learn more about [Customizing Themes] in the Dash docs, and at the Dash  Bootstrap Theme Explorer [Dash AG Grid ](https://hellodash.pythonanywhere.com/adding-themes/ag-grid) section.
  
__Note: Requires Dash Bootstrap Components>=1.5.0__

"""



text5 = f"""

## AG Grid Auto dark themes

The 'auto' versions of each theme use the [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS media feature to switch between dark and light
 variants depending on whether the user has enabled dark mode on their operating system.
 
This is a cool feature  -- however you would also have to make the rest of your app to switch themes based on the `prefers-color-schemes` else the only component that will switch is the grid!


## Styling other Dash component libraries

Dash is highly customizable and it's possible to get a pixel perfect design with custom CSS.  Here is more information
 on adding themes in other Dash component libraries.
  
1.  Dash Bootstrap Components: As of dbc version 1.5.0, the
  [Bootstrap Color Modes](https://getbootstrap.com/docs/5.3/customize/color-modes/) are supported.  All the dbc 
  components respond to a light and dark color mode of your selected Bootstrap theme.
  
2. [Dash Mantine Components](https://www.dash-mantine-components.com/):  All versions support light and dark themes.

3. Plotly figures:  You can update the [figure template](https://plotly.com/python/templates/)  in a callback when
 the theme changes. If you are using Dash Bootstrap Components, you can also use a [Bootstrap themed figure template.](https://hellodash.pythonanywhere.com/adding-themes/figure-templates)

4.  Dash Core Components: Can be styled with CSS.

If you are using Dash Bootstrap Components, see a complete tutorial on how to use the Bootstrap Color modes in the [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/adding-themes/color-modes).



## Next Steps

- See the [Dash docs]({links.dag_docs}) and the [AG Grid docs]({links.ag_grid_docs}) for details on all the features.

- Have questions?  Ask them on the [Dash Community Form]({links.forum})

Happy Coding!

"""



layout = html.Div(
    [
        make_md(text1),

      #  example_app("examples.get_started.V31_tutorial", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.styling.theme_switch_callback", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.styling.theme_switch_callback2", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.get_started.V31_tutorial", make_layout=make_tabs),
        make_md(text5),
        up_next()
    ],
)

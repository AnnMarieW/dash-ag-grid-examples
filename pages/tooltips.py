from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Tooltips", path=links.tooltips
)

text1 = """
# Dash AG Grid Tooltips

An introduction to using Tooltips in Dash AG Grid

### Overview
In this tutorial you will:

- Create a basic grid with tooltips in cells
- Add tooltips to the header
- Configure and style the Tooltip
- Create custom tooltip component for rendering Markdown
- Create a custom tooltip with a figure
- Use conditional Toolips


## Tooltips on Individual Cells

Define the tooltip in the column definitions.  

```
columndDefs = [
    {"field": "company", "tooltipField": "company"},
]

```

In this example, the value of the cell will show in a tooltip. This is
 useful when the column is too narrow for the cell content. Note that  by default, there is a 2 second delay before the
  tooltip shows. Next We'll show you how to change that.

"""

text2 = """
## Configure Tooltip

You can configure the following tooltip features in the `dashGridOptions` 
- `tooltipShowDelay` - set the number of milliseconds before the tooltip shows. In the example below it's 0 so it shows immediately. 
-  `tooltipHideDelay` - set the number of milliseconds before the tooltip is hidden. In the example it's 3000
- `tooltipInteraction` - When True, the tooltip does not hide on hover.  You can select and copy the content. 
- `tooltipMouseTrack` - makes the tooltips follow the cursor - don't use when `tooltipInteraction` = True
```"""

text3 = """
## Header Tooltip

Define the header tooltip in the column definitions.  

```
columndDefs = [
    {"field": "company", "tooltipField": "company", "headerTooltip: "This is the Company column"},
]
```

"""

text4 = """
## Formatting Tooltip text & Conditional Tooltips

Customize the tooltip text with the `tooltipValueGetter` prop.  It takes a JavaScript function that returns
 a string to display in the tooltip. 
 
For more information see:
- [Dash Docs](https://dash.plotly.com/dash-ag-grid/javascript-and-the-grid) - An Introduction to JavaScript and the Grid.
- [AG Grid docs](https://www.ag-grid.com/react-data-grid/tooltips/#reference-ColDef-tooltipValueGetter) `tooltipValueGetter` reference.

The example below demonstrates the following:

__Show content from a different column in the toolip__:
 - The Company column shows the data from the Location column in a tooltip.
 
__Conditionally show the toolip__
 - The Mission column displays "Mission Successful" if the successful value in the Success column is True.
 - The Time column displays "No Time Provided" if the field is blank.  Try deleting the time to see the message.
 
__Format the data in the tooltip__
- The Price column is formatted for currency.  Learn more about number formatting in the [Dash docs](https://dash.plotly.com/dash-ag-grid/d3-value-formatters)
  
"""

text5=f"""
## Custom Header Tooltip Component with icons

For an introduction to custom components, see the   <dccLink href="/{links.get_started_V31}" children="Getting Started" /> tutorial.

This app has custom header tooltips in the Gold, Silver and Bronze columns.  It displays a FontAwesome icon using an HTML `i` component.

"""


text6="""
### Custom Cell Tooltip Component with figures

Display a figure in a tooltip with this custom component that uses a `dcc.Graph` component.  


"""
text7="""
### Custom Cell Tooltip Component for Markdown

Add a column of markdown text to the `rowData`.  The custom component will display it in a tooltip.

"""

text8="""
### Upload image files and display them in a tooltip

"""



text_next = f"""


Congratulations! You've seen how to add Toolips to headers and cells of Dash AG Grid. 

## Next Steps

- See the [Dash docs]({links.dag_docs}) and the [AG Grid docs]({links.ag_grid_docs}) for details and more examples of custom components and tooltips

- Have questions?  Ask them on the [Dash Community Form]({links.forum})

Happy Coding!

"""

next = f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.tooltips.tooltip_cells", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.tooltips.tooltip_config", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.tooltips.tooltip_header", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.tooltips.tooltip_valuegetters", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.html_i_tooltip_header", make_layout=make_tabs),
        make_md(text6),
        example_app("examples.components.dcc_graph_in_tooltip", make_layout=make_tabs),
        make_md(text7),
        example_app("examples.components.dcc_markdown_in_tooltip", make_layout=make_tabs),
        make_md(text8),
        example_app("examples.components.html_img_upload", make_layout=make_tabs),
        make_feature_card(links.upload_image_files_tooltip_gif, "After upload"),
        make_md(text_next),
        up_next()
    ],
)

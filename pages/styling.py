from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Styling", path=links.styling
)

text1 = """
# Conditional Formatting Recipes

This section is based on the examples in the Dash docs for the [DataTable](https://dash.plotly.com/datatable/conditional-formatting#filtering-and-conditional-formatting-recipes)

For more information please see the Dash Docs AG Gris styling sections, including:
- [Styling Rows](https://dash.plotly.com/dash-ag-grid/styling-rows)
- [Styling Cells](https://dash.plotly.com/dash-ag-grid/styling-cells)


"""


text2 = """

"""

next = f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        make_md("## Highlighting the Max Value in a Column"),
        example_app("examples.styling.style_max_value_in_col", make_layout=make_tabs),

        make_md("## Highlighting a Row with the Min Value"),
        example_app("examples.styling.style_row_with_min_value", make_layout=make_tabs),

        make_md("## Highlighting the Top Three or Bottom Three Values in a Column"),
        example_app("examples.styling.style_top3_bot3_value_in_col", make_layout=make_tabs),

        make_md("## Highlighting the Max Value in Every Row"),
        example_app("examples.styling.style_max_every_row", make_layout=make_tabs),

        make_md("## Highlighting the Maximum Value in the Grid"),
        example_app("examples.styling.style_max_in_grid", make_layout=make_tabs),

        make_md("## Highlighting a Range of Values"),
        example_app("examples.styling.style_range_in_grid", make_layout=make_tabs),

        # make_md("## Highlighting Top 10% or Bottom 10% of Values by Column"),
        # example_app("examples.styling.style_", make_layout=make_tabs),

        # make_md("## Highlighting Values above Average and Below Average"),
        # example_app("examples.styling.style_", make_layout=make_tabs),

        make_md("## Highlighting None, NaN, or Empty String Values"),
        example_app("examples.styling.style_blank", make_layout=make_tabs),

        make_md("## Displaying Special Values for NaN or None Values"),
        example_app("examples.styling.format_nan", make_layout=make_tabs),

        make_md("## Highlighting Text that Contains a Value"),
        example_app("examples.styling.style_text_that_contains_value", make_layout=make_tabs),

        # make_md("## Highlighting Text that Equals a Value"),
        # example_app("examples.styling.style_", make_layout=make_tabs),

        make_md("""
        ## Highlighting Cells by Value with a Colorscale Like a Heatmap  
        - See [Dash Docs](https://dash.plotly.com/dash-ag-grid/styling-cells#cell-shading-examples)        
        """),

        make_md("""
        ## Highlighting with a Colorscale on a Single Column  
        - See [Dash Docs](https://dash.plotly.com/dash-ag-grid/styling-cells#cell-shading-examples)        
        """),

        make_md("## Displaying Data Bars"),
        example_app("examples.styling.data_bars", make_layout=make_tabs),

        make_md("## Data Bars without Text"),
        example_app("examples.styling.data_bars_without_text", make_layout=make_tabs),

        # make_md("## Diverging Data Bars"),
        # example_app("examples.styling.style_", make_layout=make_tabs),

        # make_md("## Highlighting Dates"),
        # example_app("examples.styling.style_", make_layout=make_tabs),

# End DataTable Examples

        make_md("## Style Rows with a Dropdown Color Picker"),
        example_app("examples.styling.row_color_picker", make_layout=make_tabs),
        make_md("## Style Rows based on Value of 2 Columns"),
        example_app("examples.styling.style_row_based_on_column", make_layout=make_tabs),


        # make_md("## "),
        # example_app("examples.styling.style_", make_layout=make_tabs),
        # make_md("## "),
        # example_app("examples.styling.style_", make_layout=make_tabs),


        up_next()
    ],
)

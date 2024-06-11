from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card, make_card
import utils.links as links

register_page(
    __name__, order=0, description=app_description, title="Dash AG Grid Examples: Home", path="/"
)


text1 = """
__Welcome to Dash AG Grid Examples.  Here you'll find Tips and Tricks, Tutorials, and additional examples to supplement the Dash AG Grid documentation.__

"""



under_construction = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Coming Soon", href="/"
        )
    ),
    html.Div(
        "",
        className="small",
    ),
]
under_construction = make_img_card(links.under_construction_img, under_construction)


under_construction2 = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Coming Soon", href="/"
        )
    ),
    html.Div(
        "",
        className="small",
    ),
]
under_construction2 = make_img_card(links.examples_img, under_construction2)

# Documentation -----------------------------

ag_grid_docs_card = [
    html.Div("Documentation", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "AG Grid Docs", href=links.ag_grid_docs, target="_blank"
        )
    ),
    html.Div(
        "See the upstream AG Grid docs for more info, including more features, demo apps and videos",
        className="small",
    ),
]
ag_grid_docs_card = make_img_card(links.ag_grid_docs_img, ag_grid_docs_card)


dag_docs_card = [
    html.Div("Documentation", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Plotly Dash AG Grid Docs", href=links.dag_docs, target="_blank"
        )
    ),
    html.Div(
        "See the Plotly docs for information on how to use the AG Grid component in your Dash app",
        className="small",
    ),
]
dag_docs_card = make_img_card(links.dag_docs_img, dag_docs_card)

# Tutorials ------------------------------


get_started_V31 = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Get Started with Dash AG Grid V31", href=links.get_started_V31
        )
    ),
    html.Div(
        "An introduction to the key concepts of Dash AG Grid and some of the new features available in V31.",
        className="small",
    ),
]
get_started_V31 = make_img_card(links.get_started_V31_img, get_started_V31)



get_started_easy = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Dash AG Grid Quickstart", href=links.get_started_easy
        )
    ),
    html.Div(
        "Make your first grid in 30 seconds.",
        className="small",
    ),
]
get_started_easy = make_img_card(links.get_started_easy_img, get_started_easy)


theme_switch = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Dash AG Grid with light and dark theme", href=links.theme_switch
        )
    ),
    html.Div(
        "Learn how to add a theme switch to your Dash app and style the grid in light and dark mode",
        className="small",
    ),
]
theme_switch = make_img_card(links.theme_switch_img, theme_switch)


tooltips = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Tooltips ", href=links.tooltips
        )
    ),
    dcc.Markdown("""
    How to add tooltips to the cell and header in Dash AG Grid.  Includes examples of conditional tooltips,
     formatting tooltips and tooltips with custom components.
    
    With 8 examples.  
    """, className="small",
    ),
]
tooltips = make_img_card(links.tootips_img, tooltips)


grid_api = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            " How to use the AG Grid API with Dash ", href=links.grid_api
        )
    ),
    dcc.Markdown("""
    - Accessing the Grid's API in a Dash Clientside Callback
    - Determining the Correct AG Grid Docs Version for Dash AG Grid
    - Examples: Flashing Cells using the Grid's API
    - Differentiating Between Dash AG Grid Functions: `getApiAsync` and `getApi`
    """, className="small",
                 ),
]
grid_api = make_img_card(links.get_started_V31_img, grid_api)


external_filter = [
    html.Div("Tutorial", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            " How to filter grid data with external components", href=links.external_filters
        )
    ),
    dcc.Markdown("""
    - Examples: Filtering the grid with a figure and other Dash components.
    - How to use External filters:
      - External Filter API
      - Updating rowData
      - Using the Filter Model     
    """, className="small",
                 ),
]
external_filter = make_img_card(links.external_filter_gif, external_filter)



# Component GALLERY -----------------------------------------------

dbc_components = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "dbc components", href=links.components_dbc
        )
    ),
    dcc.Markdown(
        """
        Examples of  __Dash Bootstrap Components__ in AG Grid cells
        - `dbc.Button` with icons
        - `dbc.Progress`
        - `dbc.Switch`   
        - `dbc.Spinner`
        - `dbc.DropdownMenu`
        """,
        className="small",
    ),
]
dbc_components = make_card("### dbc Components", dbc_components)


dcc_components = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "dcc components", href=links.components_dcc
        )
    ),
    dcc.Markdown(
        """
        Examples of  __Dash Core Components__ in AG Grid cells
        - `dcc.Clipboard` - copy cell
        - `dcc.Clipboard` - copy row
        - `dcc.Graph` - Figure in Tooltip
        - `dcc.Markdown` - Markdown text in a Tooltip
        - `dcc.Markdown` - Markdown with MathJax
        - `dcc.RadioItems` - Custom Filter in header
        
        """,
        className="small",
    ),
]
dcc_components = make_card("### dcc Components", dcc_components)

html_components = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "html components", href=links.components_html
        )
    ),
    dcc.Markdown(
        """
        Examples of  __HTML Components__ in AG Grid cells
        - `img`  Image of flag in cells 
        - `img`  Upload images and display them in a tooltip
        - `i  `   Icons in header toolip
        - `i `    Icons to indicated editable cells 
        - `button` Delete row button   
                

        """,
        className="small",
    ),
]
html_components = make_card("### html Components", html_components)

dmc_components = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "dmc components", href=links.components_dmc
        )
    ),
    dcc.Markdown(
        """
        Examples of  __Dash Mantine Components__ in AG Grid cells
        - `dmc.Button`
        - `dmc.Select`
        - `dmc.Select` with Popup Parent
        - `dmc.Select` with Grouping
        - `dmc.RadioGroup`

        """,
        className="small",
    ),
]
dmc_components = make_card("### dmc Components", dmc_components)


# Examples ---------------------------


import_export  = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Import & Export", href=links.import_export
        )
    ),
    dcc.Markdown(
        """
        Export to CSV and Excel
        - CSV export with params
        - Excel export (community) 4 examples    
        """,
        className="small",
    ),
]
import_export = make_card("### Import & Export", import_export)

styling = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Styling -  Conditional Formatting", href=links.styling
        )
    ),
    dcc.Markdown(
        """
        10+ Conditional formatting recipies!
        
        """,
        className="small",
    ),
]
styling = make_card("### Styling", styling)

migrating_DataTable = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Migrating From DataTable", href=links.migrating_DataTable
        )
    ),
    dcc.Markdown(
        """
        Examples to help migrate your app from Dash DataTable to Dash AG Grid.

        """,
        className="small",
    ),
]
migrating_DataTable = make_card("### Migrating from DataTable", migrating_DataTable)


tips_and_tricks = [
    html.Div("Examples", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Tips & Tricks ", href=links.tips_and_tricks
        )
    ),
    dcc.Markdown("""            
        - Make a grid with less code  -- by using functions to create a grid with all your favorite features
        - Access data created with a `valueGetter` in a callback
        - Dynamic Select Options- Dropdown options in the "Cities" column change based on the "Country" column.
        - Formatting numbers by row and conditional editing
    
    """, className="small",
                 ),
]
tips_and_tricks = make_card("### Tips & Tricks", tips_and_tricks)




layout = html.Div(
    [
        dbc.Row(dbc.Col(make_md(text1, className="mt-4 m-auto"))),
        html.H2("AG Grid Documentation", className="text-center py-2"),
        dbc.Row(
            [
                dbc.Col(dag_docs_card, md=6),
                dbc.Col(ag_grid_docs_card, md=6),
            ],
            className="px-5",
        ),
        html.H2("Dash AG Grid Tutorials", className="text-center py-2 mt-4"),
        dbc.Row(
            [
                dbc.Col(get_started_easy),
                dbc.Col(get_started_V31),
                dbc.Col(theme_switch),
                dbc.Col(tooltips),
                dbc.Col(grid_api),
                dbc.Col(external_filter)

            ]
        ),
        html.H2("Dash AG Grid Examples", className="text-center py-2 mt-4 pt-4"),
        dbc.Row(
            [

                dbc.Col(import_export),
                dbc.Col(styling),
                dbc.Col(migrating_DataTable),
                dbc.Col(tips_and_tricks),
                #dbc.Col(under_construction2),

            ]
        ),
        html.H2("Dash AG Grid Custom Component Gallery", className="text-center py-2 mt-4 pt-4"),
        dbc.Row(
            [
                dbc.Col(dbc_components),
                dbc.Col(dcc_components),
                dbc.Col(dmc_components),
                dbc.Col(html_components),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(under_construction2),
           #     dbc.Col(under_construction2)
            ]
        )
    ],
)

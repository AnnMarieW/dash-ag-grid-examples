from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_nav_card
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
under_construction = make_nav_card(links.under_construction_img, under_construction)


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
under_construction2 = make_nav_card(links.examples_img, under_construction2)



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
ag_grid_docs_card = make_nav_card(links.ag_grid_docs_img, ag_grid_docs_card)


dag_docs_card = [
    html.Div("Documentation", className="text-primary border-top pt-2"),
    html.H4(
        dcc.Link(
            "Plotly Dash AG Grid Docs", href=links.ag_grid_docs, target="_blank"
        )
    ),
    html.Div(
        "See the Plotly docs for information on how to use the AG Grid component in your Dash app",
        className="small",
    ),
]
dag_docs_card = make_nav_card(links.dag_docs_img, dag_docs_card)


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
get_started_V31 = make_nav_card(links.get_started_V31_img, get_started_V31)



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
get_started_easy = make_nav_card(links.get_started_easy_img, get_started_easy)


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
theme_switch = make_nav_card(links.theme_switch_img, theme_switch)

layout = html.Div(
    [
        dbc.Row(dbc.Col(make_md(text1, className="mt-4 m-auto"))),
        html.H2("Documentation", className="text-center py-2"),
        dbc.Row(
            [
                dbc.Col(dag_docs_card, md=6),
                dbc.Col(ag_grid_docs_card, md=6),
            ],
            className="px-5",
        ),
        html.H2("Tutorials", className="text-center py-2 mt-4"),
        dbc.Row(
            [
                dbc.Col(get_started_easy),
                dbc.Col(get_started_V31),
                dbc.Col(theme_switch),
            ]
        ),
        html.H2("Examples", className="text-center py-2 mt-4 pt-4"),
        dbc.Row(
            [
                dbc.Col(under_construction2),
                dbc.Col(under_construction2),
                dbc.Col(under_construction2)
            ]
        ),
    ],
)

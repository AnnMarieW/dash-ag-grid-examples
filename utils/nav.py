"""
This is a collection of nav components and headers

"""
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


# Links
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"
plotly_ddk_url = "https://plotly.com/dash/design-kit/"
aggrid_logo = "https://user-images.githubusercontent.com/72614349/211098297-c208fed6-6bda-4f1d-8506-3051e1a8ec07.png"
aggrid_docs_url = "https://www.ag-grid.com/react-data-grid/"

examples_index_url = "https://dash-example-index.herokuapp.com/"
dash_docs_url = "https://dash.plotly.com/"
dash_forum_url = "https://community.plotly.com/"

color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=False, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ], className="text-primary  pb-1 ms-3 bg-white rounded", style={"height": 16, "marginTop":18, "fontSize":11 }
)

navbar = dbc.NavbarSimple(
    [
        html.A(
            html.Img(src=plotly_logo, height=36, className="m-2 shadow rounded"),
            href=dash_docs_url,
            target="blank",
            title="Plotly",
        ),
        html.A(
            html.Img(src=aggrid_logo, height=36, className="m-2 shadow rounded"),
            href=aggrid_docs_url,
            target="blank",
            title="Plotly",
        ),
        html.A(
            html.I(className="bi bi-github ps-2 text-white fs-2"),
            href="https://github.com/AnnMarieW/dash-ag-grid-examples",
            target="blank",
            title="GitHub"
        ),
        color_mode_switch
    ],
    brand="Dash AG Grid Examples",
    brand_href="/",
    color="primary",
    dark=True,
    fixed="top",
    className="mb-2  position-relative",
    style={"minWidth": 800},
)

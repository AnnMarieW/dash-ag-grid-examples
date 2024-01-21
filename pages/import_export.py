from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Import & Export", path=links.import_export
)


text1 = """
# Import & Export Data

Here are some additional examples of exporting grid data to CSV and Excel files.  

For more information see:
 - Dash AG Grid Docs [Import Export CSV](https://dash.plotly.com/dash-ag-grid/export-data-csv)
 - AG Grid Docs [Import Export](https://ag-grid.com/react-data-grid/csv-export/) for CSV and Excel(Enterprise).  
 
--------------

` `  
` `  

## CSV Export - Customizing exported data

See the Dash doc for more examples.  This one shows how to customize the data before export:
- Excludes the rows where the model is Ford
- Formats the values in the price column

"""

text2 = """


--------------

` `  
` `  

## Export to Excel

If you are using AG Grid Enterprise, please see the [AG Grid Excel Export](https://www.ag-grid.com/react-data-grid/excel-export/) docs.  This example is for AG Grid community, and it
 uses [`dcc.Download`](https://dash.plotly.com/dash-core-components/download) to export data to Excel. 
  

### Example 1: Export to Excel - basic

"""

text3 = """
### Example 2: Export to Excel - multiple grids, one sheet
"""


text4 = """
### Example 3: Export to Excel - one grid, multiple sheets
"""

next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.import_export.csv_export_params", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.import_export.excel_dcc_download", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.import_export.excel_dcc_download_multi_grids_one_sheet", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.import_export.excel_dcc_download_multi_sheets", make_layout=make_tabs),
        up_next()
    ],
)


from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

app = Dash(__name__)


colors = [
  'AliceBlue',
  'AntiqueWhite',
  'Aqua',
  'Aquamarine',
  'Azure',
  'Beige',
  'Bisque',
  'Black',
  'BlanchedAlmond',
  'Blue',
  'BlueViolet',
  'Brown',
  'BurlyWood',
  'CadetBlue',
  'Chartreuse',
  'Chocolate',
  'Coral',
  'CornflowerBlue',
  'Cornsilk',
  'Crimson',
  'Cyan',
  'DarkBlue',
  'DarkCyan',
  'DarkGoldenrod',
  'DarkGray',
  'DarkGreen',
  'DarkGrey',
  'DarkKhaki',
  'DarkMagenta',
  'DarkOliveGreen',
  'DarkOrange',
  'DarkOrchid',
  'DarkRed',
  'DarkSalmon',
  'DarkSeaGreen',
  'DarkSlateBlue',
  'DarkSlateGray',
  'DarkSlateGrey',
  'DarkTurquoise',
  'DarkViolet',
  'DeepPink',
  'DeepSkyBlue',
  'DimGray',
  'DodgerBlue',
  'FireBrick',
  'FloralWhite',
  'ForestGreen',
  'Fuchsia',
  'Gainsboro',
  'GhostWhite',
  'Gold',
  'Goldenrod',
  'Gray',
  'Green',
  'GreenYellow',
  'Grey',
  'Honeydew',
  'HotPink',
  'IndianRed',
  'Indigo',
  'Ivory',
  'Khaki',
  'Lavender',
  'LavenderBlush',
  'LawnGreen',
  'LemonChiffon',
  'LightBlue',
  'LightCoral',
  'LightCyan',
  'LightGoldenrodYellow',
  'LightGray',
  'LightGreen',
  'LightGrey',
  'LightPink',
  'LightSalmon',
  'LightSeaGreen',
  'LightSkyBlue',
  'LightSlateGray',
  'LightSlateGrey',
  'LightSteelBlue',
  'LightYellow',
  'Lime',
  'LimeGreen',
  'Linen',
  'Magenta',
  'Maroon',
  'MediumAquamarine',
  'MediumBlue',
  'MediumOrchid',
  'MediumPurple',
  'MediumSeaGreen',
  'MediumSlateBlue',
  'MediumSpringGreen',
  'MediumTurquoise',
  'MediumVioletRed',
  'MidnightBlue',
  'MintCream',
  'MistyRose',
  'Moccasin',
  'NavajoWhite',
  'Navy',
  'OldLace',
  'Olive',
  'OliveDrab',
  'Orange',
  'OrangeRed',
  'Orchid',
  'PaleGoldenrod',
  'PaleGreen',
  'PaleTurquoise',
  'PaleVioletRed',
  'PapayaWhip',
  'PeachPuff',
  'Peru',
  'Pink',
  'Plum',
  'PowderBlue',
  'Purple',
  'Rebeccapurple',
  'Red',
  'RosyBrown',
  'RoyalBlue',
  'SaddleBrown',
  'Salmon',
  'SandyBrown',
  'SeaGreen',
  'Seashell',
  'Sienna',
  'Silver',
  'SkyBlue',
  'SlateBlue',
  'SlateGray',
  'SlateGrey',
  'Snow',
  'SpringGreen',
  'SteelBlue',
  'Tan',
  'Teal',
  'Thistle',
  'Tomato',
  'Turquoise',
  'Violet',
  'Wheat',
  'White',
  'WhiteSmoke',
  'Yellow',
  'YellowGreen',
]
df = pd.DataFrame({"color": colors})

columnDefs = [
  {
    'headerName': 'Allow Typing (Match)',
    'field': 'color',
    'cellRenderer': 'ColourCellRenderer',
    'cellEditor': 'agRichSelectCellEditor',
    'cellEditorParams': {
      'values': colors,
      'searchType': 'match',
      'allowTyping': True,
      'filterList': True,
      'highlightMatch': True,
      'valueListMaxHeight': 220,
    },
  },
  {
    'headerName': 'Allow Typing (MatchAny)',
    'field': 'color',
    'cellRenderer': 'ColourCellRenderer',
    'cellEditor': 'agRichSelectCellEditor',
    'cellEditorParams': {
      'values': colors,
      'searchType': 'matchAny',
      'allowTyping': True,
      'filterList': True,
      'highlightMatch': True,
      'valueListMaxHeight': 220,
    },
  }
]

app.layout = html.Div(
    [
        dag.AgGrid(
            enableEnterpriseModules=True,
        #    licenseKey =  Your license key here
            columnDefs=columnDefs,
            defaultColDef={"editable": True},
            rowData=df.to_dict('records'),
            columnSize="sizeToFit",
            dashGridOptions={"animateRows": False}
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)


"""
Add the following to the dashAgGridComponentFunctions.js file in the assets folder:

 var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

 dagcomponentfuncs.ColourCellRenderer = (props) => {
  
  const styles = {
    verticalAlign: "middle",
    border: "1px solid black",
    margin: 3,
    display: "inline-block",
    width: 20,
    height: 10,
    backgroundColor: props.value.toLowerCase(),
  };
  return React.createElement("div", {}, [
    React.createElement("span", { style: styles }),
    React.createElement("span", {}, props.value),
  ]);
};


"""
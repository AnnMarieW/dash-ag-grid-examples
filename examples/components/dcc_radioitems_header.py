from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    { 'field': 'age', 'filter': 'agNumberColumnFilter' },
    { 'field': 'country', 'minWidth': 150 },
    { 'field': 'year', 'filter': {'function': 'YearFilter'}},
    {
      'field': 'date',
      'minWidth': 130,
      'filter': 'agDateColumnFilter',
      'filterParams': {
        'comparator': {'function':'dateComparator'},
      },
    },
    { 'field': 'sport' },
    { 'field': 'total', 'filter': 'agNumberColumnFilter' },
]

defaultColDef = {
    'editable': True,
    'flex': 1,
    'minWidth': 100,
    'filter': True,
}


app.layout = html.Div(
    [
        html.H3("See the custom filter component in the Year column"),
        dag.AgGrid(
            id="grid",
            columnDefs=columnDefs,
            rowData=df.to_dict('records'),
            defaultColDef=defaultColDef
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)


"""
Add this to the dashAgGridFunctions.js file in the assets folder


----------------


var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

const [useImperativeHandle, useState, useEffect, forwardRef, Component] = [React.useImperativeHandle, React.useState, React.useEffect, React.forwardRef, React.component]

dagfuncs.YearFilter = forwardRef((props, ref) => {
   const [year, setYear] = useState('All');

   useImperativeHandle(ref, () => {
       return {
           doesFilterPass(params) {
               return params.data.year >= 2010;
           },

           isFilterActive() {
               return year === '2010'
           },

           // this example isn't using getModel() and setModel(),
           // so safe to just leave these empty. don't do this in your code!!!
           getModel() {
           },

           setModel() {
           }
       }
   });

   useEffect(() => {
       props.filterChangedCallback()
   }, [year]);

    setProps = (props) => {
        if (props.value) {
            setYear(props.value)
        }
    }

    return React.createElement(
        window.dash_core_components.RadioItems,
        {
            options:[
                {'label': 'All', 'value': 'All'},
                {'label': 'Since 2010', 'value': '2010'},
            ],
            style: { 'padding': 5},
            value: year,
            setProps
        }
    )
});

dagfuncs.dateComparator = function (filterLocalDateAtMidnight, cellValue) {

    const dateAsString = cellValue;
    const dateParts = dateAsString.split('/');
    const cellDate = new Date(
        Number(dateParts[2]),
        Number(dateParts[1]) - 1,
        Number(dateParts[0])
    );
    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
        return 0;
    }
    if (cellDate < filterLocalDateAtMidnight) {
        return -1;
    }
    if (cellDate > filterLocalDateAtMidnight) {
        return 1;
    }

}

"""
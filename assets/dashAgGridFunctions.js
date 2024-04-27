var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});


// used in style_edits
dagfuncs.addEdits = function (params) {
    if (params.data.changes) {
        var newList = JSON.parse(params.data.changes)
        newList.push(params.colDef.field)
        params.data.changes = JSON.stringify(newList)
    } else {
        params.data.changes = JSON.stringify([params.colDef.field])
    }
    params.data[params.colDef.field] = params.newValue
    return true;
}

dagfuncs.highlightEdits = function (params) {
    if (params.data.changes) {
        if (JSON.parse(params.data.changes).includes(params.colDef.field)) {
            return true
        }
    }
    return false;
}


dagfuncs.Intl = Intl;

// used in format_by_row (tips and tricks)
dagfuncs.FormatNumbersByRow = function(params) {
    if (params.data["Val ID"] == "Hours") {
        return Intl.NumberFormat("en-US").format(params.value);
    }
    if (params.data["Val ID"] == "Value") {
        return Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
          }).format(params.value);
    }
}




dagfuncs.dynamicOptions = function (params, options) {
    return {values: options[params.data.country]}
};


// used in updating_rowData_with_ValueGetter
dagfuncs.commentsValueGetter = (params) => {
   const newComment = "The " + params.data.model + "Sold for $" + params.data.price
   params.data.comments = newComment
   return newComment
}



// used in dmc.Select popup parent
dagfuncs.setBody = () => {
    return document.querySelector('body')
}

// Used in the dcc.RadioItems header filter
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
// end


// cell editor custom component  - dmc.Select
dagfuncs.DMC_Select = class {
    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.params = params;

        // function for when Dash is trying to send props back to the component / server
        var setProps = (props) => {
            if (typeof props.value != typeof undefined) {
                // updates the value of the editor
                this.value = props.value;

                // re-enables keyboard event
                delete params.colDef.suppressKeyboardEvent;

                // tells the grid to stop editing the cell
                params.api.stopEditing();

                // sets focus back to the grid's previously active cell
                this.prevFocus.focus();
            }
        };
        this.eInput = document.createElement('div');

        // renders component into the editor element
        ReactDOM.render(
            React.createElement(window.dash_mantine_components.Select, {
                data: params.options,
                value: params.value,
                setProps,
                style: {width: params.column.actualWidth-2,  ...params.style},
                className: params.className,
                clearable: params.clearable,
                searchable: params.searchable || true,
                creatable: params.creatable,
                debounce: params.debounce,
                disabled: params.disabled,
                filterDataOnExactSearchMatch:
                params.filterDataOnExactSearchMatch,
                limit: params.limit,
                maxDropdownHeight: params.maxDropdownHeight,
                nothingFound: params.nothingFound,
                placeholder: params.placeholder,
                required: params.required,
                searchValue: params.searchValue,
                shadow: params.shadow,
                size: params.size,
                styles: params.styles,
                switchDirectionOnFlip: params.switchDirectionOnFlip,
                variant: params.variant,
                zIndex: params.zIndex,
            }),
            this.eInput
        );

        // allows focus event
        this.eInput.tabIndex = '0';

        // sets editor value to the value from the cell
        this.value = params.value;
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    focusChild() {
        // needed to delay and allow the component to render
        setTimeout(() => {
            var inp = this.eInput.getElementsByClassName(
                'mantine-Select-input'
            )[0];
            inp.tabIndex = '1';

            // disables keyboard event
            this.params.colDef.suppressKeyboardEvent = (params) => {
                const gridShouldDoNothing = params.editing;
                return gridShouldDoNothing;
            };
            // shows dropdown options
            inp.focus();
        }, 100);
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        // stores the active cell
        this.prevFocus = document.activeElement;

        // adds event listener to trigger event to go into dash component
        this.eInput.addEventListener('focus', this.focusChild());

        // triggers focus event
        this.eInput.focus();
    }

    // returns the new value after editing
    getValue() {
        return this.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // sets focus back to the grid's previously active cell
        this.prevFocus.focus();
    }
};
// end dmc.Select


// used in the csv export
dagfuncs.shouldRowBeSkipped = (params) => {
    return params.node.data.make == "Ford"
}

dagfuncs.processCellCallback = (params) => {
    return params.column.colDef.field == 'price'? '$' + params.value : params.value
}
//end



// Returns the max number in a row.  Used in Styling
dagfuncs.maxRowValue = (obj) => {
    const numericValues = Object.values(obj).filter(value => typeof value === 'number' && !isNaN(value));
    return  Math.max(...numericValues)
}

// Returns the max number in a grid.  Used in Styling
dagfuncs.maxGridValue = (params) => {
    const maxRowValues = [];
    params.api.forEachLeafNode((node) => {
        maxRowValues.push(dagfuncs.maxRowValue(node.data));
    });
    return Math.max(...maxRowValues)
}

// Used in styling format nan example
dagfuncs.formatNaN = function (val) {
    return isNaN(val) ? 'N/A' : (val === '' ? 'None' : val);
};


/////////////////  Everything below is from old docs site
dagfuncs.Round = function (v, a = 2) {
    return Math.round(v * (10 ** a)) / (10 ** a)
}

dagfuncs.toFixed = function (v, a = 2) {
    return Number(v).toFixed(a)
}

dagfuncs.addEdits = function (params) {
    if (params.data.changes) {
        var newList = JSON.parse(params.data.changes)
        newList.push(params.colDef.field)
        params.data.changes = JSON.stringify(newList)
    } else {
        params.data.changes = JSON.stringify([params.colDef.field])
    }
    params.data[params.colDef.field] = params.newValue
    return true;
}

dagfuncs.highlightEdits = function (params) {
    if (params.data.changes) {
        if (JSON.parse(params.data.changes).includes(params.colDef.field)) {
            return true
        }
    }
    return false;
}


dagfuncs.Intl = Intl

dagfuncs.EUR = function (number) {
    return Intl.NumberFormat('de-DE', {style: 'currency', currency: 'EUR'}).format(number);
}


dagfuncs.JPY = function (number) {
    return Intl.NumberFormat('ja-JP', {style: 'currency', currency: 'JPY'}).format(number)
}


dagfuncs.USD = function (number) {
    return Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(number);
}


dagfuncs.CAD = function (number) {
    return Intl.NumberFormat('en-CA', {style: 'currency', currency: 'CAD', currencyDisplay: 'code'}).format(number);
}


dagfuncs.PercentageFilna = function (number, filna = "") {
    if (isNaN(number)) {
        return filna
    }
    return Intl.NumberFormat("en-US", {style: "percent"}).format(number)
}


dagfuncs.MoneyFilna = function (number, filna = "") {
    if (isNaN(number)) {
        return filna
    }
    return Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(number);
}


// used in the cell editor example
dagfuncs.DatePicker = class {

    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.eInput = document.createElement('input');
        this.eInput.value = params.value;
        this.eInput.classList.add('ag-input');
        this.eInput.style.height = 'var(--ag-row-height)';
        this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';

        // https://jqueryui.com/datepicker/
        $(this.eInput).datepicker({
            dateFormat: 'dd/mm/yy',
            onSelect: () => {
                this.eInput.focus();
            },
        });
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        this.eInput.focus();
        this.eInput.select();
    }

    // returns the new value after editing
    getValue() {
        return this.eInput.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // but this example is simple, no cleanup, we could
        // even leave this method out as it's optional
    }

    // if true, then this editor will appear in a popup
    isPopup() {
        // and we could leave this method out also, false is the default
        return false;
    }

}



// Used in the cell editor dropdown examples
//     filterArray function displays the label instead of the value when the dropdown options contain both
//     Use this in a valueFormatter
dagfuncs.filterArray = function (array, condition, col = null) {
    newArray = array.filter((t) => condition.includes(t.value));
    if (!col) {
        return newArray;
    } else {
        var values = [];
        newArray.map((t) => values.push(t[col]));
        return values;
    }
};

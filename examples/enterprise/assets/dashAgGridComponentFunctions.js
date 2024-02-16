var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

// Used in  Enterprise Group Cell Renderer example
dagcomponentfuncs.SimpleCellRenderer = function (props) {
    return React.createElement(
        'span',
        {
            style: {
                backgroundColor: props.node.group ? 'coral' : 'lightgreen',
                padding: 2,
            },
        },
        props.value
    );
};


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


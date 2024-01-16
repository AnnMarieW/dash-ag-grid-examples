var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});

// used in the V31 tutorial
dagcomponentfuncs.CompanyLogoRenderer = function (props) {
  const url = `https://www.ag-grid.com/example-assets/space-company-logos/${props.data.company.toLowerCase()}.png`

  return React.createElement("span", {}, [
    React.createElement("img", {
      style: { width: "25px", height: "auto", filter: "brightness(1.1)" },
      src: url,
    }),
    React.createElement(
      "span",
      {
        style: { paddingLeft: "4px" },
      },
      props.value
    ),
  ]);
};


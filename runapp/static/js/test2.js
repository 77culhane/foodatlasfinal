// Initializes the page with a default plot
function init() {
  data = [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16],
    fill: 'tozeroy',
    fillcolor: 'rgb(255, 0, 0)',
    mode: 'lines',
    type: 'scatter',
    name: 'bores1',
    line: {
      color: 'rgb(172, 0, 0)',
      width: 5}
   }];

  var CHART = d3.select("#testtest").node();

  Plotly.newPlot(CHART, data);
}

// Call updatePlotly() when a change takes place to the #SELECTDATASET drop down
// d3.select("select").on("change", updatePlotly);
d3.select("#SELECTDATASET").on("change", updatePlotly);
// d3.select("body").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#SELECTDATASET");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.node().value;

  var CHART = d3.select("#testtest").node();

  // Initialize x and y arrays
  var x = [];
  var y = [];

  switch(dataset) {
    case "dataset1":
      x = [1, 2, 3, 4, 5];
      y = [1, 2, 4, 8, 16];
      break;

    case "dataset2":
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
      break;

    case "dataset3":
      x = [100, 200, 300, 400, 500];
      y = [10, 100, 50, 10, 0];
      break;
    
    case "dataset4":
      x = [100, 200, 300, 400, 500];
      y = [50, 500, 560, 300, 600];
      break;

    default:
      x = [1, 2, 3, 4, 5];
      y = [1, 2, 3, 4, 5];
      break;
  }


  // Note the extra brackets around 'x' and 'y'
  Plotly.restyle(CHART, "x", [x]);
  Plotly.restyle(CHART, "y", [y]);
  Plotly.restyle(CHART, "type", type);
}

init();

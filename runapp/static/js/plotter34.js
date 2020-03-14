var url = '/runquery'
var xvalues = []
var yvalues = []
var otheryvalues = [1, [2, 3], 4, 5, 6]
d3.json(url).then(function(data){
  iter_CHILDPOVRATE15 = data.map(d=>d['CHILDPOVRATE15'])
  iter_PCT_OBESE_ADULTS08 = data.map(d=>d['PCT_OBESE_ADULTS08'])
  console.log("first")
  console.log(iter_CHILDPOVRATE15)
  console.log(iter_PCT_OBESE_ADULTS08)
  console.log("second")
  xvalues.push(iter_CHILDPOVRATE15)
  yvalues.push(iter_PCT_OBESE_ADULTS08)
  console.log(xvalues[0])
  console.log(yvalues[0])
  return iter_CHILDPOVRATE15
});
console.log("third")
console.log(xvalues[0])
console.log(yvalues[0])
console.log("fourth")
console.log(xvalues)
console.log(yvalues)
console.log(iter_CHILDPOVRATE15)
/*
console.log("divider1")
console.log(xvalues)
console.log("divider2")
console.log(yvalues)
console.log("divider3")
console.log(otheryvalues)
console.log("divider4")
console.log(otheryvalues[0])
console.log("divider5")
console.log(otheryvalues[1])
/**/
//console.log(povrate)
//console.log(obesityrate)
/*
d3.json(url).then(function(data) {
  var panel = d3.select("#notmap")
  panel.html(";")
  Object.entries(data).forEach(([key, value]) => {
    panel.append("h6").text(`${key}: ${value}`);
    console.log(key, value)
  });
});
*/
//'CHILDPOVRATE15'
//
//
//

// Initializes the page with a default plot
function init() {
  data = [{
    x: xvalues,
    y: yvalues,
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
      x = xvalues;
      y = yvalues;
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
      x = xvalues;
      y = yvalues;
      break;
  }


  // Note the extra brackets around 'x' and 'y'
  Plotly.restyle(CHART, "x", [x]);
  Plotly.restyle(CHART, "y", [y]);
  Plotly.restyle(CHART, "type", type);
}

init();

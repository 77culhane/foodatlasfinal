var url = '/runquery'
d3.json(url).then(function(data) {
  var panel = d3.select("#notmap")
  panel.html(";")
  Object.entries(data).forEach(([key, value]) => {
    panel.append("h6").text(`${key}: ${value}`);
    console.log(key, value)
  });
});
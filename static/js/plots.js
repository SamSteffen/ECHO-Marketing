//ECHO Idaho plots.js

function init() {
    var selector = d3.select("#selDataset");
  
    d3.json("static/data/series_totals.json").then((data) => {
      console.log(data);
      var sampleNames = data.Series;
      seriesNames.forEach((Series) => {
        selector
          .append("option")
          .text(Series)
          .property("value", Series);
      });
  })}
  
  init();

  function optionChanged(newSeries) {
    console.log(newSeries);
    buildMetadata(newSeries);
    //buildCharts(newSample);
  }

  function buildMetadata(series) {
    d3.json("static/data/samples.json").then((data) => {
      var metadata = data.metadata;
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var result = resultArray[0];
      var PANEL = d3.select("#sample-metadata");
  
      PANEL.html("");
      PANEL.append("h6").text("ID: " + result.id);
      PANEL.append("h6").text("Ethnicity: " + result.ethnicity);
      PANEL.append("h6").text("Gender: " + result.gender);
      PANEL.append("h6").text("Age: " + result.age);
      PANEL.append("h6").text("Location: " + result.location);
      PANEL.append("h6").text("BB-type: " + result.bb_type);
      PANEL.append("h6").text("WFREQ: " + result.wfreq);
    });
  }

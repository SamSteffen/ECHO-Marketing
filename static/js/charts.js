//ECHO Idaho charts.js

function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");

    //use the list of sample names to populate the select options
    d3.json("static/data/series_totals.json").then((data) => {
        var seriesNames = data.Series;

        seriesNames.forEach((Series) => {
            selector
                .append("option")
                .text(Series)
                .property("value", Series);
        });

        //Use the first sample from the list to build the initial plots
        var firstSeries = seriesNames[0];
        buildCharts(firstSeries);
        buildMetadata(firstSeries);
    });
}

// Initialize the dashboard
init();

  function optionChanged(newSeries) {
    // Fetch new data each time a new sample is selected
    buildMetadata(newSeries);
    buildCharts(newSeries);
    
  }

 //1. Create the buildCharts function.
  function buildCharts(sample) {
    // 2. Use d3.json to load and retrieve the samples.json file 
    d3.json("static/data/series_totals.json").then((data) => {
      console.log(data);
      // 3. Create a variable that holds the samples array. 
      var seriesArray = data.Series;
  
      // 4. Create a variable that filters the samples for the object with the desired sample number.
      var filteredSamples = samplesArray.filter(sampleObj => sampleObj.id == sample);
      // Del_3. 1. Create a variable that filters the metadata array for the object with the desired sample number.
      var filteredArray = newArray.filter(sampleObj => sampleObj.id == sample);
      
      //  5. Create a variable that holds the first sample in the array.
      var firstSample = filteredSamples[0];
      // Del_3. 2. Create a variable that holds the first sample in the metadata array.
      var firstMetadatum = filteredArray[0];
  
      // 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
      var otuIds = firstSample.otu_ids;
      var otuLabels = firstSample.otu_labels;
      var sampleValues = firstSample.sample_values;
  
      //Del 3.3 Create a variable that holds the washing frequency.
      var washFreq = parseFloat(firstMetadatum.wfreq);
  
      // 7. Create the yticks for the bar chart.
      // Hint: Get the the top 10 otu_ids and map them in descending order  
      //  so the otu_ids with the most bacteria are last. 
      var yticks = otuIds.slice(0, 10).map(otuIds => `OTU ${otuIds}`).reverse();
  
      // 8. Create the trace for the bar chart. 
      var barData = [
        {
        x: sampleValues.slice(0, 10).reverse(),
        y: yticks,
        orientation: 'h',
        hovertext: otuLabels.slice(0, 10).reverse(),
        type: 'bar'
      }];
  
      // 9. Create the layout for the bar chart. 
      var barLayout = {
        title: "<b>Top Ten Bacteria Cultures Found</b>"
      };
      
      // 10. Use Plotly to plot the data with the layout. 
      Plotly.newPlot("bar", barData, barLayout);
    });
    }

      // 1. Create the trace for the bubble chart.
    //   var bubbleData = [
    //     {
    //     x: otuIds.slice(0, 10).reverse(),
    //     y: sampleValues.slice(0, 10).reverse(),
    //     text: sampleValues.slice(0, 10).reverse(),
    //     mode: 'markers',
    //     marker: {
    //       size: sampleValues.slice(0, 10).reverse(),
    //       color: otuIds.slice(0, 10).reverse(),
    //       colorscale: 'sequential' 
    //     }}
    //   ];
  
      // 2. Create the layout for the bubble chart.
    //   var bubbleLayout = {
    //     title: "<b>Bacteria Cultures Per Sample</b>",
    //     xaxis: {title: "OTU ID"},
    //     margin:{
    //       l: 50,
    //       r: 50,
    //       b: 100,
    //       t: 100,
    //       pad: 4
    //     },
    //     showlegend: false,
    //     hovermode: 'closest'
    //   };
  
    //   // 3. Use Plotly to plot the data with the layout.
    //   Plotly.newPlot("bubble", bubbleData, bubbleLayout); 
  
      // 4. Create the trace for the gauge chart.
    //   var gaugeData = [{
    //     domain: {x: [0,1], y: [0,1]},
    //     value: washFreq,
    //     title: {text: '<b>Belly Button Washing Frequency<b><br>Scrubs per Week</br>'},
    //     type: 'indicator',
    //     mode: 'gauge+number',
    //     gauge: {
    //       axis: {range: [null, 10]},
    //       bar: {color: 'black'},
    //       steps: [
    //         { range: [0,2], color: 'red' },
    //         { range: [2,4], color: 'orange' },
    //         { range: [4,6], color: 'yellow' },
    //         { range: [6,8], color: 'lightgreen' },
    //         { range: [8,10], color: 'green' }
    //         ]
    //       }
    //   }];
        
      // 5. Create the layout for the gauge chart.
    //   var gaugeLayout = { 
    //     width: 500,
    //     height: 400,
    //     margin: { t: 0, b: 0 }
    //   };
    
    //   // 6. Use Plotly to plot the gauge data and layout.
    //   Plotly.newPlot("gauge", gaugeData, gaugeLayout);
    //   });
    // }


// function init() {
//     // Grab a reference to the dropdown select element
//     var selector = d3.select("#selDataset");
  
//     // Use the list of sample names to populate the select options
//     d3.json("static/data/samples.json").then((data) => {
//       var sampleNames = data.names;
  
//       sampleNames.forEach((sample) => {
//         selector
//           .append("option")
//           .text(sample)
//           .property("value", sample);
//       });
  
//       // Use the first sample from the list to build the initial plots
//       var firstSample = sampleNames[0];
//       buildCharts(firstSample);
//       buildMetadata(firstSample);
//     });
//   }
  
//   // Initialize the dashboard
//   init();
  
//   function optionChanged(newSample) {
//     // Fetch new data each time a new sample is selected
//     buildMetadata(newSample);
//     buildCharts(newSample);
    
//   }
  
//   // Demographics Panel 
//   function buildMetadata(sample) {
//     d3.json("static/data/samples.json").then((data) => {
//       var metadata = data.metadata;
//       // Filter the data for the object with the desired sample number
//       var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
//       var result = resultArray[0];
//       // Use d3 to select the panel with id of `#sample-metadata`
//       var PANEL = d3.select("#sample-metadata");
  
//       // Use `.html("") to clear any existing metadata
//       PANEL.html("");
  
//       // Use `Object.entries` to add each key and value pair to the panel
//       // Hint: Inside the loop, you will need to use d3 to append new
//       // tags for each key-value in the metadata.
//       Object.entries(result).forEach(([key, value]) => {
//         PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
//       });
  
//     });
//   }
  
//   // 1. Create the buildCharts function.
//   function buildCharts(sample) {
//     // 2. Use d3.json to load and retrieve the samples.json file 
//     d3.json("static/data/samples.json").then((data) => {
//       console.log(data);
//       // 3. Create a variable that holds the samples array. 
//       var samplesArray = data.samples;
//       // 3.0 Create a variable that holds the metadata array. 
//       var newArray = data.metadata;
  
//       // 4. Create a variable that filters the samples for the object with the desired sample number.
//       var filteredSamples = samplesArray.filter(sampleObj => sampleObj.id == sample);
//       // Del_3. 1. Create a variable that filters the metadata array for the object with the desired sample number.
//       var filteredArray = newArray.filter(sampleObj => sampleObj.id == sample);
      
//       //  5. Create a variable that holds the first sample in the array.
//       var firstSample = filteredSamples[0];
//       // Del_3. 2. Create a variable that holds the first sample in the metadata array.
//       var firstMetadatum = filteredArray[0];
  
//       // 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
//       var otuIds = firstSample.otu_ids;
//       var otuLabels = firstSample.otu_labels;
//       var sampleValues = firstSample.sample_values;
  
//       //Del 3.3 Create a variable that holds the washing frequency.
//       var washFreq = parseFloat(firstMetadatum.wfreq);
  
//       // 7. Create the yticks for the bar chart.
//       // Hint: Get the the top 10 otu_ids and map them in descending order  
//       //  so the otu_ids with the most bacteria are last. 
//       var yticks = otuIds.slice(0, 10).map(otuIds => `OTU ${otuIds}`).reverse();
  
//       // 8. Create the trace for the bar chart. 
//       var barData = [
//         {
//         x: sampleValues.slice(0, 10).reverse(),
//         y: yticks,
//         orientation: 'h',
//         hovertext: otuLabels.slice(0, 10).reverse(),
//         type: 'bar'
//       }];
  
//       // 9. Create the layout for the bar chart. 
//       var barLayout = {
//         title: "<b>Top Ten Bacteria Cultures Found</b>"
//       };
      
//       // 10. Use Plotly to plot the data with the layout. 
//       Plotly.newPlot("bar", barData, barLayout);
  
//       // 1. Create the trace for the bubble chart.
//       var bubbleData = [
//         {
//         x: otuIds.slice(0, 10).reverse(),
//         y: sampleValues.slice(0, 10).reverse(),
//         text: sampleValues.slice(0, 10).reverse(),
//         mode: 'markers',
//         marker: {
//           size: sampleValues.slice(0, 10).reverse(),
//           color: otuIds.slice(0, 10).reverse(),
//           colorscale: 'sequential' 
//         }}
//       ];
  
//       // 2. Create the layout for the bubble chart.
//       var bubbleLayout = {
//         title: "<b>Bacteria Cultures Per Sample</b>",
//         xaxis: {title: "OTU ID"},
//         margin:{
//           l: 50,
//           r: 50,
//           b: 100,
//           t: 100,
//           pad: 4
//         },
//         showlegend: false,
//         hovermode: 'closest'
//       };
  
//       // 3. Use Plotly to plot the data with the layout.
//       Plotly.newPlot("bubble", bubbleData, bubbleLayout); 
  
//       // 4. Create the trace for the gauge chart.
//       var gaugeData = [{
//         domain: {x: [0,1], y: [0,1]},
//         value: washFreq,
//         title: {text: '<b>Belly Button Washing Frequency<b><br>Scrubs per Week</br>'},
//         type: 'indicator',
//         mode: 'gauge+number',
//         gauge: {
//           axis: {range: [null, 10]},
//           bar: {color: 'black'},
//           steps: [
//             { range: [0,2], color: 'red' },
//             { range: [2,4], color: 'orange' },
//             { range: [4,6], color: 'yellow' },
//             { range: [6,8], color: 'lightgreen' },
//             { range: [8,10], color: 'green' }
//             ]
//           }
//       }];
        
//       // 5. Create the layout for the gauge chart.
//       var gaugeLayout = { 
//         width: 500,
//         height: 400,
//         margin: { t: 0, b: 0 }
//       };
    
//       // 6. Use Plotly to plot the gauge data and layout.
//       Plotly.newPlot("gauge", gaugeData, gaugeLayout);
//       });
//     }
  
function makeTrace(i) {
    return {
        y: Array.apply(null, Array(10)).map(() => Math.random()),
        line: { 
            shape: 'spline' ,
            color: 'red'
        },
        visible: i === 0,
        name: i,

    };
}

Plotly.plot('graph', ['2018', '2019', '2020', '2021', 'All'].map(makeTrace), {
    updatemenus: [{
        y: 0,
        yanchor: 'top',
        buttons: [{
            method: 'restyle',
            args: ['line.color', 'orange'],
            label: 'XWT'
        }, {
            method: 'restyle',
            args: ['line.color', 'blue'],
            label: 'BH in PC'
        }, {
            method: 'restyle',
            args: ['line.color', 'gold'],
            label: 'OPSUD'
        }, {
            method: 'restyle',
            args: ['line.color', 'silver'],
            label: 'Syphilis'
        }, {
            method: 'restyle',
            args: ['line.color', 'gray'],
            label: 'COVID-19'
        }, {
            method: 'restyle',
            args: ['line.color', 'lightgray'],
            label: 'PALTC'
        }, {
            method: 'restyle',
            args: ['line.color', 'skyblue'],
            label: 'PBH'
        }, {
            method: 'restyle',
            args: ['line.color', 'green'],
            label: 'CTSUDs'
        }, {
            method: 'restyle',
            args: ['line.color', 'yellow'],
            label: 'PSUD'
        }, {
            method: 'restyle',
            args: ['line.color', 'purple'],
            label: 'VHLC'
        }] 
    }, {
        y: 1,
        yanchor: 'top',
        buttons: [{
            method: 'restyle',
            args: ['visible', [true, false, false, false, false]],
            label: '2018'
        }, {
            method: 'restyle',
            args: ['visible', [false, true, false, false, false]],
            label: '2019'
        }, {
            method: 'restyle',
            args: ['visible', [false, false, true, false, false]],
            label: '2020'
        }, {
            method: 'restyle',
            args: ['visible', [false, false, false, true, false]],
            label: '2021'
        }, {
            method: 'restyle',
            args: ['visible', [false, false, false, false, true]],
            label: 'All'
        }]
    }],
});





// FOR REFERENCE
// var years = ['2014', '2015', '2016']

// Plotly.d3.csv('https://raw.githubusercontent.com/apodagrosi/datasets/master/PlotlyTest_Summary_SalesByDealerByYear.csv', (err, rows) => {
//   var data = years.map(y => {
//     var d = rows.filter(r => r.year === y)
    
//     return {
//       type: 'bar',
//       name: y,
//       x: d.map(r => r.dealer),
//       y: d.map(r => r.sales)
//     }
//   })
  
//   Plotly.newPlot('graph', data)
// });

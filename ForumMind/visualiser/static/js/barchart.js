// This barchart is INCOMPLETE!!! 131018 Still waiting on client approval.
function renderBarChart(data){
    var margin = {top: 20, right: 20, bottom: 70, left: 40},
        width = 1800 - margin.left - margin.right,
        height = 900 - margin.top - margin.bottom;

    var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    // var xAxis = d3.axisBottom(x).tickFormat(function(d){ return d.word;});
    // var yAxis = d3.axisLeft(y);
    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom")

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    var svg = d3.select("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
            "translate(" + margin.left + "," + margin.top + ")");
        
    x.domain(data.map(function(d) { return d.word; }));

    y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", "-.55em")
        .attr("transform", "rotate(-90)" );

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Frequency");

    svg.selectAll("bar")
        .data(data)
        .enter().append("rect")
        .style("fill", "steelblue")
        .attr("x", function(d) { return x(d.word); })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return y(d.frequency); })
        .attr("height", function(d) { return height - y(d.frequency); });
}

function serializeData(data){
    formattedList = [];
    var relevance_indicator = 0
    for (var o of data["words"]){
        formattedList.push({"word":o.word, "frequency":o.frequency});
    }
    console.log(formattedList)
    var size = ((relevance_indicator > 20 && relevance_indicator < 50) ? relevance_indicator : 50);
    formattedList = formattedList.slice(0,size);
    return formattedList;
}
function displayBarChart(data){
    sData = serializeData(data);
    renderBarChart(sData);
}


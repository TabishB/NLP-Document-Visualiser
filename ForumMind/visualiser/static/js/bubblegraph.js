/*
****Reference code https://bl.ocks.org/alokkshukla/3d6be4be0ef9f6977ec6718b2916d168****
*/

function renderBubbleGraph(data){
    var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 1800 - margin.left - margin.right,
    height = 900 - margin.top - margin.bottom;

    var color = d3.scaleOrdinal(d3.schemeCategory20);
    var bubble = d3.pack(data)
        .size([width, height])
        .padding(1.5);

    var svg = d3.select("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("class", "bubble")
        // .attr("transform", 
        // "translate(" + margin.left + "," + margin.top + ")");

    var nodes = d3.hierarchy(data)
        .sum(function(d) { return d.frequency; });

    var node = svg.selectAll(".node")
        .data(bubble(nodes).descendants())
        .enter()
        .filter(function(d){
            return  !d.children
        })
        .append("g")
        .attr("class", "node")
        .attr("transform", function(d) {
            console.log('transform ' + d)
            return "translate(" + d.x + "," + d.y + ")";
        });

    node.append("title")
        .text(function(d) {
            return d.word + ": " + d.frequency;
        });

    node.append("circle")
        .attr("r", function(d) {
            console.log(d)
            return d.r; 
        })
        .style("fill", function(d,i) {
            return color(i);
        });

    node.append("text")
        .attr("dy", ".2em")
        .style("text-anchor", "middle")
        .text(function(d) {
            return d.data.word.substring(0, d.r / 3);
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", function(d){
            return d.r/5 + Math.log(2*d.r)
        })
        .attr("fill", "white");

    node.append("text")
        .attr("dy", "1.3em")
        .style("text-anchor", "middle")
        .text(function(d) {
            return d.data.frequency;
        })
        .attr("font-family",  "Gill Sans", "Gill Sans MT")
        .attr("font-size", function(d){
            return d.r/5;
        })
        .attr("fill", "white");

    d3.select(self.frameElement)
        .style("height", height + "px");
}

// This function serializes data into the correct format for rendering.
function serializeData(data){
    dataset = {"children" : []};
    var formattedList = [];
    var relevance_indicator = 0;
    for (var o of data["words"]){
        formattedList.push({"word":o.word, "frequency":o.frequency})
        if (o.frequency > 1){
            relevance_indicator++;
        }
    }
    // formattedList = formattedList.reverse(function(a,b){return a.frequency - b.frequency;})
    var size = ((relevance_indicator > 20 && relevance_indicator < 50) ? relevance_indicator : 50);
    formattedList = formattedList.slice(0,size);
    dataset.children = formattedList;
    return dataset;
}

// This function is called by the template page.
function displayBubbleGraph(data){
    sData = serializeData(data);
    renderBubbleGraph(sData)
}


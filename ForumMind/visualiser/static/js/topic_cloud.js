function renderTopicCloud(data) {

    var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    color = d3.scaleOrdinal(d3.schemeCategory20),
    graph = data;

    var radius = d3.scaleSqrt()
        .range([0, 6]);

    var simulation = d3.forceSimulation()
        .force("link", 
            d3.forceLink().id(function(d) { return d.id; })
            .distance(function(d) { console.log(d.source.value); return radius(d.source.value / 5) + radius(d.target.value / 5); })
            .strength(function(d) {return 0.5; })
            )
        .force("charge", d3.forceManyBody().strength(-20))
            .force("collide", d3.forceCollide().radius(function(d) { return radius(d.value / 5) + 2; }))
        .force("center", d3.forceCenter(width / 2, height / 2));

    var link = svg.append("g")

        .attr("class", "links")
        .selectAll("path")
        .data(graph.links)
        .enter().append("svg:path")
        .attr("stroke-width", function(d) { return 1 });

    link.style('fill', 'none')
            .style('stroke', 'black')
        .style("stroke-width", '2px');

    var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
    .style('transform-origin', '50% 50%')
    .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));
    
    node.append('circle')
        .attr("r", function(d) { return radius(Math.sqrt(3*d.value)); })
        .attr("fill", function(d) { return color(d.group); })
         
    node.append("text")
        .attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .text(function(d) { return d.name; });

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {
        link.attr("d", function(d) {
            var dx = d.target.x - d.source.x,
                dy = d.target.y - d.source.y,
                dr = Math.sqrt(dx * dx + dy * dy);
            return "M" + 
                d.source.x + "," + 
                d.source.y + "A" + 
                dr + "," + dr + " 0 0,1 " + 
                d.target.x + "," + 
                d.target.y;
        });

        /*node.selectAll('circle')
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });*/
     
        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    }

    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }


    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }


    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
}
// Converts the data from the db to nodes and links objects.

function serializeData(data){
    var nodes = [];
    var links = [];
    var id = 0;
    var topicSum = 0;

    //Create a set of topic
    data["data"].forEach(function(e){
        var topicName = e["topic"];
        var topic_kw = e["keywords"];
        // console.log(topicName, topic_kw);
        // Add each child node to the topicname group
        for(var did = 0; did < topic_kw.length; did++){
            // Proportion things better.
            var frequency = topic_kw[did]["frequency"];
            var frequency = (frequency < 1 ? frequency*1000 : frequency);
            nodes.push({"id":id, "name":topic_kw[did]["word"], "value":frequency, "group":topicName});
            // keep track of topic_number and id.
            topicSum += frequency;
            id++;
        }
        //add the topicname group
        topicNode = {"id":id, "name":topicName, "value":topicSum, "group":topicName};
        id++;
        nodes.push(topicNode);
        // reset the topicsum and var i 
        topicSum = 0;

        for(var j = id-topic_kw.length-1; j < id-1; j++){
            links.push({"source":nodes[j], "target":topicNode, "group":topicName});
        }
    })
    console.log(nodes)
    console.log(links)
    serializedData = {}
    serializedData["nodes"] = nodes;
    serializedData["links"] = links;
    return serializedData
}

function displayTopicCloud(data){
    sData = serializeData(data)
    renderTopicCloud(sData);
}

/**
 * This is an incomplete function that changes the topic name to the radius. The goal of this function was to
 * display a box that would show more information about the topic including the total number of keywords and sum of frequencies.
 */
// $(document).ready(function(){
//     var topicName = '';
//     $("g").hover(function(){
//         topicName = $(this).children('text').html()
//         console.log($(this).children('circle').attr("r"))
//         console.log(topicName)
//         $(this).children('text').empty().append($(this).children('circle').attr("r"))
//     }, function(){
//         // Something to do when hover ends
//         $(this).children('text').empty().append(topicName)
//     });
// });

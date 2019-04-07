// Word cloud layout was inspired by Jason Davies, http://www.jasondavies.com/word-cloud/
function drawWordCloud(data){          
    var svg_location = "#chart";
    var width = $(document).width();
    var height = $(document).height();
    var fill = d3.scale.category20();
    wordData = data["words"]
    wordDict = convertDataToDict(wordData)
    var word_entries = d3.entries(wordDict);
    var xScale = d3.scale.linear()
        .domain([0, d3.max(word_entries, function(d) {
            return d.value;
        })
        ])
        .range([10,100]);

    d3.layout.cloud().size([width, height])
        .timeInterval(20)
        .words(word_entries)
        .fontSize(function(d) { return xScale(+d.value); })
        .text(function(d) { return d.key; })
        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .on("end", draw)
        .start();

    function draw(words) {
        d3.select(svg_location).append("svg")
            .attr("width", width)
            .attr("height", height)
        .append("g")
            .attr("transform", "translate(" + [width >> 1, height >> 1] + ")")
        .selectAll("text")
            .data(words)
        .enter().append("text")
            .style("font-size", function(d) { return xScale(d.value) + "px"; })
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return fill(i); })
            .attr("text-anchor", "middle")
            .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function(d) { return d.key; });
    }

    d3.layout.cloud().stop();
}
function UrlExists(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
}
function drawWordCloudFromJSON(filepath){
               
    console.log(filepath)
    var svg_location = "#chart";
    var width = $(document).width()*.5;
    var height = $(document).height()*.5;
    var fill = d3.scale.category20();
    //Because this runs asynchronously everything that uses the data structure has to be inside 
    //the function...
    console.log(UrlExists("wordcloud.json"))
    d3.json(filepath, function(data, error){
        var word_count = {}
        console.log(data)
        if(!error){
            data["words"].forEach(function(element) {
                word_count[element["word"]] = element["frequency"]
            })
            word_entries = d3.entries(word_count);
            console.log(word_entries)
            var xScale = d3.scale.linear()
                .domain([0, d3.max(word_entries, function(d) {
                    return d.value;
                })
                ])
                .range([10,100]);
        
            d3.layout.cloud().size([width, height])
                .timeInterval(20)
                .words(word_entries)
                .fontSize(function(d) { return xScale(+d.value); })
                .text(function(d) { return d.key; })
                .rotate(function() { return ~~(Math.random() * 2) * 90; })
                .font("Impact")
                .on("end", draw)
                .start();
        
            function draw(words) {
                d3.select(svg_location).append("svg")
                    .attr("width", width)
                    .attr("height", height)
                .append("g")
                    .attr("transform", "translate(" + [width >> 1, height >> 1] + ")")
                .selectAll("text")
                    .data(words)
                .enter().append("text")
                    .style("font-size", function(d) { return xScale(d.value) + "px"; })
                    .style("font-family", "Impact")
                    .style("fill", function(d, i) { return fill(i); })
                    .attr("text-anchor", "middle")
                    .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .text(function(d) { return d.key; });
            }
        
            d3.layout.cloud().stop();
        }
    })
}
// For testing and to call the correct function.
function displayWordCloud(data){
    console.log(data)
    drawWordCloud(data)
}

function convertDataToDict(data){
    wordDict = {};
    wordData.forEach(function(e) {
        wordDict[e["word"]] = e["frequency"]
    })
    return wordDict;

}
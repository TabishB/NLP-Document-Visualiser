//This is a test function which can also be used in the final version if necessary.
//It Creates a JSON file
function createWordData(file){
    var common = `poop,i,me,my,myself,we,us,our,ours,ourselves,you,your,yours,yourself,
                        yourselves,he,him,his,himself,she,her,hers,herself,it,its,itself,they,
                        them,their,theirs,themselves,what,which,who,whom,whose,this,that,these,
                        those,am,is,are,was,were,be,been,being,have,has,had,having,do,does,did,
                        doing,will,would,should,can,could,ought,i'm,you're,he's,she's,it's,we're,
                        they're,i've,you've,we've,they've,i'd,you'd,he'd,she'd,we'd,they'd,i'll,
                        you'll,he'll,she'll,we'll,they'll,isn't,aren't,wasn't,weren't,hasn't,haven't,
                        hadn't,doesn't,don't,didn't,won't,wouldn't,shan't,shouldn't,can't,cannot,
                        couldn't,mustn't,let's,that's,who's,what's,here's,there's,when's,where's,
                        why's,how's,a,an,the,and,but,if,or,because,as,until,while,of,at,by,for,with,
                        about,against,between,into,through,during,before,after,above,below,to,from,up,
                        upon,down,in,out,on,off,over,under,again,further,then,once,here,there,when,where,
                        why,how,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,
                        so,than,too,very,say,says,said,shall
                        `;
        // Read in JSON Data from file
        var req = new XMLHttpRequest()
        fp = "data/".concat(file)
        console.log(fp)
        req.open("GET", fp, false)
        req.send(null)
        var json_data = JSON.parse(req.responseText) // <== Comment out this and above if you want to use the function argument
        var text_string = json_data["testText"]["abstract"].join()
        text_string = JSON.stringify(text_string)
        //Start analysing the data
        var word_count = {};
        var words = text_string.split(/[ '\-\(\)\*":;\[\]|{},.!?]+/);
        if (words.length == 1){
            word_count[words[0]] = 1;
        } else {
            words.forEach(function(word){
                var word = word.toLowerCase();
                if (word != "" && common.indexOf(word)==-1 && word.length>1){
                    if (word_count[word]){
                        word_count[word]++;
                    } else {
                        word_count[word] = 1;
                    }
                }
            })
        }
        /* Testing the input is correct by printing it in the dom. */
        // docLocation = document.getElementById("test")
        // console.log(docLocation)
        // var rawWordData = JSON.stringify(word_count, null, 2)
        // docLocation.innerHTML = rawWordData
        /*This posts the json data to the server if you wanted. Need to input URL*/
        // $.ajax({
        //     url: '[input URL here]',
        //     dataType: 'json',
        //     type: 'post',
        //     contentType: 'application/json',
        //     data: JSON.stringify(word_count)
        // })
        console.log(word_count)
        return word_count
}
// Requires a JSON input
function drawWordCloud(filepath){
               
    console.log(filepath)
    var svg_location = "#chart";
    var width = $(document).width()*.5;
    var height = $(document).height()*.5;
    console.log(width, height)
    var fill = d3.scale.category20();
    console.log(filepath)
    //Because this runs asynchronously everything that uses the data structure has to be inside 
    //the function...
    d3.json(filepath, function(data, error){
        var word_count = {}
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

function displayWordCloud(){
    // word_count = createWordData("wordcloud.json")
    drawWordCloud("wordcloud.json");
}

// Run immediately
displayWordCloud()
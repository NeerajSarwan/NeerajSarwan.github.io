---
layout: page
title: Image
subtitle: Image recognition
published: true
---


<html>
<body>


<input type="url" id="myURL" value="http://cdn2-www.dogtime.com/assets/uploads/gallery/30-impossibly-cute-puppies/impossibly-cute-puppy-8.jpg">


<button onclick="myFunction()">Classify</button>
<pre id="json"></pre>

<script src="//algorithmia.com/v1/clients/js/algorithmia-0.2.0.js" type="text/javascript"></script>
<script>
function myFunction() {
    var x = document.getElementById("myURL").value;
    Algorithmia.client("simBrvTtxJZg/c/TZCBlTVKAm4p1")
           .algo("algo://deeplearning/InceptionNet/1.0.2")
           .pipe(x)
           .then(function(output) {
             console.log(output.result.tags);
             var str = JSON.stringify(output.result.tags, null, 2); // spacing level = 2
             document.getElementById("json").innerHTML =str;
           	});
          
}

</script>

</body>
</html>


"use strict";
var filename = 'Expert.json';
var map = require('./' + filename);
var maps = [];
var mapnames = ["./Easy.json", "./Normal.json", "./Hard.json", "./Expert.json", "./ExpertPlus.json"];

for(var i = 0; i < mapnames.length; i++)
{
	if (mapnames[i] != './'+filename)
	{
		try{
			var thismap = {name: mapnames[i],map:require(mapnames[i])};
			maps.push(thismap)
		}
		catch(err){
			console.log(mapnames[i] + " does not exist");
		}
	}
}
console.log(maps.length)

//copying events
for(var i = 0; i < maps.length; i++)
{
	maps[i].map._events = map._events
	//write to file
	var jsonData = JSON.stringify(maps[i].map);
	var fs = require('fs');
	fs.writeFile(maps[i].name.substring(2, maps[i].name.length), jsonData, function(err) {
	    if (err) {
	        console.log(err);
	    }
	});
}
//sort events
// events.sort(function(a,b){
// 	return a._time - b._time;
// });

//write to file



//cry a lot

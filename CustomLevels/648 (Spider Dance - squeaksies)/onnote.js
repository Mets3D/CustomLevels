"use strict";
var filename = 'Expert.json';
var map = require('./' + filename);
var events = map._events;
var notes = map._notes;
var color = "blue";
var pos = 2;
//copying events
var lasttime = 0;
var newevents = [];
for(var i = 0; i < notes.length; i++)
{
	if (notes[i]._time != lasttime)
	{
		var newevent = {
         "_time":0.0,
         "_type":pos,
         "_value":0
	    };
	    pos = 2.5 + (2.5 - pos)
	    newevent._time = notes[i]._time;
	    if(getLastColor(notes[i]._time) == "red")
	    {
	    	newevent._value = 3;
	    }
	    else
	    {
	    	newevent._value = 7;
	    }
	    newevents.push(newevent);
	    var stopevent = {
	    	"_time":newevent._time - 0.1,
		    "_type": newevent._type,
		    "_value": 0
	    }
	    newevents.push(stopevent)
	    var speedevent1 ={
	    	"_time":newevent._time,
		    "_type": newevent._type+10,
		    "_value": 0
	    }
	    var speedevent2 ={
	    	"_time":newevent._time-0.05,
		    "_type": newevent._type+10,
		    "_value": 20
	    }

	    newevents.push(speedevent1);
	    newevents.push(speedevent2);
	    var ringevent1 ={
	    	"_time":newevent._time,
		    "_type": newevent._type+6,
		    "_value": 0
	    }
	    var ringevent2 ={
	    	"_time":newevent._time+0.2,
		    "_type": newevent._type+6,
		    "_value": 8
	    }
	    newevents.push(ringevent1);
	    newevents.push(ringevent2);
	}
}
console.log(newevents.length)
map._events = events.concat(newevents);
//sort events
events.sort(function(a,b){
	return a._time - b._time;
});

//write to file
var jsonData = JSON.stringify(map);
var fs = require('fs');
fs.writeFile(filename, jsonData, function(err) {
    if (err) {
        console.log(err);
    }
});

//cry a lot
function getLastColor(time)
{
	for (var i = 0; i < events.length; i++)
	{
		if (events[i]._time >= time)
		{
			if(events[i]._type <= 3)
			{
				return "blue";
			}
			else
			{
				return "red";
			}
		}
	}
}
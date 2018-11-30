$.fn.sensorReactToTouch = function(){
	$('.update-sensor').on('click',function(){
		var id = $(this).attr('id');
		//console.log('touched');
		$.fn.updateSensor(id);
		
	});
}

$.fn.readSonar = function(number){
	// Perform Pandaboard request
	//console.log("contacting pandaboard with value: "+number);
	var sensorToRead = "S-"+number;
	$.fn.trackHistory("Updated sensor "+number);
	xml_http_post("web/index.html", sensorToRead, sonarHandler);
}

$.fn.updateSensor = function(id){
	//console.log("Sensor with ID: "+id+" is being updated");
	
	switch(id){
		case "s1": $.fn.readSonar(1);break;
		case "s2": $.fn.readSonar(2);break;
		case "s3": $.fn.readSonar(3);break;
		// Add more cases for every new sensor we add
	}
}

function sonarHandler(req){
	
	var response = req.responseText;
	var which = response.substr(0,3);
	var value = response.substr(4);
	
	//console.log("handling the sonar "+which+" "+value);
	
	switch(which){
		case "S-1": $.fn.changeSensorValue(1,value);break;
		case "S-2": $.fn.changeSensorValue(2,value);break;
		case "S-3": $.fn.changeSensorValue(3,value);break;
		case "S-4": $.fn.changeSensorValue(4,value);break;
		default: break;
	}
}

$.fn.changeSensorValue = function(which,value){
	value = value.trim();
	var floatVal = parseFloat(value);

	switch(which){
		case 1: $('.sensor-reading-1').empty().html(value);break;
		case 2: $('.sensor-reading-2').empty().html(value);break;
		case 3: $('.sensor-reading-3').empty().html(value);break;
		case 4: $('.sensor-reading-4').empty().html(value);break;
		default: break;
	}
}

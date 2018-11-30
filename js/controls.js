$.fn.controlSettings = function(){
	$("input[name='Hold']").on('change', function(){
		if($(this).val() == "hold-control-value"){
				$.fn.holdValue();
		}else{
				$.fn.allowValueChanges();
		}
		$.fn.trackHistory("changed mode to "+$(this).val());
	});
}

$.fn.holdValue = function(){
	$("#degrees").val("N/A");
	$("#seconds").val("N/A");
	$("#slider").slider("disable");
	$("#slider-duration").slider("disable");
	xml_http_post("web/index.html", "hold", req_handler);
}

$.fn.allowValueChanges = function(){
	$("#degrees").val(window.angle+" degrees");
	$("#seconds").val(window.duration+" seconds");
	$("#slider").slider("enable");
	$("#slider-duration").slider("enable");
	xml_http_post("web/index.html", "a-"+window.angle, req_handler);
	xml_http_post("web/index.html", "d-"+window.duration, req_handler);
}
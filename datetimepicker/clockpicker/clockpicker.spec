{
	"name": "datetimepicker-clockpicker",
	"displayName": "clockpicker",
	"version": 1,
	"definition": "datetimepicker/clockpicker/clockpicker.js",
	"libraries": [{
			"name": "clock picker js",
			"version": "0.0.7",
			"url": "datetimepicker/clockpicker/lib/bootstrap-clockpicker.min.js",
			"mimetype": "text/javascript"
		},
		{
			"name": "clock picker css",
			"version": "0.0.7",
			"url": "datetimepicker/clockpicker/lib/bootstrap-clockpicker.min.css",
			"mimetype": "text/css"
		}],
	"model":
	{	
		"styleClass": {"type": "styleclass","tags":{"scope": "design"}},
		"dataProviderID" : { "type":"dataprovider", "pushToServer": "allow","tags": { "scope" :"design" }, "ondatachange": { "onchange":"onDataChangeMethodID", "callback":"onDataChangeCallback"}},
		"default" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "now"},
		"placement" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "bottom ","values":["top","bottom","left","right"]},
		"align" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "left", "values":["top","bottom","left","right"]},
		"donetext" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "Done"},
		"autoclose" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"vibrate" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : true},
		"twelvehour" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false}
	},
	
	"handlers":
	{
	"onDataChangeMethodID" : {
	          "returns": "boolean",

	        	"parameters":[
								{
						          "name":"oldValue",
								  "type":"${dataproviderType}"
								},
								{
						          "name":"newValue",
								  "type":"${dataproviderType}"
								},
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
	        },
	"init" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"beforeShow" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"afterShow" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"beforeHide" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"afterHide" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"beforeHourSelect" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"afterHourSelect" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"beforeDone" : {"parameters":[{"name":"event","type":"JSEvent"}]},
	"afterDone" : {"parameters":[{"name":"event","type":"JSEvent"}]}
	},
	
	"api":
	{
	 "show": {"parameters":[]},
	 "hide": {"parameters":[]},
	 "toggleView": {"parameters":[]}
	}
}
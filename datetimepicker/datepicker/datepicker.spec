{
	"name": "datetimepicker-datepicker",
	"displayName": "datepicker",
	"version": 1,
	"definition": "datetimepicker/datepicker/datepicker.js",
	"libraries": [{
			"name": "date picker js",
			"version": "4.3.1",
			"url": "datetimepicker/datepicker/lib/jtsage-datebox.bootstrap.min.js",
			"mimetype": "text/javascript"
		},
		{
			"name": "date picker css",
			"version": "4.3.1",
			"url": "datetimepicker/datepicker/lib/jtsage-datebox.bootstrap.min.css",
			"mimetype": "text/css"
		},
		{
			"name": "date picker custom css",
			"version": "1.0.0",
			"url": "datetimepicker/datepicker/datepicker.css",
			"mimetype": "text/css"
		}],
	"model":{
		"afterToday" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"beforeToday" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"dataProviderID" : { "type":"dataprovider", "pushToServer": "allow","tags": { "scope" :"design" }, "ondatachange": { "onchange":"onDataChangeMethodID", "callback":"onDataChangeCallback"}},
		"lockInput" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"styleClass": {"type": "styleclass","tags":{"scope": "design"}},				
		"useFocus" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"useKinetic" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : false},
		"useSetButton" : {"type":"boolean" , "tags": { "scope" :"design" }, "default" : true},
		"dateFieldOrder" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "m,d,y"},
		"dateFormat" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "%m/%d/%Y"},
		"maxDays" : {"type":"string" , "tags": { "scope" :"design" }},
		"setDateButtonLabel" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "Set Date"},
		"titleDateDialogLabel" : {"type":"string" , "tags": { "scope" :"design" }, "default" : "Set Date"}
				
		},
	"handlers":{
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
	        }
	},
	"api":{}
}


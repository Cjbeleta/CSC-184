// get latitude and longitude of specific location

const https = require("https");

var cityname;
var input = process.openStdin();
var url = "https://maps.googleapis.com/maps/api/geocode/json?address=";

process.stdout.write("\nEnter city: ");

input.addListener("data", function(d) {
	cityname = d.toString();
	url += cityname;
	process.stdout.write(url);
	https.get(url, res => {
  	res.setEncoding("utf8");
  	var store_data = "";
  	res.on("data", data => {
    	store_data += data;
  	});
  	res.on("end", () => {
  		
    	store_data = JSON.parse(store_data);
    	console.log(
      	`\nLocation: ${store_data.results[0].formatted_address}`,
      	`\n\nLatitude: ${store_data.results[0].geometry.location.lat}`,
      	`\n\nLongitude: ${store_data.results[0].geometry.location.lng}`
    		);
  		});
	});
});


var map, heatmap;
var layers = [];

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 12,
		center: {lat: 25.0551755, lng: 121.5446997},
		mapTypeControl: false,
		streetViewControl: false,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	stationPoints = getStationPoints()
	heatmap = new google.maps.visualization.HeatmapLayer({
		data: stationPoints,
		radius: 10,
		map: map
	});
	layers.push(heatmap);
}

function updateMap() {
	initMap()
}

function clearLayers() {
	for (var l in layers) {
		layers[l].setMap(null);
	}
	layers = []
	return
}

function printPoints() {
	for (var s in stationPoints) {
		console.log(stationPoints[s].weight)
	}
}

// function changeData() {
// 	d3.csv("data2.csv", draw);
// 	stationPoints = getStationRadPoints('2015-11-19')
// 	var points = []
// 	for (var s in stationPoints) {
// 		var radius = getRadius(stationPoints[s].weight)
// 		// radius = getRadius(flow['STATION_ID']);
// 		if (points[radius] == null) {
// 			points[radius] = [stationPoints[s]];
// 		} else {
// 			points[radius].push(stationPoints[s]);
// 		}
		
// 	}
	
// 	clearLayers();
// 	var tmp = []
// 	var min = 100
// 	for (var p in points) {
// 		if (parseInt(p) < min) {
// 			min = parseInt(p)
// 		}
// 		heatmap = new google.maps.visualization.HeatmapLayer({
// 			data: points[p],
// 			map: map,
// 			radius: p
// 		});
// 		console.log('Radius:', p);
// 		layers.push(heatmap);
// 	}

// }

// function getFlow(data) {
// 	return flow;
// }

function getRadius(flow) {
	var r = flow;
	r = Math.floor(flow/10000)*10
	if (r > 100) {
		r = 50
	} else if (r == 0) {
		r = 1
	} else {
		r /= 2
	}
	console.log('Rad:', r, flow/1000, Math.floor(Math.log(Math.pow(2, r))) / 20, flow);
	return r
}

function getRadiusMap(date) {
	var points = {}
	var num = 0
	stationPoints = getStationRadPoints(date)
	for (var s in stationPoints) {
		var radius = getRadius(stationPoints[s].weight)
		// radius = getRadius(flow['STATION_ID']);
		if (points[radius] == null) {
			num += 1
			points[radius] = [stationPoints[s]];
		} else {
			points[radius].push(stationPoints[s]);
		}		
	}
	
	clearLayers();
	var tmp = []
	var min = 100
	for (var p in points) {
		if (parseInt(p) < min) {
			min = parseInt(p)
		}
		heatmap = new google.maps.visualization.HeatmapLayer({
			data: points[p],
			map: map,
			radius: p
		});
		// console.log('Radius:', p);
		layers.push(heatmap);
	}
	return 
}

function getStationRadPoints(file) {
	var data = data_all[file]
	var points = []
	for ( var s in stations) {
		points.push({location: new google.maps.LatLng(stations[s]['lat'], stations[s]['lng']), weight: data[stations[s]['id']]})
	}
	return points
}

function getStationPoints() {
	var points = []
	for ( var s in stations) {
		points.push({location: new google.maps.LatLng(stations[s]['lat'], stations[s]['lng']), weight: 1})
	}
	return points
}

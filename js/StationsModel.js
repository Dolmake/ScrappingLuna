
function StationsModel() {


	this.helloWorld = function () {
		console.log("helloWorld from stations model")
	}
	var This = this;
	This._stations = [];
	This._initiated = false;

	this.initialize = function (url, callback) {
		//TODO: load the Model

		$.getJSON(url, function (data) {
			console.log(data);
			This._stations = data["stations"];
			This._initiated = true;

			callback();
		});
	}

	this.getStations = function () {
		//TODO: return the proper station
		return This._stations
	}

	this.transformStationsToD3 = function () {

		var result = []

		var index = 0
		This._stations.forEach(function (station) {

			//Para cada station, creamos un objeto nuevo con los
			//campos que necesita el gráfico de D3 para pintarse : 
			// { State: 'AL', freq: { low: 4786, mid: 1319, high: 249 } }

			var stationTransformed = {}
			stationTransformed["State"] = station["name"]
			var freq = {}
			freq["low"] = station["dock_bikes"]
			freq["high"] = station["total_bases"]
			freq["mid"] = 0
			stationTransformed["freq"] = freq


			index += 1

			if (index <= 10) {
				result.push(stationTransformed)
			}


		}, this);

		return result

	}

	this.sortStationsBy = function (key) {

		This._stations.sort(function (a, b) {
			var keyA = a[key];
			var	keyB = b[key]
			// Compare the 2 dates
			if (keyA < keyB) return -1;
			if (keyA > keyB) return 1;
			return 0;
		});

	}


}

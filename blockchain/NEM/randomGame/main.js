$(document).ready(function () {

	// Load nem-browser library
	var nem = require("nem-sdk").default;

    // Create an NIS endpoint object
	var endpoint = nem.model.objects.create("endpoint")(nem.model.nodes.defaultTestnet, nem.model.nodes.defaultPort);
	var common = nem.model.objects.create("common")("1983Nem2#75019;", "7a431b6f6047ce1b44fb1c779f5dec3f97817ed644340dfe379b798103f507fb");
	var mosaicDefinitions = nem.model.objects.get("mosaicDefinitionMetaDataPair");

	var savedScores = JSON.parse(window.localStorage.getItem('random-game-score'));
	var scores = {};

	if (savedScores !== null)
	{
		scores = savedScores;
	}
	else
	{
		scores = {};
	}

  function roll() {
		var random = Math.floor(Math.random() * 1000001);
		console.log(random);
		$("#result").html(random);
  }

  function save() {
		var address = nem.model.address.clean($('#address').val());
		var result = $('#result').html();
		if (!(result => 0)) return alert("You need to roll the dice first!");

		var transferTransaction = nem.model.objects.get('transferTransaction');
		transferTransaction.amount = 0;
		transferTransaction.recipient = address;
		transferTransaction.message = "NEM Random Game Transaction";

		var mosaicAttachment = nem.model.objects.create('mosaicAttachment')("emacsfreeman", "score", result);
		transferTransaction.mosaics.push(mosaicAttachment);

		nem.com.requests.namespace.mosaicDefinitions(endpoint, mosaicAttachment.mosaicId.namespaceId).then(function(res){
			var definition = nem.utils.helpers.searchMosaicDefinitionArray(res.data, ["score"]);
			var fullName = nem.utils.format.mosaicIdToName(mosaicAttachment.mosaicId);
			mosaicDefinitions[fullName] = {};
			mosaicDefinitions[fullName].mosaicDefinition = definition[fullName];

			var preparedTransaction = nem.model.transactions.prepare("mosaicTransferTransaction")(common, transferTransaction, mosaicDefinitions, nem.model.network.data.testnet.id);
			preparedTransaction.fee = 500000;

			nem.model.transactions.send(common, preparedTransaction, endpoint).then(function(res){
				if (res.code >= 2)
				{
					 alert(res.message);
				}
				else
				{
					scores[address] = result;
					window.localStorage.setItem('random-game-score', JSON.stringify(scores));
					updateScoringTable();
				}
			}, function(err){
				console.log(err);
			});
		}, function(err){
			console.log(err);
		});


  }

	function updateScoringTable(){
		var list = [];
		for (var key in scores)
		{
			if (scores.hasOwnProperty(key))
			{
				list.push(key + ": " + scores[key]);
			}
		}
		var highscoreTable = $('#highscoreTable');
		highscoreTable.html('');
		$.each(list, function(i){
			var li = $('<li/>').appendTo(highscoreTable);
			var text = $('<span/>').text(list[i]).appendTo(li);
		});
	}


	updateScoringTable();

	$("#roll").click(function() {
	  roll();
	});
  $("#save").click(function() {
	  save();
	});

});



$(function() {

    $('#side-menu').metisMenu();

	$("#user-profile").submit(function(e){
		e.preventDefault();
		var data = $(this).serializeArray()
		data = objectifyForm(data);
		console.log(data);
		$.ajax({
			data: data,
			type: "POST",
			success: function(data) {
				console.log(data);
			},
			error: function(data) {
				console.log(data);
			}
		})
	})

	function objectifyForm(formArray) {
		let returnArray = {};
		for (var i=0;i<formArray.length;i++) {
			if (formArray[i]['value']) {
				returnArray[formArray[i]['name']] = formArray[i]['value'];
			}			
		}
		return returnArray;
	}

});
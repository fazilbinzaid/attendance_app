

$(function() {

  $('#side-menu').metisMenu();

	$("#user-profile").submit(function(e){
		e.preventDefault();
		var data = $(this).serializeArray();
		data = objectifyForm(data);
		$.ajax({
			data: data,
			type: "POST",
			success: function(data) {
				$(".alert").append('<div id="alert" class="alert text-center alert-info alert-dismissable">' +
												 		"<strong>" + data.message + "</strong></div>");
			},
			error: function(data) {
        console.log(data);
				$(".alert").append('<div id="alert" class="alert text-center alert-danger alert-dismissable">' +
												 		"<strong>" + data + "</strong></div>");
			}
		});
	});

	function objectifyForm(formArray) {
		var returnArray = {};
		for (var i=0;i<formArray.length;i++) {
			if (formArray[i].value) {
				returnArray[formArray[i].name] = formArray[i].value;
			}
		}
		return returnArray;
	}

});

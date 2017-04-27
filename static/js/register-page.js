

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
												 		"<strong>" + data.message + "</strong></div>");
			}
		});
	});

});

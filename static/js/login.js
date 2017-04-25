





$(function() {

	$('#side-menu').metisMenu();

  $.validate({
            modules: 'security'
        });


	$("#forgot-password-form").hide();

	$('#forgot-password-form-link').click(function(e) {
		$("#forgot-password-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
 		$("#register-form").fadeOut(100);
		e.preventDefault();
	});
    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").delay(100).fadeIn(100);
 		$("#forgot-password-form").fadeOut(100);
		e.preventDefault();
	});
	// $('#register-form-link').click(function(e) {
	// 	$("#register-form").delay(100).fadeIn(100);
 // 		// $("#login-form").delay(100).fadeIn(100);
 // 		$("#forgot-password-form").fadeOut(100);
	// 	e.preventDefault();
	// });

	});

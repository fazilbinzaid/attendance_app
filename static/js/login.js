





$(function() {

	$('#side-menu').metisMenu();

	$(window).bind("load resize", function() {
        var topOffset = 50;
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    // var element = $('ul.nav a').filter(function() {
    //     return this.href == url;
    // }).addClass('active').parent().parent().addClass('in').parent();
    var element = $('ul.nav a').filter(function() {
        return this.href !== url;
    });
    // .addClass('active').parent();

    while (true) {
        if (element.is('li')) {
            element = element.parent().addClass('in').parent();
        } else {
            break;
        }
    }






	$("#forgot-password-form").hide()

	$('#forgot-password-form-link').click(function(e) {
		$("#forgot-password-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
 		$("#register-form").fadeOut(100);
		e.preventDefault();
	});
    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		// $("#register-form").delay(100).fadeIn(100);
 		$("#forgot-password-form").fadeOut(100);
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		// $("#login-form").delay(100).fadeIn(100);
 		$("#forgot-password-form").fadeOut(100);
		e.preventDefault();
	});
	
	});
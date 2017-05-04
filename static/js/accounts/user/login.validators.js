

$(function() {

  $("#id_username").on("change", function(){
    $.ajax({
      data: {
        username: $(this).val()
      },
      url: "/check-username/",
      success: function(data) {
        if (data === "False") {
          $("#username").append('<span class="help-block form-error">This username has already been taken. Choose another.</span>');
          return false;
        }
      }
    });
  });
});

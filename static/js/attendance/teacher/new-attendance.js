
// =============FUNCTION RUNS EVERYTIME PAGE RELOADS===================

$(function() {
  $("#side-menu").metisMenu();
  checkBox();
  $("#mytable").DataTable();
});

$("#attendance").submit(function(event) {
  event.preventDefault();
  var data = $(this).serializeArray();
  console.log(data);
  data = objectifyForm(data, true);
  if (!data.hour) {
    $(".alert").html('<div id="alert" class="alert text-center alert-danger alert-dismissable">' +
                        "<strong>" + "Please select the corresponding hour." + "</strong></div>");
    return false;
  }
  console.log(data);
  $.ajax({
    type: "POST",
    data: data,
    success: function(data) {
      $successDiv = $('<div id="alert" class="alert text-center alert-info alert-dismissable">' +
                          "<strong>" + data.message + "</strong></div>");
      $(".alert").html($successDiv);
    },
    error: function(data) {
      console.log(data);
      $errorDiv = $('<div id="alert" class="alert text-center alert-danger alert-dismissable">' +
                          "<strong>" + data.responseText.substring(0, 250) + "</strong></div>");
      $(".alert").html($errorDiv);
    }
  });
});

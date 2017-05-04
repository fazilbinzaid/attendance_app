
// =============FUNCTION RUNS EVERYTIME PAGE RELOADS===================

$(function() {
  $("#side-menu").metisMenu();
  checkBox();
});

// ==========SELECTING CHECKBOX IF EVERYONE IS PRESENT=================

function checkBox(){
  $("#mytable #checkall").click(function () {
          if ($("#mytable #checkall").is(':checked')) {
              $("#mytable input[type=checkbox]").each(function () {
                  $(this).prop("checked", true);
              });

          } else {
              $("#mytable input[type=checkbox]").each(function () {
                  $(this).prop("checked", false);
              });
          }
      });

      $("[data-toggle=tooltip]").tooltip();
}

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

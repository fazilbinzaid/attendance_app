
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
  console.log(data);
  $.ajax({
    type: "POST",
    data: data,
    success: function(data) {
      console.log(data);
    },
    error: function(data) {
      console.log(data);
    }
  });
});



$(function(){

  $("#edit-att-tab").hide();

// ============AJAX Query to get the attendance data from backend===============

  $("#get-date").submit(function(event) {
    event.preventDefault();
    var date = $("#id_for_history").val();
    var batch = $("#id_for_batch").val();
    var hour = $("#id_for_hour").val();
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var history = {           //data to be sent to
      batch_id: batch,        //backend for
      hour: hour,             //querying
      day: day,               //attendance
      month: month,           //data.
      year: year
    }

    $.ajax({
      url: "/user/class/get-history/",
      type: "GET",
      data: history,
      success: function(data) {

        $("#edit-att-tab").show();       //show the hidden table on request.
        $("#mytable tbody").empty();     //empty the element on each request.
        $(".alert").empty();             //empty the element on each request.
        var inputDate = new Date(date);  //create date instance.
        var today = new Date();          //create today's date instance.
        var tr = "";

        for (var i=0; i<data.results.length; i++) {

          if (inputDate.setHours(0,0,0,0) == today.setHours(0,0,0,0)) {   //check whether date is today or not.

              if (data.results[i].is_present) { //if the student is present in the requested data => check the checkbox.

                tr += '<tr><td><input type="hidden" id="id_is_present" name="';
                tr += data.results[i].student__pk + '" value="0">';

                tr += '<input type="checkbox" id="id_is_present" name="'
                tr += data.results[i].student__pk + '" value="1" checked></td>';

              }
              else {

                tr += '<tr><td><input type="hidden" id="is_present" name="'
                tr += data.results[i].student__pk + '" value="0">';

                tr += '<input type="checkbox" id="id_is_present" name="'
                tr += data.results[i].student__pk + '" value="1"></td>';

              }

              $("#att_button").show()
          }
          else {

              $("#att_button").hide();

              tr += '<tr><td>' + attendance(data.results[i].is_present) + '</td>';

          }

          tr += '<td>' + data.results[i].code + '</td>';
          tr += '<td>' + data.results[i].student__roll_no + '</td>';
          tr += '<td>' + data.results[i].student__first_name
          tr += ' ' + data.results[i].student__last_name + '</td></tr>';

        }

        $("#mytable tbody").append(tr);

      },
      error: function(data) {
        console.log(data);
      }
    });
  });

  // ================ AJAX request for editing attendance data. ================

  $("#edit-att-form").submit(function(event) {
    event.preventDefault();
    var attData = $(this).serializeArray();
    var depData = $("#get-date").serializeArray();

    attData = objectifyForm(attData, true);
    depData = objectifyForm(depData);

    var date = $("#id_for_history").val();
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var postData = {
      month: month,
      day: day,
      year: year,
    }

    postData = Object.assign(postData, depData, attData);

    $.ajax({
      type: "POST",
      data: postData,
      success: function(data) {
        $successDiv = $('<div id="alert" class="alert text-center alert-info alert-dismissable col-lg-8">' +
                            "<strong>" + data.message + "</strong></div>");
        $(".alert").html($successDiv).fadeOut(6000);
      },
      error: function(data) {
        console.log(data);
      }
    });
  });

});

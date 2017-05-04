

$(function(){

  $("#edit-att-tab").hide();

// ============AJAX Query to get the attendance data from backend===============
  $("#get-date").submit(function(event) {
    event.preventDefault();
    var date = $("#history").val();
    // console.log(date)
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var batch = $("#id_for_batch").val();
    var hour = $("#id_for_hour").val();
    // console.log(day, month, year);
    // console.log(batch);
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
        // console.log(data);
        $("#edit-att-tab").show();       //show the hidden table on request.
        $("#mytable tbody").empty();     //empty the element on each request.
        $(".alert").empty();             //empty the element on each request.
        var inputDate = new Date(date);  //create date instance.
        // console.log(inputDate);
        var today = new Date();          //create today's date instance.
        // console.log(today);

        if (inputDate.setHours(0,0,0,0) == today.setHours(0,0,0,0)) {   //check whether date is today or not.
          for (var i=0;i<data.results.length;i++) {

            if (data.results[i].is_present) {               //if the student is present in the requested data => check the checkbox.
              $("#mytable tbody").append('<tr><td><input type="hidden" id="id_is_present" name="' + data.results[i].student__pk + '" value="0">' +
                                      '<input type="checkbox" id="id_is_present" name="' + data.results[i].student__pk + '" value="1" checked></td>' +
                                      '<td>' + data.results[i].code + '</td>' +
                                      '<td>' + data.results[i].student__roll_no + '</td>' +
                                      '<td>' + data.results[i].student__first_name + ' ' + data.results[i].student__last_name + '</td></tr>'
                                      );
            }
            else {
              $("#mytable tbody").append('<tr><td><input type="hidden" id="is_present" name="' + data.results[i].student__pk + '" value="0">' +
                                      '<input type="checkbox" id="id_is_present" name="' + data.results[i].student__pk + '" value="1"></td>' +
                                      '<td>' + data.results[i].code + '</td>' +
                                      '<td>' + data.results[i].student__roll_no + '</td>' +
                                      '<td>' + data.results[i].student__first_name + ' ' + data.results[i].student__last_name + '</td></tr>'
                                      );
            }

          }
          $("#att_button").show()
        }
        else {
          $("#att_button").hide();
          for (var i=0;i<data.results.length;i++) {
            $("#mytable tbody").append('<tr><td>' + attendance(data.results[i].is_present) + '</td>' +
                                    '<td>' + data.results[i].code + '</td>' +
                                    '<td>' + data.results[i].student__roll_no + '</td>' +
                                    '<td>' + data.results[i].student__first_name + ' ' + data.results[i].student__last_name + '</td></tr>');
          }
        }

      },
      error: function(data) {
        console.log(data);
      }
    });
  });

  $("#edit-att-form").submit(function(event) {
    event.preventDefault();
    var attData = $(this).serializeArray();
    console.log(attData);
    attData = objectifyForm(attData, true);
    console.log(attData);
    var depData = $("#get-date").serializeArray();
    depData = objectifyForm(depData);
    // console.log(depData);
    var date = $("#history").val();
    // console.log(date)
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var postData = {
      month: month,
      day: day,
      year: year,
    }
    postData = Object.assign(postData, depData, attData);
    // console.log(postData);

    $.ajax({
      type: "POST",
      data: postData,
      success: function(data) {
        $successDiv = $('<div id="alert" class="alert text-center alert-info alert-dismissable">' +
                            "<strong>" + data.message + "</strong></div>");
        $(".alert").html($successDiv).fadeOut(10000);
      },
      error: function(data) {
        console.log(data);
      }
    });
  });

});

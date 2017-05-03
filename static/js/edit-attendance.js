

$(function(){

  $("#edit-att-tab").hide();

  $("#get-date").submit(function(event) {
    event.preventDefault();
    var date = $("#history").val();
    // console.log(date)
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var batch = $("#id_for_batch").val();
    var hour = $("#id_for_hour").val();
    // console.log(day, month, year);
    // console.log(batch);
    var history = {
      batch_id: batch,
      hour: hour,
      day: day,
      month: month,
      year: year
    }
    $.ajax({
      url: "/user/class/get-history/",
      type: "GET",
      data: history,
      success: function(data) {
        console.log(data);
        $("#edit-att-tab").show();
        var inputDate = new Date(date);
        console.log(inputDate);
        var today = new Date();
        console.log(today);

        if (inputDate.setHours(0,0,0,0) == today.setHours(0,0,0,0)) {
          for (var i=0;i<data.results.length;i++) {

            if (data.results[i].is_present) {
              $("#mytable tbody").append('<tr><td><input type="hidden" id="' + data.results[i].student__pk + '" name="" value="0">' +
                                      '<input type="checkbox" id="id_is_present" name="' + data.results[i].student__pk + '" value="1" checked></td>' +
                                      '<td>' + data.results[i].code + '</td>' +
                                      '<td>' + data.results[i].student__roll_no + '</td>' +
                                      '<td>' + data.results[i].student__first_name + ' ' + data.results[i].student__last_name + '</td></tr>'
                                      );
            }
            else {
              $("#mytable tbody").append('<tr><td><input type="hidden" id="' + data.results[i].student__pk + '" name="" value="0">' +
                                      '<input type="checkbox" id="id_is_present" name="' + data.results[i].student__pk + '" value="1"></td>' +
                                      '<td>' + data.results[i].code + '</td>' +
                                      '<td>' + data.results[i].student__roll_no + '</td>' +
                                      '<td>' + data.results[i].student__first_name + ' ' + data.results[i].student__last_name + '</td></tr>'
                                      );
            }

          }
          $("#edit-att-form").append('<button type="submit" class="btn btn-success" name="button">Edit now!</button>');
        }
        else {
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
    attData = objectifyForm(attData, true);
    console.log(attData);
    var depData = $("#get-date").serializeArray();
    depData = objectifyForm(depData);
    console.log(depData);
    var date = $("#history").val();
    // console.log(date)
    var data = date.split("/"), month = data[0], day = data[1], year = data[2];
    var postData = {
      month: month,
      day: day,
      year: year,
    }
    postData = Object.assign(postData, depData, attData);
    console.log(postData);

    $.ajax({
      type: "POST",
      data: postData,
      success: function(data) {
        console.log(data);
      },
      error: function(data) {
        console.log(data);
      }
    });
  });

});

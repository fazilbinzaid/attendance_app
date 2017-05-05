


/* Function for converting serializeArray output into an object.
 Also an argument to flag if attendance data is passed,
 if so, then convert the attendance data into a single object,
 then append into the actual object created. */
var objectifyForm = (function(){

  function objectifyForm(formArray, flag) {
    var hour = {};
    var returnArray = {};
    for (var i=0;i<formArray.length;i++) {

      if (!isNaN(formArray[i].name)) {
        hour[formArray[i].name] = formArray[i].value;
      }
      else {
        if (formArray[i].value) {
          returnArray[formArray[i].name] = formArray[i].value;
        }
      }
    }
    returnArray.attendance = JSON.stringify(hour);
    return returnArray;
  }

  return objectifyForm;

})();

// ================CSRF SCRIPT==================================================

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// ======================ATTENDANCE_PRESENT=====================================

var attendance = (function() {
  function attendance(event) {
    if(event) {
      return "PRESENT";
    }
    else {
      return "ABSENT";
    }
  }
  return attendance;
})();


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

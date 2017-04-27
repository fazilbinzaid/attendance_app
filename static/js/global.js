


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

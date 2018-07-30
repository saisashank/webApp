function validateForm ( form ) {
          
          requiredText = new Array( "name","email","username","password", "repassword", 
                                    "phone",,"birthday","birthyear"
                                     );
          
          requiredSelect = new Array(   "birthmonth" );
          requiredRadio  = new Array( "gender" );
          
          return checkForm(form) && requireValues ( form, requiredText   ) &&
                 requireSelects( form, requiredSelect ) &&
                 requireRadios ( form, requiredRadio  ) &&
                 checkProblems () ;
}
function checkForm(form)
  {
    if(form.username.value == "") {
    alert( "username cannot be empty");

      
      form.username.focus();
      return false;
    }
    re = /^\w+$/;
    if(!re.test(form.username.value)) {
     alert( "Error: Username must contain only letters, numbers and underscores!");
      form.username.focus();
      return false;
    }
    
    if(form.password.value != "" && form.password.value == form.repassword.value) {
      if(form.password.value.length < 6) {
        alert( "Error: Password must contain at least six characters!");
        form.password.focus();
        return false;
      }
      if(form.password.value == form.username.value) {
        alert( "Error: Password must be different from Username!");
        form.password.focus();
        return false;
      }
      re = /[0-9]/;
      if(!re.test(form.password.value)) {
        alert( "Error: password must contain at least one number (0-9)!");
        form.password.focus();
        return false;
      }
      re = /[a-z]/;
      if(!re.test(form.password.value)) {
        alert( "Error: password must contain at least one lowercase letter (a-z)!");
        form.password.focus();
        return false;
      }
      re = /[A-Z]/;
      if(!re.test(form.password.value)) {
        alert("Error: password must contain at least one uppercase letter (A-Z)!");
        form.password.focus();
        return false;
      }
    } else {
      alert( "Error: Please check that you've entered and confirmed your password!");
      form.password.focus();
      return false;
    }

   // alert( "You entered a valid password: " + form.password.value;
    return true;

  }
  
  
  // formLib.js
// Common functions used with forms
// 

// We use this as a hash to track those elements validated on a per element
// basis that have formatting problems
validate = new Object();


// Takes a value, checks if it's an integer, and returns true or false
function isInteger ( value ) {
    return ( value == parseInt( value ) );
}


// Takes a value and a range, checks if the value is in the range, and
// returns true or false
function inRange ( value, low, high ) {
    return ( !( value < low ) && value <= high );
}


// Checks values against formats such as '#####' or '###-##-####'
function checkFormat( value, format ) {
    var formatOkay = true;
    if ( value.length != format.length ) {
        return false;
    }
    for  ( var i = 0; i < format.length; i++ ) {
        if ( format.charAt(i) == '#' && ! isInteger( value.charAt(i) ) ) {
            return false;
        }
        else if ( format.charAt(i) != '#' &&
                  format.charAt(i) != value.charAt(i) ) {
            return false;
        }
    }
    return true;
}


// Takes a form and an array of element names; verifies that each has a value
function requireValues ( form, requiredValues ) {
    for ( var i = 0; i < requiredValues.length; i++ ) {
        element = requiredText[i];
        if ( form[element].value == "" ) {
            alert( "Please enter a value for " + element + "." );
            return false;
        }
    }
    return true;
}


// Takes a form and an array of element names; verifies that each has an
// option selected (other than the first; assumes that the first option in
// each select menu contains instructions)
function requireSelects ( form, requiredSelect ) {
    for ( var i = 0; i < requiredSelect.length; i++ ) {
        element = requiredSelect[i];
        if ( form[element].selectedIndex <= 0 ) {
            alert( "Please select a value for " + element + "." );
            return false;
        }
    }
    return true;
}


// Takes a form and an array of element names; verifies that each has a
// value checked
function requireRadios ( form, requiredRadio ) {
    for ( var i = 0; i < requiredRadio.length; i++ ) {
        element = requiredRadio[i];
        isChecked = false;
        for ( j = 0; j < form[element].length; j++ ) {
            if ( form[element][j].checked ) {
                isChecked = true;
            }
        }
        if ( ! isChecked ) {
            alert( "Please choose a " + form[element][0].name + "." );
            return false;
        }
    }
    return true;
}


// Verify there aren't any uncorrected formatting problems with elements
// validated on a per element basis
function checkProblems () {
    for ( element in validate ) {
        if ( ! validate[element] ) {
            alert( "Please correct the format of " + element + "." );
            return false;
        }
    }
    return true;
}


// Verifies that the value of the provided element has ##### format
function checkZip ( element ) {
    if ( ! checkFormat( element.value, "#####" ) ) {
        alert( "Please enter a five digit zip code." );
        element.focus();
        validate[element.name] = false;
    }
    else {
        validate[element.name] = true;
    }
    return validate[element.name];
}


// Verifies that the value of the provided element has ###-###-#### format
function checkPhone ( element ) { 
    if ( ! checkFormat( element.value, "###-###-####" ) ) {
        alert( "Please enter " + element.name + " in 800-555-1212 " +
               "format." );
        element.focus();
        validate[element.name] = false;
    }
    else {
        validate[element.name] = true;
    }
    return validate[element.name];
}

function checkEmail ( element ) {
  var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if (!filter.test(element.value)) {
  alert('Please provide a valid email address.');
  element.focus();
        validate[element.name] = false;
  }
  else {
        validate[element.name] = true;
  }
  return validate[element.name];
}

// Verifies that the value of the provided element has ###-##-#### format
function checkSSN ( element ) {
    if ( ! checkFormat( element.value, "###-##-####" ) ) {
        alert( "Please enter your Social Security Number in " +
               "123-45-6789 format." );
        element.focus();
        validate[element.name] = false;
    }
    else {
        validate[element.name] = true;
    }
    return validate[element.name];
}


// Verifies that the value of the provided element is an integer between 1 and 150
function checkAge ( element ) {
    if ( ! isInteger( element.value ) ||
         ! inRange( element.value, 1, 150 ) ) {
        alert( "Please enter a number between 1 and 150 for age." );
        element.focus();
        validate[element.name] = false;
    }
    else {
        validate[element.name] = true;
    }
    return validate[element.name];
}

$(document).ready(function(){
    // wanted to open the nav on the right of screen, answer found here https://stackoverflow.com/questions/37207668/how-do-i-open-a-materialize-sidenav-on-the-right-instead-of-the-left
    $('.sidenav').sidenav({
        edge:'right'
    });
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 1,
        showClearBtn: true,
        i18n: {
            done: "Select"
        },
        autoClose: true,
    });
  });
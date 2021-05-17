$(document).ready(function(){
        
    $("#save_recipe").click(function(){
        $(this).clone().appendTo("#saved_recipe");
    });
})
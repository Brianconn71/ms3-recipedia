// got help and guidance on creating dynamic forms which I altered to suit my needs here: https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
let ingred = 1;
let max_ingred = 20;

$(".add_ingredient").click(function(e){
    e.preventDefault();
    if(ingred < max_ingred){
        ingred ++;
        $(".ingred_list").append(`
        <div class="input-field col s12">
        <i class="fas fa-clipboard-list prefix shadow-text recipedia-text"></i>
        <input id="ingredients${ingred}" name="ingredients" minlength="2" maxlength="60" type="text" class="validate" required>
        <label for="ingredients${ingred}">Ingredient ${ingred}:</label>
        <a type="button" class="btn unsave-btn remove_ingredient"><i class="far fa-minus-square submit-icon"></i>Remove</a></div>`)
    }
})

// got the same help and guidance which i changed to suit my needs as above: https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery

let step = 1;
let max_steps = 10;

$(".add_step").click(function(e){
    e.preventDefault();
    if(step < max_steps){
        step ++;
        $(".step_list").append(`
        <div class="input-field col s12">
        <i class="fas fa-list-ol prefix shadow-text recipedia-text"></i>
        <input id="steps${step}" name="steps" minlength="3" maxlength="500" type="text" class="validate" required>
        <label for="steps${step}">Step ${step}:</label>
        <a type="button" class="btn unsave-btn remove_step"><i class="far fa-minus-square submit-icon"></i>Remove</a></div>`)
    }
})

// below are two functions which remove the last added step/ingredient filed on the form
// spent some time stuck on this but eventually got the guidance i needed here: https://www.bootstrapfriendly.com/blog/dynamically-add-or-remove-form-input-fields-using-jquery/
$("body").on('click', ".remove_ingredient",function(){
    $(this).parent('div').remove();
    ingred--;
})
// remove step
$("body").on('click', ".remove_step",function(){
    $(this).parent('div').remove();
    step--;
})
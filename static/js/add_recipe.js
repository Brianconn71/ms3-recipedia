// got help and guidance on creating dynamic forms which I altered to suit my needs here: https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
let ingred = 1;
let max_ingred = 10

$(".add_ingredient").click(function(e){
    e.preventDefault();
    if(ingred < max_ingred){
        ingred ++;
        $(".ingred_list").append(`
        <div class="input-field col s12">
        <i class="fas fa-clipboard-list prefix shadow-text recipedia-text"></i>
        <input id="ingredients${ingred}" name="ingredients" minlength="2" maxlength="60" type="text" class="validate" required>
        <label for="ingredients${ingred}">Ingredient ${ingred}:</label></div>`)
    }
})
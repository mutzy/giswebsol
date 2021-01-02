const user_input = $('#search');
const user_input_alt = $('#search_alt');
//const search_icon = $('#search-icon')
const artists_div_alt = $('#location_info_alt');
const artists_div = $('#location_info');
const endpoint = '/search/';
const delay_by_in_ms = 700;
let scheduled_function = false;
//$('.datepicker').datepicker();

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters).done(response => {
            // fade out the artists_div, then:
            artists_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                artists_div.html(response['html_from_view']);
                // fade-in the div with new contents
                artists_div.fadeTo('slow', 1);
                // stop animating search icon
                //search_icon.removeClass('blink')
            });
        });
}
let ajax_call_alt = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters).done(response => {
            // fade out the artists_div, then:
            artists_div_alt.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                artists_div_alt.html(response['html_from_view']);
                
                // fade-in the div with new contents
                artists_div_alt.fadeTo('slow', 1);
                // stop animating search icon
                //search_icon.removeClass('blink')
            });
        });
}


user_input.on('keyup', function () {
    
    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }

    if (Tmarker != undefined) {
        mymap.removeLayer(Tmarker);
    }
    
    // start animating the search icon with the CSS class
    //search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function);
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters);
});

user_input_alt.on('keyup', function () {
    
    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }
   
    // start animating the search icon with the CSS class
    //search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function);
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call_alt, delay_by_in_ms, endpoint, request_parameters);
});
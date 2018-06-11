/*
 * Miscellaneous scripts.
 */

/*
 * Configures the CSRF request header
 * Original snippet by Django from https://docs.djangoproject.com/en/1.9/ref/csrf/#ajax
 */
function csrfSafeMethod(method: string) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(parseString(settings.type && !this.crossDomain))) {
            xhr.setRequestHeader("X-CSRFToken", parseString(Cookies.get("csrftoken")));
        }
    }
});

/*
 * Reads the Get Vars in the url
 * Original snippet created by https://css-tricks.com/snippets/javascript/get-url-variables/
 * `$_GET("var")` returns "abc" from `example.com/php.aspx?var=abc`.
 * `$_GET("var", false)` returns false if var cannot be found.
 */
function $_GET(variable: string, notFound?: any): string | any {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if(pair[0] == variable) {
			return pair[1];
		}
    }
    return notFound;
}

/*
 * Converts any type to string.
 * Avoids the "Object is possibly undefined/null/etc..." error.
 */
function parseString(object: any): string {
    switch (typeof(object)) {
        case "string":
            return object;

        case "number":
        case "boolean":
            return object.toString();

        case "undefined":
            try {
                return object.toString();
            } catch (TypeError) {
                return "";
            }

        default:
            return "";
    }
}

/*
 * Clears all form text inputs in a specified selector.
 */
function clearFormInputs(selector: string) {

    // The input types to clear
    var textInputTypes = [
        "text",
        "number",
        "url",
        "email",
        "password",
        "tel",
    ];

    // Clear the text inputs
    textInputTypes.forEach(function (type) {
        $(selector + " input[type=\""+ type +"\"]").val("");
    });

    // Clears the textarea
    $(selector + " textarea").val("");
}
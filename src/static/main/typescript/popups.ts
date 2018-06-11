/*
 * Toggles a popup.
 * 
 * @param {string} selector - The jQuery selector of the popup.
 * 
 */
function popupToggle(selector: string) {
    $(selector).fadeToggle(75);
}

/*
 * Deletes a popup.
 * 
 * @param {string} selector - The jQuery selector of the popup.
 * 
 */
function popupDelete(selector: string) {
    $(selector).remove();
}

// Hides all popups.
function popupHideAll() {
    $(".popup").hide();
}

/*
 * Displays a new popup message.
 * 
 * @param {string} content - The popup message content.
 * 
 * NOTE: Be sure to sanitize untrusted data to prevent XSS.
 * 
 */
function popupWrite(content: string) {
    var popupID = "popup-generic-" + (Math.floor(Math.random() * (0 - 10000)) + 10000).toString();

    var popupHTML = `
    <div id="`+ popupID +`" class="popup popup-generic">
        <div class="popup-content">
            <span class="popup-close"><a href="javascript:void(0)"><i class="fa fa-times" onclick="popupDelete('#`+ popupID +`')"></i></a></span>
            `+ content +`
        </div>
    </div>
    `;

    $("body").append(popupHTML);
    popupToggle("#" + popupID);

}
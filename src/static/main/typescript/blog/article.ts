// If true, the current page is the article edit page.
// If false, the current page is the article creation page.
var articleEdit: boolean = Boolean($("meta[name=\"article-edit\"]").attr("content"));

// Initialize a clipboard for the article file URLs.
var clipboard = new Clipboard('.btn-article-file-url');

/*
 * Create an article.
 *
 * @param {string} selector - The jQuery selector of the element from which to obtain the URL.
 *
 * Add a 'data-submit-url' attribute to the element corresponding to the 'selector' argument
 * containing the URL of the article creation API, and a 'data-redirect-url' containing an
 * example article edit page URL with an ID of 0.
 *
 */
function articleCreate(selector: string) {
    $("#article-edit-submit-message").html('Submitting...');

    var submit = $.ajax({
        type: "POST",
        url: $(selector).attr("data-submit-url"),
        data: {
            "html": true,
            "markdown": true,
        },
    })

    submit.done(function(r) {
        if (r.submitted) {
            $("#article-submit-message").html('<span class="submitted">Submitted.</span>');

            var redirect = $(selector).attr("data-redirect-url").replace("0", r.data.id);
            if ($("meta[name='no-redirect']").attr("content") != "True") {
                window.location.replace(redirect);
            }

        } else {
            $("#article-submit-message").html('<span class="error">An error occured when submitting. See the console for details.</span>');
            console.log('Article creation error:\n', r);
        }
    });

    submit.fail(function(response) {
        $("#article-submit-message").html('<span class="error">An error occured when submitting: ' + response.status + '</span>');
    });
}

/*
 * Form submission function for the article edit form.
 */
function articleEditSubmit() {
    $("#article-edit-submit-message").html('Submitting...');

    var submit = $.ajax({
        type: "POST",
        url: $("#article-edit-submit").attr("action"),
        data: $("#article-edit-submit").serialize()
    })

    submit.done(function(r) {

        if (r.submitted) {
            $("#article-edit-submit-message").html('<span class="submitted" >Submitted.</span>');

            setTimeout(function () {
                $("#article-edit-submit-message .submitted").fadeOut();
            }, 3000);

        } else {
            if (r.error.code == "form_invalid") {
                $("#article-edit-submit-message").html("<span>Submitted.</span>");
                $("#article-edit-submit-message .inputs").html(r.form);
            } else {
                $("#article-edit-submit-message").html('<span class="error">An error occured when submitting. See the console for details.</span>');
                console.log('Article '+ articleEdit ? 'edit':'creation' +' error:\n', r);
            }
        }
    });

    submit.fail(function(response) {
        $("#article-edit-submit-message").html('<span class="error">An error occured when submitting: ' + response.status + '</span>');
    });
}

/*
 * Render an article file thumbnail.
 */
function renderFileThumbnail(data: any) {
    var image: string;

    // Display a placeholder if the file is not an image
    if (data.file.image) {
        image = `<img class="media-object" src="`+ data.file.url +`" alt="Image Thumbnail" />`;
    } else {
        image = `<img class="media-object" src="/static/img/blog/article-file-placeholder.png" alt="Image Thumbnail Placeholder" />`;
    }

    var fileThumbnail: string = `
        <div class="media article-file-item" id="article-file-item-`+ data.id +`">
            <div class="input-group article-file-url">
                <input type="text" class="form-control" value="`+ data.file.name +`" readonly />
                <span class="input-group-btn">
                    <button class="btn btn-default btn-article-file-url" type="button" data-clipboard-text="`+ data.file.url +`" title="Copy URL">
                        <i class="fa fa-clipboard" aria-hidden="true"></i>
                    </button>
                </span>
            </div>
            <div class="media-left">`+ image +`</div>
            <div class="media-body">
                <div id="article-file-options-`+ data.id +`">
                    <button class="btn btn-danger btn-article-file-delete" onclick="articleFileDelete('`+ data.id +`', '`+ data.file.url +`')">
                        <i class="fa fa-trash-o" aria-hidden="true"></i>
                    </button>
                    <a class="btn btn-primary btn-article-file-edit" href="/admin/article/articlefile/`+ data.id +`/change/" target="_blank">
                        <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
                    </a>
                </div>
            </div>
        </div>
    `;
    $("#article-file-list").prepend(fileThumbnail);
    $("#article-file-empty").remove()
}

/*
 * Dropzone for article image uploading.
 */
Dropzone.options.articleFileSubmit = {
    paramName: "associated_file",
    maxFilesize: 1000,
    parallelUploads: 10,
    headers: {
        "X-CSRFToken": Cookies.get("csrftoken"),
    },
    init: function () {
        this.on("success", function(file: any, r: any) {
            this.removeFile(file);
            if (r.submitted) {
                $("#article-file-upload-message").html("");
                renderFileThumbnail(r.data);
            } else {
                $("#article-file-upload-message").html('<span class="error">An error occured when submitting. See the console for details.</span>');
                console.log('Article file upload error:\n', r);
            }
        });
    },
}

/*
 * Delete an associated article file.
 */
function articleFileDelete(id: string, path: string) {
    var deleteConfirm: string = `
        <div id="article-file-delete-`+ id +`" class="article-file-delete">
            <button class="btn btn-danger" onclick="articleFileDeleteConfirm('`+ id +`', '`+ path +`')">Yes</button>
            <button class="btn btn-success" onclick="articleFileDeleteCancel('`+ id +`')">No</button>
        </div>
    `;
    $("#article-file-options-"+ id).append(deleteConfirm);
    $("#article-file-options-"+ id +" .btn-article-file-delete").prop("disabled", true);
}
function articleFileDeleteConfirm(id: string, path: string) {
    $("#article-file-delete-"+ id).html("<span>Deleting...</span>");

    var submit = $.ajax({
        type: "POST",
        url: "/api/articles/file/delete/",
        data: {id: id, path: path}
    })
    submit.done(function(r) {

        if (r.submitted) {
            $('#article-file-item-'+ id).remove();
        } else {
            $("#article-file-delete-"+ id).html('<span class="error">An error occured when deleting. See the console for details.</span>');
            console.log('Article file deletion error:\n', r);
            $("#article-file-options-"+ id +" .btn-article-file-delete").prop("disabled", false);
        }
    });
    submit.fail(function(response) {
        $("#article-file-delete-"+ id).html('<span class="error">An error occured when deleting: ' + response.status + '</span>');
        $("#article-file-options-"+ id +" .btn-article-file-delete").prop("disabled", false);
    });
}
function articleFileDeleteCancel(id: string) {
    $("#article-file-delete-"+ id).remove()
    $("#article-file-options-"+ id +" .btn-article-file-delete").prop("disabled", false);
}

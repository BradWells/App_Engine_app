/**
 * Created by Brad on 11/5/2014.
 */

/** Source: http://stackoverflow.com/questions/18480550/how-to-load-all-the-images-from-one-of-my-folder-into-my-web-page-using-jquery **/

function loadImages() {
    var dir = "src/static/icons/";
    var fileextension = [".png", ".jpg"];

    $.ajax({
        //This will retrieve the contents of the folder if the folder is configured as 'browseable'
        url: dir,
        success: function (data) {
            //List all png file names in the page
            $(data).find("a:contains(" + (fileextension[0]) + "), a:contains(" + (fileextension[1]) + ")").each(function () {
                var filename = this.href.replace(window.location.host, "").replace("http:///", "");
                $(".photoset-grid-basic").append($("<img src=" + dir + filename + "></img>"));
            });
        }
    });
}
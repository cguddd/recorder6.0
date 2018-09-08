// Required for Django CSRF
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
 
// Actual Upload function using xhr
function uploadAudioFromBlob(blob) {
    var csrftoken = getCookie('csrftoken');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'upload_server', true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.setRequestHeader("MyCustomHeader", "Put anything you need in here, like an ID");

    /* 提示可以關掉
    xhr.upload.onloadend = function () {
        alert('上傳成功');
    };
    */
    xhr.send(blob);
}

function uploadword(word) {
    var csrftoken = getCookie('csrftoken');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'upload_word', true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.setRequestHeader("MyCustomHeader", "Put anything you need in here, like an ID");

    /* 提示可以關掉
    xhr.upload.onloadend = function () {
        alert('上傳成功');
    };
    */
    let fd = new FormData;
    fd.append('thisword',word);
    xhr.send(fd);
}


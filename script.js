$(document).ready(function () {

    $.get({
        url: 'corpusMetadata.py'
    })
    .done(function (data) {
        console.log(data)
    })

});
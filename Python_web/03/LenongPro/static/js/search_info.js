$(function () {

    $('.input_btn').click(function () {


        var a = $('.input_text').val();
        // alert(a);
        // console.log(a)
        // $('title').html(a)
        var keywords = {
            'keyword': a
        };
        $.get('/lenong/search/', keywords, function (data) {

        })


    })


});
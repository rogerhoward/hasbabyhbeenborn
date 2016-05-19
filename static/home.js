$(document).ready(function() {
    homePage = $("#fullpage");

    homePage.onepage_scroll({        
    });


    $("#question").hover(function() {
        $(this).css('cursor','pointer');
    }).click(function() {
        homePage.moveDown();
    });



});



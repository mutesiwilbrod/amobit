$(document).ready(function(){
    $('#login-modal').hide();
    $("#login").click(function(){
        $('#login-modal').show(
            console.log('>>>>mmm')
        );

    });
  
});
$(document).ready(function(){
    
    $('#close_login_model').click(function(){
        $('#login_model').hide();
    })
})
$(document).ready(function(){
    $('div#search').hide();
    $('#search-button').click(function(){
        console.log('>>>>>>>>>>>>>>>>>>>>')
        $('div#search').show({})

    })
})

$(document).ready(function(){
    
    $('#start-search').click(function(){
        $('#search').hide();
    });
});


$('#main-slider').owlCarousel({
    items:1,
    nav:false,
    dots: true,
    autoplay: true,
    autoplayHoverPause: true,
    dotsSpeed: 400,
});

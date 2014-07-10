$(document).ready(function() {


$('.customjumbo').hide();
$('.categories').hide();

/* Reveal Marauder Map password: 
 * http://stackoverflow.com/questions/4607613/jquery-text-effect-where-words-appear-one-by-one */
var str = "I solemnly swear that I am up to no good.";
var spans = '<span>' + str.split(/\s+/).join(' </span><span>') + '</span>';
$(spans).hide().appendTo('#swear').each(function(i) {
    $(this).delay(600 * i).fadeIn();
});


$('#swear').click(function() {
    $('.customjumbo').show();
    $('.categories').show();
    $('#swear').hide();
});



});

/* set glowing/pulsating 
setTimeout((function() {
    var p = $("#swear");
    for (var i=0; i<3; i++) {
        p.animate({opacity: 0.2}, 1000, 'linear')
         .animate({opacity: 1}, 1000, 'linear');
    }
  }), 6000);

*/







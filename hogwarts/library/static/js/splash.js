$(document).ready(function() {

//    $('#swear').fadeIn('10000').removeClass('hidden');
//});
//$("#swear").hide().delay(3);

//var words = p.text();
//var spans = '<span>' + str.split(/\s+/).join(' </span><span>') + '</span>';
//$(spans).hide().appendTo('body').each(function(i) {
//    $(this).delay(1000*i).fadeIn();
//});

/* this code snippet from: STACK OVERFLOW */
//var p = $("#swear").hide();
var str = "I solemnly swear that I am up to no good.";
var spans = '<span>' + str.split(/\s+/).join(' </span><span>') + '</span>';

$(spans).hide().appendTo('#swear').each(function(i) {
    $(this).delay(500 * i).fadeIn();
});





setTimeout((function() {
    var p = $("#swear");
    for (var i=0; i<3; i++) {
        p.animate({opacity: 0.2}, 1000, 'linear')
         .animate({opacity: 1}, 1000, 'linear');
    }
  }), 10000);


});



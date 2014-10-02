$(document).ready(function() {
    var revealed = false;

	$('#search-submit').click(function(e) {
		e.preventDefault();
		search_terms = $('#id_q').val();
		location.href = '/search/?q=' + search_terms;
	});

	$('#id_q').keypress(function (e) {
        	if (e.keyCode == 13 || e.which == 13) {
            	e.preventDefault();
            	search_terms = $('#id_q').val();
            	location.href = '/search/?q=' + search_terms;
        }
    });

    var showNav = function() {
    	$('#mischief-message').fadeTo(2000, 0, function() {
   			$('#mischief-message').hide();
			$('#wrap').fadeIn(2000);
   			$('#myfooter').fadeTo(2000, 1, 0);
   		});
    }

    $('#mischief-message').click(function(e){
   		e.preventDefault();
   		revealed = true;
   		showNav();
   	});

   	$('span#m1').fadeTo(2000, 1, 0);
   	$('span#m2').delay(500).fadeTo(2000, 1, 0);
   	$('span#m3').delay(1000).fadeTo(2000, 1, 0);
   	$('span#m4').delay(500).fadeTo(2000, 1, 0);
   	$('span#m5').delay(1200).fadeTo(2000, 1, 0);
   	$('span#m6').delay(800).fadeTo(2000, 1, 0);
   	$('span#m7').delay(1000).fadeTo(2000, 1, 0);
   	$('span#m8').delay(500).fadeTo(2000, 1, 0);
   	$('span#m9').delay(300).fadeTo(2000, 1, 0);
   	$('span#m10').delay(500).fadeTo(2000, 1, 0);
   	$('span#m10').delay(500).fadeTo(2000, 1, 0);
   	$('span#m11').delay(1300).fadeTo(2000, 1, 0);
   	$('span#m12').delay(800).fadeTo(2000, 1, 0);
   	$('span#m13').delay(500).fadeTo(2000, 1, 0);
   	$('span#m14').delay(1200).fadeTo(2000, 1, 0);
   	$('span#m15').delay(800).fadeTo(2000, 1, 0);
   	$('span#m16').delay(1000).fadeTo(2000, 1, 0);
   	$('span#m17').delay(500).fadeTo(2000, 1, 0);
   	$('span#m18').delay(300).fadeTo(2000, 1, 0);
   	$('span#m19').delay(500).fadeTo(2000, 1, 0);
   	$('span#m20').delay(1600).fadeTo(2000, 1, function() {
   		var $message = $('#mischief-message');
   		$message.css({'-webkit-animation': 'pulsate 1.5s ease-out', '-webkit-animation-iteration-count': 'infinite'});
   		setTimeout(function() {
   			if(!revealed)
   				showNav();
   		}, 5000);
   	});
});


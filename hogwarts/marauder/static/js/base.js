$(document).ready(function() {
	$('#search-submit').click(function(e) {
		e.preventDefault();
		search_terms = $('#id_q').val();
	    location.href = '/search/?q=' + search_terms;
	});
});
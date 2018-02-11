$(document).ready(function() {
    if ($('.post-wrapper').length) {
        $(".collapse-form").show();
    }
    if ($('.error-container').length) {
        $(".collapse-form").hide();
    } else {
        $(".collapse-form").show();
    }

    $("#add").click(function() {
		$(".error-container").hide();
		$(".button-wrapper").hide();
        $(".collapse-form").show();
	});

	$("#delete").click(function() {
	 if ($('.post-wrapper').length == 0 ) {
        $(".collapse-form").show()
     }
		$(".button-wrapper").show();
		$('.error-container').show();

     if ($('.error-container').length) {
        $(".collapse-form").hide();
     } else {
        $(".collapse-form").show();
     }

	});
});
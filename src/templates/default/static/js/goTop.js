$(function () {

	$(".top").click(
		function () {
			$('html,body').animate({ scrollTop: 0 }, 700);
	});
	
	$(".bottom").click(
		function () {
            $('html,body').animate({ scrollTop: document.body.clientHeight }, 700);
	});
	
})

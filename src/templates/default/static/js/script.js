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

$(document).ready(function() {

	var currentPage = 0;
	var articleNumEachPage = 5;

	$("#blog_index article:gt(" + (articleNumEachPage - 1) + ")").hide();
	$("#prev_page").hide();

	var articleNum = $("#blog_index article").length;
	if(articleNum >= articleNumEachPage) {
		$("#pager_bar").show();
	}

	$("#next_page").click(function() {
		$("#blog_index article").hide();

		currentPage = currentPage + 1;
		var startIndex = currentPage * articleNumEachPage;
		var endIndex = (currentPage + 1) * articleNumEachPage - 1;
		endIndex = endIndex > articleNum ? articleNum : endIndex;
		$.each($("#blog_index article"), function(index, item) {
			if(index >= startIndex && index <= endIndex) {
				$(this).show();
			}
		});

		if(endIndex + 1 >= articleNum) {
			$("#next_page").hide();
		}
		if(currentPage > 0) {
			$("#prev_page").show();
		}
	});

	$("#prev_page").click(function() {
		$("#next_page").show();
		$("#blog_index article").hide();

		currentPage = currentPage - 1;
		var startIndex = currentPage * articleNumEachPage;
		var endIndex = (currentPage + 1) * articleNumEachPage - 1;
		endIndex = endIndex > articleNum ? articleNum : endIndex;
		$.each($("#blog_index article"), function(index, item) {
			if(index >= startIndex && index <= endIndex) {
				$(this).show();
			}
		});

		if(currentPage == 0) {
			$("#prev_page").hide();
			return;
		}
	});

})

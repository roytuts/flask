$(function () {
    $(".star").on("mouseover", function () { //SELECTING A STAR
        $(".rating").hide(); //HIDES THE CURRENT RATING WHEN MOUSE IS OVER A STAR
        var d = $(this).attr("id"); //GETS THE NUMBER OF THE STAR

        //HIGHLIGHTS EVERY STAR BEHIND IT
        for (i = (d - 1); i >= 0; i--) {
            $(".transparent .star:eq(" + i + ")").css({"opacity": "1.0"});
        }
    }).on("click", function () { //RATING PROCESS
        var blog_id = $("#blog_content_id").val(); //GETS THE ID OF THE CONTENT
        var rate = $(this).attr("id"); //GETS THE NUMBER OF THE STAR

        $.ajax({
            method: "POST",
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({'blog_id': blog_id, 'rate': rate}),
            url: "/rate", //CALLBACK
            success: function (e) {
				var stars = '';
				
				for(var i=1;i<=e.vote_rate;i++){
					stars += '<div class="star" id="' + i + '"></div>';
				}
				
				var str = '<div class="r"><div class="rating">' + stars + '</div><div class="transparent"><div class="star" id="1"></div><div class="star" id="2"></div><div class="star" id="3"></div><div class="star" id="4"></div><div class="star" id="5"></div><div class="votes">(' + e.vote_dec_rate + '/5, ' + e.vote_rows + ' ' + (e.vote_rows > 1 ? ' votes' : ' vote') + ') ' + (e.vote_curr_rate > 0 ? '<strong>You rated this: <span style="color:#39C;">' + e.vote_curr_rate + '</span></strong>' : '') + '</div></div></div>'
				
                $("#ajax_vote").html(str); //DISPLAYS THE NEW RATING IN HTML
            },
            error: function (e) {
                console.log(e);
            }
        });
    }).on("mouseout", function () { //WHEN MOUSE IS NOT OVER THE RATING
        $(".rating").show(); //SHOWS THE CURRENT RATING
        $(".transparent .star").css({"opacity": "0.25"}); //TRANSPARENTS THE BASE
    });
});
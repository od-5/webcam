$(document).ready(function(){	

	// fancybox
	$('.fancybox').fancybox();
	$('.js-popup-form__button').fancybox();
	$('.work-popup').fancybox({
		'width' : $(window).width() - 80,
		'height' : $(window).height() - 80,
		'autoScale' : true,
		type: 'iframe'
	});
	$('form').each(function(){
		$(this).validate({
			   rules: {
				phone: {
					required: true,
					minlength: 6
				},
				name: {
					required: true
				},
				mail: {
					email: true
				}
			}
	    });
	});	
	
	// slider
	$('.demo-slider .owl-carousel').owlCarousel({
		loop: true,
		items: 1,
		nav: true,
		dots: false,
		//autoHeight : true,
		navText: [''],
		autoplay: false	
	});
	
	$(window).scroll( function(){
		if ($(this).scrollTop() > 100){
			$('.fixed-top').addClass('fixed');	
		}else{
			$('.fixed-top').removeClass('fixed');
		}
		
	});
	// scroll
	$('.fixed-nav-list a').click(function(e){
		e.preventDefault();
		var selected = $(this).attr('href').replace('/', '');
		$.scrollTo(selected, 1000, {offset: -50});
		$('.fixed-nav').removeClass('active');
		$('.fixed-bg').removeClass('active');
		return false;
	});
	
	
	// nav
	$(document).on('click','.nav-icon',function(e){
		e.preventDefault();
		$('.fixed-nav').addClass('active');
		$('.fixed-bg').addClass('active');
	});
	$(document).on('click','.nav-close',function(e){
		e.preventDefault();
		$('.fixed-nav').removeClass('active');
		$('.fixed-bg').removeClass('active');
	});
	
	//popup
	$('.modal').click(function(e) {
		e.preventDefault();
		
		$('#mask, .window').hide();
		var id = $(this).attr('href');
		var maskHeight = $(document).height();
		var maskWidth = $(window).width();
		$('#mask').css({'height':maskHeight});
		$('#mask').fadeTo("slow",1);
		var winH = $(window).height();
		var winW = $(window).width();
		$(id).css('top',  winH/2-$(id).height()/2);
		$(id).css('left', winW/2-$(id).width()/2);
		$(id).fadeIn(1000);	
	});
	$('.window .close').click(function (e) {
		e.preventDefault();
		$('#mask, .window').hide();
	});
	$('#mask').click(function () {
		$(this).hide();
		$('.window').hide();
	});
	//popup
	
});	

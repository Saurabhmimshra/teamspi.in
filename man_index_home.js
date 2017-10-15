// scroll reveal control
	window.sr = ScrollReveal();
	sr.reveal(".main-image", {duration : 2000, origin : 'right', distance : '200px'});
	sr.reveal(".odd", {duration : 1500, origin : 'left', distance : '500px'});
	sr.reveal(".main-heading", {duration : 2000, origin : 'left', distance : '200px'});
	sr.reveal(".even", {duration : 1500, origin : 'right', distance: '500px'});
	sr.reveal(".activities", {duration : 1500, origin : 'bottom', distance : '500px'});
	sr.reveal(".contact-spi", {duration : 1500, origin : 'bottom', distance : '200px'});
	sr.reveal(".project-for-scrvl", {duration : 1500, origin : 'bottom', distance : '100px'});


// smooth scroll api

var scroll = new SmoothScroll('a[href*="#"]', {
	// Selectors
	ignore: ['#myCarousel', '#teamact'], // Selector for links to ignore (must be a valid CSS selector)
	header: ['.navbar'],  // Selector for fixed headers (must be a valid CSS selector)

	// Speed & Easing
	speed: 800, // Integer. How fast to complete the scroll in milliseconds
	offset: 0, // Integer or Function returning an integer. How far to offset the scrolling anchor location in pixels
	easing: 'easeInOutCubic', // Easing pattern to use
	customEasing: function (time) {}, // Function. Custom easing pattern

	// Callback API
	before: function () {}, // Callback to run before scroll
	after: function () {} // Callback to run after scroll
});


// scroll back 

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("myBtn").style.display = "block";
        // sr.reveal("#top", {duration : 1000});
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	var anchor = document.querySelector( '#top' );
	scroll.animateScroll( anchor );
}
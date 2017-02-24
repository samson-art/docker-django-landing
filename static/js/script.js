/**
 * Created by artemsamsonov on 21.02.17.
 */

$(document).ready(function () {

    $('a.smooth-scroll').on('click', function (event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $('#'+$anchor.attr('href').split('#')[1]).offset().top-70
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });


    $('#map').addClass('scrolloff'); // set the pointer events to none on doc ready
    $('.map-container').on('click', function () {
        $('#map').removeClass('scrolloff'); // set the pointer events true on click
    });
    // you want to disable pointer events when the mouse leave the canvas area;
    $(".map-container").mouseleave(function () {
        $('#map').addClass('scrolloff'); // set the pointer events to none when mouse leaves the map area
    });

    $('.slider-wrap').each(function () {
        $(this).owlCarousel({
            items: 1,
            nav: false,
            dots: false,
            rewind: true,
            autoplay: true,
            autoplayTimeout: 3500,
            autoplayHoverPause: true,
            animateIn: 'bounceInRight',
            animateOut: 'bounceOutLeft',

        })
    });
    $('#decoration ul.nav').find('li a[data-first=True]').first().tab('show');
    lightbox.option({
        'disableScrolling': true,
        'wrapAround': true,
    });

    $('.history-slider').owlCarousel({
        nav: true,
        autoplay: true,
        autoplayTimeout: 3500,
        autoplayHoverPause: true,
        animateIn: 'slideInRight',
        animateOut: 'slideOutLeft',
        // stagePadding: 15,
        rewind: true,
        items: 3,
        navText: [
            '<',
            '>'
        ],
    });
    $('#trusts-slider').owlCarousel({
        autoplay: true,
        autoplayTimeout: 3500,
        autoplayHoverPause: false,
        animateIn: 'slideInRight',
        animateOut: 'slideOutLeft',
        rewind: true,
        items: 3,
    });

    $('.dropdown-toggle').dropdown();
});
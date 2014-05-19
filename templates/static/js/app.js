// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs

var document_top = 0;
$(document).foundation({
    reveal: {
        opened: function() {
            document_top = $('.modal.open').offset().top;
        },
        closed: function() {
            $('body').css("overflow", "auto");
            $('html, body').animate({
                scrollTop: document_top
            }, 300)
        },
    }
});

// hover styles for modal header
$('.modal > h2 a').hover(
    function() {
        $(this).parent().toggleClass('modal-h2-hover');
    },
    function() {
        $(this).parent().toggleClass('modal-h2-hover');
    }
);

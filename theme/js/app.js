// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

// hover styles for modal header
$('.modal > h2 a').hover(
    function() {
        $(this).parent().toggleClass('modal-h2-hover');
    },
    function() {
        $(this).parent().toggleClass('modal-h2-hover');
    }
);

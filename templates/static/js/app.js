// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation({
    reveal: {
        open: function() {
            //$('body').css("overflow", "hidden")
        },
        close: function() {
            //$('body').css("overflow", "auto")
        },
        css : {
            open : {
              'opacity': 0,
              'visibility': 'visible',
              'display' : 'block',
              'overflow-y': 'auto',
              'max-height': '95%'
            },
            close : {
              'opacity': 1,
              'visibility': 'hidden',
              'display': 'none',
              'overflow-y': 'inherit'
            }
        }
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

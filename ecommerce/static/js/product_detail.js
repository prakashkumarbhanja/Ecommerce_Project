$(document).ready(function(){
$('.addtocart').on({
        mouseenter: function(){
            $(this).css("background-color", "#48CCCD");
        },

        mouseleave: function(){
            $(this).css("background-color", "#007bff");
        }
});

$(".wishlist").on({
        mouseenter: function(){
        $(this).css("background-color", "#7F38EC");
        $(this).css("color", "white");
        },

        mouseleave: function(){
            $(this).css("background-color", "#dc3545");
        }
})
});
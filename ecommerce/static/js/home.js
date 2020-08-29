$(document).ready(function(){
$('.addtocart').on({
        mouseenter: function(){
            $(this).css("background-color", "#48CCCD");
        },

        mouseleave: function(){
            $(this).css("background-color", "#007bff");
        }
});

$(".view").on({
        mouseenter: function(){
        $(this).css("background-color", "#7F38EC");
        $(this).css("color", "white");
        },

        mouseleave: function(){
            $(this).css("background-color", "#ffc107");
        }
});
//$('.addtocart').on('click', function(){
//    product_id = document.getElementById("demo");
//});

});
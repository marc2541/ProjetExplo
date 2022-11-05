// JS file qui contient des fonctions custom, impliquant aussi du AJAX

// Supprimer un livre sur le clic du bouton
$(document).on("click", ".delete", function(){
    
    var result = confirm("Êtes-vous certain de vouloir supprimer ce livre sacré?");

    if(result){
        var id = $(this).attr("id");

        $(this).closest("div").remove();

        $.post("/ajax_delete_book", { string: id}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
    }
});

/* Menu de nav pour la version mobile */
function menuNavMobile() {
    document.getElementById("nav-mobile").classList.toggle("hidden");
}
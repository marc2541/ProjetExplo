// JS file qui contient des fonctions custom, impliquant aussi du AJAX

// Supprimer un livre sur le clic du bouton
$(document).on("click", ".delete", function(){
    
    var result = confirm("Êtes-vous certain de vouloir supprimer ce livre sacré?");

    if(result){
        var id = $(this).attr("id");

        $.post("/ajax_delete_book", { string: id}, function(data) {
            
            $('#' + id).remove();

            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
    }
});

// Supprimer un livre sur le clic du bouton
$(document).on("click", ".submit", function(){
    // Déclaration des variables
    let error = false;
    let errorMSG = "";
    var titre, auteur, pages, comment;

    // Set des variables
    titre = document.getElementById("title").value;
    auteur = document.getElementById("author").value;
    pages = document.getElementById("pages_num").value;
    comment = document.getElementById("review").value;

    // Réinitialise le message d'erreur
    $("#displaymessage").html("");

    if (titre == "") {
        errorMSG += "Veuillez entrer un titre<br>";
        error = true;
    };
    if (auteur == "") {
        errorMSG += "Veuillez entrer un auteur<br>";
        error = true;
    };
    if (pages <= 0) {
        errorMSG += "Veuillez entrer un chiffre plus grand que zéro<br>";
        error = true;
    };
    if (comment == "") {
        errorMSG += "Veuillez entrer un commentaire<br>";
        error = true;
    };


    if(error){
        $("#displaymessage").html(errorMSG);
        $("#displaymessage").show();

        return false;
    }
    return true;
});




/* Menu de nav pour la version mobile */
function menuNavMobile() {
    document.getElementById("nav-mobile").classList.toggle("hidden");
}
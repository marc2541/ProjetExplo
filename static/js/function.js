// JS file qui contient du AJAX

// Ajoute des écouteurs sur les boutons portant la class delete
/*let deleteButton = document.getElementsByClassName('delete');
for (i = 0; i < deleteButton.length; i++) {
    deleteButton[i].addEventListener('click', confirmeDeletion);
}*/

// Demande à l'utilisateur de confirmer avant de supprimer un livre
/*function confirmeDeletion(e){

    var result = confirm("Êtes-vous certain de vouloir supprimer ce livre sacré?");

    if(result){

        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {

                // delete du div qui contient le livre
                e.target.parentNode.remove();
            }
        };
        
        xhttp.open("POST", "index.php", true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.send("action=deleteProduct&idProduct=" + idProduct);

        
    }
}*/

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
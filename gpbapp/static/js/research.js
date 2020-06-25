/*
* JavaScript - Project 7
* Date: 2018-03-07
*/

function createMessage(userType, message){

    var messageDiv = document.createElement("div");
    var messageContent = document.createTextNode(message);

    if (userType === "user"){
        messageDiv.className = "message user_request";
    }
    else if (userType === "grandpy"){
        messageDiv.className = "message grandpy_response"
    }

    messageDiv.appendChild(messageContent);
    document.getElementById("chat").appendChild(messageDiv);
}

function refreshLeafletMap(lat, lon, zoom){

    // Set map view
    maCarte.setView([lat, lon], zoom);
    // Set map marker
    marker.setLatLng([lat, lon]);
}

function dispatch(serverResponse){

    if (serverResponse["keyword"]["status"] === "EMPTY"){
        createMessage("grandpy", "Tu ne m'as rien envoyé petit coquin !")
    } else if (serverResponse["keyword"]["status"] === "NO SENTENCE"){
        createMessage("grandpy", "Sais-tu écrire une question ?")
    } else if (serverResponse["keyword"]["status"] === "FOUND"){

        if (serverResponse["address"]["status"] === "FOUND"){
            refreshLeafletMap(serverResponse["address"]["lat"], serverResponse["address"]["lon"], 20);
            createMessage("grandpy", "Voici l'adresse ! " + serverResponse["address"]["display_name"]);

            if (serverResponse["address_story"]["status"] === "FOUND"){
                createMessage("grandpy", "Mais t'ai-je déjà raconter l'histoire de ce lieu ? " + serverResponse["address_story"]["extract"]);
            } else if (serverResponse["address_story"]["status"] === "NOT FOUND"){
                createMessage("grandpy", "Ma mémoire me fait parfois défaut ! Je ne me rappel plus grand chose sur l'histoire de ce lieu !");
            }

        } else if (serverResponse["address"]["status"] === "NOT FOUND"){
            createMessage("grandpy", "Je suis désolé, je n'ai pas trouvé d'adresse");
        }

    }

}

// -----------------------------------
// Application initialization
// -----------------------------------

$("#loading").css({display : "none"});

// Leaflet initialization
var maCarte = L.map('maCarte').setView([0, 0], 15);
var marker = L.marker([0, 0]).addTo(maCarte);

// Open Street Map tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    id: 'mapbox.streets',
    attribution: ' <a href="http://www.openstreetmap.org/copyrigh">OpenStreetMap</a>'
}).addTo(maCarte);

// Wait Ajax Start
$(document).ajaxStart(function() {

    var userRequest = $('#userRequest').val()

    // Write user request in the chat
    if ($('#userRequest').val() === ""){

    }else{
        // Reset form to user browser
        $('#formulaire')[0].reset()
        createMessage("user", userRequest)
    }
    // Replace the form with the loading image
    $("#formulaire").hide();
    $('#loading').show()

}).ajaxStop(function(){

    // Replace the loading image with the form
    $("#loading").hide();
    $("#formulaire").show()
});

// Wait 'button' click
$('button').click(function (e) {
    e.preventDefault();

    $.ajax({
        url: $SCRIPT_ROOT + '/_query',
        type: 'POST',
        data: $('form').serialize(),
        dataType: 'json',
        success: function(serverResponse) {

            dispatch(serverResponse)
        },
        error: function(error){
            $('#chat').append("<div class=\"grandpy_response\"> Oups ! Je n'ai pas compris ! </div>");
        }
                                                 
    });

});

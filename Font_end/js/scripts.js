// Get the current year for the copyright
// $("#year").text(new Date().getFullYear());

// Get Gooogle Map
// index
function initMap() {
  var options = {
    zoom: 8,
    center: { lat: 52.2297, lng: 21.0122 }
  };

  var map = new google.maps.Map(document.getElementById("map"), options);
}

// animallist
function initMapList() {
  var options = {
    zoom: 8,
    center: { lat: 52.2297, lng: 21.0122 }
  };

  var map = new google.maps.Map(document.getElementById("map-list"), options);
}

// Animal Details Map
function initMapDetails() {
  var options = {
    zoom: 8,
    center: { lat: 52.2297, lng: 21.0122 }
  };

  var map = new google.maps.Map(
    document.getElementById("map-details"),
    options
  );
}

// Get animal list

$(function() {
  var $animals_cards = $("#animal-cards");
  $.ajax({
    url: "http://127.0.0.1:8000/animals/",
    method: "GET"
  }).done(function(response) {
    for (var i = 0; i < 15; i++) {
      var $card = $('<div class="card">');
      var $img = $(
        '<img src="' +
          response[i].img_main +
          '" alt="' +
          response[i].img_main_alt +
          '" class="img-fluid card-img-top">'
      );
      var $card_body = $('<div class="card-body">');
      var $title = $('<h4 class="card-title"></h4>');
      $title.text(response[i].name);
      var $race = $('<small class="text-muted"></small>');
      $race.text(response[i].race);
      var $hr = $("<hr>");
      var $sex = $('<p class="card-text"></p>');
      $sex.text("Płeć: " + response[i].sex);
      var $age = $('<p class="card-text"></p>');
      $age.text("wiek: " + response[i].age);
      var $weight = $('<p class="card-text"></p>');
      $weight.text("Wielkość: " + response[i].weight);
      var $button = $('<a class="btn btn-outline-primary btn-block" href=#>');
      $button.attr("href", "/animals/" + response[i].id);
      $button.text("Więcej szczegółów");

      $animals_cards.append($card);
      $card.append($img);
      $card_body.append($title);
      $race.insertAfter($title);
      $hr.insertAfter($race);
      $sex.insertAfter($hr);
      $age.insertAfter($sex);
      $weight.insertAfter($age);
      $button.insertAfter($weight);
      $card_body.insertAfter($img);
    }
  });
});

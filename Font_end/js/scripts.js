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

// Animal list Map
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

$(document).ready(function() {
  var $animals_cards = $("#animal-cards");
  var $listpagination = $("#animal-list-pagination");
  var $animal_details = $("#animal-details-card");

  $.ajax({
    url: "http://127.0.0.1:8000/animals/",
    method: "GET"
  }).done(function(response) {
    var $result = response["results"];

    for (var i = 0; i < $result.length; i++) {
      var $card = $('<div class="card">');
      var $img = $(
        '<img src="' +
          $result[i].img_main +
          '" alt="' +
          $result[i].img_main_alt +
          '" class="img-fluid card-img-top">'
      );
      var $card_body = $('<div class="card-body">');
      var $title = $('<h4 class="card-title"></h4>');
      $title.text($result[i].name);
      var $race = $('<small class="text-muted"></small>');
      $race.text($result[i].race);
      var $hr = $("<hr>");
      var $sex = $('<p class="card-text"></p>');
      $sex.text("Płeć: " + $result[i].sex);
      var $age = $('<p class="card-text"></p>');
      $age.text("wiek: " + $result[i].age);
      var $weight = $('<p class="card-text"></p>');
      $weight.text("Wielkość: " + $result[i].weight);
      var $button = $(
        '<a class="details btn btn-outline-primary btn-block" data-id="' +
          $result[i].id +
          '" href="">'
      );
      $button.attr("href", "animal_detail.html");
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

    // var $previous = $(
    //   '<li class="page-item"><a class="page-link" href="#"><span>&laquo;</span><span class="sr-only">Previous</span></a></li>'
    // );
    // $previous.attr("href", response.previous);

    // var $next = $(
    //   '<li class="page-item"><a class="page-link" href="#"><span>&raquo;</span><span class="sr-only">Next</span></a></li>'
    // );
    // $next.attr("href", response.next);

    // $listpagination.append($previous);
    // $listpagination.append($next);

    // <li class="page-item disabled">
    //         <a class="page-link" href="#">
    //             <span>&laquo;</span>
    //             <span class="sr-only">Previous</span>
    //         </a>
    //     </li>
    //     <li class="page-item active">
    //         <a class="page-link" href="#">1</a>
    //     </li>
    //     <li class="page-item">
    //         <a class="page-link" href="#">2</a>
    //     </li>
    //     <li class="page-item">
    //         <a class="page-link" href="#">3</a>
    //     </li>
    // <li class="page-item">
    //     <a class="page-link" href="#">
    //         <span>&raquo;</span>
    //         <span class="sr-only">Next</span>
    //     </a>
    // </li>
  });

  // Animal details
  $animals_cards.find(".details").on("click", function(event) {
    var $id = $(this).data("id");
    $.ajax({
      url: "http://127.0.0.1:8000/animals/" + $id,
      method: "GET"
    }).done(function(response) {
      // Description Card

      var $name = $('<div class="card-header mt-3 mx-3 p-3 h4"></div>');
      $name.text(response.name);

      var $card_body = $('<div class="card-body">');
      var $title_species = $(
        '<span class="card-title font-weight-bold">Gatunek: </span>'
      );
      var $species = $('<p class="card-text ml-4 mb-2"></p>');
      $species.text(response.species);
      var $title_race = $(
        '<span class="card-title font-weight-bold">Rasa: </span>'
      );
      var $race = $('<p class="card-text ml-4 mb-2"></p>');
      $race.text(response.race);
      var $title_sex = $(
        '<span class="card-title font-weight-bold">Płeć: </span>'
      );
      var $sex = $('<p class="card-text ml-4 mb-2"></p>');
      $sex.text(response.sex);
      var $title_age = $(
        '<span class="card-title font-weight-bold">Wiek: </span>'
      );
      var $age = $('<p class="card-text ml-4 mb-2"></p>');
      $age.text(response.age);
      var $title_weight = $(
        '<span class="card-title font-weight-bold">Waga: </span>'
      );
      var $weight = $('<p class="card-text ml-4 mb-2"></p>');
      $weight.text(response.weight);
      var $title_sterilized_castrated = $(
        '<span class="card-title font-weight-bold">Wysterylizowana/Wykastrowany: </span>'
      );
      var $sterilized_castrated = $('<p class="card-text ml-4 mb-2"></p>');
      $sterilized_castrated.text(response.sterilized_castrated);
      var $title_description = $(
        '<span class="card-title font-weight-bold">Opis: </span>'
      );
      var $description = $('<p class="card-text text-justify"></p>');
      $description.text(response.description);

      $card_body.append($title_species);
      $species.insertAfter($title_species);
      $title_race.insertAfter($species);
      $race.insertAfter($title_race);
      $title_sex.insertAfter($race);
      $sex.insertAfter($title_sex);
      $title_age.insertAfter($sex);
      $age.insertAfter($title_age);
      $title_weight.insertAfter($age);
      $weight.insertAfter($title_weight);
      $title_sterilized_castrated.insertAfter($weight);
      $sterilized_castrated.insertAfter($title_sterilized_castrated);
      $title_description.insertAfter(sterilized_castrated);
      $description.insertAfter($title_description);

      $animal_details.append($name);
      $card_body.insertAfter($name);
    });
  });
});

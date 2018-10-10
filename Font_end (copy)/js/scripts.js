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

$(function() {
  var $animals_cards = $("#animal-cards");
  var $listpagination = $("#animal-list-pagination");
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
      var $button = $('<a class="btn btn-outline-primary btn-block" href=#>');
      $button.attr("href", "/animals/" + $result[i].id);
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

    var $previous = $('<li class="page-item"></li>');
    var $a_previous = $(
      '<a class="page-link" href="#"><span>&laquo;</span><span class="sr-only">Previous</span></a>'
    );
    $a_previous.attr("href", response["previous"]);
    $previous.append($a_previous);

    var $next = $('<li class="page-item"></li>');
    $a_next = $(
      '<a class="page-link" href="#"><span>&raquo;</span><span class="sr-only">Next</span></a>'
    );
    $a_next.attr("href", response["next"]);
    $next.append($a_next);

    $listpagination.append($previous);
    $listpagination.append($next);

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
});

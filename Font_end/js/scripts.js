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
<<<<<<< Updated upstream
// $(function() {

//     var $animals_cards = $('#animal-cards');
//     $.ajax({
//         url: 'http://127.0.0.1:8000/animals/',
//         method: 'GET'
//     }).done(function(response) {

//         for(var i= 0; i < response.length; i++) {
//             var $li = $('<li data-id="' + response[i].id + '">');
//             $li.text(response[i].title);
//             var $div = $('<div class="description hidden">');
//             var $del = $('<a href="#" class="del" style="margin-left: 10px">');
//             $del.text('Usuń');
//             $gitanimals_cards.append($li);
//             $li.append($del);
//             $div.insertAfter($li);

//             $del.on('click', function(event) {
//                 var $id = $(this).parent().data('id');
//                 $.ajax({
//                     url: 'http://127.0.0.1:8000/book/' + $id,
//                     method: 'DELETE',
//                     data: 'pk="' + $id +'"'
//                 }).done(function() {
//                     location.reload();
//                     alert('Książka usunięta');
//                 });

//             });
//         }

//     });
=======

// Get animal list

$(function() {
  var $animals_cards = $("#animal-cards");
  $.ajax({
    url: "http://127.0.0.1:8000/animals/",
    method: "GET"
  }).done(function(response) {
    for (var i = 0; i < response.length; i++) {
      var $card = $('<div class="card">');
      var $img = $(
        '<img src="' +
          response[i].img_main +
          '" alt="' +
          response[i].img_main_alt +
          '" class="img-fluid card-im g-top">'
      );
      var $card_body = $('<div class="card-body">');
      var $title = $('<h4 class="card-title"></h4>');
      $title.text(response[i].name);
      var $race = $('<small class="text-muted"></small><hr>');
      $race.text(response[i].race);
      var $sex = $('<p class="card-text"</p>');
      $sex.text(response[i].sex);
      var $age = $('<p class="card-text"</p>');
      $age.text(response[i].age);
      var $weight = $('<p class="card-text"</p>');
      $weight.text(response[i].weight);
      var $button = $(
        '<a class="btn btn-outline-primary btn-block" href="/animals/' +
          response[i].id +
          ">Więcej szczegółów</a>"
      );

      $animals_cards.append($card);
      $card.append($img);
      $card_body.append($title);
      $race.insertAfter($title);
      $sex.insertAfter($race);
      $age.insertAfter($sex);
      $weight.insertAfter($age);
      $button.insertAfter($weight);
      $card_body.isertAfter($img);
    }
  });
});
>>>>>>> Stashed changes

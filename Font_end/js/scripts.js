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

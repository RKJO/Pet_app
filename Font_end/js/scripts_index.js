// Get the current year for the copyright
// $("#year").text(new Date().getFullYear());

// Get Gooogle Map
// index

var latlng = { lat: 51.9194, lng: 19.1451 };
var marker;
// var map; /* make the map available in all scopes */

var markersList = []; /* container to store references to newly added markers */

function addMarkers(map, markers) {
  for (i = 0; i < markers.length; i++) {
    marker = new google.maps.Marker({
      position: markers[i].location,
      position: new google.maps.LatLng(markers[i].lat, markers[i].lng),
      label: String(markers[i].label),
      animation: google.maps.Animation.DROP, //google.maps.Animation.BOUNCE,
      map: map
    });
  }
}

// google.maps.event.addDomListener(window, "load", initMap);

$(document).ready(function() {
  $.ajax({
    url: "http://127.0.0.1:8000/location/",
    method: "GET"
  }).done(function(response) {
    for (var i = 0; i < response.length; i++) {
      var name = response[i].name;
      var label = response[i].animals_count;
      markersList.push({
        name: name,
        lat: response[i].latitude,
        lng: response[i].longitude,
        label: label
      });
    }
  });
  // Animal filters Funaction

  // Search form
  var $search_form = $("#search-form-index");
  var $submit_btn_index = $("#submit_index");
  $submit_btn_index.on("click", function(event) {
    event.preventDefault();

    var formDataIndex = {
      species_dog: $search_form.find("#dog").prop("checked"),
      species_cat: $search_form.find("#cat").prop("checked"),
      species_other: $search_form.find("#other").prop("checked"),
      age_from: $search_form.find("#age_from").val(),
      age_to: $search_form.find("#age_to").val(),
      sex: $search_form.find("#sex").val(),
      weight: $search_form.find("#weight").val()
    };

    window.localStorage.setItem("formDataIndex", JSON.stringify(formDataIndex));
    window.location.href = "animal_list.html";
  });
});

function initMap() {
  var options = {
    zoom: 6,
    center: latlng
  };
  var map = new google.maps.Map(document.getElementById("map"), options);

  addMarkers(map, markersList);
}

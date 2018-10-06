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

// Adds a marker to the map.
function addMarker() {
  var marker = new google.maps.Marker({
    position: location[i],
    label: label[i],
    map: map
  });
}

$(document).ready(function() {
  // $.ajax({
  //   url: "http://127.0.0.1:8000/location/",
  //   method: "GET"
  // }).done(function(response) {
  //   for (var i = 0; i < response.length; i++) {
  //     location.push(
  //       new google.maps.LatLng(response[i].latitude, response[i].longitude)
  //     );
  //     label.push(response[i].animals_count);
  //   }
  //   addMarker()
  // });

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

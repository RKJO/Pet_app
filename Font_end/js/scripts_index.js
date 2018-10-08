// Get the current year for the copyright
// $("#year").text(new Date().getFullYear());

// Get Leaflet Map

var latlng = [51.9194, 19.1451];

$(document).ready(function() {
  var map = L.map("map").setView(latlng, 6);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  $.ajax({
    url: "http://127.0.0.1:8000/location/",
    method: "GET"
  }).done(function(response) {
    for (var i = 0; i < response.length; i++) {
      var name = response[i].name;
      var label = response[i].animals_count;
      var lat = response[i].latitude;
      var lng = response[i].longitude;
      L.marker([lat, lng])
        .addTo(map)
        .bindPopup(name)
        .bindTooltip(String(label), {
          permanent: true,
          direction: "left",
          offset: L.point({ x: 12, y: 15 })
        })
        .openTooltip();
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

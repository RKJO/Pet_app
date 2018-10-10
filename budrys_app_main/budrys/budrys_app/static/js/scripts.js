document.addEventListener("DOMContentLoaded", function(event) {

    var name = document.getElementById('name');
    var location = [parseFloat(name.dataset.lat), parseFloat(name.dataset.lng)];

    var mapdetails = L.map("map-details").setView(location, 11);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapdetails);

    L.marker(location)
        .addTo(mapdetails)
        .bindPopup(name.dataset.sheltername) //, {maxWidth: 200})
        .openPopup();

    // var popupContent = document.querySelectorAll('.leaflet-popup-content-wrapper').classList;
    // console.log(popupContent);
    // popupContent.firstChild.classList.add('text-center')

});
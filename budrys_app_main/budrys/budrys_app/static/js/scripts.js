function initMapDetails() {
  var name = document.getElementById('name');

  var location = {lat: parseFloat(name.dataset.lat), lng: parseFloat(name.dataset.lng)};
  var options = {
      zoom: 12,
      center: location
  };

  var map = new google.maps.Map(
      document.getElementById("map-details"),
      options
  );

  var marker = new google.maps.Marker({
      draggable: true,
      animation: google.maps.Animation.DROP, //google.maps.Animation.BOUNCE,
      position: location,
      map: map,
  });

  var contentString = '<div id="content">'+
            '<div id="siteNotice">'+
            '</div>'+
            '<h5 id="firstHeading" class="firstHeading h6 text-center">'+name.dataset.sheltername+'</h5>'+
            '<div id="bodyContent">'+
            // can add body content
            '</div>'+
            '</div>';

  var infowindow = new google.maps.InfoWindow({
      content: contentString,
      maxWidth: 250,
  });
  marker.addListener('click', function() {
    infowindow.open(map, marker);
        });
}

// Get the current year for the copyright
// $("#year").text(new Date().getFullYear());

// Adds a marker to the map.
function addMarker() {
  var marker = new google.maps.Marker({
    position: location[i],
    label: label[i],
    map: map
  });
}

// Animal list Map
function initMapList() {
  var options = {
    zoom: 8,
    center: { lat: 52.2297, lng: 21.0122 }
  };

  var map = new google.maps.Map(document.getElementById("map-list"), options);
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

  // Animal list Page
  var $animals_cards = $("#animal-cards");
  var $listpagination = $("#animal-list-pagination");
  // function shows proper way to show years

  function polishPlural(
    singularNominativ,
    pluralNominativ,
    pluralGenitive,
    value
  ) {
    if (value === 1) {
      return singularNominativ;
    } else if (
      value % 10 >= 2 &&
      value % 10 <= 4 &&
      (value % 100 < 10 || value % 100 >= 20)
    ) {
      return pluralNominativ;
    } else {
      return pluralGenitive;
    }
  }

  // Animal cards function

  function getAnimalCards(response) {
    var $result = response["results"];

    for (var i = 0; i < $result.length; i++) {
      var $card = $('<div class="card">');
      var $img = $(
        '<img src="' +
          $result[i].img_main +
          '" alt="Image not Found" class="img-fluid card-img-top">'
      );
      $img.on("error", { alt_img_path: $result[i].img_main_alt }, function(
        event
      ) {
        $(this).attr("src", event.data.alt_img_path);
      });
      var $card_body = $('<div class="card-body">');
      var $title = $('<h4 class="card-title"></h4>');
      $title.text($result[i].name);
      var $race = $('<small class="text-muted"></small>');
      $race.text($result[i].race);
      var $hr = $("<hr>");
      var $sex = $('<p class="card-text"></p>');
      $sex.text("Płeć: " + $result[i].sex);
      var $age = $('<p class="card-text"></p>');
      $age.text(
        "Wiek: " +
          $result[i].age +
          polishPlural(" rok", " lata", " lat", $result[i].age)
      );
      var $weight = $('<p class="card-text"></p>');
      $weight.text("Wielkość: " + $result[i].weight);
      var $button = $(
        '<a class="details btn btn-outline-primary btn-block" data-id="' +
          $result[i].id +
          '" href="">'
      );
      $button.attr(
        "href",
        "http://127.0.0.1:8000/animals/" + $result[i].id + "/"
      );
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

    var $previous = $(
      '<li id="class="page-item disabled"><a class="page-link" data-url="' +
        response.previous +
        '" href="#"><span>&laquo;</span><span class="sr-only">Previous</span></a></li>'
    );

    var $next = $(
      '<li class="page-item disabled"><a class="page-link" data-url="' +
        response.next +
        '" href="#"><span>&raquo;</span><span class="sr-only">Next</span></a></li>'
    );

    $listpagination.append($previous);
    $listpagination.append($next);

    if (response.previous != null) {
      $previous.toggleClass("disabled");
    }

    if (response.next != null) {
      $next.toggleClass("disabled");
    }

    $previous.on("click", function(event) {
      event.preventDefault();
      $animals_cards.find(".card").remove();
      $listpagination.find(".page-item").remove();

      $previous_url = $(this)
        .find("a")
        .data("url");

      $.ajax({
        url: $previous_url,
        method: "GET"
      }).done(getAnimalCards);
    });

    $next.on("click", function(event) {
      event.preventDefault();
      $animals_cards.find(".card").remove();
      $listpagination.find("li").remove();

      $next_url = $(this)
        .find("a")
        .data("url");

      $.ajax({
        url: $next_url,
        method: "GET"
      }).done(getAnimalCards);
    });
  }

  // function Combine URL

  function combineURL(formData) {
    var url = "http://127.0.0.1:8000/animals/";
    if (formData.species_dog) {
      url += "?species=Pies";
    } else if (formData.species_cat) {
      url += "?species=Kot";
    } else if (formData.species_other) {
      url += "?species=Inne";
    }

    if (formData.age_from) {
      url += "&min_age=" + formData.age_from;
    }

    if (formData.age_to) {
      url += "&max_age=" + formData.age_to;
    }

    if (formData.sex) {
      url += "&sex=" + formData.sex;
    }

    if (formData.location) {
      url += "&location=" + formData.location;
    }

    if (formData.distance) {
      url += "&distance=" + formData.distance;
    }

    $.ajax({
      url: url,
      method: "GET"
    }).done(getAnimalCards);
  }

  // Animal filters Funaction

  // all Animals + form data from index page.
  var formDataIndex = JSON.parse(window.localStorage.getItem("formDataIndex"));

  combineURL(formDataIndex);
  // $.ajax({
  //   url: "http://127.0.0.1:8000/animals/",
  //   method: "GET"
  // }).done(getAnimalCards);

  // Search form
  var $search_form = $("#search-form-list");
  var $submit_btn = $("#submit");
  $submit_btn.on("click", function(event) {
    event.preventDefault();
    $animals_cards.find(".card").remove();
    $listpagination.find("li").remove();

    var formData = {
      species_dog: $search_form.find("#dog").prop("checked"),
      species_cat: $search_form.find("#cat").prop("checked"),
      species_other: $search_form.find("#other").prop("checked"),
      age_from: $search_form.find("#age_from").val(),
      age_to: $search_form.find("#age_to").val(),
      sex: $search_form.find("#sex").val(),
      weight: $search_form.find("#weight").val(),
      location: $search_form.find("#address").val(),
      distance: $search_form.find("#distance").val()
    };

    combineURL(formData);
  });
});

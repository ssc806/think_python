

//Set the init map and the center lat and alt
var centerLat = new google.maps.LatLng(30.307182, -97.755996);
var map = new google.maps.Map(document.getElementById('map'), {
                                  center: centerLat,
                                  zoom: 11,
                                  mapTypeId: google.maps.MapTypeId.ROADMAP
});
//The global list of the markers. Use it to clear the map before show the search result.
var markers = []; 

//Set the markers on the map
function setMarkers(locations) {
  var infowindow = new google.maps.InfoWindow();
  var marker, i;

  //Set markers
  for (i = 0; i < locations.length; i++) {  
    console.log(locations[i])
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][2], locations[i][3]),
      map: map
    });

    //Set infowindows
    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        pop_info = "<p>" + 
                   "Camera ID:" + locations[i][0] + 
                   "<br />" + 
                   "Address: " + locations[i][1] +
                   "</p>"
        infowindow.setContent(pop_info);
        infowindow.open(map, marker);
      }
    })(marker, i));

    //Store the markers to the global list
    markers.push(marker);
  }
}


function displaySearch(result) {
    // Loop through markers and set map to null for each
    for (var i=0; i<markers.length; i++) {

        markers[i].setMap(null);
    }

    // Reset the markers array
    markers = [];

    // Call set markers to re-add markers
    setMarkers(result);
}

//Show all the locations on the init map
function initialize() {
  setMarkers(allLocations);
}

//Creat a ajax request for search
function createPost() {
    var post_form = $('#custom-search-form')

    //Popup the alert if no data for the search
    var fail_html = ' \
          <div class="span4"> \
            <div id="fail-html" class="alert alert-danger alert-dismissable">  \
                <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>  \
                <strong>No data found</strong>  \
            </div>  \
          </div> \
    '

    //console.log(post_form.serialize())
    //console.log(post_form.attr('action'))
    //console.log(post_form.attr('method'))
    $.ajax({
        url: post_form.attr('action'), 
        type: post_form.attr('method'),
        data: post_form.serialize(),
        success: function(response){
            //console.log(response)
            if (jQuery.isEmptyObject(response)){
                 $(fail_html).insertAfter($('#div-search-form'))
            }else{
                 displaySearch($.parseJSON(response))
            }
        }
    });
}

// Submit post on submit
$('#custom-search-form').on('submit', function(e){
    $('#fail-html').remove();
    console.log("form submitted!");
    createPost()

    e.preventDefault();
})

//Show the map when loading completing
initialize();





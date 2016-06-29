function initMap() {
       
    
    // Create a map object and specify the DOM element for display.
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.0, lng: 0.0},
        scrollwheel: false,
        zoom: 3,
        mapTypeControl: false,
        streetViewControl: false,
        styles: mapStyles
    });
}

$(document).ready(function (e){
    $("#view_crime_info").hide();
    $("#add_crime_info").hide();
    $("#search").val("");
    $('#datepick').hide();
    $('#category').hide();
    $('#aff').hide();
    $('#ami').hide();
    $('#default1').prop('checked', false);
    $('#d1').prop('checked', false);
    $('#default2').prop('checked', false);
    $('#default2').hide();
    $('#d2').prop('checked', false);
    $('#map_view').hide();
    $('#sizetoggle').prop('checked', false);
});
function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = ampm;
    return strTime;
  }
  
  if(formatAMPM(new Date) === "am"){
        $('#ai').html('Good Morning ,');
  }else{
        $('#ai').html('Good Afternoon ,');
  }


$('#d1').change(function(e){
    e.preventDefault();
    $('#ami').hide();
    $('#aff').toggle();
    $('#ami').scrollTop = 0;
    $('#d2').prop('checked', false);
});
$('#d2').change(function(e){
    e.preventDefault();
    $('#aff').hide();
    $('#ami').toggle();
    $('#d1').prop('checked', false);
    $('#ami').scrollTop = 0;
});
$('#default1').change(function(e){
    e.preventDefault();
    $('#datepick').hide();
    $('#category').toggle();
    $('#default2').prop('checked', false);
    $('#map_view').hide();
});
$('#default2').change(function(e){
    e.preventDefault();
    $('#datepick').toggle();
    $('#category').hide();
    $('#search').val("");
    $('#default1').prop('checked', false);
    $('#map_view').hide();
});

$('#sizetoggle').change(function(e) {
   e.preventDefault();

   if($('#sizetoggle').prop('checked')){
      $('#mapdisplay').removeClass('col-sm-9');
      $('#sidemenu').removeClass('col-sm-3');
      $('#mapdisplay').addClass('col-sm-11');
      $('#sidemenu').addClass('col-sm-1 ');
      $('#one').css({'display':'none'});
      $('#two').css('display','none');
      $('#four').css('display','none');
      $('#m_three').hide();
      $('#location_info').hide();
      $('#noexp').hide();
      $("#view_crime_info").hide();
      $("#add_crime_info").hide();
      $('#map_view').hide();
      $('#m_one').removeAttr('onclick','addCrime()');
      $('#m_two').removeAttr('onclick','viewCrime()');
      $('#m_four').removeAttr('onclick','map_view()');
      $('.fa-fw').removeClass('fa-lg');
      $('.fa-fw').addClass('fa-2x');
      $('.c').addClass('w-75');
      $('#m_one').attr( {'data-toggle':'modal', 'data-target':'#modal1'});
      $('#m_two').attr( {'data-toggle':'modal', 'data-target':'#modal2'});
      $('#m_four').attr( {'data-toggle':'modal', 'data-target':'#modal3'});
 }else{
    $('#mapdisplay').removeClass('col-sm-11');
    $('#sidemenu').removeClass('col-sm-1');
    $('#mapdisplay').addClass('col-sm-9');
    $('#sidemenu').addClass('col-sm-3');
    $('#one').css('display','');
    $('#two').css('display','');
    $('#m_three').show();
    $('#location_info').show();
    $('#four').css('display','');
    $('#noexp').show();
    $("#view_crime_info").removeAttr('hidden');
    $("#add_crime_info").removeAttr('hidden');
    $("#map_view").removeAttr('hidden');
    $('#m_one').attr('onclick','addCrime()');
    $('#m_two').attr('onclick','viewCrime()');
    $('#m_four').attr('onclick','map_view()');
    $('#m_one').removeAttr( 'data-toggle','data-target');
    $('#m_two').removeAttr( 'data-toggle','data-target');
    $('#m_four').removeAttr( 'data-toggle','data-target');
    $('.fa-fw').removeClass('fa-2x');
    $('.fa-fw').addClass('fa-lg');

    $('.c').removeClass('w-75');
 } 
});

function addCrime(){
    $("#add_crime_info").toggle();
    $("#view_crime_info").hide();
    $('#d1').prop('checked', false);
    $('#d2').prop('checked', false);
    $('#aff').hide();
    $('#map_view').hide();
}
function viewCrime(){
    $("#view_crime_info").toggle();
    $("#add_crime_info").hide();
    $('#datepick').hide();
    $('#category').hide();
    $('#default1').prop('checked', false);
    $('#map_view').hide();
    $('#default2').prop('checked', false);    
}


function map_view() {

    $("#view_crime_info").hide();
    $("#add_crime_info").hide();
    $('#datepick').hide();
    $('#category').hide();
    $('#map_view').toggle();
    $('#search').val("");
    const request_parameters = "";
    // if scheduled_function is NOT false, cancel the execution of the function
  //  if (scheduled_function) {
     //   clearTimeout(scheduled_function);
  //  }
    // setTimeout returns the ID of the function to be executed
    setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters);
    $('#default1').prop('checked', false);
    $('#default2').prop('checked', false);
}

const mymap = L.map('map').setView([0.0236, 37.9062], 6);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Warrior Insight &copy; <a href="https://www.bunasilia.co.ke/">Developed by Bunasilia</a>, <a href="https://creativecommons.org/licenses/by-sa/2.0/">Warrior Insight</a>',
    maxZoom: 15,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibXV0enk4OSIsImEiOiJja2VuNGtibDUwamQ5MnV0OGcwM3BrNzllIn0.UrzPwKYZKyxtCfwbvHUoHQ'
}).addTo(mymap);

 //let markersLayer = L.markerClusterGroup();

  //mymap.addLayer(markersLayer);

let Tmarker = {};
function marker(lat,lng) {
             
        if (Tmarker != undefined) {
            mymap.removeLayer(Tmarker);
        }

        Tmarker = L.marker([lat, lng]).addTo(mymap);
}


$.ajaxSetup({ headers: { 'csrftoken' : '{{ csrf_token() }}' } });
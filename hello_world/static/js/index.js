/**
 * Created by demus on 09/10/16.
 */

$(document).ready(function ()
{
   $('a').click(function (event) {

       event.preventDefault();
       var url = $(this).attr('href');
       console.log(url);

       $.get(url).done(window.location.reload(true))
   })
});
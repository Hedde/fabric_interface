/**
 * Created by heddevanderheide on 28/03/14.
 */

$(document).ready(function(){
   $('.change-language li a').click(function(){
       $.ajax({
           type: 'POST',
           url: '/i18n/setlang/',
           data: {
               'csrfmiddlewaretoken': $(this).parent().parent().data('csrf'),
               'language': $(this).data('code')
           },
           complete: function () {
               window.location.reload(true);
           }
       });
   });
});
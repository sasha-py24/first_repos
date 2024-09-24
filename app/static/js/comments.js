$(document).ready(function(){
    $('#sendComment').click(function(){
        var btn = $(this);
        $.ajax(btn.data('url'),{
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
//            - ключі по айді робимо:
                'text': $('#comment').val(),
},
            'success':function(response){
                var comments = document.getElementById('comments');
                comments.innerHTML = `<p>${$('#comment').val()}</p><button class="btnDelete" data-url="{{ url_for('post_delete_comment', id=c.id) }}">Delete</button>` + comments.innerHTML;
                $('#comment').val('');
//                - метод вал коли передаємо якесь знач, тут просто очистка
          }
       });
   });




    $('.btnDelete').click(function(){
        var btn = $(this);
        $.ajax(btn.data('url'),{
            'type': 'POST',
            'async': true,
            'dataType': 'json',

//


            'success':function(response){

                var comments = document.getElementById(String(response.id));
                comments.outerHTML = ``;

          }
       });
   });
})


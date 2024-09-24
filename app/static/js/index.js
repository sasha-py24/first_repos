document.getElementById('but').addEventListener('click', function(){
        var formData = new FormData();
        formData.append('title', $('#title').val());
        formData.append('text' , $('#text' ).val());
        formData.append('image', document.getElementById('image').files[0]);
        $.ajax('/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function(data) {
                let posts = document.getElementById('posts');
                posts.innerHTML = `<h3>${$('#title').val()}</h3>` + posts.innerHTML;
                 $('#title').val('');
                 $('#text').val('');
//               очищюємо від input

            }
        });
    })














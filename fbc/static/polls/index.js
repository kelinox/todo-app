$(document).ready(function(){
    $('#todo_list').sortable();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#form').submit(function(e){
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            var notif = $('body').find('.notif');
            if(data.error == "no"){
                var inputElem = document.createElement('input');
                inputElem.type = 'hidden';
                inputElem.name = 'csrfmiddlewaretoken';
                inputElem.value = $('#form').find('input[type=hidden]').val();
                $('#todo_list').append(                        
                '<div class="todo_item">'+
                    '<li class="todo_text False">'+ data.todo_name+'</li>'+
                    '<div class="button validation" >&#x2714;</div>'+
                    '<div class="button delete" >&#10006;</div>'+
                '</div>');
                var elem = $('.todo_action').last().append(inputElem);
                $('#todo_list').sortable();
                notif.text('Successfuly added the task');
                notif.removeClass('red').addClass('green');
            }
            else{
                notif.text('An error occured');
                notif.addClass('red');
            }
            notif.addClass('show');
            setTimeout(function(){$('body').find('.notif').removeClass('show');},3000);
        });
        e.preventDefault();
    });

    $('#todo_list').on('click','.delete',(function(){
        var elem = $(this);
        $.ajax({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            method: 'POST',
            dataType:'json',
            data:{
                text: $(this).parent().find('li').text()
            },
            url:'delete',
            success: function(data){
                elem.parent().remove();
                var notif = $('body').find('.notif');
                notif.text(data.message);
                notif.removeClass('red').removeClass('show');
                notif.addClass('show').addClass('green');
                setTimeout(function(){$('body').find('.notif').removeClass('show');},3000);
            },
            error: function(data){
                alert('fail');
            }
        }) 
    }))

    $('#todo_list').on('click','.validation',(function(){
        var elem = $(this);
        var notif = $('body').find('.notif');
        if(elem.parent().find('li').hasClass('True')){            
            notif.text("Task already validate");
            notif.removeClass('green');
            notif.addClass('show').addClass('red');
            setTimeout(function(){$('body').find('.notif').removeClass('show');},3000);
        }else{
            $.ajax({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },
                method: 'POST',
                dataType:'json',
                data:{
                    text: $(this).parent().find('li').text()
                },
                url:'validate',
                success: function(data){
                    elem.parent().find('li').removeClass('False').addClass('True');
                    notif.text(data.message);
                    notif.removeClass('red');
                    notif.addClass('show').addClass('green');
                    setTimeout(function(){$('body').find('.notif').removeClass('show');},3000);
                },
                error: function(data){
                    alert('fail');
                }
            })
        }

    }))

})
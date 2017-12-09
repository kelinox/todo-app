$(document).ready(function(){
    $('#todo_list').sortable();
    $('#form').submit(function(e){
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            console.log(data.error);
            if(data.error.length < 1){
                var inputElem = document.createElement('input');
                inputElem.type = 'hidden';
                inputElem.name = 'csrfmiddlewaretoken';
                inputElem.value = $('#form').find('input[type=hidden]').val();
                $('#todo_list').append(                        
                '<div class="todo_item">'+
                    '<li>'+ data.todo_name+'</li>'+
                    '<form method="post" class="todo_action">'+
                        '<input type="hidden" name="text" value="'+ data.todo_name+'"></input>'+
                        '<input type="submit" class="validation" value="&#x2714;"></input>'+
                        '<input type="submit" class="delete" value="&#10006;"></input>'+
                    '</form>'+
                '</div>');
                var elem = $('.todo_action').last().append(inputElem);
            }
        });
        e.preventDefault();
    });

    $('#todo_list').on('click','.delete',(function(){
        $(this).parent().submit(function(e){
            var elem = $(this);
            $.post('delete',elem.serialize(),function(data){
                elem.parent().remove();
            })
            e.preventDefault();
        })
    }))

    $('.validate').click(function(e){
    })

})
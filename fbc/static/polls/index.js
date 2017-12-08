$(document).ready(function(){
    $('#todo_list').sortable();
    $('#form').submit(function(e){
        e.preventDefault({
            'placeholder':true,
            'zindex': 1
        });
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            $('#todo_list').append('<li id="'+ data.todo_id+'">'+ data.todo_name+'</li>');
        });
    });
})
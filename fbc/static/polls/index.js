$(document).ready(function(){
    $('#form').submit(function(e){
        e.preventDefault();
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            $('#todo_list').append('<li id="'+ data.todo_id+'">'+ data.todo_name+'</li>')
            console.log(data.todo);
        });
    });
})
$(document).ready(function(){
    $('#todo_list').sortable();
    $('#form').submit(function(e){
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            console.log(data.error);
            if(data.error.length < 1){
                $('#todo_list').append('<li id="'+ data.todo_id+'">'+ data.todo_name+'</li>');
            }
        });
        e.preventDefault();
    });

})
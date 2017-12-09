$(document).ready(function(){
    $('#todo_list').sortable();
    $('#form').submit(function(e){
        $.post('/', $(this).serialize(), function(data){ 
            data = JSON.parse(data);
            console.log(data.error);
            if(data.error.length < 1){
                $('#todo_list').append(                        
                '<div class="todo_item">'+
                    '<li>'+ data.todo_name+'</li>'+
                    '<div class="todo_action">'+
                       '<span class="validation">&#x2714;</span>'+
                       '<span class="delete">&#10006;</span>'+
                   ' </div>'+
                '</div>');}
        });
        e.preventDefault();
    });

})
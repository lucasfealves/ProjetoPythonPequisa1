/**
 * 
 */
function AskMessage(message, prev_link, action_link, pk) {
	//var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.post({
    	url: '/Systema/AskMessage/', 
    	data: {'message': message, 'prev_link': prev_link, 'action_link': action_link, 'id_pk': pk},
    	success: function(data) {
    		document.write(data);
    	}
    	
    });
    /*$.ajax({
        type: 'POST',
        url: '/Systema/AskMessage/',
        data: {'message': message, 'prev_link': prev_link, 'action_link': action_link, 'pk': pk},
        dataType: 'json',
        encode: true,
        crossDomain: false,
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
        success: function(data){
          console.log(data);
        },
        error: function(){
          // alert('Deu Erro');
          console.log('Deu Erro');
        }
      });*/
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

    $form = $("form#comentario-form");
    $mensajeComentario = $('div#mensaje-comentario');
    $contenedorComentarios = $('section#contenedor-comentarios');

	$form.on('submit', function(event) {
		event.preventDefault();
		botonComentario = document.querySelector('button#enviar-comentario');
		botonComentario.disabled = true;
		comentario = $form[0]['comentario'].value;
		usuario = $form[0]['usuario'].value;
		post = $form[0]['post'].value;
		csrfMiddleware = $form[0]['csrfmiddlewaretoken'].value;

		submitData = {
			"comentario": comentario,
			"usuario": usuario,
			"post": post
		};

		console.log(usuario);
		console.log(post);

		console.log(submitData);

		$.ajax({
			data: JSON.stringify(submitData),
			type: "POST",
			dataType: "json",
			headers: {
				'X-CSRFToken': csrfMiddleware,
				"Content-Type": "application/json; charset=UTF-8"
			},
			url: "procesar_comentario",
			success: function(data) {
				//$form[0]['comentario'].value = "";
				botonComentario.disabled = false;
	            if (data.response == 'success') {

	            	$divMedia = $('<div class="media"></div>');
	            	$imageLink = $('<a class="pull-left" href="#"></a>');
	            	$image = $('<img class="media-object" src="'+ data.url +'" alt="" />');
	            	$divMediaBody = $('<div class="media-body"></div>');
	            	$head = $('<h4 class="media-heading"></h4>');
	            	$fecha = $('<small>  </small>').text(data.fecha);

	            	$head.append(data.usuario);
	            	$head.append($fecha);

	            	$imageLink.append($image);

	            	$divMediaBody.append($head);
	            	$divMediaBody.append(data.comentario);

	            	$divMedia.append($imageLink);
	            	$divMedia.append($divMediaBody);
	            	
	            	$contenedorComentarios.append($divMedia);
	            	$mensajeComentario.hide();

	            }	
	            else if (data.response == 'fail') {
	            	$mensajeComentario.show();
	            }
			}
		});
	});










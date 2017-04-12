#! usr/bin/local
# coding: latin-1

regex = {
    'texto': r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$',
    'genero': r'^(hombre|mujer)$'
}

error_messages = {
    'texto': 'Ingrese solo letras.',
    'genero': u'Género no válido.',
}

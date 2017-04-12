import base64
import json


def encode(data):
    return base64.b64encode(data)


def decode(data):
    return base64.b64decode(data)


def convertir_datos_comentarios(json_data):
    data = json.loads(json_data)
    data_form = {}

    for clave, valor in data.items():
        if clave == 'post' or clave == 'usuario':
            data_form[clave] = decode(valor)
        else:
            data_form[clave] = valor

    return data_form

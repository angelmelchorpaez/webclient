import http.client

conexion=http.client.HTTPSConnection(host="www.angelmelchor.pro",port=443)
conexion.request(method="GET",url="/angelmelchor.png")
respuesta=conexion.getresponse()
print(f"Respuesta completa: {respuesta}")
print(f"Propiedades: {respuesta.status}, {respuesta.reason}")
if respuesta.status == 200:
    contenido=respuesta.read()
    with open("foto.png","wb") as fichero:
        fichero.write(contenido)
else:
    print("ha ocurrido un error accediendo al archivo")
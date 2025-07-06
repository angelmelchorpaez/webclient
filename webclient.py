import http.client

conexion=http.client.HTTPSConnection(host="www.angelmelchor.pro",port=443)
conexion.request(method="GET",url="/")
respuesta=conexion.getresponse()
print(f"Respuesta completa: {respuesta}")
print(f"Propiedades: {respuesta.status}, {respuesta.reason}")
print(f"Método: {respuesta.read()}")
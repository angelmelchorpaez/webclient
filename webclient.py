import http.client

conexion=http.client.HTTPConnection(host="iottemp.martybel.es",port=80)
conexion.request(method="GET",url="/")
respuesta=conexion.getresponse()
print(f"Respuesta completa: {respuesta}")
print(f"Propiedades: {respuesta.status}, {respuesta.reason}")
print(f"Método: {respuesta.read()}")
import argparse
import http.client
import urllib.parse
import os

def descargar_archivo(url):
    for _ in range(5):  # Límite de redirecciones (para evitar bucles)
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname
        port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)
        path = parsed_url.path or '/'

        if parsed_url.query:
            path += '?' + parsed_url.query

        nombre_archivo = os.path.basename(path)
        if not nombre_archivo:
            print("No se puede determinar el nombre del archivo desde la URL.")
            return

        # Crear conexión HTTP o HTTPS
        if parsed_url.scheme == 'https':
            conexion = http.client.HTTPSConnection(host, port)
        else:
            conexion = http.client.HTTPConnection(host, port)

        conexion.request("GET", path)
        respuesta = conexion.getresponse()
        print(f"Respuesta: {respuesta.status} {respuesta.reason}")

        # Redirección (HTTP 3xx)
        if respuesta.status in (301, 302, 303, 307, 308):
            nueva_url = respuesta.getheader('Location')
            if not nueva_url:
                print("Redirección sin cabecera Location.")
                return
            print(f"Redirigiendo a: {nueva_url}")
            url = nueva_url
            conexion.close()
            continue

        # Respuesta OK
        if respuesta.status == 200:
            with open(nombre_archivo, "wb") as fichero:
                buffer_size = 8192
                while True:
                    chunk = respuesta.read(buffer_size)
                    if not chunk:
                        break
                    fichero.write(chunk)
            print(f"Archivo guardado como: {nombre_archivo}")
        else:
            print("Error al acceder al recurso")
        conexion.close()
        break
    else:
        print("Demasiadas redirecciones.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descarga archivos grandes sin cargar todo en RAM")
    parser.add_argument("--url", required=True, help="URL completa del archivo a descargar")
    args = parser.parse_args()

    descargar_archivo(args.url)
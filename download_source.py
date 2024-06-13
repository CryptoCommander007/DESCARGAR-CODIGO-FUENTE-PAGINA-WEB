import requests

def descargar_codigo_fuente(url, nombre_archivo):
    try:
        # Realizar la solicitud GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar que la solicitud fue exitosa

        # Guardar el contenido en un archivo
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(response.text)

        print(f"El código fuente de {url} se ha guardado en {nombre_archivo}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la página: {e}")

# Ejemplo de uso
url = 'https://www.amarillas.cl/b/hoteles'
nombre_archivo = 'amarillas.html'
descargar_codigo_fuente(url, nombre_archivo)

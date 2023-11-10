#import openai
from openai import OpenAI
import os

client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            )

def comprueba_ruta(pathfile):
    try:
        with open(pathfile, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "El archivo no existe"
    except Exception as e:
        return "Error al leer el archivo: " + str(e)
    
def obtener_contenido():
    while True:
        ruta = input("Por favor, ingresa la ruta del archivo: ")
        resultado_path = comprueba_ruta(ruta)

        if resultado_path == "El archivo no existe" or resultado_path.startswith("Error al leer el archivo"):
            print(resultado_path)
            print("Por favor, intenta de nuevo.")
        else:
            return resultado_path



def analisis_generalpy(contenido):
    respuesta = client.completions.create(
                    model="gpt-3.5-turbo-instruct",
                    prompt=accion + contenido,
                    max_tokens=350,
                    temperature=0
                    )
    return respuesta.choices[0].text.strip()


def calentando_motores():
    try:
        # Enviar la petición a la API de OpenAI
        respuesta = client.completions.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt="Say this is a test",
                        max_tokens=7,
                        temperature=0
                        )
                                
        # Procesar y mostrar la respuesta
        return respuesta.choices[0].text.strip()
    
    
    except Exception as e:
        print(f"Error al enviar la petición a OpenAI: {e}")


if __name__ == "__main__":
    print('test/correcto.py')
    print('test/error.py')
    print('test/mejorable.py')

    accion = "analiza la siguiente script de python: "
    contenido_archivo = obtener_contenido()
    resultado = analisis_generalpy(accion + contenido_archivo)
    print(resultado)
    
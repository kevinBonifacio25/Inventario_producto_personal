
import json
import os

ARCHIVO_DATA = "Clientes.json"

def cargar_datos():
    """aqui buscamos el archivo .json al iniciar el programa"""

    if not os.path.exists(ARCHIVO_DATA):
        return[] #si el archivo no existe, devuelve una lista vacia
    
    try: 
        """abre el archivo con whit open para
        leerlo y garantiza que el archivo se cierre correctamente"""
        with open(ARCHIVO_DATA, "r", encoding="utf-8") as f:
            return json.load(f) 
        """ el return json.load(f) lee el contenido del archivo
          y lo transforma de texto JSON  a listas en pyhton"""
        
    except(json.JSONDecodeError, FileNotFoundError):
        """el FileNotFoundError ocurrira si el archivo no existe
          todavia, por ejemplo como cuando inicializamos el programa por primera vez"""
        
        """el json.JSONDecodeError ocurre si el archivo existe pero
          esta dañado, vacio o por alguna razon tiene texto no json valido como un texto al azar"""

        return[]
    
        """return [] es un plan de respaldo si ocurre cualquiera
        de los dos errores anteriores la funcion responde
        con una lista vacia porque asi el resto del
        codigo como el for o la funcion registrar puede seguir
        trabajando con una lista vacia en lugar 
        de fallar por no encontrar los datos"""




def guardar_datos(lista_clientes):
    """sobreescribe el archivo json con una lista actualizada"""

    with open(ARCHIVO_DATA, "w", encoding="utf-8")as f:
        json.dump(lista_clientes, f, indent=4, ensure_ascii=False)
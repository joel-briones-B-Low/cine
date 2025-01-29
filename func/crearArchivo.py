from pathlib import Path
from func.costos import total
import os


def crearArchivo(personas):
    if personas:
        actual = os.getcwd()
        ruta = Path(actual)
        archivo = open('cineTicket.txt', 'w')
        archivo.write('-'* 34 + '\n')
        archivo.write('|Persona   |Boletos   |Total     |\n')        
        archivo.write('-'* 34 + '\n')
        for persona in personas:
            total_persona = total(persona.boletos, 12, persona.metodo)
            archivo.write(f'|{persona.nombre:<10}|{persona.boletos:<10}|{total_persona:<10}|\n')
            archivo.write('-'* 34 + '\n')

        archivo.close()
        
    else:
        print("No hay personas para crear el archivo")
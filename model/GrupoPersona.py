from model.Persona import Persona
import os

class GrupoPersona:
    def __init__(self):
        self.personas = []

    def crearGrupo(self):
        try:
            i = 0
            os.system('cls')
            cantidad = int(input('Ingresa la cantidad de personas: '))
            for _ in range(cantidad):
                os.system('cls')
                i = i + 1
                print(f'persona numero : {i}')
                persona = Persona()
                comprobar = persona.crearPersona()
                if comprobar is True:
                    self.personas.append(persona)
                else:
                    opcion = self.opciones()
                    if opcion == 1:
                        self.reiniciarGrupo()
                        break
                    elif opcion == 2:
                        persona = persona.reiniciarBoletos(persona)
                        self.personas.append(persona)             
                    else:
                        print('Opcion invalida')
                        self.crearGrupo()
        except Exception as e:
            print(f'Error: {e}')
            
    def opciones(self):
        try:
            
            opcionLista = """
                1- modificar cantidad personas
                2- modificar boletos
            """
            print(opcionLista)
            opcion = int(input('Ingresa la opcion deseada: '))
            return opcion
        except Exception as joel:
            print(f'Error: {joel}')

    def reiniciarGrupo(self):
        try:
            self.personas = []
            self.crearGrupo()
        except Exception as briones:
            print(f'Error: {briones}')

from cinepolis.model.Persona import Persona

class GrupoPersona:
    def __init__(self):
        self.personas = []

    def crearGrupo(self):
        i = 0
        cantidad = int(input('Ingresa la cantidad de personas: '))
        for _ in range(cantidad):
            i = i + 1
            persona = Persona()
            comprobar = persona.crearPersona()
            if comprobar:
                self.personas.append(persona)
            else:
                opcionLista = """
                1- modificar cantidad personas
                2- modificar boletos
                """
                print(opcionLista)
                opcion = int(input('Ingresa la opcion deseada: '))                
                if opcion == 1:
                    self.crearGrupo()
                elif opcion == 2:
                    persona = persona.reiniciarBoletos(persona)
                    self.personas.append(persona)             
                else:
                    print('Opcion invalida')
                    self.crearGrupo()
                    
    
            

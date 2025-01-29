from model.GrupoPersona import GrupoPersona
import os
from model.Ticket import Ticket

def opcionCap():
        opciones = """
        |1- Comprar |
        |2- Terminar|
        """
        print(opciones)
        opcion = int(input('Ingresa la opcion deseada: '))
        return opcion

def runMenu():
        # Simulación de uso
        try:
                os.system('cls')
                continuar = True
                while continuar:
                        opcion = opcionCap()
                        if opcion == 1:
                                grupo = GrupoPersona()
                                grupo.crearGrupo()
                                ticket = Ticket()
                                ticket.imprimirTicket(grupo.personas)
                                ticket.imprimirTicket([])
                        elif opcion == 2:
                                print('adios')
                                continuar = False
                        else: continuar = False # cierra el ciclo
                runMenu() # creo se llava recursividad o reciprocidad, algo asi
        except Exception as e:
                runMenu()
                


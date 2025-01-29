from cinepolis.model.GrupoPersona import GrupoPersona
import os
from cinepolis.func.costos import costo
from cinepolis.model.Ticket import Ticket

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
        continuar = True
        while continuar:
                opcion = opcionCap()
                if opcion == 1:
                        grupo = GrupoPersona()
                        grupo.crearGrupo()
                        ticket = Ticket()
                        ticket.imprimirTicket(grupo.personas)
                        ticket.imprimirTicket([])
                else:
                        print('adios')
                        continuar = False



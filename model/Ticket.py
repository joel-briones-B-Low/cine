from func.costos import total
from func.crearArchivo import crearArchivo
import os

class Ticket:
        def __init__(self):
                self.total = 0
                self.boletos = 0
                self.costo = 12
        def TicketPersona(self,personas):
                try:
                        if personas:
                                self.encabezadoTicket_persona()
                                crearArchivo(personas=personas)
                                for persona in personas:
                                        self.boletos = self.boletos + persona.boletos
                                        total_persona = total(persona.boletos, self.costo, persona.metodo)
                                        # dato: el < lo que hace es limitar el len del str 
                                        print(f'|{persona.nombre:<10}|{persona.boletos:<10}|{total_persona:<10}|')
                                        print('-'*34)
                                        self.total = self.total + total_persona
                except Exception as e:
                        print(f'Error: {e}')
                        
        def imprimirTicket(self, personas):
                        if personas != []:
                                os.system('cls')
                                self.TicketPersona(personas=personas)
                        else:
                                self.ticketFinal()
        def encabezadoTicket_persona(self):
                print('*'*34)
                print(' '*9+'Ticket persona'+' '*9)
                print('|Persona   |Boletos   |Total     |')
                print('-'*34)
        def ticketFinal(self):
                print('!' * 34)
                print(' '*10+'Ticket Final'+' '*10)
                print('_' * 34)
                print(f'|Boletos{" " * 3}|Costo{" " * 5}|Total{" " * 5}|')
                print('-'*34)
                print(f'|{self.boletos:<10}|{self.costo:<10}|{round(self.total,3):<10}|')
                print('-'*34)
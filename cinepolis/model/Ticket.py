from cinepolis.func.costos import total, costo

class Ticket:
        
        def __init__(self):
                self.total = 0
                self.boletos = 0
                self.costo = 12
        def TicketPersona(self,personas):
                if personas:
                        print('|Persona   |Boletos   |Total     |')
                        print('-'*34)
                        for persona in personas:
                                self.boletos = self.boletos + persona.boletos
                                total_persona = total(persona.boletos, self.costo, persona.metodo)
                                # dato: el < lo que hace es limitar el len del str 
                                print(f'|{persona.nombre:<10}|{persona.boletos:<10}|{total_persona:<10}|')
                                print('-'*34)
                                
        def imprimirTicket(self, personas):
                        if personas != []:
                                self.TicketPersona(personas=personas)
                        else:
                                print('' * 5)
                                print('Ticket Final')
                                print(f'|Boletos{" " * 3}|Costo{" " * 5}|Total{" " * 5}|')
                                print(f'|{self.boletos:<10}|{self.costo:<10}|{self.boletos * self.costo:<10}|')
                                print('-'*34)
                
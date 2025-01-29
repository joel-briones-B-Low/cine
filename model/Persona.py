
class Persona():
    def __init__(self, nombre='', metodo = ''):
        self.nombre = nombre
        self.metodo = metodo
    
    def crearPersona(self) -> bool:
        self.nombre = input('Ingresa tu nombre: ')
        self.boletos = int(input('ingresa la cantidad de boletos: '))
        self.metodo = int(input('si el metodo es CINECO solo oprimir el 1\n de lo contario oprimir otro caracter: '))
        if self.metodo == 1:
            self.metodo = 'CINECO'
        else:
            self.metodo = 'OTRO'
            
        if self.boletos <= 0 or self.boletos > 7:
            print('La cantidad de boletos debe ser mayor a 0 y menor o igual a 7')
            return False
        
        return True
    
    def reiniciarBoletos(self, persona):
        persona.boletos = int(input('ingresa la nueva cantidad de boletos: '))
        return persona
        
    def __str__(self):
        return f'el nombre de la persona es: {self.nombre}'
    
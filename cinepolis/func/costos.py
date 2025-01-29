"""_summary_:
    archivo unico para funciones de
    """
def costo(boletos, costoBoleto) -> int:
    #print('|Boleto    |Costo     |Total     |')
    return boletos * costoBoleto

"""
si se compra mas de 5 boletas le dan un 15%
se se compran 3, 4, 5 le dan un 10% sobre el valor a pagar
si se compran hasta 2 no hay nada
"""
def descuento_masCinco():
    return 0.15
def descuento_tresCuatroCinco():
    return 0.10

def total(boletos, costoBoleto, tipoPago) -> float:
    boletosLocal = costo(boletos, costoBoleto)
    if tipoPago == 'CINECO':
        adicional = 0.10
        if boletos > 5:
            local = round(boletosLocal - (boletosLocal * descuento_masCinco()), 3)
            return round(local - (local) *adicional,3)
        elif boletos == 3 or boletos == 4 or boletos == 5:
            local =  round(boletosLocal - (boletosLocal * descuento_masCinco()), 3)
            return round(local - (local) * adicional, 3)
        else :
            local =  round(boletosLocal - ((boletosLocal) * adicional), 3)
    else:
        if boletos > 5:
            return round(boletosLocal - (boletosLocal * descuento_masCinco()), 3)
        elif boletos == 3 or boletos == 4 or boletos ==5:
            return round(boletosLocal - (boletosLocal * descuento_tresCuatroCinco()), 3)
        else :
            return round(boletosLocal, 3)
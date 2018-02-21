# GABARITO
def calcular_inss (salario):
    if salario <= 1000.0:
        return 0.0
    if salario <= 2000.0:
        return salario * 0.1
    else:
        return salario * 0.2

def calcular_ir (salario_liquido):
    if salario_liquido <= 1400.0:
        return 0.0
    elif salario_liquido <= 2500.0:
        return salario * 12 / 100
    elif salario_liquido <= 5000.0:
        return salario_liquido* 20 / 100
    else:
        return salario_liquido * 27 / 100

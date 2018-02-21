def calcula_inss (salario):
    imposto_inss = int (salario * 20 / 100)
    return imposto_inss

salario = ("Digite o valor do salario", salario)
imposto_inss= calcula_inss(salario)

print ("valor do imposto e: ", imposto_inss)

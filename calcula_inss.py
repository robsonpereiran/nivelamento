def calcula_inss (salario):
    imposto_inss = int (salario * 20 / 100)
    return imposto_inss

salario = 3000
imposto_inss= calcula_inss(salario)

print ("valor do imposto e: ", imposto_inss)

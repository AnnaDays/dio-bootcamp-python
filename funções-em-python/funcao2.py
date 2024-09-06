# parametros por posicao ou nomeação (OPCIONAL) *: nomeação; /: posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # valores que estao no parametro no lado direito aceitam que sejam passados por posicao, e apos a / sao passados por nomeação  
    print(modelo, ano,placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor= "1.0", combustivel='Gasolina')

#-----------------------------------------------------------------------------------------------
#parametros por nomeação

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
     print(modelo, ano,placa, marca, motor, combustivel)
    
criar_carro(modelo ="Palio", ano= 1999, placa="ABC-1234", marca="Fiat", motor= "1.0", combustivel='Gasolina')

#------------------------------------------------------------------------------------------------

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b
    
def potencia(a, b):
    return a ** b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)
exibir_resultado(10, 10, potencia)

op = somar

print(op(1, 23))
#--------------------------------------------------------------------------------------
#ESCOPO LOCAL E GLOBAL

salario = 2000 #variavel *GLOBAL*

def salario_bonus(bonus, lista):
    global salario #utilizar a variavel que esta fora da funcao,usa-se global
    lista_aux = lista.copy() #copia a lista qu esta no escopo GLOBAL
    lista_aux.append(2) #após a copia, o nº 2 é inserido na lista copiada
    print(f"lista aux = {lista_aux}")
    salario += bonus #VARIAVEL SALARIO RECEBE O VALOR DA VARIAVEL GLOBAL *SALARIO*
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)
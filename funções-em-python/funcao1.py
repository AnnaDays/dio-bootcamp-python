def exibir_mensagem():
    print("Olá Mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo {nome}!")
    

exibir_mensagem()
exibir_mensagem_2(nome="José")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

# ---------------------------------------------------------
def calcular_total(numeros):
    return sum(numeros)

def retorne_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")


print(calcular_total([10, 20, 34]))
print(retorne_antecessor_e_sucessor(10))
print(func_3())

#---------------------------------------------------------
#ARGUMENTOS NOMEADOS
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso!! {marca}/{modelo}/{ano}/{placa}")
    
    
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
print("\n")
#----------------------------------------------------------
def exibir_poema(data_extenso,*tupla, **dicionario): #args -> tupla; kwargs -> dicionario
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Sexta-feira, 06 de Setembro de 2024", 'BootCamp DIO - Engenharia de Dados com Python', autor="DIO e NTT Data", ano=2024)
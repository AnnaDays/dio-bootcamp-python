text = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in text:
    if letra.upper() in VOGAIS:
        print(letra, end='')
    else:
        print()

# ----------------------------------------------------
#RANGE

for numero in range(0, 11):
    print(numero, end=" ")

# Exemplo utilizando a função built-in range                
for numero in range(0, 51, 5): # 0 -> inicio; 51 -> o fim; 5 -> é o passo
    print(numero, end=" ")
    
# ----------------------------------------------------
# WHILE

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))
    
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
    else:
        print('Obrigado por usar nosso sistema bancário, até logo!')

# -------------------------------------------------------------------------
# ESTRUTURA C/ BREAK

while True:
    numero = int(input('Informe um número:'))
    
    if numero == 10:
        break
    
    print(numero)
    
# --------------------------------------------------------------------------

for numero in range (100):
    
    if numero == 12:
        break # quebra a sequencia quando o nº 12 é mostrado
    
    print(numero, end= " ")
    
# ---------------------------------------------------------------------------
    
for numero in range (100):
    
    if numero == 12:
        continue # a sequencia continua mas o nº 12 não é impresso
    
    print(numero, end= " ")

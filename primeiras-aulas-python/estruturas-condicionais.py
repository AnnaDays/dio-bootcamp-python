MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
    
if idade < MAIOR_IDADE:
    print('Menor de idade, não pode tirar a CNH.')
     
#-------------------------------------------------------------------------   
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
else:
    print('Menor de idade, não pode tirar a CNH.')
    
#-------------------------------------------------------------------------
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
elif idade >= IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas!!')
else:
    print('Menor de idade, não pode tirar a CNH.')
    
#--------------------------------------------------------------------------
#IF ANINHADO

conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema nã reconheceu seu tipo de conta, entre em contato com o seu gerente!')
    
# -------------------------------------------------------------------------------------------------
#IF TERNÁRIO

saldo = 2000
saque = 500

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f"{status} ao realizar o saque")
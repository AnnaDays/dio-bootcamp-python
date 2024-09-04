# AND -> para ser TRUE, tudo tem que ser TRUE
# OR -> para ser TRUE, apenas um tem que ser TRUE

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite or conta_especial and saldo >= saque) # TRUE

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # TRUE

conta_normal_com_saldo = (saldo >= saque and saque <= limite)
conta_especial_com_saldo = (conta_especial and saldo >= saque)

exp3 = conta_normal_com_saldo or conta_especial_com_saldo
print(exp3)
menu = """
    ---------------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    --------------- 
    
    => """

saldo = 0
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor_deposito = float(input("Quanto você deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} efetuado com sucesso!")
        else:
            print('Não foi possível depositar uma quantia negativa ou zero!')
        
    elif opcao == "2":
        valor_saque = float(input("Quanto você deseja sacar? "))
        if valor_saque > 0:
            if valor_saque <= saldo:
                if numero_de_saques < LIMITE_SAQUES:
                    saldo -= valor_saque
                    numero_de_saques += 1
                    print(f"Saque de R$ {valor_saque:.2f} efetuado com sucesso!")
                else:
                    print("Limite de saques diários excedido!")
            else:
                print("Saldo insuficiente para o saque solicitado!")
        else:
            print("O valor do saque deve ser positivo!")
            
    elif opcao == "3":
        print(f"""
        --------------------------
                 EXTRATO
            
            Saldo: R$ {saldo:.2f}
            Saques realizados: {numero_de_saques}
            Limite de Saques disponíveis: {LIMITE_SAQUES - numero_de_saques}
            
        ---------------------------
        """)
    
    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

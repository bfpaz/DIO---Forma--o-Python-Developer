

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == 'd':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falou! Valor informado é inválido!!!')
    elif opcao.lower() == 's':
        valor = float(input('Informe o valor do saque: '))
        if valor <= (saldo) and numero_saques <= LIMITE_SAQUES:
            saldo -= valor
            numero_saques +=1
            extrato += f'saque: R$ -{valor:.2f}\n'
        elif valor > saldo and valor <= (saldo + limite):
            saldo = 0
            limite = saldo + limite - valor
            extrato += f'saque: R$ -{valor:.2f}\n'
        else:
            print('Não foipossível realizar o saque, você não tem saldo/limite suficiente.')
    elif opcao.lower() == 'e':
        print(extrato)
    elif opcao.lower() == 'q':
        break
    else:
        print('Opção inválida!!!')

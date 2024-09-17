comandos = """

[d] Depositar
[s] Sacar
[x] Extrato
[q] Sair
[u] criar usuario
[c] para criar conta
[z] visualizar contas
[n] visualizar usuarios
=> """
print(comandos)

saldo_1 = 0
LIMITE = 500
extrato_1 = ""
numero_saques = 0
LIMITE_SAQUES = 3
total_usu = []
contas = []
AGENCIA = '0001'
numero_conta = 1
while True:
    
    def main():
        global entrada
        entrada = input("Digite a operação que deseja")
    main()

    def filtrar_usu(cpf, usuraio1):
            filtro = [usuraio1 for usu in usuraio1 if usu['cpf'] == cpf]
            if filtro:
                return filtro[0]
            else:
                None
    if entrada == 's':
        def saque (*,saldo, limite, limite_saque):
            global numero_saques
           
            global extrato_1
            sacar = int(input("valor para sacar : "))
            if limite_saque > numero_saques: 
                if saldo > 0:
                   
                    if sacar <= limite:
                        resultado = saldo - sacar
                        print(f'valor sacado : {sacar}')
                        extrato_1 += f' Saque : R$ {sacar} '
                        numero_saques +=1
                        return saldo
                    elif sacar > limite:
                        print("ultrapassou o limite de saque")
              
        saque(saldo=saldo_1, limite=LIMITE, limite_saque = LIMITE_SAQUES)

    elif entrada == 'd':
        depositar = int(input("valor para deposito"))
       
        def deposito(saldo1, extrato):
            global saldo_1
            global extrato_1
            if depositar > 0:
                saldo1 = depositar
                saldo_1 += saldo1
                print(f"Seu saldo atual {saldo_1}")
                extrato_1 += f' Deposito : R$ {depositar} '

            elif depositar < 0:
                print("Esse valor não pode ser depositado")

            return saldo1, extrato
        
        deposito(saldo_1, extrato_1)
      
    elif entrada == 'u':

        def cadastrar_usuario(usuario):
           
            nome = input("nome:")
            data = input("data de nascimento: ")
            cpf = input("cpf: ")
            endereco = input("endereco:")
            verificar = filtrar_usu(cpf, usuario)
            if verificar:
                print('usuario ja existe')
                return total_usu
            total_usu.append({'nome':nome, 'data_nascimento':data, 'cpf':cpf, 'endereço':endereco})
           
            print("usuario cadastrado com sucesso")
            print(total_usu)
            return total_usu
        
        cadastrar_usuario(total_usu)
       
    elif entrada == 'n':
        for i in total_usu:
            print(f"{i['nome']} - {i['data_nascimento']} - {i['cpf']} - {i['endereço']}\n")
        
    elif entrada == 'c':
    
          
            def conta_corrente(agencia, numero_conta, usuario1):
                cpf = input("cpf usuario : ")
                verificar = filtrar_usu(cpf, total_usu)
                if verificar:
                    print('usuario  existe, conta criada')
                    return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario1}
                print("usuario não encontrado")

               
            numero_conta = len(contas)          
            conta = conta_corrente(AGENCIA, numero_conta, total_usu)
            if conta :
                contas.append(conta)
        
    elif entrada == 'z':
        for i in contas:
            print(f"agencia - {i['agencia']} | numero_conta - {i['numero_conta']} | nome - {i['usuario'][0]['nome']} \n")
    
    elif entrada == 'q':
        print('saindo do sistema...')
        break

    elif entrada == 'x':
        
        def extrato1(extrato=extrato_1):
            
            if not extrato:
                print("********extrato********")
                print("***********sem movimentaçôes************")

            else:
                extrato
                print("\n*********extrato********")
                print("\n*****suas movimentaçôes*******")
                print(f"\n***** {extrato_1}")
                return extrato
        extrato1()
    else:
        print("operação nâo identificada, tente novamente")
    

           
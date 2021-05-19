import random
import time
lista_clientes = []
root_password = 'trustme'
class Client:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.password = ''
        self.cpf = 0
        self.card = 0
        self.credit = -1
        self.saldo = 0
        self.fatura = 0
        self.gastos = {
            'alimentação': 0,
            'casa': 0,
            'diversão': 0,
            'saúde': 0,
            'educação': 0
        }
cliente = Client()
#loop do menu principal
def main():
    print('-' * 20)
    print('Bem vindo(a) ao terminal do CCbank\nDigite 1 para acessar o usuário root\nDigite 2 para logar como cliente\nDigite 3 para sair')
    try:
        menu_input = int(input("Insira o comando aqui: "))
        if menu_input == 1:
            rootLogin()
        elif menu_input == 2:
            login()
        elif menu_input == 3:
            print('Obrigado por usar o CCBank!')
            time.sleep(1)
            return None
        else:
            wrongInput()
            return main()
    except ValueError:#checa se o tipo do input é o tipo requerido
        wrongInput()
        return main()
#função chamada em caso de erros de input, mostra uma mensagem de erro
def wrongInput():
    print('Comando inválido.')
    time.sleep(1)
#gera um número de cartão aleatório e único
def card_generator():
    equal_card = True
    while equal_card == True:
        card_number = []
        for i in range(10):
            card_number.append(str(random.randrange(0, 10)))
        if len(lista_clientes) > 0:
            #checa se não há outro número de cartão igual
            for j in range(len(lista_clientes)):
                for k in range(len(card_number)):
                    if lista_clientes[j].card[k] != card_number[k]:
                        equal_card = False
                        break
        elif len(lista_clientes) == 0:
            equal_card = False
    card_number = "".join(card_number)
    card_number = str(card_number)
    print(f'Seu novo número de cartão é: {card_number}')
    return card_number
#gera uma senha aleatória e única
def password_generator():
    password = []
    equal_password = True
    while equal_password == True:
        if len(lista_clientes) < 1:
            for i in range(6):
                password.append(str(random.randrange(0, 10)))
            equal_password = False
        elif len(lista_clientes) > 0:
            for i in range(6):
                password.append(str(random.randrange(0, 10)))
            for j in range(len(lista_clientes)):
                for k in range(len(password)):
                        if lista_clientes[j].password[k] != password[k]:
                            equal_password = False
                            break
    
    password = "".join(password)#transforma a lista em uma única string
    password = str(password)
    print(f'Sua nova senha é: {password}')
    return password
#valida o cpf
def validate_cpf(cpf):
    equal_cpf = True
    if len(cpf)!= 11:
        root_input = str(input('CPF inválido. Deseja digitar novamente(S/N)? '))
        root_input = root_input.upper()
        if root_input == 'S':
            root_input = str(input('Informe o cpf: '))
            return validate_cpf(root_input)
        elif root_input == 'N':
            return None
        else:
            wrongInput()
            return main()
    if len(lista_clientes) > 0:
        for i in range(len(lista_clientes)):
            for j in range(len(cpf)):
                if lista_clientes[i].cpf[j] != cpf[j]:
                    equal_cpf = False
                    break
        if equal_cpf == True:
            root_input = str(input('CPF já cadastrado. Deseja digitar novamente(S/N)? '))
            root_input = root_input.upper()
            if root_input == 'S':
                root_input = str(input('Informe o cpf: '))
                return validate_cpf(root_input)
            elif root_input == 'N':
                return None
    cont = 10
    resultado = 0
    #checar se todos os algarismos são iguais
    checker_1 = cpf[0]
    checker_1 = int(cpf[0])
    equal_numbers = 0
    #checa se todos os algarismos são iguais
    for i in range(11):
        checker_2 = int(cpf[i])
        if checker_2 == checker_1:
            equal_numbers+=1
        elif checker_1 != checker_2:
            break
        #x+=1
    if equal_numbers == 11:
        print('CPF inválido, todos os algarismos são iguais')
        return None
    else:
        for c in range(9):
            algarismo = int(cpf[c])
            calculador = algarismo * cont
            cont-=1
            resultado+=calculador
        a = (resultado * 10) % 11
        if a == 10:
            a = 0
        if a == int(cpf[9]):
            cont = 11
            resultado = 0
            for c in range(10):
                algarismo = int(cpf[c])
                calculador = algarismo * cont
                cont-=1
                resultado+=calculador
        b = (resultado * 10) % 11
        if b == 10:
            b = 0
        if a == int(cpf[9]) and b == int(cpf[10]):
            return cpf
        else:
            root_input = str(input('CPF inválido. Deseja digitar novamente(S/N)?'))
            root_input = root_input.upper()
            if root_input == 'S':
                root_input = str(input('Informe o cpf: '))
                return validate_cpf(root_input)
            elif root_input == 'N':
                return None
def rootLogin():
    root_input = str(input('Digite a senha de administrador: '))
    if root_input == root_password:
        return rootUserMenu()
    else:
        print('Senha incorreta. Retornando ao menu principal.')
        time.sleep(1)
        return main()
def rootUserMenu():
    print('-' * 20)
    print('Bem vindo(a) ao terminal de administrador do CCbank\nDigite 1 adicionar um novo cliente\nDigite 2 para visualizar a lista de clientes\nDigite 3 para modificar um cliente\nDigite 4 para sair')
    print('-' * 20)
    root_input = int(input('Digite seu comando aqui: '))
    if root_input == 1:
        cliente = Client()
        addClient(cliente)
    elif root_input == 2:
        viewClientList()
    elif root_input == 3:
        root_input = str(input('Digite o cpf do usuário que deseja visualizar: '))
        searchUser(root_input)
    elif root_input == 4:
        return main()
    else:
        wrongInput()
        rootUserMenu()
def addClient(pessoa):
        pessoa.nome = str(input('Digite o nome do usuário: '))
        pessoa.sobrenome = str(input('Digite o ultimo nome do usuário: '))
        pessoa.cpf = validate_cpf(str(input('Digite o cpf do usuário: ')))
        while pessoa.cpf == None:
            pessoa.cpf = validate_cpf(str(input('É necessário o CPF para realizar o cadastro, por favor digite novamente: ')))
        pessoa.password = password_generator()
        pessoa.card = card_generator()
        while pessoa.credit < 0 or pessoa.credit > 999999:
            pessoa.credit = int(input('Defina o limite de crédito: '))
            if pessoa.credit < 0 or pessoa.credit > 999999:
                print('Quantidade inválida de crédito. Tente novamente.')
        lista_clientes.append(pessoa)
        print('Cadastro concluído com sucesso. ')
        root_input = str(input('Deseja adicionar outro cliente(S/N)? '))
        root_input = root_input.upper()
        if root_input == 'S':
            cliente = Client()
            return addClient(cliente)
        elif root_input == 'N':
            cliente = Client()
            return rootUserMenu()
        else:
            wrongInput()
            return main()
#dado o cpf, mostra os dados do usuário e chama a função updateClient()
def searchUser(cpf):
    global user_pos
    for i in range(len(lista_clientes)):
        if lista_clientes[i].cpf == cpf:
            print('-' * 20)
            print(f'Nome: {lista_clientes[i].nome}\nSobrenome: {lista_clientes[i].sobrenome}\nCPF: {lista_clientes[i].cpf}\nSenha: {lista_clientes[i].password}\nNúmero do cartão: {lista_clientes[i].card}\nLimite do cartão: R$ {lista_clientes[i].credit}\nSaldo: R$ {lista_clientes[i].saldo}\nFatura: R$ {lista_clientes[i].fatura}\nGastos: {lista_clientes[i].gastos}')
            print('-' * 20)
            user_pos = i
            root_input = int(input('O que deseja modificar?\n'
            'Digite 1 para alterar o nome\nDigite 2 para alterar o último nome\nDigite 3 para alterar a senha\n'
            'Digite 4 para alterar o número do cartão\n'
            'Digite 5 para alterar o limite do cartão\nDigite 6 para excluir o usuário\nDigite 7 para voltar: '))
            updateClient(root_input)
        elif i == len(lista_clientes) - 1:
            root_input = str(input('CPF não encontrado. Deseja tentar novamente(S/N)?'))
            root_input = root_input.upper()
            if root_input == 'S':
                rootUserMenu()
            elif root_input == 'N':
                main()
            else:
                wrongInput()
                return main()
#modifica os dados do cliente
def updateClient(rootinput):
    if rootinput == 1:
        root_input = str(input("Digite o novo nome do usuário:"))
        lista_clientes[user_pos].nome = root_input
        main()
    elif rootinput == 2:
        root_input = str(input('Digite o novo sobrenome do usuário: '))
        lista_clientes[user_pos].sobrenome = root_input
    elif rootinput == 3:
        password_generator()
    elif rootinput == 4:
        root_input = card_generator()
        lista_clientes[user_pos].card = root_input
    elif rootinput == 5:
        root_input = str(input('Confirme sua senha para alterar o limite de crédito: '))
        if root_input == root_password:
            root_input = int(input('Digite o novo limite de crédito: '))
            if root_input < 0 or root_input > 999999:
                print('Quantidade inválida de crédito. Tente novamente.')
                return updateClient(5)
            elif root_input >= 0 and root_input < 999999:
                lista_clientes[user_pos].credit = root_input
                print('Limite de crédito alterado com sucesso.')
                time.sleep(1)
                return rootUserMenu()
        else:
            root_input = str(input('Senha incorreta. Deseja tentar novamente(S/N)? '))
            root_input = root_input.upper()
            if root_input == 'S':
                return updateClient(5)
            elif root_input == 'N':
                print('Retornando ao menu principal.')
                time.sleep(1)
                return main()
            else:
                wrongInput()
                return main()
    elif rootinput == 6:
        root_input = str(input('Confirme sua senha para deletar o usuário: '))
        if root_input == root_password:
            lista_clientes.pop(user_pos)
            print('Cliente excluído.')
            return rootUserMenu()
        else:
            root_input = str(input('Senha incorreta. Deseja tentar novamente(S/N)? '))
            root_input = root_input.upper()
            if root_input == 'S':
                return updateClient(6)
            elif root_input == 'N':
                print('Retornando ao menu principal.')
                time.sleep(1)
                return main()
            else:
                wrongInput()
                print('Retornando ao menu principal.')
    elif rootinput == 7:
        rootUserMenu()
#lista todos os clientes e seus dados
def viewClientList():
    if len(lista_clientes) < 1:
        print('Não há usuários cadastrados.')
        time.sleep(1)
        return rootUserMenu()   
    for i in range(len(lista_clientes)):
        if i == 0:
            print('-' * 20)
        print(f'Nome: {lista_clientes[i].nome}\nSobrenome: {lista_clientes[i].sobrenome}\nCPF: {lista_clientes[i].cpf}\nSenha: {lista_clientes[i].password}\nNúmero do cartão: {lista_clientes[i].card}\nLimite do cartão: R$ {lista_clientes[i].credit}\nSaldo: R$ {lista_clientes[i].saldo}\nFatura: R$ {lista_clientes[i].fatura}\nGastos: {lista_clientes[i].gastos}')
        print('-' * 20)
    time.sleep(3)
    return rootUserMenu()
#login do usuário
def login():
    validCPF = False
    validPassword = 0
    global user_pos
    while validCPF == False:
        if len(lista_clientes) < 1:
            print('Não há usuários cadastrados.')
            time.sleep(1)
            return main()
        cpf = str(input('Digite seu cpf:'))
        for i in range(len(lista_clientes)):
            if lista_clientes[i].cpf == cpf:
                user_pos = i
                validCPF = True
                break
        if validCPF == False:
            user_input = str(input('cpf não encontrado. Deseja digitar novamente(S/N)? '))
            user_input = user_input.upper()
            if user_input == 'S':
                continue
            elif user_input == 'N':
                return main()
            else:
                wrongInput()
                return main()
    password = str(input('Digite sua senha: '))
    validPassword = confirmPassword(password)
    if validPassword == 0:
        return main()
    if validCPF == True and validPassword == 1:
        return client_page(user_pos)
#confirma a senha informada, retorna 1 ou 0
def confirmPassword(senha):
    if lista_clientes[user_pos].password == senha:
        return 1
    elif lista_clientes[user_pos].password != senha:
        user_input = str(input('Senha incorreta. Deseja digitar novamente(S/N)?: '))
        user_input = user_input.upper()
        if user_input == 'S':
            user_input = str(input('Informe sua senha: '))
            return confirmPassword(user_input)
        elif user_input == 'N':
            return 0
        else:
            wrongInput()
            return 0
#menu do cliente
def client_page(userpos):
    print('-' * 20)
    print(f'Bem-vindo(a), {lista_clientes[userpos].nome}')
    print('Digite 1 para comprar\nDigite 2 para depositar dinheiro\nDigite 3 para pagar sua fatura\nDigite 4 para visualizar seus dados\nDigite 5 para visualizar os valores aplicados em suas compras:\nDigite 6 para sair')
    user_input = int(input('Digite seu comando aqui: '))
    if user_input == 1:
        pay()
    elif user_input == 2:
        depositar()
    elif user_input == 3:
        pagarFatura()
    elif user_input == 4:
        userData(userpos)
        client_page(userpos)
    elif user_input == 5:
        print('-' * 20)
        for i, j in lista_clientes[user_pos].gastos.items():
            print(i,':', 'R$',j)
        print('Digite 1 para adicionar uma categoria de compra\nDigite 2 para voltar ao menu do cliente ')
        user_input = int(input('Digite seu comando aqui: '))
        if user_input == 1:
            return alterarGastos()
        elif user_input == 2:
            return client_page(userpos)
        else:
            wrongInput()
            return main()
    elif user_input == 6:
        main()
    else:
        wrongInput()
        return main()
#mostra os dados do cliente
def userData(userpos):
    print('-' * 20)
    print(f'Nome: {lista_clientes[userpos].nome}\nSobrenome: {lista_clientes[userpos].sobrenome}\nCPF: {lista_clientes[userpos].cpf}\nNúmero do cartão: {lista_clientes[userpos].card}\nLimite do cartão: R$ {lista_clientes[userpos].credit}\nSaldo: R$ {lista_clientes[userpos].saldo}\nFatura: R$ {lista_clientes[userpos].fatura}')
    time.sleep(2)
#chama funções de pagamento de crédito ou débito
def pay():
    user_input = int(input('Digite 1 para comprar usando crédito. Digite 2 para comprar usando débito: '))
    print('Categorias de compra: ')
    if user_input == 1:
        creditPurchase()
    elif user_input == 2:
        debitPurchase()
#pagamento usando crédito
def creditPurchase():
    for i in lista_clientes[user_pos].gastos.keys():
        print(i)
    purchase_category = str(input('Informe a categoria da compra: '))
    while purchase_category not in lista_clientes[user_pos].gastos.keys():
        purchase_category = str(input('Categoria não encontrada. Por favor, digite novamente: '))
    user_input = float(input('Digite o valor da compra: '))
    password = str(input('Digite sua senha para confirmar o pagamanto: '))
    confirmation = confirmPassword(password)
    if confirmation == 1:
        if lista_clientes[user_pos].credit < user_input or lista_clientes[user_pos].fatura + user_input > lista_clientes[user_pos].credit:
            print('Transação negada. crédito infuciciente.')
            time.sleep(1)
            return client_page(user_pos)
        elif lista_clientes[user_pos].credit >= user_input and lista_clientes[user_pos].fatura + user_input <= lista_clientes[user_pos].credit:
            lista_clientes[user_pos].fatura+=user_input
            lista_clientes[user_pos].gastos[purchase_category]+=user_input
            print('Transação confirmada.')
            time.sleep(1)
            return client_page(user_pos)
    elif confirmation == 0:
        print('Transação negada. Senha incorreta')
        time.sleep(1)
        return client_page(user_pos)
#pagamento usando débito
def debitPurchase():
    for i in lista_clientes[user_pos].gastos.keys():
        print(i)
    purchase_category = str(input('Informe a categoria da compra: '))
    while purchase_category not in lista_clientes[user_pos].gastos.keys():
        purchase_category = str(input('Categoria não encontrada. Por favor, digite novamente: '))
    user_input = float(input('Digite o valor da compra: '))
    password = str(input('Digite sua senha para confirmar o pagamanto: '))
    confirmation = confirmPassword(password)
    if confirmation == 1:
        if lista_clientes[user_pos].saldo < user_input or lista_clientes[user_pos].saldo - user_input < 0:
            print('Transação negada. Saldo infuciciente.')
            time.sleep(1)
            return client_page(user_pos)
        elif lista_clientes[user_pos].saldo > user_input and lista_clientes[user_pos].saldo - user_input >= 0:
            lista_clientes[user_pos].saldo-=user_input
            lista_clientes[user_pos].gastos[purchase_category]+=user_input
            print('Transação confirmada.')
            time.sleep(1)
            return client_page(user_pos)
    elif confirmation == 0:
        print('Transação negada. Senha incorreta')
        time.sleep(1)
        return client_page(user_pos)
def depositar():
    user_input = float(input('Informe a quantia que deseja depositar: '))
    password = str(input('Informe sua senha para confirmar a transação: '))
    confirmation = confirmPassword(password)
    if confirmation == 1:
        lista_clientes[user_pos].saldo+=user_input
        print('Transação confirmada.')
        time.sleep(1)
        return client_page(user_pos)
    elif confirmation == 0:
        print('Transação negada.')
        time.sleep(1)
        return client_page(user_pos)
def pagarFatura():
    user_input = float(input('Digite o valor que deseja pagar: '))
    password = str(input("Digite sua senha: "))
    password = confirmPassword(password)
    if password == 0:
        print('Transação negada. Retornando ao menu do cliente. ')
        time.sleep(1)
        return client_page(user_pos)
    elif password == 1:
        if lista_clientes[user_pos].saldo < user_input:
            print('Transação negada. Saldo insuficiente.')
            time.sleep(1)
            return client_page(user_pos)
        elif lista_clientes[user_pos].fatura <= user_input:
            lista_clientes[user_pos].saldo-= lista_clientes[user_pos].fatura
            lista_clientes[user_pos].fatura = 0
            print('Transação concluída')
            time.sleep(1)
            return client_page(user_pos)
        elif lista_clientes[user_pos].fatura > user_input:
            lista_clientes[user_pos].saldo-= user_input
            lista_clientes[user_pos].fatura-= user_input
            print('Transação concluída')
            time.sleep(1)
            return client_page(user_pos)
def alterarGastos():
    user_input = str(input('Digite a categoria que deseja adicionar: '))
    password = str(input('Digite sua senha: '))
    password = confirmPassword(password)
    if password == 1:
        lista_clientes[user_pos].gastos.update({user_input: 0})
        print('Modificação feita com sucesso.')
        time.sleep(1)
        return client_page(user_pos)
    elif password == 0:
        print('Modificação cancelada. Retornando ao menu do cliente')
        time.sleep(1)
        return client_page(user_pos)
main()

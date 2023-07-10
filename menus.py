import dataUtils
import authUtils
from utils import clear, delaySeconds

employeeList = dataUtils.loadEmployees()
clientsList = dataUtils.loadClients()


def mainFunct():
    mainMenu()


def mainMenu():
    while True:
        employeeList = dataUtils.loadEmployees()
        clientsList = dataUtils.loadClients()
        clear()
        print()
        print("PyHair")
        print("1 - Login de Funcionários")
        print("2 - Sobre o desenvolvedor")
        print("3 - Para fechar")
        print()
        decisionOp = input("Digite sua escolha: ")
        match decisionOp:
            case "1":
                menuLogin()
            case "2":
                infoDesenvolvedor()
            case "3":
                dataUtils.saveAll(employeeList, clientsList)
                break


def menuLogin():
    clear()
    print()
    print("PyHair")
    print("Digite suas informações para logar")
    print()
    employeeCpf = input("Digite seu CPF: ")
    employeePwd = authUtils.inputPassword()
    if authUtils.authenticateWorker(employeeCpf, employeePwd):
        print()
        print("Autenticando...")
        delaySeconds(2)
        menuEmployee()
    else:
        pass


def menuEmployee():
    while True:
        clear()
        print()
        print("PyHair")
        print("1 - Registros (Funcionários ou clientes)")
        print("2 - Listagem (Funcionários ou clientes)")
        print("3 - Editar (Funcionários ou Clientes) ")
        print("4 - Deletar (Funcionários ou Clientes)")
        print("5 - Reserva de horários")
        print("6 - Gerar nota de pagamento")
        print("7 - Sair")
        print()
        decisionInput = input("Digite sua escolha: ")
        match decisionInput:
            case "1":
                menuRegister()
            case "2":
                menuListagem()
            case "3":
                menuEdit()
            case "4":
                menuDelete()
            case "5":
                menuReserva()
            case "6":
                menuPagamento()
            case "7":
                break


def menuRegister():
    clear()
    print()
    print("PyHair")
    print("1 - Registrar Funcionário")
    print("2 - Registrar Cliente")
    decisionInput = input("Digite sua escolha: ")
    match decisionInput:
        case "1":
            menuRegisterEmployee()
        case "2":
            menuRegisterClient()


def infoDesenvolvedor():
    clear()
    print("Nome: Iago Gouveia Gurgel")
    print("Idade: 18 anos")
    print("Telefone: (83) 999486943")
    print("Matrícula: 20230033117")
    print("Curso: BSI")
    print("E-mail: iagoggurgel25@gmail.com")
    print("Objetivos do projeto: Criar uma estrutura válida para utilização em um salão de cabeleireiros, \n com ideia de expansão posterior")
    input("Aperte enter para sair...")


def menuRegisterEmployee():
    clear()
    print("Digite as informações necessárias")
    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone (com DDD): ")
    cpf = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")
    email = input("Digite o E-mail: ")
    ocupacao = input("Digite a Ocupação: ")
    senha = authUtils.inputPassword()

    myDict = {cpf: {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf,
        "email": email,
        "ocupacao": ocupacao,
        "senha": authUtils.encryptPassword(senha),
        "notas": []
    }}

    employeeList.update(myDict)
    dataUtils.saveEmployees(employeeList)


def menuRegisterClient():
    clear()
    print("Digite as informações necessárias")
    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone (com DDD): ")
    cpf = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")
    email = input("Digite o E-mail: ")

    myDict = {cpf: {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf,
        "email": email,
        "totalPagar": "0",
        "reservasPagas": {},
        "reservasAtivas": {}
    }}

    clientsList.update(myDict)
    dataUtils.saveClients(clientsList)


def menuListagem():
    clear()
    print()
    print("PyHair")
    print("1 - Listar funcionários")
    print("2 - Listar clientes")
    print()
    decisionInput = input("Digite sua escolha: ")
    match decisionInput:
        case "1":
            listEmployees()
        case "2":
            listClients()


def menuDelete():
    clear()
    print()
    print("PyHair")
    print("1 - Deletar funcionário")
    print("2 - Deletar cliente")
    print()
    decisionInput = input("Digite sua escolha: ")
    match decisionInput:
        case "1":
            deleteEmployee()
        case "2":
            deleteClient()


def menuEdit():
    clear()
    print()
    print("PyHair")
    print("1 - Editar funcionários ")
    print("2 - Editar cliente")
    print()
    decisionInput = input("Digite sua escolha: ")
    match decisionInput:
        case "1":
            editEmployee()
        case "2":
            editClient()


def menuReserva():
    clear()
    print()
    print("PyHair")
    print("1 - Reservar horário")
    print("2 - Cancelar reserva")
    print()
    decisionInput = input("Digite sua escolha: ")
    match decisionInput:
        case "1":
            clear()
            dataReserva = input("Digite a data da reserva(DD/MM/YYYY): ")
            horarioReserva = input("Digite o horário da reserva: ")
            cpfFuncionario = input("Digite o CPF do funcionário: ")
            if cpfFuncionario in dataUtils.loadEmployees().keys():
                reserva = {dataReserva : {
                    "dataReserva" : dataReserva,
                    "horarioReserva" : horarioReserva,
                    "funcionarioReserva" : cpfFuncionario
                }}
            cpfCliente = input("Digite o CPF do cliente: ")
            clientsDict = dataUtils.loadClients()
            clientsDict[cpfCliente]["reservasAtivas"].update(reserva)
            dataUtils.saveClients(clientsDict)
        
        case "2":
            clear()
            clientsDict = dataUtils.loadClients()
            cpfCliente = input("Digite o CPF do cliente: ")
            if cpfCliente in clientsDict.keys():
                cliente = clientsDict[cpfCliente]
                dataReserva = input("Digite a data da reserva a ser cancelada: ")
                if dataReserva in cliente["reservasAtivas"]:
                    del cliente["reservasAtivas"][dataReserva]
                    dataUtils.saveClients(clientsDict)
                else:
                    print("Não existe nenhuma reserva nessa data.")
                    delaySeconds(1)
            else:
                print("Não existe nenhum cliente com esse CPF.")
                delaySeconds(1)


def menuPagamento():
    clear()
    clientsDict = dataUtils.loadClients()
    employeeDict = dataUtils.loadEmployees()
    print()
    print("PyHair")
    print("Realizar pagamentos")
    print()
    cpfClient = input("Digite o CPF do cliente: ")
    if cpfClient in clientsDict.keys():
        client = clientsDict[cpfClient]
        dataReserva = input("Digite a data da reserva: ")
        if dataReserva in client["reservasAtivas"]:
            reserva = client["reservasAtivas"][dataReserva]
            employee = employeeDict[reserva["funcionarioReserva"]]
            preco = input("Digite o preço da reserva: ")
            nota = float(input("Dê uma avaliação para o funcionário( 0 - 10 ): "))
            clear()
            print()
            print(f"Nome do cliente: {client['nome']}")
            print(f"Data da reserva: {reserva['dataReserva']}")
            print(f"Horário da reserva: {reserva['horarioReserva']}")
            print(f"Funcionário da reserva: {employee['nome']}")
            print()
            print(f"Preço da reserva: {preco}")
            dataUtils.openImage()
            del client["reservasAtivas"][dataReserva]
            employee["notas"].append(nota)
            employeeDict.update({employee["cpf"] : employee})
            clientsDict[cpfClient]["reservasPagas"].update({reserva['dataReserva'] : reserva})
            dataUtils.saveClients(clientsDict)
            dataUtils.saveEmployees(employeeDict)
            input("Aperte qualquer coisa para sair...")


def listEmployees():
    clear()
    employeeDict = dataUtils.loadEmployees()
    for employee in employeeDict.values():
        notas = employee["notas"]
        if len(notas) != 0:
            media = sum(notas) / len(notas)
        else:
            media = "Não tem avaliações"
        print()
        print(f"CPF (CHAVE DE BUSCA): {employee['cpf']}")
        print(f"NOME COMPLETO: {employee['nome']}")
        print(f"TELEFONE: {employee['telefone']}")
        print(f"E-MAIL: {employee['email']}")
        print(f"OCUPAÇÃO: {employee['ocupacao']}")
        print(f"AVALIAÇÕES: {media}")
    print()
    input("Aperte qualquer tecla para sair...")


def listClients():
    clear()
    clientsDict = dataUtils.loadClients()
    for client in clientsDict.values():
        print()
        print(f"CPF (CHAVE DE BUSCA): {client['cpf']}")
        print(f"NOME COMPLETO: {client['nome']}")
        print(f"TELEFONE: {client['telefone']}")
        print(f"E-MAIL: {client['email']}")
    print()
    input("Aperte qualquer tecla para sair...")


def deleteEmployee():
    clear()
    employeesDict = dataUtils.loadEmployees()
    cpfBusca = input("Informe o CPF do funcionário que deseja deletar: ")
    if cpfBusca in employeesDict.keys():
        del employeesDict[cpfBusca]
        dataUtils.saveEmployees(employeesDict)
        return True
    else:
        print("Não há funcionário com este CPF")
        delaySeconds(1.5)

def deleteClient():
    clear()
    clientsDict = dataUtils.loadClients()
    cpfBusca = input("Informe o CPF do funcionário que deseja deletar: ")
    if cpfBusca in clientsDict.keys():
        del clientsDict[cpfBusca]
        dataUtils.saveClients(clientsDict)
        return True
    else:
        print("Não há cliente com esse CPF")
        delaySeconds(1.5)

def editEmployee():
    clear()
    employeeDict = dataUtils.loadEmployees()
    cpfBusca = input("Informe o CPF do funcionário que deseja editar: ")
    if cpfBusca in employeeDict.keys():
        clear()
        employee = employeeDict[cpfBusca]
        print("Informações do funcionário")
        print()
        print(f"CPF (CHAVE DE BUSCA): {employee['cpf']}")
        print(f"NOME COMPLETO: {employee['nome']}")
        print(f"TELEFONE: {employee['telefone']}")
        print(f"E-MAIL: {employee['email']}")
        print(f"OCUPAÇÃO: {employee['ocupacao']}")
        print()
        print("1 - CPF")
        print("2 - NOME")
        print("3 - TELEFONE")
        print("4 - E-MAIL")
        print("5 - OCUPAÇÃO")
        print("6 - SENHA")
        print()
        decisionInput = input("Digite a chave que deseja alterar: ")
        match decisionInput:
            case "1":
                newCpf = input("Digite o novo CPF: ")
                employee["cpf"] = newCpf
                del employeeDict[cpfBusca]
                employeeDict.update({newCpf : employee})
            case "2":
                newNome = input("Digite o novo nome: ")
                employee["nome"] = newNome
                employeeDict.update({cpfBusca : employee})
            case "3":
                newTelefone = input("Digite o novo telefone: ")
                employee["telefone"] = newTelefone
                employeeDict.update({cpfBusca : employee})
            case "4":
                newEmail = input("Digite o novo e-mail: ")
                employee["email"] = newEmail
                employeeDict.update({cpfBusca : employee})
            case "5":
                newOcupacao = input("Digite a nova ocupação: ")
                employee["ocupacao"] = newOcupacao
                employeeDict.update({cpfBusca : employee})
            case "6":
                senhaAntiga = input("Digite a senha antiga do funcionário: ")
                if authUtils.authenticateWorker(cpfBusca, senhaAntiga):
                    newSenha = input("Digite a nova senha: ")
                    employee["senha"] = authUtils.encryptPassword(newSenha)
                    employeeDict.update({cpfBusca : employee})
        dataUtils.saveEmployees(employeeDict)



def editClient():
    clear()
    clientsDict = dataUtils.loadClients()
    cpfBusca = input("Informe o CPF do cliente que deseja editar: ")
    if cpfBusca in clientsDict.keys():
        clear()
        client = clientsDict[cpfBusca]
        print("Informações do funcionário")
        print()
        print(f"CPF (CHAVE DE BUSCA): {client['cpf']}")
        print(f"NOME COMPLETO: {client['nome']}")
        print(f"TELEFONE: {client['telefone']}")
        print(f"E-MAIL: {client['email']}")
        print()
        print("1 - CPF")
        print("2 - NOME")
        print("3 - TELEFONE")
        print("4 - E-MAIL")
        print()
        decisionInput = input("Digite a chave que deseja alterar: ")
        match decisionInput:
            case "1":
                newCpf = input("Digite o novo CPF: ")
                client["cpf"] = newCpf
                del clientsDict[cpfBusca]
                clientsDict.update({newCpf : client})
            case "2":
                newNome = input("Digite o novo nome: ")
                client["nome"] = newNome
                clientsDict.update({cpfBusca : client})
            case "3":
                newTelefone = input("Digite o novo telefone: ")
                client["telefone"] = newTelefone
                clientsDict.update({cpfBusca : client})
            case "4":
                newEmail = input("Digite o novo e-mail: ")
                client["email"] = newEmail
                clientsDict.update({cpfBusca : client})
        dataUtils.saveClients(clientsDict)

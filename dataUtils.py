import json

admin = {"admin": {"nome": "ADMIN",
                   "telefone": "",
                   "cpf": "admin",
                   "senha": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                   "email": "",
                   "ocupacao": "",
                   "nota": ""}}


def saveEmployees(listOfEmployees):
    with open("employees.json", "w") as final:
        jsonObject = json.dumps(listOfEmployees)
        final.write(jsonObject)
    return jsonObject


def saveClients(listOfClients):
    with open("clients.json", "w") as final:
        jsonObject = json.dumps(listOfClients)
        final.write(jsonObject)
    return jsonObject


def loadEmployees():
    file = open("employees.json", "r")
    return json.load(file)


def loadClients():
    file = open("clients.json", "r")
    return json.load(file)


def saveAll(workersList, clientsList):
    saveEmployees(workersList)
    saveClients(clientsList)


def searchByCPF(personList, cpf):
    if cpf in personList.keys():
        return personList[cpf]
    else:
        return False

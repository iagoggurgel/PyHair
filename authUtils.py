import hashlib, dataUtils, getpass


def encryptPassword(password):
  hashedPassword = hashlib.sha256(password.encode()).hexdigest()
  return hashedPassword


def authenticateWorker(cpf, password):
  worker = dataUtils.searchByCPF(dataUtils.loadEmployees(), cpf)
  if worker["senha"] == encryptPassword(password):
    return True
  else:
    return False
  
def inputPassword():
  password = getpass.getpass("Digite sua senha: ")
  return password
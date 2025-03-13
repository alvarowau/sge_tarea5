from parte_uno.credential_validator import validate_credentials


def request_name():
    print("Digite el nombre")
    name = input()
    return name

def request_password():
    print("Digite la contraseña")
    password = input()
    return password

def request_value_central():
    name = request_name()
    password = request_password()
    respuesta = validate_credentials(name, password)
    print(respuesta)

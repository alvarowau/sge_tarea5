from parte_uno.credential_validator import validate_credentials


def init():
    respuesta = comprobacion_user_pass()
    if respuesta[0]:
        nombre ,password  = list(respuesta[1])
        print(f"el nombre es {nombre} la contraselña es: {password}")
    else:
        print("salimos del programa")


def request_name():
    print("Digite el nombre")
    name = input()
    return name

def request_password():
    print("Digite la contraseña")
    password = input()
    return password

def comprobacion_user_pass():
    name = request_name()
    password = request_password()
    respuesta = validate_credentials(name, password)
    respuesta_nombre = respuesta["username_valid"]
    respuesta_pass = respuesta["password_valid"]
    if respuesta_nombre:
        if respuesta_pass:
            return True, (name, password)
        else:
            print(respuesta["password_message"])
            return False, ()
    else:
        print(respuesta["username_message"])
        return False, ()

# credential_validator.py

# Importar los módulos de validación de username y password
from .username_validation import validate_username
from .password_validation import validate_password


def validate_credentials(username, password):
    """
    Valida un nombre de usuario y una contraseña utilizando los módulos
    username_validation y password_validation.

    Args:
        username (str): El nombre de usuario a validar.
        password (str): La contraseña a validar.

    Returns:
        dict: Un diccionario que contiene los resultados de la validación
              para el nombre de usuario y la contraseña.
              Estructura del diccionario:
              {
                  'username_valid': bool,
                  'username_message': str,
                  'password_valid': bool,
                  'password_message': str
              }
              'username_valid' será True si el nombre de usuario es válido, False si no.
              'username_message' contendrá un mensaje indicando el resultado de la validación del nombre de usuario.
              'password_valid' será True si la contraseña es válida, False si no.
              'password_message' contendrá un mensaje (por ahora simple: 'Válida' o 'No válida') sobre la validación de la contraseña.
    """

    resultado_validacion_nombre = validate_username(username)
    es_contrasena_valida = validate_password(password)

    resultados_credenciales = {
        "username_valid": resultado_validacion_nombre[0] == 0,
        "username_message": resultado_validacion_nombre[1],
        "password_valid": es_contrasena_valida,
        "password_message": (
            "Válida"
            if es_contrasena_valida
            else "No válida según criterios de seguridad."
        ),
    }
    return resultados_credenciales


if __name__ == "__main__":
    # Ejemplos de uso del validador de credenciales (solo si se ejecuta este script directamente)

    # Ejemplo 1: Credenciales válidas
    credenciales1 = validate_credentials("UsuarioValido1", "Password123!")
    print("Ejemplo 1 - Credenciales Válidas:")
    print(
        f"  Nombre de usuario válido: {credenciales1['username_valid']}, Mensaje: {credenciales1['username_message']}"
    )
    print(
        f"  Contraseña válida: {credenciales1['password_valid']}, Mensaje: {credenciales1['password_message']}"
    )
    print("-" * 30)

    # Ejemplo 2: Nombre de usuario inválido (demasiado corto)
    credenciales2 = validate_credentials("User", "Password123!")
    print("Ejemplo 2 - Nombre de usuario inválido (demasiado corto):")
    print(
        f"  Nombre de usuario válido: {credenciales2['username_valid']}, Mensaje: {credenciales2['username_message']}"
    )
    print(
        f"  Contraseña válida: {credenciales2['password_valid']}, Mensaje: {credenciales2['password_message']}"
    )
    print("-" * 30)

    # Ejemplo 3: Contraseña inválida (sin caracter especial)
    credenciales3 = validate_credentials("UsuarioValido1", "Password123")
    print("Ejemplo 3 - Contraseña inválida (sin caracter especial):")
    print(
        f"  Nombre de usuario válido: {credenciales3['username_valid']}, Mensaje: {credenciales3['username_message']}"
    )
    print(
        f"  Contraseña válida: {credenciales3['password_valid']}, Mensaje: {credenciales3['password_message']}"
    )
    print("-" * 30)

    # Ejemplo 4: Nombre de usuario inválido (caracteres no alfanuméricos) y contraseña inválida (demasiado corta)
    credenciales4 = validate_credentials("Usuario-Invalido", "Short")
    print("Ejemplo 4 - Nombre de usuario y contraseña inválidos:")
    print(
        f"  Nombre de usuario válido: {credenciales4['username_valid']}, Mensaje: {credenciales4['username_message']}"
    )
    print(
        f"  Contraseña válida: {credenciales4['password_valid']}, Mensaje: {credenciales4['password_message']}"
    )
    print("-" * 30)

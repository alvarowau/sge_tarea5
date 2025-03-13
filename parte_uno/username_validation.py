import re


def validate_username(name: str):
    """Valida un nombre de usuario según ciertos criterios.

    El nombre de usuario debe cumplir las siguientes condiciones para ser considerado válido:
    - Tener una longitud mínima de 6 caracteres.
    - Tener una longitud máxima de 12 caracteres.
    - Contener únicamente caracteres alfanuméricos (letras y números).

    Args:
        name (str): El nombre de usuario que se va a validar.

    Returns:
        tuple: Un tuple que contiene dos elementos:
            - int: Un código de estado que indica el resultado de la validación:
                - 0: El nombre de usuario es válido.
                - 1: El nombre de usuario es demasiado corto (menos de 6 caracteres).
                - 2: El nombre de usuario es demasiado largo (más de 12 caracteres).
                - 3: El nombre de usuario contiene caracteres no alfanuméricos.
            - str: Un mensaje descriptivo asociado al código de estado.
                 "El nombre de usuario es válido" si el código es 0, o un mensaje de error
                 específico en caso contrario.

    Examples:
        Ejemplo de nombre de usuario válido:
        >>> is_name_valido("UsuarioValido1")
        (0, "El nombre de usuario es válido")

        Ejemplo de nombre de usuario demasiado corto:
        >>> is_name_valido("User")
        (1, "El nombre de usuario debe contener al menos 6 caracteres")

        Ejemplo de nombre de usuario demasiado largo:
        >>> is_name_valido("UsuarioDemasiadoLargo")
        (2, "El nombre de usuario no puede contener más de 12 caracteres")

        Ejemplo de nombre de usuario con caracteres no alfanuméricos:
        >>> is_name_valido("Usuario-Invalido")
        (3, "El nombre de usuario puede contener solo letras y números")
    """
    if not len(name) >= 6:  # Corregido a >= para incluir 6 caracteres como mínimo
        return (1, "El nombre de usuario debe contener al menos 6 caracteres")
    if not len(name) <= 12:  # Corregido a <= para incluir 12 caracteres como máximo
        return (2, "El nombre de usuario no puede contener más de 12 caracteres")
    if not re.match(r"^[a-zA-Z0-9]*$", name):
        return (3, "El nombre de usuario puede contener solo letras y números")
    return (0, "El nombre de usuario es válido")

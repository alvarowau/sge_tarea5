def validate_password(password: str) -> bool:
    """Valida una contraseña según criterios de seguridad.

    La contraseña debe cumplir los siguientes requisitos para ser considerada válida:
    - Tener una longitud mínima de 8 caracteres.
    - No contener espacios en blanco.
    - Incluir al menos una letra minúscula.
    - Incluir al menos una letra mayúscula.
    - Incluir al menos un dígito (número).
    - Incluir al menos un carácter no alfanumérico (símbolos como !, @, #, $, %, etc.).

    Args:
        password (str): La contraseña que se va a validar.

    Returns:
        bool: True si la contraseña cumple con todos los criterios de seguridad, False en caso contrario.

    Examples:
        Ejemplos de contraseñas y su validez:
        >>> validate_password("Password123!")
        True

        >>> validate_password("short")
        False  # Demasiado corta

        >>> validate_password("No spaces")
        False  # Contiene espacios

        >>> validate_password("PASSWORD")
        False  # No tiene minúsculas

        >>> validate_password("password")
        False  # No tiene mayúsculas

        >>> validate_password("Password")
        False  # No tiene dígitos

        >>> validate_password("Password12")
        False  # No tiene caracteres no alfanuméricos
    """
    if len(password) < 8:
        return False
    if " " in password:
        return False

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return has_lower and has_upper and has_digit and has_special

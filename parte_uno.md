# Parte I: Módulos de Validación en Python

## Descripción General

Esta sección del proyecto corresponde a la Parte I, cuyo objetivo principal es la **familiarización con el lenguaje de programación Python** y la **creación de módulos reutilizables** para la validación de datos.  Se han desarrollado tres módulos Python que implementan la lógica de validación para nombres de usuario y contraseñas, y un módulo adicional que combina estas validaciones.

## Módulos Desarrollados

Se han creado los siguientes módulos Python, cada uno en un archivo `.py` separado:

1.  **`username_validation.py`**:  Módulo para la validación de nombres de usuario.
2.  **`password_validation.py`**: Módulo para la validación de contraseñas.
3.  **`credential_validator.py`**: Módulo que utiliza los dos módulos anteriores para validar credenciales completas (nombre de usuario y contraseña conjuntamente).

A continuación, se describe cada módulo en detalle:

### 1. `username_validation.py`

Este módulo contiene la función `validate_username(name: str)` que se encarga de validar nombres de usuario según los siguientes criterios:

*   **Longitud:** El nombre de usuario debe tener una longitud entre 6 y 12 caracteres, ambos inclusive.
*   **Alfanumérico:** El nombre de usuario debe contener únicamente caracteres alfanuméricos (letras de la 'a' a la 'z', tanto mayúsculas como minúsculas, y dígitos del '0' al '9').

**Función Principal:**

*   **`validate_username(name: str)`**:
    *   **Argumentos:**
        *   `name` (str): El nombre de usuario a validar.
    *   **Retorno:** Un `tuple` que contiene dos elementos:
        *   El primer elemento es un `int` que representa un código de estado:
            *   `0`:  Nombre de usuario válido.
            *   `1`:  Nombre de usuario demasiado corto (menos de 6 caracteres).
            *   `2`:  Nombre de usuario demasiado largo (más de 12 caracteres).
            *   `3`:  Nombre de usuario contiene caracteres no alfanuméricos.
        *   El segundo elemento es un `str` que contiene un mensaje descriptivo del resultado de la validación.

**Ejemplo de Uso (interno al módulo, en el bloque `if __name__ == "__main__":`)**:

```python
# ... (código de username_validation.py) ...

if __name__ == "__main__":
    # Ejemplos de validación de nombres de usuario
    nombres_usuario_prueba = {
        "UsuarioValido1": "Válido",
        "User": "Demasiado corto",
        "UsuarioDemasiadoLargo": "Demasiado largo",
        "Usuario-Invalido": "Caracteres no alfanuméricos",
        "Usuario Válido": "Caracteres no alfanuméricos",
        "": "Demasiado corto"
    }

    for nombre, esperado in nombres_usuario_prueba.items():
        resultado, mensaje = validate_username(nombre)
        print(f"Nombre de usuario: '{nombre}' - Resultado: {mensaje} (Código: {resultado})")

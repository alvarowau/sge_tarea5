# Informe sobre el Módulo de Validación de Credenciales en Python

Se ha desarrollado un conjunto de módulos en Python para la validación de nombres de usuario y contraseñas, cumpliendo con los requisitos de seguridad especificados. Estos módulos permiten verificar la validez de credenciales ingresadas por un usuario, asegurando que cumplan con criterios predefinidos.

## 1. Módulo de validación de nombres de usuario

Se ha implementado el módulo `username_validation.py`, el cual verifica si un nombre de usuario cumple con los siguientes requisitos:

-   Debe tener una longitud mínima de 6 caracteres y máxima de 12.
-   Solo puede contener caracteres alfanuméricos (letras y números).
-   Retorna un código de estado y un mensaje descriptivo:
    -   `0`: Nombre de usuario válido ("El nombre de usuario es válido").
    -   `1`: Nombre de usuario demasiado corto ("El nombre de usuario debe contener al menos 6 caracteres").
    -   `2`: Nombre de usuario demasiado largo ("El nombre de usuario no puede contener más de 12 caracteres").
    -   `3`: Nombre de usuario con caracteres inválidos ("El nombre de usuario puede contener solo letras y números").

## 2. Módulo de validación de contraseñas

El módulo `password_validation.py` se encarga de verificar si una contraseña cumple con los criterios de seguridad establecidos:

-   Debe contener al menos 8 caracteres.
-   Debe incluir al menos una letra minúscula, una letra mayúscula, un número y un carácter no alfanumérico (por ejemplo, `!`, `@`, `#`, etc.).
-   No puede contener espacios en blanco.
-   Retorna `True` si la contraseña es válida y `False` en caso contrario.

## 3. Módulo de validación de credenciales

El módulo `credential_validator.py` integra los dos módulos anteriores y permite validar un nombre de usuario y una contraseña de manera conjunta. Su funcionamiento es el siguiente:

-   Importa los módulos `username_validation` y `password_validation`.
-   Evalúa el nombre de usuario con `validate_username`, obteniendo un código de estado y un mensaje descriptivo.
-   Evalúa la contraseña con `validate_password`, retornando `True` si es válida y `False` si no lo es.
-   Devuelve un diccionario con los resultados de ambas validaciones, proporcionando mensajes de error cuando corresponda.

Este conjunto de módulos proporciona una solución robusta para la validación de credenciales en aplicaciones que requieran asegurar la calidad de los nombres de usuario y contraseñas ingresadas por los usuarios.

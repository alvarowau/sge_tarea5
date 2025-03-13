# Proyecto de Validación de Credenciales y Manipulación de Datos

## Descripción del Proyecto

Este proyecto práctico se divide en tres partes principales, diseñadas para explorar y aplicar conceptos de programación en Python, desde la validación de datos hasta la integración con el sistema Odoo 17.0.

**Parte I: Fundamentos de Python y Validación de Datos**

La primera parte se centra en la familiarización con el lenguaje de programación Python y la creación de módulos reutilizables. Se utilizará tanto el paradigma de programación imperativa como la Programación Orientada a Objetos (POO) para desarrollar programas modulares y robustos.

**Parte II: Aplicación Python de Manipulación de Datos**

En la segunda parte, se aprovecharán los módulos desarrollados en la Parte I para construir una aplicación Python que permita la manipulación y búsqueda de datos en una tabla construida con diccionarios. Se incluirá la persistencia de datos mediante ficheros CSV.

**Parte III: Integración con Odoo 17.0**

La parte final del proyecto consiste en integrar la aplicación o módulos creados en las partes anteriores dentro del entorno de Odoo 17.0, transformándolos en módulos funcionales dentro de este sistema ERP.

## Partes del Proyecto y Actividades

### Parte I: Módulos de Validación en Python

**Objetivo:** Familiarizarse con Python y crear módulos de validación reutilizables.

1.  **Módulo de Validación de Nombres de Usuario:**
    *   **Descripción:** Desarrollar un módulo Python que valide nombres de usuario según las siguientes reglas:
        *   Longitud mínima de 6 caracteres y máxima de 12.
        *   Debe ser alfanumérico (letras y números).
    *   **Retorno:**
        *   En caso de nombre de usuario válido, retornar `0` o el mensaje "El nombre de usuario es válido".
        *   Para nombres de usuario inválidos, retornar un código de error numérico y un mensaje descriptivo:
            *   `1`:  "El nombre de usuario debe contener al menos 6 caracteres" (si es demasiado corto).
            *   `2`:  "El nombre de usuario no puede contener más de 12 caracteres" (si es demasiado largo).
            *   `3`:  "El nombre de usuario puede contener solo letras y números" (si contiene caracteres no alfanuméricos).

2.  **Módulo de Validación de Contraseñas:**
    *   **Descripción:** Crear un módulo Python para validar contraseñas que cumplan los siguientes criterios de seguridad:
        *   Longitud mínima de 8 caracteres.
        *   Debe contener letras minúsculas, mayúsculas, números y al menos un carácter no alfanumérico.
        *   No debe contener espacios en blanco.
    *   **Retorno:**
        *   Para contraseñas válidas según los criterios, retornar `True`.
        *   Para contraseñas inválidas, retornar `False`.

3.  **Módulo de Validación de Credenciales:**
    *   **Descripción:**  Desarrollar un módulo Python que integre y utilice los módulos creados en las actividades 1 y 2. Este módulo debe:
        *   Solicitar un nombre de usuario y una contraseña.
        *   Utilizar el módulo de validación de nombres de usuario (Actividad 1) para validar el nombre de usuario.
        *   Utilizar el módulo de validación de contraseñas (Actividad 2) para validar la contraseña.
        *   Gestionar y mostrar los resultados de ambas validaciones.

### Parte II: Aplicación Python de Tabla de Datos y Búsqueda

**Objetivo:** Crear una aplicación Python para la manipulación de datos en una tabla utilizando diccionarios y ficheros CSV.

4.  **Módulo de Gestión de Tabla de Datos:**
    *   **Descripción:** Desarrollar un módulo Python que construya y gestione una tabla de datos utilizando diccionarios. La aplicación debe presentar un menú interactivo con las siguientes opciones:
        *   **Solicitar datos:** Permitir al usuario introducir datos para almacenar en la tabla (ej. apellidos, nombre, fecha de nacimiento, dirección, contraseña, etc.).
        *   **Buscar datos:** Permitir la búsqueda de datos en la tabla por nombre o apellido introducido por el usuario, mostrando los resultados en pantalla.
        *   **Exportar a CSV:**  Añadir todos los datos de la tabla a un fichero CSV.
        *   **Importar desde CSV:**  Permitir recuperar datos desde un fichero CSV (con un formato predefinido) para completar o cargar datos en la tabla.

### Parte III: Módulos Odoo para Stock y Clientes/Proveedores

**Objetivo:** Integrar funcionalidades Python en Odoo 17.0 como módulos.

5.  **Módulo Odoo de Stock:**
    *   **Descripción:** Desarrollar un módulo Odoo que permita interactuar con la tabla de productos de Odoo y generar información de stock. La funcionalidad debe incluir:
        *   **Listado de productos:** Acceder a la tabla de productos de Odoo y mostrar un listado al usuario.
        *   **Información de producto:** Permitir al usuario seleccionar un producto del listado para obtener y mostrar información detallada: código de producto, descripción y stock actual.
        *   **Exportar Stock a CSV:** Generar un fichero CSV que contenga el stock de todos los productos. El fichero debe incluir como mínimo el código, la descripción y el stock actual de cada producto, ordenados por descripción.

6.  **Módulo Odoo de Clientes/Proveedores:**
    *   **Descripción:** Desarrollar un módulo Odoo que permita importar y gestionar datos de clientes y/o proveedores desde un fichero CSV. La funcionalidad debe incluir:
        *   **Importar Clientes desde CSV:**  Leer datos de clientes desde un fichero CSV con los siguientes campos: Nombre del cliente, Nombre a mostrar, Dirección, Teléfono, e-mail, Página web, Población, Código Postal, Tipo (Proveedor 'P', Cliente 'C', Ambos 'T').
        *   **Actualización de Clientes Existentes:**  Antes de añadir un cliente, comprobar si ya existe en la base de datos de Odoo (comparando por Nombre del cliente). Si existe, modificar el registro existente con los datos del fichero CSV.
        *   **Generación de Login de Usuario:** Crear un login para cada cliente/proveedor utilizando la primera letra del nombre y el primer apellido en minúsculas. Validar el login generado utilizando el módulo de validación de nombres de usuario de la Actividad 1.
        *   **Generación y Validación de Contraseña:** Generar una contraseña compleja para cada usuario siguiendo las reglas especificadas (mezcla de nombre, apellidos, hora actual, símbolos aleatorios). Validar la contraseña generada utilizando el módulo de validación de contraseñas de la Actividad 2.
        *   **Almacenamiento en Odoo:** Almacenar el login y la contraseña generados en la tabla correspondiente de Odoo.
        *   **Informe de Modificaciones:**  Informar al usuario al finalizar el proceso, indicando si se han realizado modificaciones, cuántos registros se han añadido y cuántos se han modificado.
        *   **Categorías de Contacto:** Considerar el campo 'Tipo' del CSV para asignar categorías de contacto en Odoo (Proveedor, Cliente, Ambos). En caso de no existir las categorías, se deben crear previamente en Odoo.

## Paradigmas de Programación

*   **Paradigma Imperativo (estructurado, procedimental, modular):** Se utilizará para la organización y flujo general de los programas.
*   **Paradigma de Programación Orientada a Objetos (POO):** Se empleará para modelar los datos y las funcionalidades, utilizando clases y objetos, y gestionando excepciones para un código más robusto y mantenible.

## Tecnologías Utilizadas

*   **Lenguaje de Programación:** Python
*   **Sistema ERP:** Odoo 17.0 (para la Parte III)
*   **Módulos Python:** `re` (para expresiones regulares), `csv` (para manipulación de ficheros CSV), `random` (para generación aleatoria de contraseñas) y otros módulos estándar de Python que puedan ser necesarios.

## Cómo Utilizar/Ejecutar

Para ejecutar los módulos Python de las Partes I y II:

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Guarda los ficheros `.py` de cada módulo en el mismo directorio.
3.  Puedes ejecutar cada módulo individualmente desde la línea de comandos utilizando `python nombre_del_modulo.py`.

Para la Parte III (módulos Odoo):

1.  Asegúrate de tener instalado Odoo 17.0 y un entorno de desarrollo configurado.
2.  Coloca los módulos Odoo desarrollados dentro de la carpeta de addons de tu instalación de Odoo.
3.  Activa el modo desarrollador en Odoo.
4.  Actualiza la lista de módulos y busca e instala los módulos creados (Módulo Stock, Módulo Clientes/Proveedores).

## Autor

Álvaro Wau

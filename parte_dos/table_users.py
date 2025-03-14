import csv
import os

from parte_uno.credential_validator import validate_credentials


class UserDataTable:
    """Clase para gestionar una tabla de datos de usuarios.

    Esta clase permite solicitar, validar, buscar, almacenar y recuperar datos de usuarios
    en un archivo CSV. Además, proporciona un menú interactivo para realizar estas operaciones.

    Atributos:
        password_requirements (str): Requisitos para la contraseña del usuario.
        username_requirements (str): Requisitos para el nombre de usuario.
        data_table (list): Lista que almacena los datos de los usuarios.
    """

    password_requirements = """
- Tener una longitud mínima de 8 caracteres.
- No contener espacios en blanco.
- Incluir al menos una letra minúscula.
- Incluir al menos una letra mayúscula.
- Incluir al menos un dígito (número).
- Incluir al menos un carácter no alfanumérico (símbolos como !, @, #, $, %, etc."""
    username_requirements = """
- Tener una longitud mínima de 6 caracteres.
- Tener una longitud máxima de 12 caracteres.
- Contener únicamente caracteres alfanuméricos (letras y números)
"""

    def __init__(self):
        """Inicializa la clase con una lista vacía para almacenar datos."""
        self.data_table = []

    def request_person_data(self):
        """Solicita y valida los datos de una persona.

        Solicita al usuario que ingrese datos personales, como nombre, apellidos, fecha de nacimiento,
        dirección, nombre de usuario y contraseña. Valida las credenciales y, si son válidas, añade
        los datos a la tabla.
        """
        person_data = {}
        print("\nIntroduce los datos de la persona:")
        person_data["apellidos"] = input("Apellidos: ")
        person_data["nombre"] = input("Nombre: ")
        person_data["fecha_nacimiento"] = input("Fecha de Nacimiento: ")
        person_data["direccion"] = input("Dirección: ")
        person_data["username"] = input(
            f"Nombre de usuario ({self.username_requirements}): "
        )
        person_data["contraseña"] = input(
            f"Contraseña ({self.password_requirements}): "
        )
        response = self.check_data(
            person_data["username"],
            person_data["contraseña"],
        )
        if response[0]:
            self.data_table.append(person_data)
            print("Datos de persona añadidos correctamente.")
        else:
            print(f"El usuario no ha podido ser creado, motivo {response[1]}")
            person_data = {}

    def check_data(self, username: str, password: str):
        """Valida las credenciales del usuario.

        Args:
            username (str): Nombre de usuario a validar.
            password (str): Contraseña a validar.

        Returns:
            tuple: Una tupla con un booleano que indica si las credenciales son válidas y un mensaje de error (si aplica).
        """
        response = validate_credentials(username, password)
        if response["username_valid"]:
            if response["password_valid"]:
                return True, ""
            else:
                return False, response["password_message"]
        else:
            return False, response["username_message"]

    def find_person(self):
        """Busca una persona por nombre, apellido o nombre de usuario.

        Solicita un término de búsqueda y muestra los resultados coincidentes.
        """
        search_term = input(
            "Introduce nombre de usuario, nombre o apellido a buscar: "
        ).lower()
        results = []
        for person in self.data_table:
            if (
                search_term in person["nombre"].lower()
                or search_term in person["apellidos"].lower()
                or search_term in person["username"].lower()
            ):
                results.append(person)

        if results:
            print("\nResultados de la búsqueda:")
            for person in results:
                self.show_person_data(person)
        else:
            print("No se encontraron coincidencias.")

    def show_person_data(self, person):
        """Muestra los datos de una persona.

        Args:
            person (dict): Diccionario con los datos de la persona.
        """
        print("-" * 30)
        print(f"Nombre de usuario: {person['username']}")
        print(f"Nombre: {person['nombre']}")
        print(f"Apellidos: {person['apellidos']}")
        print(f"Fecha de Nacimiento: {person['fecha_nacimiento']}")
        print(f"Dirección: {person['direccion']}")
        print(f"Contraseña: {person['contraseña']} (¡No mostrar en sistemas reales!)")
        print("-" * 30)

    def add_to_csv(self, filename="tabla_datos_usuarios.csv"):
        """Guarda los datos en un archivo CSV.

        Args:
            filename (str): Nombre del archivo CSV donde se guardarán los datos.
        """
        try:
            with open(filename, "w", newline="", encoding="utf-8") as csv_file:
                column_names = [
                    "username",
                    "apellidos",
                    "nombre",
                    "fecha_nacimiento",
                    "direccion",
                    "contraseña",
                ]
                csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)
                csv_writer.writeheader()
                csv_writer.writerows(self.data_table)
                print(f"Tabla de datos guardada en '{filename}' correctamente.")
        except Exception as e:
            print(f"Error al guardar en CSV: {e}")

    def recover_from_csv(self, filename="tabla_datos_usuarios.csv"):
        """Recupera los datos desde un archivo CSV.

        Args:
            filename (str): Nombre del archivo CSV desde donde se recuperarán los datos.
        """
        try:
            if not os.path.exists(filename):
                print(
                    f"El fichero CSV '{filename}' no existe. Se creará uno nuevo al guardar."
                )
                self.data_table = []
                return

            self.data_table = []
            with open(filename, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.data_table.append(dict(row))
            print(f"Datos recuperados de '{filename}' correctamente.")
        except Exception as e:
            print(f"Error al recuperar datos desde CSV: {e}")

    def show_menu(self):
        """Muestra el menú de opciones."""
        print("\n--- Menú Tabla de Datos ---")
        print("1. Solicitar datos de persona")
        print("2. Buscar persona")
        print("3. Añadir tabla a CSV")
        print("4. Recuperar tabla desde CSV")
        print("5. Mostrar tabla completa (¡Solo para pruebas!)")
        print("6. Salir del menú Tabla de Datos")

    def execute_menu(self):
        """Ejecuta el menú interactivo."""
        option = ""
        self.recover_from_csv()
        while option != "6":
            self.show_menu()
            option = input("Selecciona una opción: ")
            if option == "1":
                self.request_person_data()
            elif option == "2":
                self.find_person()
            elif option == "3":
                self.add_to_csv()
            elif option == "4":
                self.recover_from_csv()
            elif option == "5":
                print("\n--- Tabla de Datos Completa (¡Solo para pruebas!) ---")
                if self.data_table:
                    for person in self.data_table:
                        self.show_person_data(person)
                else:
                    print("La tabla está vacía.")
            elif option == "6":
                print("Saliendo del menú Tabla de Datos...")
            else:
                print("Opción no válida. Inténtalo de nuevo.")


def main_activity4():
    """Función principal para ejecutar la actividad 4."""
    my_table = UserDataTable()
    my_table.execute_menu()




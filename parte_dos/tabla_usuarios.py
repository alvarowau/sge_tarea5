import csv
import os  # Para comprobar si existe el fichero CSV


class TablaDatosUsuario:
    def __init__(self):
        """Inicializa la tabla de datos como un diccionario vacío."""
        self.tabla_datos = []  # Usaremos una lista de diccionarios para la tabla

    def solicitar_datos_persona(self):
        """Solicita al usuario los datos de una persona y los guarda en la tabla."""
        datos_persona = {}
        print("\nIntroduce los datos de la persona:")
        datos_persona["apellidos"] = input("Apellidos: ")
        datos_persona["nombre"] = input("Nombre: ")
        datos_persona["fecha_nacimiento"] = input("Fecha de Nacimiento: ")
        datos_persona["direccion"] = input("Dirección: ")
        datos_persona["contraseña"] = input(
            "Contraseña (¡Precaución!): "
        )  # Advertencia sobre seguridad
        self.tabla_datos.append(datos_persona)
        print("Datos de persona añadidos correctamente.")

    def buscar_persona(self):
        """Permite buscar personas por nombre o apellido y muestra los resultados."""
        termino_busqueda = input("Introduce nombre o apellido a buscar: ").lower()
        resultados = []
        for persona in self.tabla_datos:
            if (
                termino_busqueda in persona["nombre"].lower()
                or termino_busqueda in persona["apellidos"].lower()
            ):
                resultados.append(persona)

        if resultados:
            print("\nResultados de la búsqueda:")
            for persona in resultados:
                self.mostrar_datos_persona(
                    persona
                )  # Llama a un método para formatear la salida
        else:
            print("No se encontraron coincidencias.")

    def mostrar_datos_persona(self, persona):
        """Muestra los datos de una persona de forma formateada."""
        print("-" * 30)
        print(f"Nombre: {persona['nombre']}")
        print(f"Apellidos: {persona['apellidos']}")
        print(f"Fecha de Nacimiento: {persona['fecha_nacimiento']}")
        print(f"Dirección: {persona['direccion']}")
        print(
            f"Contraseña: {persona['contraseña']} (¡No mostrar en sistemas reales!)"
        )  # Advertencia
        print("-" * 30)

    def añadir_a_csv(self, nombre_fichero="tabla_datos_usuarios.csv"):
        """Guarda los datos de la tabla en un fichero CSV."""
        try:
            with open(nombre_fichero, "w", newline="", encoding="utf-8") as fichero_csv:
                nombres_columnas = [
                    "apellidos",
                    "nombre",
                    "fecha_nacimiento",
                    "direccion",
                    "contraseña",
                ]
                escritor_csv = csv.DictWriter(fichero_csv, fieldnames=nombres_columnas)
                escritor_csv.writeheader()
                escritor_csv.writerows(self.tabla_datos)
            print(f"Tabla de datos guardada en '{nombre_fichero}' correctamente.")
        except Exception as e:
            print(f"Error al guardar en CSV: {e}")

    def recuperar_de_csv(self, nombre_fichero="tabla_datos_usuarios.csv"):
        """Carga datos desde un fichero CSV para completar la tabla."""
        try:
            if not os.path.exists(nombre_fichero):
                print(
                    f"El fichero CSV '{nombre_fichero}' no existe. Se creará uno nuevo al guardar."
                )
                self.tabla_datos = []  # Inicializar tabla vacía si no existe CSV
                return

            self.tabla_datos = []  # Limpiar la tabla antes de cargar
            with open(nombre_fichero, "r", newline="", encoding="utf-8") as fichero_csv:
                lector_csv = csv.DictReader(fichero_csv)
                for fila in lector_csv:
                    self.tabla_datos.append(
                        dict(fila)
                    )  # Añadir cada fila como diccionario
            print(f"Datos recuperados de '{nombre_fichero}' correctamente.")
        except Exception as e:
            print(f"Error al recuperar datos desde CSV: {e}")

    def mostrar_menu(self):
        """Muestra el menú de opciones para la tabla de datos."""
        print("\n--- Menú Tabla de Datos ---")
        print("1. Solicitar datos de persona")
        print("2. Buscar persona")
        print("3. Añadir tabla a CSV")
        print("4. Recuperar tabla desde CSV")
        print(
            "5. Mostrar tabla completa (¡Solo para pruebas!)"
        )  # Opción extra para ver la tabla
        print("6. Salir del menú Tabla de Datos")

    def ejecutar_menu(self):
        """Ejecuta el bucle principal del menú."""
        opcion = ""
        self.recuperar_de_csv()  # Cargar datos CSV al inicio, si existe
        while opcion != "6":
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.solicitar_datos_persona()
            elif opcion == "2":
                self.buscar_persona()
            elif opcion == "3":
                self.añadir_a_csv()
            elif opcion == "4":
                self.recuperar_de_csv()
            elif (
                opcion == "5"
            ):  # Opción extra para mostrar la tabla (solo para desarrollo)
                print("\n--- Tabla de Datos Completa (¡Solo para pruebas!) ---")
                if self.tabla_datos:
                    for persona in self.tabla_datos:
                        self.mostrar_datos_persona(persona)
                else:
                    print("La tabla está vacía.")
            elif opcion == "6":
                print("Saliendo del menú Tabla de Datos...")
            else:
                print("Opción no válida. Inténtalo de nuevo.")


def main_actividad4():
    """Función principal para ejecutar el módulo de la tabla de datos."""
    mi_tabla = TablaDatosUsuario()
    mi_tabla.ejecutar_menu()


if __name__ == "__main__":
    main_actividad4()

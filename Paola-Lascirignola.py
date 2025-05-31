import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre


class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{self.nombre}.txt"

    def agregar(self, pelicula):
        with open(self.ruta_archivo, "a") as archivo:
            archivo.write(pelicula.get_nombre() + "\n")
        print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print("El catálogo no existe.")
            return
        with open(self.ruta_archivo, "r") as archivo:
            peliculas = archivo.readlines()
            if not peliculas:
                print("El catálogo está vacío.")
            else:
                print("\n--- Lista de Películas ---")
                for contador, nombre in enumerate(peliculas, start=1):
                    print(f"{contador}. {nombre.strip()}")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.ruta_archivo}' eliminado correctamente.")
        else:
            print("El catálogo no existe o ya fue eliminado.")


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar catálogo")
    print("4. Salir")


def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas (sin .txt): ")
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)
        elif opcion == "2":
            catalogo.listar()
        elif opcion == "3":
            catalogo.eliminar()
        elif opcion == "4":
            print("Gracias por usar el catálogo de películas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

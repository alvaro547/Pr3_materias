print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos una lista con las materias del curso
materias = [
    "Pensamiento matemático",
    "Español",
    "Inglés",
    "Química",
    "Civismo",
    "Francés"
]

# Función para mostrar el mensaje de las materias cursadas
def mostrar_materias_cursadas(lista_materias):
    for materia in lista_materias:
        print(f"Estoy cursando {materia}.")

# Llamamos a la función para mostrar el mensaje
mostrar_materias_cursadas(materias)

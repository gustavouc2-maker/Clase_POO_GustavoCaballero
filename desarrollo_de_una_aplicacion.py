
# Clase para representar a un estudiante
class Estudiante:

    # Constructor: inicializa los atributos
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []

    # Método para agregar una calificación
    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)

    # Método para calcular el promedio
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)



# Prueba del programa
if __name__ == "__main__":

    # Crear un estudiante
    alumno1 = Estudiante("Carlos", "2026001")

    # Agregar calificaciones
    alumno1.agregar_calificacion(90)
    alumno1.agregar_calificacion(80)

    # Mostrar resultados
    print("Nombre:", alumno1.nombre)
    print("Matrícula:", alumno1.matricula)
    print("Promedio:", alumno1.calcular_promedio())

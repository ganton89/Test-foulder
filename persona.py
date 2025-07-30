class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hi! Im a person named", self.nombre, "and I am", self.edad, "years old.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, id_estudiante):
            super().__init__(nombre, edad)
            self.id_estudiante = id_estudiante
    
    def saludar(self):
        super().saludar()
        print(f"I am a student with ID:", self.id_estudiante)

student = Estudiante("Gema", 29, "12345")
student.saludar()

personita = Persona("Ismael", 32)
personita.saludar()



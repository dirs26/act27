#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro


class Alumno:
    def __init__(self,id, nombre, email):
        self.id=id
        self.nombre=nombre
        self.email=email
    def ficha(self):
        print(f'Alumno {self.id}, con nombre: {self.nombre} y correo electrónico de contacto: {self.email}')
alumn1=Alumno(1,'Sophia','sopm@gmail.com')
alumn2=Alumno(2,'Diego','dirs26@gmail.com')

alumn1.ficha()
alumn2.ficha()

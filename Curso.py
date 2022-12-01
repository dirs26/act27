#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro

class Curso:
    def __init__(self,id,nombre, creditos, anosDeEstudio):
        self.id=id
        self.nombre=nombre
        self.creditos=creditos
        self.anosDeEstudio=anosDeEstudio
    def ficha(self):
        print(f'{self.nombre} tiene {self.creditos} creditos, y dura un tiempo de {self.anosDeEstudio} años.')

curso1=Curso(1,'Ingeniería Mecánica',240,4)
curso2=Curso(2,'Empresa y Tecnología',240,4)
curso3=Curso(3,'Turismo',240,4)

curso1.ficha()
curso2.ficha()
curso3.ficha()
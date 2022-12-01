#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrícula
#reto*:método que muestra las matriculas realizadas en mi centro
from Curso import Curso
from Alumno import Alumno

class Matricula:
    def __init__(self,idmatricula, fechamatricula, idalumno, idcurso):
        self.idmatricula=idmatricula
        self.fechamatricula=fechamatricula
        self.idalumno=idalumno
        self.idcurso=idcurso
    def datosMatricula(self):
        print(f'El alumno {self.idalumno},cursante de {self.idcurso}, se matriculó el día {self.fechamatricula} y tiene la matricula número: {self.idmatricula}')

alumn39=Alumno(39,'kevin','yubcbe@gmail.com')
alumn40=Alumno(40,'Juan Alberto','illojuan420@gmail.com')

curso1=Curso(1,'Ingeniería Mecánica',240,4)
curso2=Curso(2,'Empresa y Tecnología',240,4)
curso3=Curso(3,'Turismo',240,4)

matricula1=Matricula(1,'10/03/2022',alumn39.nombre,curso1.nombre)
matricula2=Matricula(2,'09/06/2022',alumn40.nombre,curso3.nombre)
matricula3=Matricula(3,'10/09/2026',alumn40.nombre,curso2.nombre)

matricula1.datosMatricula()
matricula2.datosMatricula()
matricula3.datosMatricula()

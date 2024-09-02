import mysql.connector
class backend:

    def __init__(self,db):
        self.db=db
        self.base=db.getBase()
        self.cursor=db.getCursor()
    
    def agregarAlumno(self,alumno):
        self.cursor.execute("insert into alumno(nombre,apellido) values(%s,%s)",(alumno.nombre,alumno.apellido))
        self.base.commit()

    def agregarCurso(self,curso):
        self.cursor.execute("insert into curso(tipo_materia,cant_alumnos) values(%s,%s)",(curso.materia,curso.cant_alumnos))
        self.base.commit()

    def agregarNota(self,nota1,nota2,notaFinal,id_alumno,id_curso):
        self.cursor.execute("insert into calificaciones(nota1,nota2,final,id_alumno,id_curso) values(%s,%s,%s,%s,%s)",(nota1,nota2,notaFinal,id_alumno,id_curso))
        self.base.commit()
    
    def reemplazarNomOApe(self,id,columna,alumno,nuevo):
        query=f"UPDATE alumno set {columna}=%s where id=%s"
        self.cursor.execute(query,(nuevo,id)) 
        self.base.commit()
        if(columna=="apellido"):
            alumno.apellido=nuevo
        elif (columna=="nombre"):
            alumno.nombre=nuevo

    def reemplazarNota(self,id_nota,tipo_de_nota,nueva_nota):
        query=f"update curso set {tipo_de_nota}=%s where id=%s"
        self.cursor.execute(query,(nueva_nota,id_nota))
        self.base.commit()

    def eliminarAlumno(self,id_alumno):
        self.cursor.execute("DELETE from calificaciones where id_alumno=%s",(id_alumno,))
        self.cursor.execute("DELETE from alumno where id=%s",(id_alumno,))
        self.base.commit()
    
    def eliminarCurso(self,id_curso):
        self.cursor.execute("DELETE from calificaciones where id_curso=%s",(id_curso,))    
        self.cursor.execute("DELETE from curso where id_curso=%s",(id_curso,))
        self.base.commit()

    def eliminarNota(self,id):
        self.cursor.execute("delete from calificaciones where id=%s",(id,))
        self.base.commit()
    
    def devolverAlumno(self,nombre,apellido=" "):
        if apellido!=" ":
            self.cursor.execute("select * from alumno where nombre=%s and apellido=%s",(nombre,apellido))
        else: 
            self.cursor.execute("select * from alumno where nombre=%s",(nombre,))
        
        resultado= self.cursor.fetchone()
        return resultado

    def devolverAlumnoId(self,id):
        self.cursor.execute("select nombre , apellido from alumno where id=%s",(id,))
        resultado= self.cursor.fetchone()
        return resultado


    def devolverNotasCurso(self,id_curso):
        self.cursor.execute("select * from calificaciones where id_curso=%s",(id_curso,))
        resultados=self.cursor.fetchall()
        return resultados
    
    def devolverNotasAlumno(self,id_alumno,curso=" "):
        datos=None
        if curso!=" ":
            query="select * from calificaciones where id_alumno=%s and id_curso=%s"
            self.cursor.execute(query,(id_alumno,curso,))
            datos=self.cursor.fetchone()
        elif curso==" ":
            query="select * from calificaciones where id_alumno=%s"
            self.cursor.execute(query,(id_alumno,))
            datos=self.cursor.fetchall()
        
        return list(datos)
    def devolverAlumnos(self):
        self.cursor.execute("select * from alumno")
        resultados=self.cursor.fetchall()
        return resultados
    
    def devolverCursos(self):
        self.cursor.execute("select * from curso")
        cursos=self.cursor.fetchall()
        return cursos
    
    def idAlumno(self):
        self.cursor.execute("select COUNT(id) from alumno")
        resultado=list(self.cursor.fetchone())
        return resultado[0] if resultado else 0

    def idCurso(self):
        self.cursor.execute("select COUNT(id_curso) from curso")
        resultado=list(self.cursor.fetchone())
        return resultado[0] if resultado else 0
    
    def idnotas(self):
        self.cursor.execute("select COUNT(id) from calificaciones")
        resultado=list(self.cursor.fetchone())
        return resultado[0] if resultado else 0
    
    def cerrar(self):
        self.db.cerrar()
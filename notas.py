import customtkinter as ctk
class notas:

    def __init__(self,id,nota1,nota2,final,id_alumno,id_curso,scrollbar=" ",nombre=" "):
        self.id=id
        self.nota1=nota1
        self.nota2=nota2
        self.final=final
        self.id_alumno=id_alumno
        self.id_curso=id_curso
        if scrollbar!=" ":
            self.scrollbar=scrollbar
        if nombre!=" ":
            self.nombre=nombre[0]
            self.apellido=nombre[1]
    
    
    def boton(self):
        return ctk.CTkButton(self.scrollbar,text=f"1*:{self.nota1} 2*:{self.nota2} F*:{self.final} nombre:{self.nombre} {self.apellido}  ",height=100,width=450)
        
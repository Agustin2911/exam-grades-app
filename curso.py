import customtkinter as ctk

class curso:

    def __init__(self,id,asignatura, cant,scrollbar=" "):
        self.id_materia=id
        self.materia=asignatura
        self.cant_alumnos=cant
        if scrollbar!=" ":
            self.scrollbar=scrollbar

    
    

    def boton(self):
        return ctk.CTkButton(self.scrollbar,text=f"{self.id_materia} {self.materia} {self.cant_alumnos}",height=100,width=100)

    def  __str__(self):
        return f"{self.id_materia} {self.materia}"
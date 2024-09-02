import customtkinter as ctk
class alumno:


    def __init__(self,id,nombre,apellido,scrollbar=" "):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        if scrollbar!=" ":
            self.scrollbar=scrollbar
        

    
    def boton(self):
        return ctk.CTkButton(self.scrollbar,text=f"{self.id} {self.nombre} {self.apellido}",height=100,width=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
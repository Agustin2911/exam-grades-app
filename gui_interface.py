import customtkinter as ctk
from curso import *
from alumno import *
from notas import *
class gui:
    
    def __init__(self,back) :
        self.back=back
        self.ventana=ctk.CTk()
        self.ventana.geometry("800x600")
        self.ventana.resizable(False,False)
        self.ventana.pack_propagate(False)
        frame1=ctk.CTkFrame(self.ventana,height=100,width=800)
        frame1.pack_propagate(False)
        frame1.grid(row=0,column=0)
        titulo_principal=ctk.CTkLabel(frame1,text="Sistemas de notas",anchor="center",justify="center",height=100,width=800,font=("Arial", 16))
        titulo_principal.pack_propagate(False)
        titulo_principal.grid(row=0,column=0)
        frame2=ctk.CTkFrame(self.ventana,height=500,width=800)
        frame2.grid(row=1,column=0)
        frame2.pack_propagate(False)
        boton_gestionar_nota=ctk.CTkButton(frame2,text="gestionar notas", height=100,width=400,command=lambda:self.ventana_gestionar_notas())
        boton_gestionar_nota.grid(row=0,column=0,pady=(50,0))
        boton_gestionar_alumnos=ctk.CTkButton(frame2,text="gestionar alumnos",height=100,width=400,command=lambda:self.ventana_gestionar_alumnos())
        boton_gestionar_alumnos.grid(row=1,column=0,pady=(20,0))
        boton_gestionar_cursos=ctk.CTkButton(frame2,text="gestionar cursos",height=100,width=400,command= lambda: self.ventana_gestionar_cursos())
        boton_gestionar_cursos.grid(row=2,column=0,pady=(20,0))
        self.ventana.mainloop()

    #getion de notas 
    def ventana_gestionar_notas(self):
        ventana_hija=ctk.CTkToplevel(self.ventana,height=600,width=600)
        ventana_hija.transient(self.ventana)
        ventana_hija.grab_set()
        ventana_hija.pack_propagate(False)
        frame_central=ctk.CTkFrame(ventana_hija,height=600,width=600)
        frame_central.pack_propagate(False)
        frame_central.grid(row=0,column=1)
        boton_agregar=ctk.CTkButton(frame_central,text="agregar nota",height=150,width=300, command=lambda:self.ventana_agregar_notas(ventana_hija))
        boton_agregar.pack_propagate(False)
        boton_agregar.grid(row=0,padx=50,pady=20)
        boton_buscar=ctk.CTkButton(frame_central,text="buscar nota",height=150,width=300,command=lambda:self.ventana_buscar_nota(ventana_hija))
        boton_buscar.pack_propagate(False)
        boton_buscar.grid(row=2, padx=50,pady=20)
        

    def ventana_agregar_notas(self,ventana):
        ventana_hija=ctk.CTkToplevel(ventana, height=600,width=600)
        ventana_hija.grab_set()
        ventana_hija.transient(ventana)
        frame_izquierdo=ctk.CTkFrame(ventana_hija,height=600,width=300)
        frame_izquierdo.pack_propagate(False)
        frame_izquierdo.grid(row=0,column=0)
        titulo_nota_1=ctk.CTkLabel(frame_izquierdo,text="nota del primer parcial : ",height=50,width=240)
        titulo_nota_1.pack_propagate(False)
        titulo_nota_1.grid(row=0,padx=20,pady=20)
        entrada_nota_1=ctk.CTkEntry(frame_izquierdo,placeholder_text="-",height=50,width=240)
        entrada_nota_1.pack_propagate(False)
        entrada_nota_1.grid(row=1,padx=20,pady=20)
        titulo_nota_2=ctk.CTkLabel(frame_izquierdo,text="nota del segundo parcial: ",height=50,width=300)
        titulo_nota_2.pack_propagate(False)
        titulo_nota_2.grid(row=2,padx=20,pady=20)
        entrada_nota_2=ctk.CTkEntry(frame_izquierdo,placeholder_text="-",height=50,width=240)
        entrada_nota_2.pack_propagate(False)
        entrada_nota_2.grid(row=3,padx=20,pady=20)
        titulo_final=ctk.CTkLabel(frame_izquierdo,text="nota del final: ",height=50,width=300)
        titulo_final.pack_propagate(False)
        titulo_final.grid(row=4,padx=20,pady=20)
        entrada_final=ctk.CTkEntry(frame_izquierdo,placeholder_text="-",height=50,width=240)
        entrada_final.pack_propagate(False)
        entrada_final.grid(row=5,padx=20,pady=20)
        frame_derecho=ctk.CTkFrame(ventana_hija,height=600,width=300)
        frame_derecho.pack_propagate(False)
        frame_derecho.grid(row=0,column=1)
        alumno_opcion=ctk.StringVar(value="alumno")
        alumnos=self.cargar_alumnos()
        dic_alumnos={str(alumno):alumno for alumno in alumnos}
        alumnos=[str(alumno) for alumno in alumnos]
        opciones_1=ctk.CTkOptionMenu(frame_derecho,values=alumnos,variable=alumno_opcion)
        opciones_1.grid(row=0,column=0,padx=20,pady=20)
        curso_opcion=ctk.StringVar(value="curso")
        cursos=self.cargar_cursos()
        dic_cursos={str(curso):curso for curso in cursos}
        cursos=[str(curso) for curso in cursos]
        opciones_2=ctk.CTkOptionMenu(frame_derecho,values=cursos,variable=curso_opcion)
        opciones_2.grid(row=1,column=0,padx=20,pady=20)
        agregar_nota=ctk.CTkButton(frame_derecho,text="agregar nota",command=lambda:self.agregar_nota([entrada_nota_1.get(),entrada_nota_2.get(),entrada_final.get(),dic_alumnos[alumno_opcion.get()],dic_cursos[curso_opcion.get()]]))
        agregar_nota.pack_propagate(False)
        agregar_nota.grid(row=2,padx=20,pady=20)
        
    def ventana_buscar_nota(self,ventana):
        ventana_hija=ctk.CTkToplevel(ventana,height="600",width="600",fg_color="#2E2E2E")
        ventana_hija.grab_set()
        ventana_hija.transient(ventana)
        self.nota=None
        frame_arriba=ctk.CTkFrame(ventana_hija,height=200,width=600)
        frame_arriba.pack_propagate(False)
        frame_arriba.grid(row=0,column=0)
        titulo_busqueda=ctk.CTkLabel(frame_arriba,text="tipo de busqueda: ",height=50,width=260)
        titulo_busqueda.pack_propagate(False)
        titulo_busqueda.grid(row=0,column=0)
        primera_opcion_1=ctk.StringVar(value="elige el tipo de busqueda")
        opciones_1=ctk.CTkOptionMenu(frame_arriba,values=["busqueda de curso","busqueda de alumno"],variable=primera_opcion_1,height=50,width=260)
        opciones_1.grid(row=1,column=0,padx=20,pady=20)
        titulo_curso=ctk.CTkLabel(frame_arriba,text="curso: ",height=50,width=260)
        titulo_curso.pack_propagate(False)
        titulo_curso.grid(row=0,column=1,padx=20,pady=20)
        primera_opcion_2=ctk.StringVar(value="seleccione el curso buscado")
        cursos=self.cargar_cursos()
        dic_cursos={str(curso):curso for curso in cursos}
        dic_cursos["seleccione el curso buscado"]=" "
        cursos=[str(curso) for curso in cursos]
        cursos.append("seleccione el curso buscado")
        opciones_2=ctk.CTkOptionMenu(frame_arriba,values=cursos,variable=primera_opcion_2,height=50,width=260)
        opciones_2.grid(row=1,column=1,padx=20,pady=20)
        titulo_alumno=ctk.CTkLabel(frame_arriba,text="alumno: ",height=50,width=260)
        titulo_alumno.grid(row=0,column=2,padx=20,pady=20)
        alumnos=self.cargar_alumnos()
        dic_alumnos={str(alumno):alumno for alumno in alumnos}
        dic_alumnos["elige el nombre del alumno"]=" "
        alumnos=[str(alumno) for alumno in alumnos]
        primero_opcion_3= ctk.StringVar(value="elige el nombre del alumno")
        opciones_3=ctk.CTkOptionMenu(frame_arriba,values=alumnos,variable=primero_opcion_3,height=50,width=260)
        opciones_3.grid(row=1,column=2,padx=20,pady=20)
        frama_de_abajo=ctk.CTkFrame(ventana_hija,height=400,width=600)
        frama_de_abajo.pack_propagate(False)
        frama_de_abajo.grid(row=1,column=0)
        datos=ctk.CTkScrollableFrame(frama_de_abajo,height=300,width=500)
        datos.grid(row=0,column=0,padx=50,pady=50)
        boton_buscar=ctk.CTkButton(frame_arriba,text="buscar",height=60,width=100,command=lambda:self.buscar(opciones_1.get(),dic_cursos[opciones_2.get()],dic_alumnos[opciones_3.get()],datos))
        boton_buscar.pack_propagate(False)
        boton_buscar.grid(row=3,column=0,padx=20,pady=20)
        boton_eliminar=ctk.CTkButton(frame_arriba,text="eliminar nota",height=60, width=100,command=lambda: self.eliminar_nota(self.nota.id,[opciones_1.get(),dic_cursos[opciones_2.get()],dic_alumnos[opciones_3.get()],datos]))
        boton_eliminar.pack_propagate(False)
        boton_eliminar.grid(row=3,column=1,padx=20,pady=20)


    def buscar(self,dato1,dato2,dato3,scrollbar):
        for widget in scrollbar.winfo_children():
            widget.destroy()

        if dato1=="busqueda de curso":
            for i in self.back.devolverNotasCurso(dato2.id_materia):
                nombre=self.back.devolverAlumnoId(i[4])
                curso_nuevo=notas(i[0],i[1],i[2],i[3],i[4],i[5],scrollbar,nombre)
                boton=curso_nuevo.boton()
                boton.configure(command=self.hacer_referencia_1(curso_nuevo))
                boton.pack(padx=20,pady=20)
        elif dato1=="busqueda de alumno":
            for i in self.back.devolverNotasAlumno(dato3.id):
                nombre=self.back.devolverAlumnoId(i[4])
                curso_nuevo=notas(i[0],i[1],i[2],i[3],i[4],i[5],scrollbar,nombre)
                boton=curso_nuevo.boton()
                boton.configure(command=self.hacer_referencia_1(curso_nuevo))
                boton.pack(padx=20,pady=20)

    def cargar_alumnos(self):        
        alumnos=[]
        for i in self.back.devolverAlumnos():
                alumnos.append(alumno(i[0],i[1],i[2]))
        return alumnos

    def cargar_cursos(self):        
        cursos=[]
        for i in self.back.devolverCursos():
                cursos.append(curso(i[0],i[1],i[2]))
        return cursos
    
    def agregar_nota(self,datos):
        self.back.agregarNota(datos[0],datos[1],datos[2],datos[3].id,datos[4].id_materia)


    def hacer_referencia_1(self,nota):
        def callback():
            self.nota=nota
        return callback

    def eliminar_nota(self,id,datos):
        self.back.eliminarNota(id)
        self.buscar(datos[0],datos[1],datos[2],datos[3])
        
    #gestionar alumnos
    def ventana_gestionar_alumnos(self):
        ventana_hija=ctk.CTkToplevel(self.ventana,height=600,width=600)
        ventana_hija.transient(self.ventana)
        ventana_hija.grab_set()
        self.alumno=None
        frame_izquierda=ctk.CTkFrame(ventana_hija,height=600,width=400)
        frame_izquierda.pack_propagate(False)
        frame_izquierda.grid(row=0,column=0)
        frame_alumnos=ctk.CTkFrame(frame_izquierda,height=600,width=400)
        frame_alumnos.pack_propagate(False)
        frame_alumnos.grid(row=0,column=0)
        alumnos=ctk.CTkScrollableFrame(frame_izquierda,height=500,width=300)
        alumnos.grid(row=0,column=0,pady=50,padx=50)
        frame_derecho=ctk.CTkFrame(ventana_hija,height=600,width=200)
        frame_derecho.pack_propagate(False)
        frame_derecho.grid(row=0,column=1)
        boton_agregar=ctk.CTkButton(frame_derecho,text="agregar alumnos",height=100,width=100,command=lambda:self.ventana_agregar_alumnos(ventana_hija,alumnos))
        boton_agregar.pack_propagate(False)
        boton_agregar.grid(row=0,padx=20,pady=20)
        boton_eliminar=ctk.CTkButton(frame_derecho,text="eliminar alumnos",height=100,width=100,command=lambda: self.eliminar_alumnos(alumnos))
        boton_eliminar.pack_propagate(False)
        boton_eliminar.grid(row=1,padx=20,pady=20)
        boton_buscar=ctk.CTkButton(frame_derecho,text="buscar alumnos",height=100,width=10, command=lambda:self.ventana_buscar_alumno(ventana_hija))
        boton_buscar.pack_propagate(False)
        boton_buscar.grid(row=2, padx=20,pady=20)
        self.agregarItems_2(alumnos)

    def ventana_agregar_alumnos(self,ventana,scrollbar):
        ventana_hija=ctk.CTkToplevel(ventana,height=600,width=400)
        ventana_hija.transient(ventana)
        ventana_hija.grab_set()
        titulo_nombre=ctk.CTkLabel(ventana_hija,text="nombre del alumno",height=50,width=300)
        titulo_nombre.pack_propagate(False)
        titulo_nombre.grid(row=0,column=0,padx=30,pady=30)
        entrada_nombre=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese el nombre del alumno:",height=50,width=300)
        entrada_nombre.pack_propagate(False)
        entrada_nombre.grid(row=1,column=0,padx=30,pady=30)
        titulo_apellido=ctk.CTkLabel(ventana_hija,text="apellido del alumno",height=50,width=300)
        titulo_apellido.pack_propagate(False)
        titulo_apellido.grid(row=2,column=0,padx=30,pady=30)
        entrada_apellido=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese el apellido del alumno:",height=50,width=300)
        entrada_apellido.pack_propagate(False)
        entrada_apellido.grid(row=3,column=0,padx=30,pady=30)
        boton_agregar_alumno=ctk.CTkButton(ventana_hija,text="agregar alumno",height=50,width=300,command=lambda:self.agregar_alumno(entrada_nombre.get(),entrada_apellido.get(),scrollbar))
        boton_agregar_alumno.pack_propagate(False)
        boton_agregar_alumno.grid(row=4,column=0,padx=30,pady=30)
        
    def ventana_buscar_alumno(self,ventana):
        ventana_hija=ctk.CTkToplevel(ventana,height=600,width=400)
        ventana_hija.transient(ventana)
        ventana_hija.grab_set()
        resultado=ctk.CTkEntry(ventana_hija,height=50,width=300)
        resultado.grid(row=5,column=0,padx=20,pady=20)
        titulo_nombre=ctk.CTkLabel(ventana_hija,text="nombre del alumno",height=50,width=300)
        titulo_nombre.pack_propagate(False)
        titulo_nombre.grid(row=0,column=0,padx=20,pady=20)
        entrada_nombre=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese el nombre del alumno:",height=50,width=300)
        entrada_nombre.pack_propagate(False)
        entrada_nombre.grid(row=1,column=0,padx=20,pady=20)
        titulo_apellido=ctk.CTkLabel(ventana_hija,text="apellido del alumno",height=50,width=300)
        titulo_apellido.pack_propagate(False)
        titulo_apellido.grid(row=2,column=0,padx=20,pady=20)
        entrada_apellido=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese el apellido del alumno:",height=50,width=300)
        entrada_apellido.pack_propagate(False)
        entrada_apellido.grid(row=3,column=0,padx=20,pady=20)
        boton_agregar_alumno=ctk.CTkButton(ventana_hija,text="buscar alumno",height=50,width=300,command=lambda:self.buscar_alumno(entrada_nombre.get(),entrada_apellido.get(),resultado))
        boton_agregar_alumno.pack_propagate(False)
        boton_agregar_alumno.grid(row=4,column=0,padx=20,pady=20)
        
    
    def buscar_alumno(self,nombre,apellido,posicion):
        resultado=self.back.devolverAlumno(nombre,apellido)
        posicion.delete(0,'end')
        posicion.insert(0,f"id: {resultado[0]}  nombre: {nombre} apellido: {apellido}")
        
    def agregar_alumno(self,nombre,apellido,scrollbar):
        id=self.back.idAlumno()
        self.back.agregarAlumno(alumno(id,nombre,apellido))
        self.agregarItems_2(scrollbar)

    def eliminar_alumnos(self,scrollbar):
        self.back.eliminarAlumno(self.alumno)
        self.agregarItems_2(scrollbar)

    #ventana gestora de cursos
    def ventana_gestionar_cursos(self):
        ventana_hija=ctk.CTkToplevel(self.ventana,height=600,width=600)
        ventana_hija.transient(self.ventana)
        ventana_hija.grab_set()
        self.curso=None
        frame_izquierda=ctk.CTkFrame(ventana_hija,height=600,width=400)
        frame_izquierda.pack_propagate(False)
        frame_izquierda.grid(row=0,column=0)
        cursos=ctk.CTkScrollableFrame(frame_izquierda,height=500,width=300)
        cursos.grid(row=0,column=0,pady=50,padx=50,sticky="nsew")
        frame_derecho=ctk.CTkFrame(ventana_hija,height=600,width=200)
        frame_derecho.pack_propagate(False)
        frame_derecho.grid(row=0,column=1)
        boton_agregar=ctk.CTkButton(frame_derecho,text="agregar curso",height=100,width=100,command=lambda:self.ventana_agregar_curso(ventana_hija,cursos))
        boton_agregar.pack_propagate(False)
        boton_agregar.grid(row=0,padx=20,pady=20)
        boton_eliminar=ctk.CTkButton(frame_derecho,text="eliminar curso",height=100,width=100,command=lambda:self.eliminarCurso(cursos))
        boton_eliminar.pack_propagate(False)
        boton_eliminar.grid(row=1,padx=20,pady=20)
        self.agregarItems_3(cursos)
        

    def ventana_agregar_curso(self,ventana,scrollbar):
        ventana_hija=ctk.CTkToplevel(ventana,height=400,width=400)
        ventana_hija.transient(ventana)
        ventana_hija.grab_set()
        titulo_materia=ctk.CTkLabel(ventana_hija,text=" nombre de la materia",height=50,width=300)
        titulo_materia.pack_propagate(False)
        titulo_materia.grid(row=0,padx=20,pady=20)
        entrada_materia=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese el nombre de la materia: ",height=50,width=300)
        entrada_materia.pack_propagate(False)
        entrada_materia.grid(row=1,padx=20,pady=20)
        titulo_cant_alumnos=ctk.CTkLabel(ventana_hija,text=" cantidad de alumnos",height=50,width=300)
        titulo_cant_alumnos.pack_propagate(False)
        titulo_cant_alumnos.grid(row=2,padx=20,pady=20)
        entrada_cant_alumnos=ctk.CTkEntry(ventana_hija,placeholder_text="ingrese la cantidad de alumnos de la materia: ",height=50,width=300)
        entrada_cant_alumnos.pack_propagate(False)
        entrada_cant_alumnos.grid(row=3,padx=20,pady=20)
        boton_agregar_curso=ctk.CTkButton(ventana_hija,text="agregar curso",height=50,width=300, command=lambda: self.agregarCurso(entrada_materia.get(),entrada_cant_alumnos.get(),scrollbar))
        boton_agregar_curso.pack_propagate(False)
        boton_agregar_curso.grid(row=4,padx=20,pady=20)

    def agregarCurso(self,materia,cant,scrollbar):
        id=self.back.idCurso()
        self.back.agregarCurso(curso(id,materia,int(cant),scrollbar))
        self.agregarItems_3(scrollbar)
    
    def eliminarCurso(self,scrollbar):
        self.back.eliminarCurso(self.curso)
        self.agregarItems_3(scrollbar)

    
    def agregarItems_2(self,scrollbar):

        for widget in scrollbar.winfo_children():
            widget.destroy()
        
        for i in self.back.devolverAlumnos():
            curso_nuevo=alumno(i[0],i[1],i[2],scrollbar)
            boton=curso_nuevo.boton()
            boton.configure(command=self.hacer_referencia_2(i[0]))
            boton.pack(pady=5, padx=5, fill="x")
    
    def hacer_referencia_2(self,id):
        def callback():
            self.alumno = id
        return callback

    def agregarItems_3(self, scrollbar):
        for widget in scrollbar.winfo_children():
            widget.destroy()

        for i in self.back.devolverCursos():
            curso_nuevo = curso(i[0], i[1], i[2], scrollbar)
            boton = curso_nuevo.boton()
            boton.configure(command=self.hacer_referencia_3(i[0]))
            boton.pack(pady=5, padx=5, fill="x")

    def hacer_referencia_3(self, id):
        def callback():
            self.curso = id
        return callback





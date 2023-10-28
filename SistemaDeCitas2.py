import tkinter as tk
from tkinter import messagebox 
from tkcalendar import Calendar
import os
from plyer import notification  

def mostrar_notificacion(recordatorio):
    notification.notify(title='Recordatorio de Cita', message=recordatorio, app_name='Registro de Citas', app_icon=None,)
    
def buscar_citas():
    def ver_citas():
        nombr_info = nombre_busqueda.get()
        if not nombr_info:
            messagebox.showerror("Error", "Por favor, ingrese el nombre para buscar las citas.")
            return

        archivo_nombre = "Citas/Citas paciente_{}.txt".format(nombr_info.replace("/", ""))
        try:
            with open(archivo_nombre, "r") as archivo:
                citas = archivo.readlines()
            if citas:
                messagebox.showinfo("Citas para el paciente", "\n".join(citas))
            else:
                messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")
        except FileNotFoundError:
            messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")

    def editra_cita():
        info = nombre_busqueda.get()
        if not info:
            messagebox.showerror("ERROR","Ingrese el nombre para buscar la cita")
            return
        archivo_original = "Citas/Citas paciente_{}.txt".format(info.replace("/", ""))
        if not os.path.exists(archivo_original):
           messagebox.showerror("ERROR", "No se encontraron citas para el paciente con el nombre proporcionado.")
           return
       
        try:
            with open(archivo_original,"r")as archivo:
                citas = archivo.readlines()
            if citas:
                nombre, numero, cuestion, fecha = citas[0].strip().split("\t")
                
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                
                entrada1.insert(0, nombre)
                entrada2.insert(0, numero)
                entrada3.insert(0, cuestion)
                
                boton_guardar = tk.Button(ventana, text="Guardar Edición", command=lambda: guardar_edicion(archivo_original), width="25", height="2", bg="#ffda9e")
                boton_guardar.place(x=205, y=470)
            else:
                messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")
        except FileExistsError:
               messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")
              
    def guardar_edicion(archivo_original):
        nuevo_nombre = entrada1.get()
        nuevo_numero = entrada2.get()
        nueva_cuestion = entrada3.get()  
        nueva_fecha = cal.get_date()
        
        if not nuevo_nombre or not nueva_cuestion or not nuevo_numero:
            messagebox.showerror("Error", "Debes completar los campos de Nombre numero consulta y fecha para guardar la edición.")
            return
        
        #esto permitira que cuando no se hagan cambios en las entradas pero si en la fecha se mantengan
        archivo_nombre_nuevo = "Citas/Citas paciente_{}.txt".format(nuevo_nombre.replace("/", "")) 
        
        with open(archivo_nombre_nuevo, "w") as archivo_nuevo:
            archivo_nuevo.write(f"{nuevo_nombre}\t{nuevo_numero}\t{nueva_cuestion}\t{nueva_fecha}\n")
            
            #esto cambia en nombre del archivo asi lo puedo buscar en citas
        if archivo_original != archivo_nombre_nuevo:
             os.remove(archivo_original)
        
        messagebox.showinfo("Cita editada", "Los datos de la cita han sido editados y guardados espere unos segundos.")
        
        entrada1.delete(0, tk.END)
        entrada2.delete(0, tk.END)
        entrada3.delete(0, tk.END)  
         
    def eliminar_citas():
     nombr_info = nombre_busqueda.get()
     if not nombr_info:
        messagebox.showerror("Error", "Por favor, ingrese el nombre para buscar la citas.")
        return

     archivo_nombre = "Citas/Citas paciente_{}.txt".format(nombr_info.replace("/", ""))
     try:
        with open(archivo_nombre, "r") as archivo:
            citas = archivo.readlines()
        if citas:
            respuesta = messagebox.askquestion("Eliminar Cita", "¿Desea eliminar esta cita?")
            if respuesta == 'yes':
                # elimina archivos de txt
                os.remove(archivo_nombre)
                messagebox.showinfo("Cita eliminada", "La cita ha sido eliminada con éxito.")
        else:
            messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")
     except FileNotFoundError:
        messagebox.showinfo("Citas para el paciente", "No hay citas programadas para este paciente.")
    #Esta es la entrada de datos para buscar las citas
    nombre_busqueda = tk.Entry(ventana, width="40")
    nombre_busqueda.place(x=22, y=390)
    
    boton_ver_citas = tk.Button(ventana, text="Buscar Citas por Nombre", command=ver_citas, width="25", height="2", bg="#ffda9e")
    boton_ver_citas.place(x=22, y=420)

    boton_editar_citas = tk.Button(ventana, text="Editar Cita por Nombre", command=editra_cita, width="25", height="2", bg="#ffda9e")
    boton_editar_citas.place(x=200, y=420)

    boton_eliminar_citas = tk.Button(ventana, text="borrar cita", command=eliminar_citas, width="25", height="2", bg="#ffda9e")
    boton_eliminar_citas.place(x=378, y=420)
    boton_salir = tk.Button(ventana, text="Salir", command=salir, width="25", height="2", bg="#ffda9e")
    boton_salir.place(x=22, y=470)
    
    boton_ver_todas_las_citas = tk.Button(ventana, text="Ver Todas las Citas", command=ver_todas_las_citas, width="25", height="2", bg="#ffda9e")
    boton_ver_todas_las_citas.place(x=378, y=470)

def enviar_datos():
    nombr_info = entrada1.get()
    numero_info = entrada2.get()
    cuestion_info = entrada3.get()
    fecha_info = cal.get_date()
    if not (nombr_info and cuestion_info):
        messagebox.showerror("error","Debe rellenar los campos obligatorios.")
        return
    if not numero_info.isdigit():
        messagebox.showerror("ERROR","termine de rellenar los campos de forma correcta")
        return
    archivo_nombre = "Citas/Citas paciente_{}.txt".format(nombr_info.replace("/", ""))
    print(nombr_info,"\t",numero_info,"\t",cuestion_info,"\t",fecha_info)
    
    archivo_nombre = "Citas/Citas paciente_{}.txt".format(nombr_info.replace("/", ""))
    with open(archivo_nombre, "w") as nuevo_archivo:
        nuevo_archivo.write(nombr_info)
        nuevo_archivo.write("\t")
        nuevo_archivo.write(numero_info)
        nuevo_archivo.write("\t")
        nuevo_archivo.write(cuestion_info)
        nuevo_archivo.write("\t")
        nuevo_archivo.write(fecha_info)
        nuevo_archivo.write("\n")
    
    recordatorio =f"Tiene una cita el {fecha_info} para {cuestion_info}."
    mostrar_notificacion(recordatorio)
    
    print("Cita registrada en", archivo_nombre)
    
    #Borra los datos de la entrada ingresados
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    entrada3.delete(0, tk.END)

def ver_todas_las_citas():
    try:
        citas_dir = "Citas/"
        citas_archivos = os.listdir(citas_dir)
        
        todas_las_citas = []
        for archivo in citas_archivos:
            with open(os.path.join(citas_dir, archivo), "r") as archivo_cita:
                citas = archivo_cita.readlines()
                todas_las_citas.extend(citas)
        
        if todas_las_citas:
            messagebox.showinfo("Todas las Citas", "\n".join(todas_las_citas))
        else:
            messagebox.showinfo("Todas las Citas", "No hay citas programadas en la base de datos.")
    except FileNotFoundError:
        messagebox.showinfo("Todas las Citas", "No hay citas programadas en la base de datos.")


def salir():
    ventana.quit()
       
ventana = tk.Tk()
ventana.geometry("650x550")
ventana.title("Registro de citas")
ventana.resizable(False,False)
ventana.config(background="#84b6f4")
menu_titulo = tk.Label(text="Registro de citas python",font = ("cambria",13), bg = "green", fg="white",width="550", height="2")
menu_titulo.pack()

nombre = tk.Label(text="Nombre Completo",bg="white")
nombre.place(x=22,y=70)
numero = tk.Label(text="Numero Celular",bg="white")
numero.place(x=22,y=130)
cuestion = tk.Label(text="Informacion de la consulta",bg="white")
cuestion.place(x=22,y=190)

entrada1 = tk.Entry(textvariable=nombre,width="40")
entrada2 = tk.Entry(textvariable=numero,width="40")
entrada3 = tk.Entry(textvariable=cuestion,width="40")
entrada1.place(x=22,y=100)
entrada2.place(x=22,y=160)
entrada3.place(x=22,y=220)

cal = Calendar(ventana)
cal.place(x=300,y=50)

boton = tk.Button(ventana,text="Guardar Cita", command=enviar_datos,width="25",height="2",bg="#ffda9e")
boton.place(x=22,y=290)
boton = tk.Button(ventana,text="y ver cita", command=buscar_citas,width="25",height="2",bg="#ffda9e")
boton.place(x=22,y=340)


ventana.mainloop()
import tkinter as ventana

raiz=ventana.Tk()

raiz.title("Carga de datos personales")

anchoVentana=1000
altoVentana=800
anchoPantalla=raiz.winfo_screenwidth()
altoPantalla=raiz.winfo_screenheight()
centroX=int(anchoPantalla/2 - anchoVentana/2)
centroY=int(altoPantalla/2 - altoVentana/2)

#Centrar ventana
raiz.geometry(str(anchoVentana)+"x"+str(altoVentana)+"+"+str(centroX)+"+"+str(centroY))
raiz.resizable(True, True)

#familia tk
def confirmacionEnvio ():
    print("Enviado correctamente")

def salir():
    raiz.destroy()

ventana.Label(raiz, text="Es necesario cargar los datos que se piden a continuación para continuar con el proceso").pack(padx=5, pady=5)

ventana.Label(raiz, text="Nombre").pack(padx=5, pady=5)
ventana.Entry(raiz,width=40).pack()

apellido=ventana.Label(raiz, text="Apellidos").pack(padx=5, pady=5)
ventana.Entry(raiz,width=40).pack()
ventana.Label(raiz, text="Edad").pack(padx=5, pady=5)
ventana.Spinbox(raiz,width=10,from_=0,to=100).pack(padx=5, pady=5)

v=ventana.IntVar()
v.set(0)
radioBoton1=ventana.Radiobutton(raiz, text="hombre", variable=v, value=1)
radioBoton1.pack()
radioBoton2=ventana.Radiobutton(raiz, text="mujer", variable=v, value=2)
radioBoton2.pack()
radioBoton3=ventana.Radiobutton(raiz, text="prefiero no especificar", variable=v, value=3)
radioBoton3.pack()

#mensaje
texto1=ventana.Message(raiz,text="En el siguiente listado se especifican todos los puestos de trabajo que actualmente se encuentran disponibles,"+
                "por favor escoga la opción que más le interesa")
texto1.config(width=300)
texto1.pack(padx=5, pady=5)

#lista de objetos
puestosDisponibles=['Comercial clientes nuevos','Comercial ya clientes','Atención al cliente','RRHH','IT','Contabilidad', 'Departamento Legal', 'Administración']
listado=ventana.Listbox(raiz)
for puesto in puestosDisponibles:
    listado.insert(ventana.END,puesto)
listado.config(width=30)
listado.pack(padx=5, pady=5)

ventana.Label(raiz, text="Justifique,brevemente, porque cree que es el mejor cantidato.").pack()
texto=ventana.Text(raiz)
texto.config(width=20, height=10)
texto.pack()

#boton cuadrado
ventana.Checkbutton(raiz, text="Estoy de acuerdo con la política de protección de datos ").pack()

#boton
ventana.Button(raiz,text="Enviar", command=confirmacionEnvio).pack(padx=5,pady=5)


#menu
barraMenu=ventana.Menu(raiz)
raiz.config(menu=barraMenu)

archivo=ventana.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="archivo",menu=archivo)
archivo.add_command(label="nuevo")
archivo.add_command(label="abrir")
archivo.add_command(label="guardar")

editar=ventana.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="editar",menu=editar)
editar.add_command(label="copiar")
editar.add_command(label="borrar")
editar.add_command(label="cortar")

ayuda=ventana.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="ayuda",menu=ayuda)
ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Documentacion")
ayuda.add_command(label="Soporte")

Salir=ventana.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Salir", menu=Salir)
Salir.add_command(label="Salir",command=salir)

#ventana se ejecute si se habre desde el archivo
raiz.mainloop() 

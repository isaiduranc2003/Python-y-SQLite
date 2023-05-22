
from tkinter import *
from tkinter import ttk
raiz = Tk()

import sqlite3
conexion = sqlite3.connect('Registrobdd.db')

c = conexion.cursor()
#c.execute("SELECT * FROM registro")
#c.execute('''CREATE TABLE registro (nombre text, apaterno text, amaterno text, correo text, movil text,p1 text,p2 text, p3 text, eed text)''')

class ejercicioformulario:
    def __init__(self,raiz):
        file = open("formularioarch2.csv", "w")
        #ttk.Button(mainFramebutton, text="Guardar", command= self.guardar).grid(column=0,row=2,sticky=(S,W))
        raiz.title("Muestra widgets")
        
    
        nombre = StringVar()
        apaterno = StringVar()
        amaterno = StringVar()
        correo = StringVar()
        movil = StringVar()
    
        mainFrame = ttk.Frame(raiz,padding="20 20 20 20")
        mainFrame.grid()

        mainFrame2 = ttk.Frame(mainFrame,padding="10 10 10 10",relief="raised")
        mainFrame2.grid(pady=20)

        mainFrame3 = ttk.Frame(mainFrame,padding="30 20 35 20",relief="raised")
        mainFrame3.grid(pady=20,padx=15)

        mainFrame4 = ttk.Frame(mainFrame)
        mainFrame4.grid(column=2,row=0)

        mainFrame5 = ttk.Frame(mainFrame)
        mainFrame5.grid(column=2,row=1)
        #Funcion para guardar los datos en el archivo 
        def guardar():
            print("Boton guardar presionado")
            with open("formularioarch2.csv", "a") as file:
                file.write(nombre.get())
                file.write(",")
                file.write(apaterno.get())
                file.write(",")
                file.write(amaterno.get())
                file.write(",")
                file.write(correo.get())
                file.write(",")
                file.write(movil.get())
                file.write(",")
                
                if pasatiempo1.get() == 1:
                    file.write("leer")
                    file.write(",")
                if pasatiempo2.get() == 1:
                    file.write("Musica")
                    file.write(",")
                if pasatiempo3.get() == 1:
                    file.write("videojuegos")
                    file.write(",")

                if eed.get()==1:
                    file.write("Estudiante")
                if eed.get()==2:
                    file.write("Empleado")
                if eed.get()==3:
                    file.write("Desempleado")    

                file.write("\n")    

        def guardarbdd():
            print("Guardar en base de datos")
            if pasatiempo1.get() == 1:
                l = 'leer'
            if pasatiempo1.get() == 0:
                l= None
            if pasatiempo2.get() == 1:
                m = 'musica'
            if pasatiempo2.get() == 0:
                m= None
            if pasatiempo3.get() == 1:
                v = 'videojuegos'
            if pasatiempo3.get() == 0:
                v= None
                    
            if eed.get()==1:
                ocupacion = 'Estudiante'
            if eed.get()==2:
                ocupacion = 'Empleado'
            if eed.get()==3:
                ocupacion = 'Desempleado'

                    
            Formulariodb = [(nombre.get(),apaterno.get(),amaterno.get(),correo.get(),movil.get(),l,m,v,ocupacion)]
            c.executemany('INSERT INTO registro VALUES (?,?,?,?,?,?,?,?,?)', Formulariodb)
            conexion.commit()
        
        def delete_window():
            conexion.close()
            raiz.destroy()
            

        mainFramebutton = ttk.Frame(mainFrame)
        mainFramebutton.grid(column=0,row=5,padx=30)
        ttk.Button(mainFramebutton, text="Guardar",command=guardar ).grid(column=0,row=2,sticky=(S,W))
        ttk.Label(mainFramebutton, text="   ").grid(column=1,row=2)
        ttk.Button(mainFramebutton, text="Cancelar").grid(column=2,row=2,sticky=(S))
        ttk.Label(mainFramebutton, text="   ").grid(column=3,row=2)
        ttk.Button(mainFramebutton, text="Guardar en BDD",command=guardarbdd).grid(column=4,row=2)
        raiz.bind(guardar)
        

        ttk.Label(mainFrame2, text="Nombre:").grid(column=0,row=0)
        ttk.Label(mainFrame2, text="").grid(column=0,row=1)
        ttk.Label(mainFrame2, text="A.Paterno:").grid(column=0,row=2)
        ttk.Label(mainFrame2, text="").grid(column=0,row=3)
        ttk.Label(mainFrame2, text="A.Materno:").grid(column=0,row=4)
        ttk.Label(mainFrame2, text="").grid(column=0,row=5)
        ttk.Label(mainFrame2, text="Correo:").grid(column=0,row=6)
        ttk.Label(mainFrame2, text="").grid(column=0,row=7)
        ttk.Label(mainFrame2, text="Movil:").grid(column=0,row=8)


        nombreEntry = ttk.Entry(mainFrame2,width=30,textvariable=nombre)
        nombreEntry.grid(column=1,row=0)
        apaternoEntry = ttk.Entry(mainFrame2,width=30,textvariable=apaterno)
        apaternoEntry.grid(column=1,row=2)
        amaternoEntry = ttk.Entry(mainFrame2,width=30,textvariable=amaterno)
        amaternoEntry.grid(column=1,row=4)
        correoEntry = ttk.Entry(mainFrame2,width=30,textvariable=correo)
        correoEntry.grid(column=1,row=6)
        movilEntry = ttk.Entry(mainFrame2,width=30,textvariable=movil)
        movilEntry.grid(column=1,row=8)
    
        ttk.Label(mainFrame3, text="Aficiones:").grid(column=0,row=0,sticky=(E))
        aficiones = StringVar()
        #variables para comprobar que el boton este seleccionado
        pasatiempo1=IntVar()
        pasatiempo2=IntVar()
        pasatiempo3=IntVar()

        leer = ttk.Checkbutton(mainFrame3,text="leer",variable=pasatiempo1).grid(column=0,row=2)
        musica = ttk.Checkbutton(mainFrame3,text="musica",variable=pasatiempo2).grid(column=1,row=2)
        videojuegos = ttk.Checkbutton(mainFrame3,text="videojuegos",variable=pasatiempo3).grid(column=2,row=2)

        ttk.Label(mainFrame4, text="").grid(column=0,row=0,sticky=(E))
        #variable para saber cual es la opcion seleccionada
        eed = IntVar()
        estudiante = ttk.Radiobutton(mainFrame4,text="estudiante",variable=eed,value=1).grid(column=0,row=0,sticky=W)
        empleado = ttk.Radiobutton(mainFrame4,text="Empleado",variable=eed,value=2).grid(column=0,row=1,sticky=W)
        desempleado = ttk.Radiobutton(mainFrame4,text="Desempleado",variable=eed,value=3).grid(column=0,row=2,sticky=W)
        

        estado = StringVar()
        comboEstados = ttk.Combobox(mainFrame5, textvariable=estado)
        comboEstados.grid()
        comboEstados['values']= ("Jalisco", "Nayarit", "Colima","Michoacan","Estados(32)")

        raiz.protocol("WM_DELETE_WINDOW",delete_window)
        file.close()
ejercicioformulario(raiz)
raiz.mainloop()







import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas, listar_generos, listar_peliculas , guardar_peli, editar_peli, borrar_peli

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 500 , height = 500)
    menu_inicio = tk.Menu(barra, tearoff=0)

    #  niveles  #

    #principal

    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Consultas')
    barra.add_cascade(label='Acerca de..')
    barra.add_cascade(label='Ayuda')

    #submenu
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=580,height=520)
        self.root = root
        self.pack()
        self.id_peli = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 14,'bold'))
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)

        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=('Arial', 14,'bold'))
        self.label_duracion.grid(row= 1, column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text="Genero: ")
        self.label_genero.config(font=('Arial', 14,'bold'))
        self.label_genero.grid(row= 2, column=0,padx=10,pady=10)
        
        self.label_anio_de_estreno = tk.Label(self, text="Año de Estreno: ")
        self.label_anio_de_estreno.config(font=('Arial', 14, 'bold'))
        self.label_anio_de_estreno.grid(row=3, column=0, padx=10, pady=10)

        self.label_protagonista = tk.Label(self, text="Protagonista: ")
        self.label_protagonista.config(font=('Arial', 14, 'bold'))
        self.label_protagonista.grid(row=4, column=0, padx=10, pady=10)
        
       
    
    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled',font=('Arial',12))
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10, columnspan='2')

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.duracion)
        self.entry_duracion.config(width=50, state='disabled',font=('Arial',12))
        self.entry_duracion.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        #aca limpiamos la lista de tuplas que nos retorna la funcion
        x = listar_generos()
        #print(x)
        y = []
        for i in x:
            y.append(i[1])
        #print(y)
        
        self.anio_de_estreno = tk.StringVar()
        self.entry_anio_de_estreno = tk.Entry(self, textvariable=self.anio_de_estreno)
        self.entry_anio_de_estreno.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_anio_de_estreno.grid(row=3, column=1, padx=10, pady=10, columnspan='2')

        self.protagonista = tk.StringVar()
        self.entry_protagonista = tk.Entry(self, textvariable=self.protagonista)
        self.entry_protagonista.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_protagonista.grid(row=4, column=1, padx=10, pady=10, columnspan='2')

        #concatenemos el nuevo array
        self.generos = ['Seleccione uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=48, state='disabled',font=('Arial',12))
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#8944c9',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 5, column=0,padx=10,pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#e0972f',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row= 5, column=1,padx=10,pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#bb8ebd',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row= 5, column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_anio_de_estreno.config(state='normal')
        self.entry_protagonista.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_anio_de_estreno.config(state='disabled')
        self.entry_protagonista.config(state='disabled')
        self.entry_genero.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.duracion.set('')
        self.anio_de_estreno.set('')
        self.protagonista.set('')
        self.id_peli = None
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current(),
            self.anio_de_estreno.get(),
            self.protagonista.get()
        )

        if self.id_peli is None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    def mostrar_tabla(self):
        self.lista_p = listar_peliculas()
        self.lista_p.reverse()
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Genero', 'Año de Estreno', 'Protagonista'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse')
    
    

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')
        self.tabla.heading('#4', text='Año de Estreno')
        self.tabla.heading('#5', text='Protagonista')
       
        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values = (p[1], p[2], p[3], p[4], p[5]))
            
       
        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#d179b1',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 10, column=0,padx=10,pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#c42137',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 10, column=1,padx=10,pady=10)

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']

            self.nombre_peli_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.anio_peli_e = self.tabla.item(self.tabla.selection())['values'][3]
            self.prota_peli_e = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli_e)
            self.duracion.set(self.dura_peli_e)
            self.entry_genero.current(self.generos.index(self.gene_peli_e))
            self.anio_de_estreno.set(self.anio_peli_e)
            self.protagonista.set(self.prota_peli_e)

        except:
            pass
    
    def eliminar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            borrar_peli(int(self.id_peli))
            self.mostrar_tabla()
            self.id_peli = None #reseteanis el id luego de eliminar
        except:
            pass
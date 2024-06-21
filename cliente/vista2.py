import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Directores, listar_peliculas, listar_directores, guardar_director, editar_director, borrar_director

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra, width=500, height=500)
    menu_inicio = tk.Menu(barra, tearoff=0)

    barra.add_cascade(label='Inicio', menu=menu_inicio)
    barra.add_cascade(label='Consultas')
    barra.add_cascade(label='Acerca de..')
    barra.add_cascade(label='Ayuda')

    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=580, height=520)
        self.root = root
        self.pack()
        self.id_director = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 14, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial', 14, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)

        self.label_pelicula = tk.Label(self, text="Película: ")
        self.label_pelicula.config(font=('Arial', 14, 'bold'))
        self.label_pelicula.grid(row=2, column=0, padx=10, pady=10)
        
        self.label_nacionalidad = tk.Label(self, text="Nacionalidad: ")
        self.label_nacionalidad.config(font=('Arial', 14, 'bold'))
        self.label_nacionalidad.grid(row=3, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.apellido)
        self.entry_apellido.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.nacionalidad = tk.StringVar()
        self.entry_nacionalidad = tk.Entry(self, textvariable=self.nacionalidad)
        self.entry_nacionalidad.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nacionalidad.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        x = listar_peliculas()
        y = [i[1] for i in x]
        
        self.peliculas = ['Seleccione uno'] + y
        self.entry_pelicula = ttk.Combobox(self, state="readonly")
        self.entry_pelicula['values'] = self.peliculas
        self.entry_pelicula.current(0)
        self.entry_pelicula.config(width=48, state='disabled', font=('Arial', 12))
        self.entry_pelicula.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#8944c9', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#e0972f', cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#bb8ebd', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_pelicula.config(state='normal')
        self.entry_nacionalidad.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_pelicula.config(state='disabled')
        self.entry_nacionalidad.config(state='disabled')
        self.entry_pelicula.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.apellido.set('')
        self.nacionalidad.set('')
        self.id_director = None
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        director = Directores(
            self.nombre.get(),
            self.apellido.get(),
            self.entry_pelicula.current(),
            self.nacionalidad.get()
        )

        if self.id_director is None:
            guardar_director(director)
        else:
            editar_director(director, int(self.id_director))

        self.mostrar_tabla()
        self.bloquear_campos()

    def mostrar_tabla(self):
        self.lista_p = listar_directores()
        self.lista_p.reverse()
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Apellido', 'Película', 'Nacionalidad'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='Película')
        self.tabla.heading('#4', text='Nacionalidad')

        for p in self.lista_p:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4]))

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#d179b1', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=10, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#c42137', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=10, column=1, padx=10, pady=10)

    def editar_registro(self):
        try:
            self.id_director = self.tabla.item(self.tabla.selection())['text']
            self.nombre_director_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_director_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.pelicula_director_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.nacionalidad_director_e = self.tabla.item(self.tabla.selection())['values'][3]
           

            self.habilitar_campos()
            self.nombre.set(self.nombre_director_e)
            self.apellido.set(self.apellido_director_e)
            self.entry_pelicula.current(self.peliculas.index(self.pelicula_director_e))
            self.nacionalidad.set(self.nacionalidad_director_e)
            

        except:
            pass
    
    def eliminar_registro(self):
        try:
            self.id_director = self.tabla.item(self.tabla.selection())['text']
            borrar_director(int(self.id_director))
            self.mostrar_tabla()
            self.id_peli = None 
        except:
            pass
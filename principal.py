import tkinter as tk
from tkinter import ttk
from cliente.vista import Frame as FramePeliculas
from cliente.vista2 import Frame as FrameDirectores
from cliente.vista import barrita_menu as barrita_menu_peliculas
from cliente.vista2 import barrita_menu as barrita_menu_directores

def main():
    ventana = tk.Tk()
    ventana.title('Películas y directores')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(True, True)
    ventana.configure(background='#b580c4')  # Cambia el color de fondo de la ventana
    

    # Crear un canvas
    canvas = tk.Canvas(ventana, bg='#b580c4')
    canvas.pack(fill='both', expand=True)

    # Agregar texto al canvas
    canvas.create_text(200, 150, text='Películas y Directores', font=('Arial', 24), fill='white')


 
    estilo = ttk.Style()
    estilo.theme_use('clam')  # Usa el tema 'clam' para mejor compatibilidad con estilos personalizados
    estilo.configure('TButton', background='#d294e3', foreground='#e1cfe6', font=('Arial', 12, 'bold'))
    estilo.map('TButton', background=[('active', '#b07bcf')], foreground=[('active', '#1d0721')])

    barra_menu = tk.Menu(ventana, background='#3c3f41', foreground='#ffffff', activebackground='#505357', activeforeground='#ffffff')
    ventana.config(menu=barra_menu)

    menu_peliculas = tk.Menu(barra_menu, tearoff=0, background='#3c3f41', foreground='#ffffff', activebackground='#505357', activeforeground='#ffffff')
    barra_menu.add_cascade(label='Películas', menu=menu_peliculas)
    menu_peliculas.add_command(label='Administrar Películas', command=lambda: abrir_frame(FramePeliculas, barrita_menu_peliculas))

    menu_directores = tk.Menu(barra_menu, tearoff=0, background='#3c3f41', foreground='#ffffff', activebackground='#505357', activeforeground='#ffffff')
    barra_menu.add_cascade(label='Directores', menu=menu_directores)
    menu_directores.add_command(label='Administrar Directores', command=lambda: abrir_frame(FrameDirectores, barrita_menu_directores))

  
    def abrir_frame(Frame, barrita_menu_func):
        for widget in ventana.winfo_children():
            widget.destroy()
        barrita_menu_func(ventana)
        frame = Frame(ventana)
        frame.pack(expand=True, fill='both')

    ventana.mainloop()

if __name__ == '__main__':
    main()
from .conneciondb import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql = '''
            CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(50),
            PRIMARY KEY (ID AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            Anio_de_estreno VARCHAR(10),
            Protagonista VARCHAR(15),
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Genero) References Genero(ID)
            );
            
            
           CREATE TABLE Directores (
           ID INTEGER NOT NULL,
           Nombre VARCHAR(20),
           Apellido VARCHAR(20),
           Peliculas INTEGER,
           Nacionalidad VARCHAR(15),
           PRIMARY KEY (ID AUTOINCREMENT)
           FOREIGN KEY (Peliculas) REFERENCES Peliculas(ID)
);
            '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

def listar_generos():
    conn = ConeccionDB()
    listar_generos = []
    sql = """
            SELECT * FROM Genero
         """
    
    try:
        conn.cursor.execute(sql)
        listar_generos = conn.cursor.fetchall()
        conn.cerrar_con()
        return listar_generos
    except Exception as e:
        print(f"Error al listar géneros: {e}")
        return []


def listar_peliculas():
    conn = ConeccionDB()
    listar_peliculas = []
    sql = """
         SELECT p.ID, p.Nombre, p.Duracion, g.Nombre as Genero, p.Anio_de_estreno, p.Protagonista
            FROM Peliculas as p
            INNER JOIN Genero as g
            ON p.Genero = g.ID;
          """
    
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except Exception as e:
        print(f"Error al listar películas: {e}")
        return []

def listar_directores():
    conn = ConeccionDB()
    listar_directores = []
    sql = """
       SELECT d.ID, d.Nombre, d.Apellido, p.Nombre as Pelicula, d.Nacionalidad
       FROM Directores as d
       INNER JOIN Peliculas as p
       ON d.Peliculas = p.ID;
         """
    
    try:
        conn.cursor.execute(sql)
        listar_directores = conn.cursor.fetchall()
        conn.cerrar_con()
        return listar_directores
    except Exception as e:
        print(f"Error al listar directores: {e}")
        return []
    
class Peliculas:
    def __init__(self, nombre, duracion, genero, anio_de_estreno, protagonista):
        self.id_peliculas = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.anio_de_estreno = anio_de_estreno
        self.protagonista = protagonista

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion}, {self.genero}, {self.anio_de_estreno}, {self.protagonista}]'

class Directores:
    def __init__(self, nombre, apellido, pelicula, nacionalidad):
        self.id_directores = None
        self.nombre = nombre
        self.apellido = apellido
        self.pelicula = pelicula
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f'Director[{self.nombre}, {self.apellido}, {self.pelicula} {self.nacionalidad}]'
    
def guardar_peli(pelicula):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Peliculas (Nombre, Duracion, Genero, Anio_de_estreno, Protagonista)
            VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}', '{pelicula.anio_de_estreno}', '{pelicula.protagonista}');
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar película: {e}")
        
def guardar_director(director):
    conn = ConeccionDB()
        
    sql = f"""
            INSERT INTO Directores (Nombre, Apellido, Peliculas, Nacionalidad)
            VALUES('{director.nombre}', '{director.apellido}', '{director.pelicula}', '{director.nacionalidad}');
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar director: {e}")

def editar_peli(pelicula, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Peliculas
            SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = '{pelicula.genero}', Anio_de_estreno = '{pelicula.anio_de_estreno}', Protagonista = '{pelicula.protagonista}'
            WHERE ID = {id};
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar película: {e}")


def editar_director(director, id):
    conn = ConeccionDB()
    sql = f"""
            UPDATE Directores
            SET Nombre = '{director.nombre}', Apellido = '{director.apellido}', Peliculas= '{director.pelicula}', Nacionalidad = '{director.nacionalidad}'
            WHERE ID = {id};
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar director: {e}")


def borrar_peli(id):
    conn = ConeccionDB()
    
    sql = f"""
            DELETE FROM Peliculas
            WHERE ID = {id};
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar película: {e}")
    
def borrar_director(id):
    conn = ConeccionDB()
    sql = f"""
            DELETE FROM Directores
            WHERE ID = {id};
            """
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar director: {e}")

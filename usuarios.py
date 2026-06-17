"""estructura basica y fundamental para estructural
class Usuario: 
    id_usuario = 1
    documento = 1085950123
    nombre = "laura"
    apellido = "gomez"
    correo = "@lauragomez"
    telefono = "3217857450"
    direccion = "calle 123"

# crear una instancia de la clase usuario copia 
usuario_1 = Usuario()
uauario_2 = Uauario()

usuaruo_."felipe"
 print (usuario_1.nombre) 
 print (usuario_2.nombre)"""


# estructura vase 
lista_usuario = [] # lista global para almacenar los usuarios creados 
class Usuario:
    # crear una funcion para el constructor _int_
    def __init__(self, id_usuario, documento, nombre:str, apellido, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apelliod = apellido 
        self. correo = correo 
        self.telefono = telefono 
        self.direccion = direccion 
    def saludar(self):
        print (f"hola mi nombre es {self.nombre} {self.apellido}")
# metod face CRUD

# CREATE crear

    def crear_usuario(self):
        lista_usuario.append(self)
        print(f"el usuario {self.nombre} ha sido registrado en el sistema")

    # READ leer
    def ver_usuario(self):
        print(f"ID: {self.id_usuario} nombre: {self.nombre} apellido: {self.apellido}")

    # UPDATE actualizar
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"exito: el usuario a sido actualizado a {self.nombre}  {self.apelliod}")

    # DELETE eliminar
    def eliminar_usuario(self):
        if self in lista_usuario:
            lista_usuario.remove(self)
            print(f"✅exito: el usuario {self.nombre} ha sido eliminado del sistema")
        else:
            print(f"❌advertencia: el usuario {self.nombre} no se encuentra en el sistema ")





# crear una instancia/ copia de la clase usuario 
usuario_1 = Usuario (1, 1070385600, "laura", "gomez", "@lauragomez", "3123744259", "calle 34" )

usuario_2 = Usuario (1, 1070385600, "juana", "gomez", "@lauragomez", "3123744259", "calle 34" )

# llame a motodos o funcion de la clase usuario 
usuario_1.saludar
usuario_2.saludar

# llamar los metods CREATE
print (f"lista usuario: {lista_usuario}")# lista vacia 

usuario_1.crear_usuario()
usuario_2.crear_usuario()

# llamar los metodos READ
print (f"lista de usuario: {lista_usuario [0].nombre}") #lista con un usuario

print (f"lista de usuario: {lista_usuario [1].nombre}") #lista con un usuario
usuario_1.ver_usuario() 
usuario_2.ver_usuario() 


# LLAMAR  LOS METODOS UPDATE 
usuario_1.actualizar_usuario("messi", "ronaldo")
usuario_1.ver_usuario() 


# llamar los metodos DALETE 
usuario_2.eliminar_usuario ()
usuario_2.ver_usuario() 





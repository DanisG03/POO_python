
lista_accesorios= []
class Accesorio:
    def __init__(self, id,marca, precio, cantidad, color, categoria):
        self.id = id 
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
        self.color = color 
        self.categoria = categoria 
    
    def agregar_accesorio(self):
        lista_accesorios.append(self)
        print(f"el accesorio  {self.marca} ha sido registrado en el sistema")

    def ver_accesorio(self):
        print(f"ID: {self.id} marca: {self.marca} cantidad: {self.cantidad}")

    def listar_accesorio(self):
        print(f"listando accesorios {self.marca}")
    
    def actualizar_accesorio(self, nuevo, cantidad_nueva):
        self.marca = nuevo
        self.cantidad = cantidad_nueva
        print(f"exito: el accesorio a sido actualizado a {self.marca}  {self.cantidad}")

    def buscar_accesorio(self):
        print(f"buscando el accesorio {self.marca}")
    
    def vender_accesorio(self):
        print(f"el accesorio {self.marca} fue vendido ")

    def eliminar_accesorio(self):
        if self in lista_accesorios:
            lista_accesorios.remove(self)
            print(f"✅exito: el accesorio {self.marca} ha sido eliminado del sistema")
        else:
            print(f"❌advertencia: el accesorio {self.marca} no se encuentra en el sistema ")

# instanciar d,marca, precio, cantidad, color, categoria
accesorio_1 = Accesorio (1, "rolex",1000000, 5, "plateado","clasica")
accesorio_2 = Accesorio (1, "inox",1000000, 5, "plateado","clasica")

# create
print (f"lista usuario: {lista_accesorios}")# lista vacia 

accesorio_1.agregar_accesorio()
accesorio_2.agregar_accesorio()

#READ
print (f"lista de accesorio: {lista_accesorios [0].marca}") #lista con un usuario

print (f"lista de accesorio: {lista_accesorios [1].marca}") #lista con un usuario
accesorio_1.ver_accesorio() 
accesorio_2.ver_accesorio() 


# LLAMAR  LOS METODOS UPDATE 
accesorio_1.actualizar_accesorio("marca", "cantidad")
accesorio_1.ver_accesorio() 


# llamar los metodos DALETE 
accesorio_2.eliminar_accesorio ()
accesorio_2.ver_accesorio() 





# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 

# class Persona:
#     def __init__(self, nombre, edad, dni):
#         #ATRIBUTOS O CARACTERISTICAS
#         self.nombre = nombre
#         self.edad = edad
#         self.dni = dni
    
#     #GETTERS
#     @property
#     def pNombre(self):
#         return self.nombre
    
#     @property
#     def pEdad(self):
#         return self.edad
    
#     @property
#     def pDni(self):
#         return self.dni
    
#     #SETTERS
#     @pNombre.setter
#     def pNombre(self, nombre):
#         self.nombre = nombre
        
#     @pEdad.setter
#     def pEdad(self, edad):
#         self.edad = edad  
    
#     @pDni.setter
#     def pDni(self, dni):
#         self.dni = dni  
    
#     #METODOS
#     def mostrarDatos(self):
#         print(f"Los datos de la primer persona es: {self.nombre} - {self.edad} - {self.dni}")
        
#     def mayorEdad(self):
        
#         if self.edad > 18:
#             print(f"La edad es {self.edad} y es menor de edad")
#         else:
#             print(f"La edad es {self.edad} y es mayor de edad")
    
# persona1 = Persona("Esteban", 31, 36010101)
# print(persona1)
# persona1.mostrarDatos()
# persona2 = Persona(20)
# persona2.mayorEdad()
# persona2.mayorEdad()



# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad 
# (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: 
#  Un constructor, donde los datos pueden estar vacíos. 
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, 
# sólo ingresando o retirando dinero. 
#  mostrar(): Muestra los datos de la cuenta. 
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Cuenta():
    #CONTRUCTOR
    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad
    
    #DECORADORES
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    #METODOS
    def mostrar(self):
        return "Datos de la cuenta\n"+"Titular: "+self.titular+" - Cantidad: "+str(self.__cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

#OBJETO
c1 = Cuenta("Pablo Diaz", 5000.10)
print(c1.mostrar()) #CONSULTO LA CUENTA
print("Ingresar dinero a la cuenta: ",c1.ingresar(-10000))
print(c1.mostrar()) 
print("Retirar dinero de la cuenta: ", c1.retirar(110000))
print(c1.mostrar())





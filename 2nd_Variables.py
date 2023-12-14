"""
Se puede cambiar el tipado de una variable dependiendo de el contexto en el que se esté utilizando la misma a la hora de estar programando.

Repasar el tipado estático y dinámico de una variable 


"""

n = 10
n = "Hola"
n = 11.5

# No errors because of what I have explained early on this doc.

"""
Strings
Ints
Booleans
Tuplas
Lists
Diccionarios

Solo se repasarán tuplas, listas y diccionarios ya que las demás ya se dominan correctamente
"""
"""
    tienen agregada la literal "j"

    Números complejos -> Están formados por letras y números. Dentro de python se pueden encontrar en el código cuando los números
"""
n = 1 +10j

"""
    Tuplas -> Tipo de datos que nos permite crear una colección de datos para agruparlos. No es necesario que los datos agrupados sean del mismo tipo
"""

tupla = (1, "jose",10.9)

# Las tuplas son inmutables (su valor no podrá ser modificado una vez esta esté definida)

# No se puede agregar, borrar o modificar elementos dentro de la misma tampoco 
print (tupla)
print (tupla[0])

"""
    se pueden mezclar los valores de dos tuplas distintas dentro de otra nueva en caso de que no se desee trabajar con las mismas por
    separado
    -- TuplaC = TuplaA + TuplaB
    
"""

# t =(1,2,3,1,1) 
# print(t.count(1)) -> Metodo para saber cuantas veces se encuentra el elemento 1 dentro de la tupla t

# Para buscar un elemento se usaria (2 in t) (elemento 2 dentro de la tupla t)

"""
    Listas -> Colección ordenada de objetos
    lista = [1,"jose",90.0] / Podemos ver que hay una semejanza entre las tuplas y las listas, pero en las listas
    debe de haber alguna colección (preferentemente) entre los elementos que forman parte de las mismas

    La otra diferencia es que para las listas utilizamos corchetes [], mientras que para las tuplas paréntesis ()

    Las listas sí pueden cambiar a lo largo de su ciclo de vida, por lo que se puede inicializar sin elementos al ser creada
    y después modificar los miembros que forman parte de la misma

    append(elemento) -> Sirve para agregar elementos a las listas que se tienen creadas en el código


"""

lista = [1,2,'m',90.8]

for i in lista:
    print(i)


    # Para concatenar listas podemos hacer el mismo proceso que se hizo con las tuplas, pero sin la necesidad de crear otra variable 
    # ya que las listas si pueden mutar durante su ciclo de vida

    """
    Se puede agregar el append para agregar elementos, pero si es que se utiliza este método, el resultado sería que 
    lo agregado se inserta entre corchetes al último 

    lB = [1,2,3]
    lista.append(lB)

    print (lista)  -> 1,2,'m',90.8,[1,2,3]

    Para agregar dentro de una posicion específica se puede utilizar el "insert"

    lista.insert(posicion.elemento)

    del para eliminar dentro de una posición en específico
    del(lista[1])

    remove tambien se puede utilizar, borra el primer elemento indicado que concuerde con lo que se desea borrar

    pop -> elimina el ultimo elemento de la lista

    sort -> ordena la lista

    """



    
    
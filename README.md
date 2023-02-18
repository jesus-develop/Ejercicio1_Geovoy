# Ejercicio1_Geovoy
lenguajes1 = {"Perl", "Javascript", "C#", "Ruby"}
lenguajes2 = {"Kotlin", "Swift", "Ruby"}
En estas dos líneas se crean los conjuntos "lenguajes1" y "lenguajes2" con los valores especificados entre llaves y separados por comas.

union = lenguajes1.union(lenguajes2)
print("Unión:", union)
En estas líneas se utiliza el método union para unir los dos conjuntos en un nuevo conjunto llamado "union". El resultado se imprime en pantalla utilizando la función print().


interseccion = lenguajes1.intersection(lenguajes2)
print("Intersección:", interseccion)
Aquí se utiliza el método intersection para obtener los elementos que se encuentran en ambos conjuntos, y el resultado se imprime de la misma manera que en la línea anterior.


diferencia = lenguajes1.difference(lenguajes2)
print("Diferencia (Lenguajes1 - Lenguajes2):", diferencia)
En estas líneas se utiliza el método difference para obtener los elementos que se encuentran en "lenguajes1" pero no en "lenguajes2". El resultado se imprime en pantalla, indicando que se trata de la diferencia de "lenguajes1" menos "lenguajes2".


diferencia_simetrica = lenguajes1.symmetric_difference(lenguajes2)
print("Diferencia simétrica:", diferencia_simetrica)
Finalmente, se utiliza el método symmetric_difference para obtener los elementos que se encuentran en uno u otro conjunto, pero no en ambos. El resultado se imprime en pantalla, indicando que se trata de la diferencia simétrica de los dos conjuntos.

# Declaración de conjuntos
lenguajes1 = {"Perl", "Javascript", "C#", "Ruby"}
lenguajes2 = {"Kotlin", "Swift", "Ruby"}

# Unión
union = lenguajes1.union(lenguajes2)
print("Unión:", union)

# Intersección
interseccion = lenguajes1.intersection(lenguajes2)
print("Intersección:", interseccion)

# Diferencia
diferencia = lenguajes1.difference(lenguajes2)
print("Diferencia (Lenguajes1 - Lenguajes2):", diferencia)

# Diferencia simétrica
diferencia_simetrica = lenguajes1.symmetric_difference(lenguajes2)
print("Diferencia simétrica:", diferencia_simetrica)
# Variables
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

# Convertir un entero a string
my_int_to_str_variable = str(my_int_variable)
print(my_string_variable)
print(type(my_string_variable))

# Len cuenta la cantidad de items en un contenedor, ya sea de str, array o list
print(len([1,2]))

# Variables en una sola linea 
# ¡Cuidado, es una mala práctica abusar de esta sintaxis!
name, surname, age = "Elias", "Cando", 23
print(name,surname, ", y tengo", age, "años")

# Inputs por consola
name = input('Cuál es tu nombre?: ')
age = input('Cuantos años tienes?: ')

print(name)
print(age)

# Cambiar su tipo
name = 23
age = "Elias"
print(name)
print(age)
list_num = [1,2,3,4,1,2,5,6,8] 

"""sets para la list comprenhension"""
set_pares = {num for num in list_num if num %2==0} 
print(set_pares)

vocales = "aeiou"

"""diccionarios para la list comprenhension"""
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)
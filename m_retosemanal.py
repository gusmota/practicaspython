def crear_listas(lista, elemento):
    """Guarda elementos en una lista"""
    lista.append(elemento)
    return lista

def comparar_listas(original, norepetidos):
    """compara dos listas"""
    list1 = set(original)
    list2 = set(norepetidos)

    return list(list1 & list2)

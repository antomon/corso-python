


def rimuovi_duplicati(lista):
    visti = set()
    
    lista_senza_duplicati = [elemento 
                             for elemento in lista 
                             if elemento not in visti and not visti.add(elemento)]
    
    return lista_senza_duplicati

# Esempio di utilizzo
lista = [4, 2, 2, 3, 1, 4, 5]

print(rimuovi_duplicati(lista)) 

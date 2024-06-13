



def rimuovi_duplicati(lista):
  return sorted(dict.fromkeys(lista))

# Esempio di utilizzo
lista = [4, 2, 2, 3, 1, 4, 5]

print(rimuovi_duplicati(lista)) 
def analizza_tupla(tupla):  # <1>
  match tupla:  # <2>
    case (x, (y, z)):  # <3>
      print(f"Primo elemento: {x}, Secondo elemento: ({y}, {z})")  # <4>
        
    case (x, y):  # <5>
      print(f"Primo elemento: {x}, Secondo elemento: {y}")  # <6>

    case _:  # <7>
      print("Pattern non riconosciuto")  # <8>

# Esempi di utilizzo della funzione
analizza_tupla((1, (2, 3)))  # <9>
analizza_tupla((1, 4))  # <10>
analizza_tupla((1, 2, 3))  # <11>

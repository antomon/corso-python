class MiaClasse:  # <1>
  def __init__(self, valore):  # <2>
    self.__valore = valore  # <3>

  def visualizza_valore(self):  # <4>
    return self.__valore  # <5>

  def __metodo_privato(self):  # <6>
    return "Questo è un metodo privato"  # <7>

istanza = MiaClasse(10)  # <8>

print(istanza.visualizza_valore())  # <9>

try:
  print(istanza.__valore)  # <10> 

except Exception as e:
  print(e)

print(istanza._MiaClasse__valore)  # <11>

try:
  print(istanza.__metodo_privato())  # <12> 

except Exception as e:
  print(e)

print(istanza._MiaClasse__metodo_privato())  # <13>

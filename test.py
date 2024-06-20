class MiaClasse:  # <1>
  primo_attributo = "esempio"  # <2>
  
  def primo_metodo(self):  # <3>
    return "Ciao, mondo!"  # <4>

print(MiaClasse.primo_attributo)  # <5>

print(MiaClasse.primo_metodo(None))  # <6>
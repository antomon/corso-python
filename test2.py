def compatibilita_indietro(f):  # <1>
  def involucro(*args, **kwargs):  # <2>
    try:
      return f(*args, **kwargs)  # <3>

    except TypeError as e:  # <4>
      if "positional argument" in str(e):  # <5>
        return f(args[0])  # <6>

      raise e  # <7>

  return involucro  # <8>

@compatibilita_indietro  # <9>
def nuova_funzione(nome, messaggio="Ciao!"):  # <10>
  print(f"{messaggio} {nome}")

nuova_funzione("Mondo", messaggio="Salve")  # <11> 

nuova_funzione("Mondo")  # <12> 
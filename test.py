


def outerFunction():
  def localFunction():  # <1>
    print("Funzione locale")

  localFunction()  # <2>

outerFunction()

localFunction()  # <3> Errore: localFunction non è visibile qui
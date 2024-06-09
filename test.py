import string

def conta_parole(frase, maiuscolo_minuscolo=False):
  if not maiuscolo_minuscolo:
    frase = frase.lower()

  frase = ''.join(carattere for carattere in frase if carattere not in string.punctuation)

  parole = frase.split()

  conteggio = {}

  for parola in parole:
    if parola in conteggio:
      conteggio[parola] += 1

    else:
      conteggio[parola] = 1

  return conteggio

# Esempio di utilizzo
frase = "Ciao, ciao! Come stai? Ciao."

print(conta_parole(frase, maiuscolo_minuscolo=False))  # <1>
print(conta_parole(frase, maiuscolo_minuscolo=True))  # <2>
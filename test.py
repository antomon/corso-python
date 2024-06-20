import json  # <1>

def converti_valore(valore):
  if isinstance(valore, str):
    try:
      valore_convertito = int(valore)  # <2> 

    except ValueError:
      try:
        valore_convertito = float(valore)  # <3>
      except ValueError:
        valore_convertito = valore  # <4>

  else:
    valore_convertito = valore

  return valore_convertito

def leggi_file_json(nome_file):
  with open(nome_file, 'r') as file:  # <5>
    dati = json.load(file)  # <6>
    
    dati_convertiti = {}

    for chiave, valore in dati.items():
      chiave_convertita = converti_valore(chiave)

      if isinstance(valore, list):
        valore_convertito = [converti_valore(v) for v in valore]

      else:
        valore_convertito = converti_valore(valore)
          
      dati_convertiti[chiave_convertita] = valore_convertito
  
    print(dati_convertiti)  # <7>

def crea_file_json(nome_file):
  dati = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30,  
    "altezza": 1.75,  
    "hobby": ["lettura", "pittura", "ciclismo"],  
    "punteggi": [8, 90, 78],  
    "info": {"stato_civile": "sposato", "figli": 2}  
  }
  with open(nome_file, 'w') as file:  # <8>
    json.dump(dati, file, indent=4)  # <9>

crea_file_json("esempio.json")

leggi_file_json("esempio.json")

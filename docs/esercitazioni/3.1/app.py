from flask import Flask, render_template, request  
import requests  

app = Flask(__name__)  

GOOGLE_API_KEY = "INSERIRE CHIAVE API GOOGLE MAPS"


@app.route('/', methods=['GET', 'POST'])  
def home():
  if request.method == 'POST':  
    indirizzo = request.form['indirizzo']  
    visualizzazione = request.form['visualizzazione']  

    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?" + \
                  f"address={indirizzo}&key={GOOGLE_API_KEY}"  

    response = requests.get(geocode_url)  
    data = response.json()  

    if data['status'] == 'OK':  
      result = data['results'][0]  
      dettagli = {  
        'Indirizzo Formattato': result['formatted_address'],
        'Latitudine': result['geometry']['location']['lat'],
        'Longitudine': result['geometry']['location']['lng'],
        'Tipo di Luogo': result['types']
      }
    else:
      dettagli = None  

    return render_template('mappa.html',
                           indirizzo=indirizzo,
                           visualizzazione=visualizzazione,
                           dettagli=dettagli,
                           api_key=GOOGLE_API_KEY)  

  return render_template('index.html')  


@app.route('/route', methods=['GET', 'POST'])  
def route():
  if request.method == 'POST':  
    start = request.form['start']  
    end = request.form['end']  

    return render_template('route.html',
                           start=start,
                           end=end,
                           api_key=GOOGLE_API_KEY)  

  return render_template('route_form.html')  


if __name__ == '__main__':
  app.run(debug=True)  

from flask import Flask, render_template, request  # <1>

app = Flask(__name__)  # <2>

@app.route('/', methods=['GET', 'POST'])  # <3>
def home():
    if request.method == 'POST':  # <4>
        indirizzo = request.form['indirizzo']  # <5>
        visualizzazione = request.form['visualizzazione']  # <6>
        return render_template('mappa.html', 
                               indirizzo=indirizzo, 
                               visualizzazione=visualizzazione)  # <7>
    return render_template('index.html')  # <8>

if __name__ == '__main__':
    app.run(debug=True)  # <9>

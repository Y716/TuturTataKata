import requests
import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=["GET", "POST"])
def index():
    hasil_definisi = []
    hasil_kata_relevan = []
    kata_dicari = None
    
    if request.method == "POST":
        kata_dicari = request.form.get('keyword')
        return redirect(url_for('index', q=kata_dicari))
    elif request.method == "GET":
        query = request.args.get("q")
        if query != None:
            kata_dicari = query
            hasil_definisi, hasil_kata_relevan = cari_kata(query)
        else:
            hasil_definisi = []
            hasil_kata_relevan = []
            kata_dicari = None
    
    return render_template('index.html',
                           definitions = hasil_definisi,
                           relations = hasil_kata_relevan,
                           keyword = kata_dicari,
                           )

@app.route("/api/definisi/<string:kata>")
def definisi_kata(kata):
    definisi = jabar_kata(kata)
    return flask.jsonify(definisi)

def cari_kata(kata: str) -> tuple[list, list]:
    try:
        url = 'https://kateglo.lostfocus.org/api.php?format=json&phrase='+kata
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        print(f"Terjadi Kesalahan: {e}")
        data = None
        return
    definitions = []
    
    for i in range(len(data['kateglo']['definition'])):
        try:
            definitions.append(data['kateglo']['definition'][i]['def_text'])
        except requests.exceptions.RequestException as e:
            print(f"Terjadi Kesalahan: {e}")
            data = None
    
    relations = {}
    for i in range(len(data['kateglo']['relation']['s'])-1):
        relations[data['kateglo']['relation']['s'][str(i)]['related_phrase']] = data['kateglo']['relation']['s'][str(i)]['rel_type_name']
    return definitions, relations

def jabar_kata(kata: str) -> list:
    try:
        url = 'https://kateglo.lostfocus.org/api.php?format=json&phrase='+kata
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        print(f"Terjadi Kesalahan: {e}")
        data = None
    definitions = []
    for i in range(len(data['kateglo']['definition'])):
        try:
            definitions.append(data['kateglo']['definition'][i]['def_text'])
        except requests.exceptions.RequestException as e:
            print(f"Terjadi Kesalahan: {e}")
            data = None
    return definitions


if __name__ == "__main__":
    app.run()
import flask
import requests

def cari_kata(kata: str) -> list:
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
        definitions.append(data['kateglo']['definition'][i]['def_text'])
    
    relations = []
    for i in range(len(data['kateglo']['all_relation'])):
        relations.append(data['kateglo']['all_relation'][i]['related_phrase'])
    
    return definitions, relations

def jabar_kata(kata):
    # TODO: Menjabarkan kata yang berelasi
    return kata

definitions, relations = cari_kata("kata")
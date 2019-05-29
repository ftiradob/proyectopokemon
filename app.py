import json
import requests
import os
port=os.environ["PORT"]

from flask import Flask, render_template
app=Flask(__name__)
URL_BASE="https://pokeapi.co/api/v2/"
URL_BASETCG="https://api.pokemontcg.io/v1/"
listainiciales=["bulbasaur","charmander","squirtle","chikorita","cyndaquil","totodile","treecko","chimchar","piplup","snivy","tepig","oshawott","chespin","fennekin","froakie","rowlet","litten","popplio"]

def mostrariniciales():
	listaimagenes=[]
	for i in listainiciales:
		r=requests.get(URL_BASE+"pokemon/"+i)
		if r.status_code==200:
			doc=r.json()
			listaimagenes.append(doc["sprites"]["front_default"])
		else:
			print("Error en la petición")
	return listaimagenes

def mostrarnombreiniciales():
    listanombres=[]
    for i in listainiciales:
        r=requests.get(URL_BASE+"pokemon/"+i)
        if r.status_code==200:
            doc=r.json()
            for pokemon in doc["forms"]:
                listanombres.append(pokemon["name"])
        else:
            print("Error en la petición")
    return listanombres

def mostrarnumeropokedex():
    listapokedex=[]
    for i in listainiciales:
        r=requests.get(URL_BASE+"pokemon/"+i)
        if r.status_code==200:
            doc=r.json()
            listapokedex.append(doc["id"])
        else:
            print("Error en la petición")
    return listapokedex

def muestradescripcion():
    encontrado=False
    objeto=input("Indique el Pokemon: ")
    r=requests.get(URL_BASE+"item/"+objeto)
    if r.status_code==200:
        doc=r.json()
        for idioma in doc["flavor_text_entries"]:
            if idioma["language"]["name"]=="es" and encontrado==False:
                print(idioma["text"])
                encontrado=True
    else:
        print("Error en la petición")


@app.route('/',methods=["GET","POST"])
def inicio():
	listaimagenes=mostrariniciales()
	listanombres=mostrarnombreiniciales()
	listapokedex=mostrarnumeropokedex()
	return render_template("index.html",lista=zip(listaimagenes,listanombres,listapokedex))

@app.route('/nivel',methods=["GET","POST"])
def nivel():
	return render_template("nivel.html",listaobjetos=zip())


app.run('0.0.0.0',int(port), debug=True)

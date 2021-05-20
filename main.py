from flask import Flask,jsonify
import requests
import simplejson
import json

app = Flask(__name__)
uriname = "https://api.namefake.com/"
urijoke = "http://api.icndb.com/jokes/random?firstName=John&lastName=Doe&limitTo=[nerdy]/"


@app.route("/")
def home():

    try:
        uResponsename = requests.get(uriname)
    except requests.ConnectionError:
       return "Connection Error"
    Jresponsename = uResponsename.text
    dataname = json.loads(Jresponsename)
    name = dataname["name"]

    try:
        uResponsejoke = requests.get(urijoke)
    except requests.ConnectionError:
       return "Connection Error"
    Jresponsejoke = uResponsejoke.text
    datajoke = json.loads(Jresponsejoke)
    joke = datajoke["value"]["joke"]

    return joke.replace('John Doe',name)

if __name__ == "__main__":
    app.run(debug = True)
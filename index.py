import os
from flask import Flask
from flask import render_template
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/")
def main():
    client = MongoClient(
        "mongodb+srv://ayusintyaadewi:sintya2203*@cluster0-mdyzg.gcp.mongodb.net/test?retryWrites=true")

    db = client.mahasiswa
    collection = db.mahasiswa
    cursor = collection.find({})

    result = ""

    for mahasiswa in cursor:
        result += dumps(mahasiswa)
        result += "\n"

    return render_template("index.html", data=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

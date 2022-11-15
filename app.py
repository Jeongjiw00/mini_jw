from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.aufj7ib.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/jiwoo", methods=["POST"])
def jiwoo_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.jiwoo.insert_one(doc)

    return jsonify({'msg': '방명록 남기기 완료!'})


@app.route("/jiwoo", methods=["GET"])
def jiwoo_get():
    jiwoo_list = list(db.jiwoo.find({}, {'_id': False}))
    return jsonify({'jiwoos': jiwoo_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

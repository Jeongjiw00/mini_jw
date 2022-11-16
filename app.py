from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.aufj7ib.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/member_jw')
def member_jw():
    return render_template('member_jw.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route("/comment", methods=["POST"])
def jiwoo_post():
    guest_jw_receive = request.form['guest_jw_give']
    cmt_jw_receive = request.form['cmt_jw_give']

    doc = {
        'name': guest_jw_receive,
        'comment': cmt_jw_receive
    }

    db.member_jw.insert_one(doc)

    return jsonify({'msg': '방명록 남기기 완료!'})

@app.route("/comment", methods=["DELETE"])
def jiwoo_delete():
    guest_jw_receive = request.form['guest_jw_give']
    cmt_jw_receive = request.form['cmt_jw_give']


    doc = {
        'name': guest_jw_receive,
        'comment': cmt_jw_receive
    }

    db.member_jw.delete_one(doc)

    return jsonify({'msg': '방명록 삭제하기 완료!'})

@app.route("/comment", methods=["GET"])
def member_jw_get():
    member_jw_list = list(db.member_jw.find({}, {'_id': False}))
    return jsonify({'member_jw': member_jw_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


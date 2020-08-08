from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 1. 클라이언트가 준 name, count, address, phone 가져오기
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    # 2. DB 에 정보 삽입하기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)
    # 3. 성공여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 등록되었습니다'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 1. DB에서 주문 정보 모두 가져오기
    orders = list(db.homework.find({}, {'_id': 0}))
    # 2. 성공여부 & 주문 목록 반환하기
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)

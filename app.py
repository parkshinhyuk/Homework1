from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']
    data = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone}

    db.dbhomework.insert_one(data)

    return jsonify({'result': 'success', 'msg': '주문완료 !!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    all_data = list(db.dbhomework.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'all_orders': all_data})
# //다시 데이터를 보내줌~!json으로 그래서 ajax로 데이터 조회(GET방식)를 응대해줌

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
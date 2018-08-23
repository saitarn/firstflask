from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

mystores = [
    {
        'name': 'My Wonderful Store',
        'item': [{'name': 'My Item', 'price': 15.99}]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - used to recieve data
# GET -  used to send data back only

# CREATE STORE
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    mystores.append(new_store)
    return jsonify(new_store)

# SHOW SPECIFIC STORE
# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # iterate ver mystores
    for store in mystores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    # if the store name matches, return it
    # if not match , return an error message

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores1': mystores})

# CREATE ITEM IN SPECIFIC STORE
# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in mystores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# SHOW ITEM IN SPECIFIC STORE
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # 'http://127.0.0.1:5000/store/some_name/item'
def get_item_in_store(name):
    for store in mystores:
        if store['name'] == name:
            return jsonify(store['item'])
    return jsonify({'message': 'store not found'})

app.run(port=5000)
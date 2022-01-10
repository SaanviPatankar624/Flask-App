from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{
    'contact': "9987644456",
    'name': u'Raju',
    'id': 1,
    'done': False
},
    {
    'contact': "9876543222",
    'name': u'Rahul',
    'id': 2,
    'done': False
}]

@app.route("/")
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)
    contact = {
        'id': data[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', " "),
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added successfullu!"
    })
 
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": data
    })


if (__name__ == "__main__"):
    app.run(debug=True)

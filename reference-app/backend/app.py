from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

metrics = PrometheusMetrics(app)
mongo = PyMongo(app)

metrics.info('app_info', 'Application info', version='1.0.3')

@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


@app.route("/error-400")
@metrics.summary('requests_by_status_4xx', 'Status Code', labels={
    'code': lambda r: '400'
})
def oops_400():
    return ":(", 400

@app.route("/error")
@metrics.summary('requests_by_status_5xx', 'Status Code', labels={
    'code': lambda r: '500'
})
def oops():
    return ":(", 500

if __name__ == "__main__":
    app.run(debug=False)

import os
import shutil
from flask import Flask, jsonify, request
from recommender import Recommender
from multiprocessing import Process, Value

application = Flask("recommender")
model_path = os.environ.get("MODEL_PATH", "data/recommender.pickle")
if not os.path.exists(model_path):
    shutil.copyfile("data/empty.pickle", model_path)

recommender = Recommender.load(model_path)
reload = Value("b", False)


def get_model():
    global recommender
    if reload.value:
        recommender = Recommender.load(model_path)
        reload.value = False
    return recommender


@application.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500


@application.route("/recommend/<int:user_id>")
def recommend(user_id):
    limit = int(request.args.get('limit', 50))
    recommendations = get_model().recommend_for_user(user_id, limit)
    return jsonify(recommendations)


@application.route("/similar/<int:post_id>")
def similar(post_id):
    limit = int(request.args.get('limit', 50))
    recommendations = get_model().recommend_for_post(post_id, limit)
    return jsonify(recommendations)


@application.route("/metrics")
def metrics():
    metrics = jsonify(get_model().metrics())
    return metrics, 200


@application.route("/train", methods=["PUT"])
def train():
    process = Process(target=train_model, args=(reload,))
    process.start()
    return "", 201


def train_model(reload):
    Recommender.create()
    reload.value = True

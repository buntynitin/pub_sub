import requests
from flask import Blueprint
from flask import request, jsonify
from .validation import ListConfigSchema

list_config = Blueprint('list_config', __name__)
list_config_schema = ListConfigSchema()


@list_config.route('/list_config', methods=['GET'])
def list_config_get():
    try:
        res = requests.get('.../action_hub/get_list_config')
        return jsonify(res.text), 200
    except():
        return jsonify({"error": "Something went wrong"}), 400


@list_config.route('/list_config', methods=['POST'])
def list_config_post():
    errors = list_config_schema.validate(request.json)
    if errors:
        return jsonify({"error": errors}), 400
    else:
        return jsonify({"message": "Your upload request has been submitted"}), 200
    # try:
    #     producer.send(request.json['topic_name'], request.json['key'], request.json['data'])
    #     return jsonify({"message": "Your upload request has been submitted"}), 200
    # except():
    #     return jsonify({"error": "Something went wrong"}), 400

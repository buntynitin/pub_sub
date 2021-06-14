import requests
from flask import Blueprint
from flask import request, jsonify
from .validation import ListAssociationSchema

list_association = Blueprint('list_association', __name__)
list_association_schema = ListAssociationSchema()


@list_association.route('/list_association', methods=['GET'])
def list_association_route_get():
    try:
        res = requests.get('.../action_hub/get_list_association')
        return jsonify(res.text), 200
    except():
        return jsonify({"error": "Something went wrong"}), 400


@list_association.route('/list_association', methods=['POST'])
def list_association_route_post():
    errors = list_association_schema.validate(request.json)
    if errors:
        return jsonify({"error": errors}), 400
    else:
        return jsonify({"message": "Your upload request has been submitted"}), 200
    # try:
    #     producer.send(request.json['topic_name'], request.json['key'], request.json['data'])
    #     return jsonify({"message": "Your upload request has been submitted"}), 200
    # except():
    #     return jsonify({"error": "Something went wrong"}), 400

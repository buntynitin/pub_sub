import requests
from flask import Blueprint
from flask import request, jsonify
from .validation import ReportSchema
from myproducer import producer

report = Blueprint('report', __name__)
report_schema = ReportSchema()


@report.route('/report', methods=['GET'])
def report_route_get():
    try:
        res = requests.get('.../action_hub/get_reports')
        return jsonify(res.text), 200
    except():
        return jsonify({"error": "Something went wrong"}), 400


@report.route('/report', methods=['POST'])
def report_route_post():
    errors = report_schema.validate(request.json)
    if errors:
        return jsonify({"error": errors}), 400
    else:
        try:
            producer.send(request.json['topic_name'], request.json['key'], request.json['data'])
            return jsonify({"message": "Your upload request has been submitted"}), 200
        except():
            return jsonify({"error": "Kafka Service Unavailable"}), 503

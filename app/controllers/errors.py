from flask import jsonify

def missing_params_error(param: str):
    return jsonify({"missing param": param}), 400

def missing_field_error(field: str):
    return jsonify({"missing field": field}), 400
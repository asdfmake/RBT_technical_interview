from flask import jsonify

def missing_params_error(param: str):
    return jsonify({"missing param": param}), 400
from flask import jsonify

def missing_params_error(param: str):
    return jsonify({"message": f"missing param {param}"}), 400

def missing_field_error(field: str):
    return jsonify({"message": f"missing field {field}"}), 400

def wrong_date_format():
    return jsonify({"message": "wrong date format"}), 400

def invalid_credentials():
    return jsonify({"error": "Invalid credentials"}), 401
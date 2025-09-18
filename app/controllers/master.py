from flask import jsonify, request

def home():
    return jsonify({"message": "Welcome to the User Management API"})
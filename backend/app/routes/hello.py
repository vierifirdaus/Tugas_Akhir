from flask import Blueprint, request, jsonify
hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/', methods=['GET'])
def hello_ges(): 
    return jsonify("Halo ges ini web vieri"), 200
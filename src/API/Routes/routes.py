from API import app
from flask import json, request, jsonify, Flask, render_template_string
from Controllers import receive_xml, get_data
import base64

@app.route("/", methods=["Get"])
def home():
    return "hello world!"

@app.route("/XML", methods=["Get"])
def xml_standard():
    
    try:
        req = request.query_string
        decodedText = base64.b64decode(req)
        d   = receive_xml(decodedText)
            
        return jsonify({"Data": [d]}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}),400
   
@app.route("/addTag", methods=["Post"])
def add_tag():
    try:
        req = request.json
        xml = request.query_string
        d   = get_data(xml, req)
        return jsonify({"Data": d})
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

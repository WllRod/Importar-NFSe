import xmltodict, json
from Errors import generate_error_message
from flask import jsonify

def return_json(xml):
    try:
        o   = xmltodict.parse(xml)
        j   = json.dumps(o)
        return json.loads(j)
    except Exception as e:
        generate_error_message(
            str(e),
            __file__
        )
        
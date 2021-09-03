import xmltodict, json

def return_json(xml):
    
    o   = xmltodict.parse(xml)
    j   = json.dumps(o)
    return json.loads(j)
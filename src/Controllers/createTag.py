import base64
from Components import return_json, returnValue
import xml.etree.ElementTree as ET
import os, sys, json
from Models import MongoConnector

def _finditem(obj, key, list):
    if key in obj: 
        #list.append(key)
        return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            
            item = _finditem(v, key, list)
            if item is not None:
                if k not in list:
                    list.append(k)
                return item

def verify_file_existance():
    FILE_PATH   = os.path.dirname(sys.argv[0])+"\\Tags.json"
    
    if not os.path.exists(FILE_PATH):
        DICT        = {}
        with open(FILE_PATH, "w") as f:
            json.dump(DICT, f, indent=4)
        f.close()

def verify_key_existance(jsonData, key, list):
    if key not in list:
        jsonData.j[key] = {}
    jsonData.set_data(jsonData.j)

def verify_subkeys_existance(jsonFile, dictReq, cityCode):
    jsonFileKeys    = [ i for i in jsonFile.j[cityCode].keys() ]
    for k, v in dictReq[cityCode].items():
        if k not in jsonFileKeys:
            if isinstance(v, list):
                jsonFile.j[cityCode][k] =   []
            elif isinstance(v, str):
                jsonFile.j[cityCode][k] = v
    jsonFile.set_data(jsonFile.j)

def set_data(dict, newArray):
    
    j   = dict
    array   = []
            
    itemFounded =  _finditem(j, newArray[0], array)
    
    newList    = [i for i in reversed(array)]
    for x in newArray:
        newList.append(x)
    
    return ';'.join(newList)

def get_data(xml, dict):
    #verify_file_existance()
    xml         = base64.b64decode(xml)
    j           = return_json(xml)
    
    errorArray      = []

    codCidade   = [ i for i in dict.keys()][0]
    mongo       = MongoConnector()
    jsonFile    = mongo.get_data()
    
    verify_key_existance(jsonFile, codCidade, [i for i in jsonFile.j.keys()])
    verify_subkeys_existance(jsonFile, dict, codCidade)
    create_values_json_file(dict[codCidade], j, jsonFile, codCidade)

def create_values_json_file(dictReq, xmlJson, jsonFile, codCidade):
    te  = [ i for i in dictReq if isinstance(dictReq[i], list)]
    errorArray  = []
    for x in te:
        
        for b in dictReq[x]:
            t    = verify_xml_tag_json(xmlJson, b.split(";"))
            if t[0] != []:
                errorArray.append(';'.join(t[0][0]))
            
            if  t[2] not in jsonFile.j[codCidade][x]:
                jsonFile.j[codCidade][x].append(t[2])
    
    if not errorArray:
        jsonFile.set_data(jsonFile.j)
    else:
        text    = "As Tag's a seguir não foram encontradas: \n"
        for i in errorArray:
           text += "\t"+i+"\n"
        raise Exception(text)
            # saveData    = set_data(xmlJson, b.split(";"))
            
            # returnData  = returnValue([saveData], xmlJson, tempErrorList)
            # print(returnData)
            # if tempErrorList:

            #     errorArray.append(';'.join(tempErrorList[0]))
            # if (
            #         returnData is not None
            #         and saveData not in jsonFile.j[codCidade][x]
            #     ):
            #         jsonFile.j[codCidade][x].append(saveData)

def verify_xml_tag_json(xmlJson, valueToFound):
    tempErrorList   = []
    saveData    = set_data(xmlJson, valueToFound)
    returnData  = returnValue([saveData], xmlJson, tempErrorList)
    return (tempErrorList, returnData, saveData)
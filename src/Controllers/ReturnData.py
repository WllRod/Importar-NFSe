from typing import Dict
from Components import returnValue, return_json
import regex, unicodedata
from .HandleFile import Handle_Json
from Models import MongoConnector

def format_xml(xml:str):
    xml = xml.decode('utf-8')
    if xml[0:1] != "<": return xml[xml.find("<"):]
    return xml

def read_xml_tag(list, response):
    for i in list:
        for b in i:
            value   = returnValue(
                [b],
                response
            )
            if value is not None:
                return value
    return None

def return_compressed_list(dictData, key, list):
    MAX_LENGHT  = 0
    return [dictData[v][key] for v in list]

"""RECEBENDO A ESTRUTURA DO XML DE ORIGEM DO ADVPL"""
def receive_xml(xml:dict):
    
    resp        = return_json(format_xml(xml))
    bdResponse  = MongoConnector()
    jsonData    = bdResponse.get_data()
    codCidade   = [i for i in jsonData.keys()]
    if not codCidade:
        raise Exception("Nenhuma cidade cadastrada no arquivo!")

    data        = { i: "" for i in jsonData[codCidade[0]] }
    estado      = return_compressed_list(jsonData, "TAG_ESTADO", codCidade)

    estado      = read_xml_tag(
        estado,
        resp
    )

    codMunTag   = return_compressed_list(jsonData, "TAG_CODMUN", codCidade)
    cidade      = read_xml_tag(
        codMunTag,
        resp
    )

    if cidade is None:
        return extract_data_city_tag(jsonData, codCidade, resp, data)

    return set_dict_data(data, jsonData[cidade], resp)

def extract_data_city_tag(jsonData, codCidade, resp, data):
    tagCid  = return_compressed_list(jsonData, "TAG_CIDADE", codCidade)
    cidade  = read_xml_tag(
        tagCid,
        resp
    )
    if cidade is None:
        raise Exception("Cidade não encontrada!")

    cidade  = regex.sub(r'\p{Mn}', '', unicodedata.normalize('NFKD', cidade.upper()))
    cidade  = [ i for i in jsonData if jsonData[i]["CIDADE"] == cidade][0]
    return set_dict_data(data, jsonData[cidade], resp)

def set_dict_data(data, json, resp):
    for v in data:
        data[v] = returnValue(
            json[v],
            resp
        )
    return data

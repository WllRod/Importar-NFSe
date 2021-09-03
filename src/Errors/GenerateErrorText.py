import os, sys, traceback
from datetime import datetime
from flask import jsonify

def generate_error_message(error, fileName):
    exc_type, exc_obj, exc_tb   = sys.exc_info()
    filename    = os.path.basename(os.path.dirname(fileName))+"\\"+os.path.basename(fileName)
    date        = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    stk     = traceback.extract_tb(sys.exc_info()[-1], 1)
    fName   = stk[0][2]
    raise Exception(f"{date}\nArquivo: {filename}\nFunção: {fName}\nLinha com erro: {exc_tb.tb_lineno}\nErro: {error}")

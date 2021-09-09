from .GenerateErrorText import generate_error_message
import traceback

def error_decorator(__file__, errors=(Exception, )):
    def wrapper(f):
        def wrapped(*args):
            try:
                return f(*args)
            except errors as e:
                import os, sys

                exc_type, exc_obj, exc_tb   = sys.exc_info()
                
                generate_error_message(
                    Nome_Arquivo=os.path.basename(os.path.dirname(__file__))+"\\"+os.path.basename(__file__),
                    Funcao=f.__name__,
                    Linha=e.__traceback__.tb_lineno,
                    Erro=str(e)
                )
        return wrapped
            
    return wrapper
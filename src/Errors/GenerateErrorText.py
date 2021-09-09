from datetime import datetime


def generate_error_message(**kwargs):
    date    = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    text    = f"[{date}]\n"
    for k, v in kwargs.items():
        text    += f"[{k}] - {v}\n"
    
    raise Exception(text)
    
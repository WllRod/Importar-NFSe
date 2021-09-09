def decorator(f):
    def wrapper(*args):
        
       f(*args)
       
    return wrapper

@decorator
def teste(*args):
    (d, s) = args
    print(d, s)

teste(1, 2)

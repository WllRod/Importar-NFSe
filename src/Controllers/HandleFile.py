import json
import sys, os

class Handle_Json():
    def __init__(self):
        self.local_path  = os.path.dirname(sys.argv[0])
        with open(self.local_path+"\\Tags.json", "r") as f:
            self.j   = json.load(f)
        f.close()
    
    def return_data(self):
        return self.j
    
    def set_data(self, data):
        with open(self.local_path+"\\Tags.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
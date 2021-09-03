
from Errors import generate_error_message

def returnValue(jsonList, tempData, errorList=None):
    try:
        for x in range(len(jsonList)):
            splited = jsonList[x].split(";")
            
            for c in range(len(splited)):
                
                if splited[c] not in tempData: 
                    
                    if errorList is not None: errorList.append([splited[i] for i in range(splited.index(splited[c])+1)])
                    break
                
                if splited[c] == splited[-1]: 
                    
                    return tempData[splited[c]]
                
                tempData = tempData[splited[c]]
        return None
    except Exception as e:
        generate_error_message(
            str(e),
            __file__
        )
def getCypress(value):
    print ("received %s" %value)

def sendCypress(value):
    print ("received %s" %value)


def processRequest(data):

    robot_directional = {'forward','backward','CW','CCW','clear','auto'}

    result=""
    result2=""
    result3=""
    result4=""

    if data in robot_directional:
        if(data=="forward"):
            result = getCypress("forw")
        elif(data=="backward"):
            result = getCypress("back")
        elif(data=="CW"):
            result = getCypress("cloc")
        elif(data=="CCW"):
            resutl = getCypress("ccws")
        elif(data=="stop"):
            result = getCypress("stop")
        elif(data=="hold"):
            result = getCypress("hold")
    else:
        result=getCypress(data)
    

import cv2

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    #Infinite loop
    while result:
        #ret- boolean = true or false
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    
    #release
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()
    




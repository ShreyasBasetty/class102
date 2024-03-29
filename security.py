import cv2
import dropbox
import time
import random

start_time = time.time()

#take_snapshot()

def take_snapshot():

    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read(0)
        img_name = "imsg"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result=False
    return img_name
    print("snapshot taken")
    vdieoCaptureObject.release()
    cv2.destroyAllWindows()


#upload_file()
def upload_file(img_name):
    access_token = "sl.Bufvg65FVgWu_RcCXGXPEjmLSx86Vu5A9K_bgUa3MN-qDF2Pgaes8NPRgo65k8uPiPC5J3ks_ErxeEXl74IKRjsguCeFc5Jpyy_Dj9osZ9blPDjINdvH5FIomHKK2RT7cuorwILg_lBRTC7k7d91vKk"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx =- dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()

import cv2 as cv
import Handtrackingmodule as htm
import time
import numpy as np
import math
import pycaw
wcam=640
hcam=480

from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
#print(f"- Muted: {bool(volume.GetMute())}")
#print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
volrange=volume.GetVolumeRange()
minvol=volrange[0]
maxvol=volrange[1]


cap=cv.VideoCapture(0)

cap.set(3,wcam)
cap.set(4,hcam)

ctime=0
ptime=0


handDetector=htm.handDetector()

while True:
    success,img=cap.read()
    img=handDetector.findHands(img)
    lms=handDetector.findPosition(img,draw=False)
    if len(lms)!=0:
       #print(lms[4],lms[8])

       x1,y1=lms[4][1],lms[4][2]
       x2,y2=lms[8][1],lms[8][2]

       cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
       cv.circle(img,(x2,y2),15,(255,0,255),cv.FILLED)
       cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
       cv.circle(img,((x1+x2)//2,(y1+y2)//2),15,(255,0,255),cv.FILLED)
       length=math.hypot(x2-x1,y2-y1)

       #Hand range 50 - 300
       #Volume range -65 - 0
       vol=np.interp(length,[50,213],[minvol,maxvol])
       print(int(length),vol)
       volume.SetMasterVolumeLevel(vol, None)

       



       if length<50:
           cv.circle(img,((x1+x2)//2,(y1+y2)//2),15,(0,255,0),cv.FILLED)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,f'FPS:{int(fps)}',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv.imshow("Image:",img)
    cv.waitKey(1)

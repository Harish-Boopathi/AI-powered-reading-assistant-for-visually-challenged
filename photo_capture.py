videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("/home/techocular/Documents/sih/result/output.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
speak('photo taken')

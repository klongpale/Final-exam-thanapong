import cv2
import numpy as np 
import numpy

cap = cv2.VideoCapture("left_output-1.mp4")
#cap = cv2.VideoCapture(0)

check ,frame1 =  cap.read()
check ,frame2 =  cap.read()

#def nothing (x):
    #pass
#cv2.namedWindow("Trackbars")
#cv2.createTrackbar("L-B" , "Trackbars" , 0 , 180 , nothing)
#cv2.createTrackbar("L-G" , "Trackbars" , 0 , 255 , nothing)
#cv2.createTrackbar("L-R" , "Trackbars" , 0 , 255 , nothing)

#cv2.createTrackbar("U-B" , "Trackbars" , 180 , 180 , nothing)
#cv2.createTrackbar("U-G" , "Trackbars" , 255 , 255 , nothing)
#cv2.createTrackbar("U-R" , "Trackbars" , 255 , 255 , nothing)

while (cap.isOpened()):
    
    if check == True :
        #L_B =cv2.getTrackbarPos("L-B","Trackbars")
        #L_G =cv2.getTrackbarPos("L-G","Trackbars")
        #L_R =cv2.getTrackbarPos("L-R","Trackbars")
        #U_B =cv2.getTrackbarPos("U-B","Trackbars")
        #U_G =cv2.getTrackbarPos("U-G","Trackbars")
        #U_R =cv2.getTrackbarPos("U-R","Trackbars")
        #upper = numpy.array([U_B,U_G, U_R]) # BGR
        #lower = numpy.array([L_B,L_G,L_R]) 
        
        upper = numpy.array([45,255, 255]) # BGR
        lower = numpy.array([25,60,100])
        mask = cv2.inRange(frame1,lower,upper)
        resu = cv2.bitwise_and(frame1,frame1,mask=mask)
        
        blur = cv2.GaussianBlur(mask,(1,1),0)
        thresh, result =cv2.threshold(blur,1,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=3)
        contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) # หาconyour 
        w_max = frame1.shape[1] / 2
        h_max = frame1.shape[0] / 2
        #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        #วาดสี่เหลี่ยมรอบสิ่งที่ต้องการ
        for contour in contours :
            (x,y,h,w) = cv2.boundingRect(contour)
            x1 = x-30
            y1 = y-30-int(w*0.55)
            org = (x1+int(w*0.5),y)
            X = (org[0]-w_max)*15/w_max
            Y = (h_max - org[1])*15/h_max
            if cv2.contourArea(contour)<2000: 
                continue
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
            text = text = 'X:' + "{:.1f}".format(X) + ' Y:' +"{:.1f}".format(Y)
            cv2.putText(frame1,text,(x,y-4),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)

        cv2.imshow("Output",dilation)
        cv2.imshow("Output2",frame1)
        cv2.imshow("Output3",resu)
        frame1 =frame2
        check, frame2 = cap.read()  
    
        if cv2.waitKey(40) & 0xFF == ord("e"):
            break
    else : 
        break
    
cap.release()
cv2.destroyAllWindows()
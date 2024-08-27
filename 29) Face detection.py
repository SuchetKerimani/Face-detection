import cv2

#casecade varieties(Classifier)= https://github.com/opencv/opencv/tree...

# +ve image: things tht hav face like animal, human etc
# -ve image: things tht dont hav face like table, tree, chair

face_cascade = cv2.CascadeClassifier('c:\\Users\\user\\OneDrive\\Desktop\\OPENCV images\\haarcascade_frontalface_default.xml')

#cv::CascadeClassifier::load to load a .xml classifier file. It can be either a Haar or a LBP classifier
#img = cv2.imread('c:\\Users\\user\\OneDrive\\Desktop\\OPENCV images\\Man.jpg')

cap = cv2.VideoCapture(0)

#while True:
while cap.isOpened():    
    _, img = cap.read()
   #_, img = cv2.imread()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #cv::CascadeClassifier::detectMultiScale to perform the detection.
    #cv.cascadeclassifier.detectMultiScale(image,scalefactor,minNeighbour)

    #image: matrix of type CV_8U containing an image where objects are detected.
    #scalefactor: Parameter specifying how much the image size is reduced at each image scale.
    #minNeighbour: Parameter specifying how many neighbors each candidate rectangle should have to keep it.

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
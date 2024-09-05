import cv2

img = cv2.imread('vida.jpeg')

if img is None:
    print("Erro: A imagem não pôde ser carregada.")
else:
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        print('Rostos não encontrados')
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (127, 0, 255), 2)        

        cv2.imshow('Detected Faces', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2

img = cv2.imread('eu.jpeg')

if img is None:
    print("Erro: A imagem não pôde ser carregada.")
else:
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
    
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes = eyes_cascade.detectMultiScale(imageGray, scaleFactor=1.2, minNeighbors=1)

    if len(eyes) == 0:
           print('Olhos não encontrados')
    else:
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (127, 0, 255), 2)        

        cv2.imshow('Detected Faces', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

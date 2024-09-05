# Face and Eye Detection with OpenCV

Este projeto demonstra como utilizar a biblioteca OpenCV para detecção de rostos e olhos em imagens. O projeto é composto por dois scripts Python que utilizam os classificadores Haarcascades para identificar rostos e olhos em imagens.

## Funcionalidades

- **Detecção de Rostos**: Um dos scripts realiza a detecção de rostos em uma imagem utilizando o classificador Haarcascades pré-treinado `haarcascade_frontalface_default.xml`. Ele desenha retângulos em volta dos rostos detectados.

- **Detecção de Olhos**: Outro script realiza a detecção de olhos em uma imagem utilizando o classificador Haarcascades `haarcascade_eye_tree_eyeglasses.xml`. Ele desenha retângulos em volta dos olhos detectados.

## Requisitos

- Python 3.x
- OpenCV (`cv2`)

Para instalar a biblioteca OpenCV, você pode usar o seguinte comando: pip install opencv-python

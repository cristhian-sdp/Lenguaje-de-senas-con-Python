# Lenguaje de Señas con Python

🙌 Hola, en este repositorio encontrarás el código del proyecto "lenguaje de señas con python".

## Introducción

👌 La lengua de señas es un medio de comunicación visual y gestual utilizado por personas sordas o con discapacidad auditiva para expresar y recibir información. Al proporcionar un código de lenguaje de señas, se busca promover la inclusión social y la participación activa de las personas sordas en la sociedad.

![Imagen de discapacidad](https://www.techtitute.com/techtitute/cursos/00143994/recursos/banner/discapacidad-auditiva-portada.jpg)

## Tecnologías Utilizadas

- Python
- OpenCV
- MediaPipe
- Scikit-learn (para SVM)
- Numpy

## Requisitos Previos

Antes de comenzar con la implementación, asegúrate de tener instaladas las siguientes bibliotecas de Python. Puedes instalarlas utilizando el siguiente comando:

```bash
pip install opencv-python mediapipe scikit-learn numpy
```

## Ejecución del Primer Código

El primer código está diseñado para capturar imágenes de las letras del abecedario en lenguaje de señas. Antes de ejecutarlo, asegúrate de tener acceso a una cámara. Al correr el código, seguirá estos pasos:

- Inicializa MediaPipe Hands y la cámara utilizando OpenCV.
- Captura 500 imágenes de cada letra del abecedario, almacenándose en carpetas separadas.
- Muestra instrucciones para cambiar a la siguiente letra después de completar la captura de imágenes.

## Ejecución del Segundo Código

Antes de ejecutar el segundo código, asegúrate de haber capturado suficientes imágenes para cada letra. Al correr el segundo código, se realizarán los siguientes pasos:

- Inicializa MediaPipe Hands y la cámara utilizando OpenCV.
- Carga las imágenes de entrenamiento desde la estructura de carpetas preparada.
- Divide el conjunto de datos en conjuntos de entrenamiento y prueba.
- Entrena un modelo SVM utilizando scikit-learn.
- Utiliza el modelo entrenado para predecir la letra de la mano en tiempo real a través de la cámara.
- Muestra la letra predicha en la ventana de la cámara.

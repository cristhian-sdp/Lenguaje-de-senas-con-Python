<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lenguaje de Señas con Python</title>
    <style>
      body {
        font-family: "Arial", sans-serif;
        line-height: 1.6;
        margin: 20px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
      }

      img {
        max-width: 90%;
        height: auto;
        border-radius: 35px;
        border: 4px solid #ff8c00;
      }

      .tech-image {
        max-width: 140px;
        border: none;
      }

      code {
        background-color: #f4f4f4;
        padding: 6px;
        border-radius: 5px;
        font-family: "Courier New", Courier, monospace;
      }

      pre {
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
        overflow: auto;
      }
    </style>
  </head>
  <body>
    <h1>lenguaje de señas con Python</h1>
    <p>
      🙌Hola en este repositorio encontrarán el código de reconocimiento de
      lenguaje de señas.
    </p>
    <h2>Introducción:</h2>
    <p>
      👌La lengua de señas es un medio de comunicación visual y gestual
      utilizado por personas sordas o con discapacidad auditiva para expresar y
      recibir información. Al proporcionar un código de lenguaje de señas, se
      busca promover la inclusión social y la participación activa de las
      personas sordas en la sociedad.
    </p>

    <img
      src="https://www.techtitute.com/techtitute/cursos/00143994/recursos/banner/discapacidad-auditiva-portada.jpg"
      alt="Imagen de discapacidad"
    />

    <h2>Tecnologías Utilizadas:</h2>
    <div class="tech-images">
      <img
        class="tech-image"
        src="https://1000marcas.net/wp-content/uploads/2020/11/Python-logo.png"
        alt="Python"
      />
      <img
        class="tech-image"
        src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*Gu37pa-mSeE-sZJa.png"
        alt="OpenCV"
      />
      <img
        class="tech-image"
        src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*Hgg6bLceoIjubE2hBiJK4g.png"
        alt="MediaPipe"
      />
      <img
        class="tech-image"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/260px-Scikit_learn_logo_small.svg.png"
        alt="Scikit-learn"
      />
      <img
        class="tech-image"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png"
        alt="Numpy"
      />
    </div>

    <h2>Requisitos Previos:</h2>
    <p>
      Antes de comenzar con la implementación, asegúrate de tener instaladas las
      siguientes bibliotecas de Python. Puedes instalarlas utilizando el
      siguiente comando:
    </p>
    <pre><code><i>pip install opencv-python mediapipe scikit-learn numpy</i></code></pre>

    <h2>Ejecución del Primer Código:</h2>
    <p>
      El primer código está diseñado para capturar imágenes de las letras del
      abecedario en lenguaje de señas. Antes de ejecutarlo, asegúrate de tener
      acceso a una cámara. Al correr el código, seguirá estos pasos:
    </p>
    <ul>
      <li>Inicializa Media Pipe Hands y la cámara utilizando OpenCV.</li>
      <li>
        Captura 500 imágenes de cada letra del abecedario, almacenándose en
        carpetas separadas.
      </li>
      <li>
        Muestra instrucciones para cambiar a la siguiente letra después de
        completar la captura de imágenes.
      </li>
    </ul>

    <h2>Ejecución del Segundo Código:</h2>
    <p>
      Antes de ejecutar el segundo código, asegúrate de haber capturado
      suficientes imágenes para cada letra. Al correr el segundo código, se
      realizarán los siguientes pasos:
    </p>
    <ul>
      <li>Inicializa Media Pipe Hands y la cámara utilizando OpenCV.</li>
      <li>
        Carga las imágenes de entrenamiento desde la estructura de carpetas
        preparada.
      </li>
      <li>
        Divide el conjunto de datos en conjuntos de entrenamiento y prueba.
      </li>
      <li>Entrena un modelo SVM utilizando scikit-learn.</li>
      <li>
        Utiliza el modelo entrenado para predecir la letra de la mano en tiempo
        real a través de la cámara.
      </li>
      <li>Muestra la letra predicha en la ventana de la cámara.</li>
    </ul>
  </body>
</html>

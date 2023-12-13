import cv2
import mediapipe as mp
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Cargar imágenes de entrenamiento
data_folder = "data"  # Asegúrate de tener la carpeta con las imágenes
letters = "abcdefghijklmnopqrstuvwxyz"
X, y = [], []

for letter in letters:
    for i in range(500):
        img_path = f"{data_folder}/{letter}/{letter}_{i}.png"
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (128, 128))  # Ajusta el tamaño según sea necesario
            X.append(img.flatten())
            y.append(letter)

X = np.array(X)
y = np.array(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo SVM
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)

# Configuración de OpenCV
cap = cv2.VideoCapture(0)  # Usa 0 para la cámara predeterminada, puedes cambiar esto según tus necesidades

# Nuevo import para drawing_utils
mp_drawing = mp.solutions.drawing_utils

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se puede abrir la cámara.")
        break

    # Convertir la imagen a RGB para mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar manos
    results = hands.process(rgb_frame)

    # Comprobar si se detecta la mano
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibuja los puntos de la mano en la imagen
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Captura una imagen de la mano cada frame
            landmarks_array = np.array([[int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])] for lm in hand_landmarks.landmark[0:21]])
            if landmarks_array.size > 0:  # Check if landmarks_array is not empty
                try:
                    x, y, w, h = cv2.boundingRect(landmarks_array)
                    hand_roi = cv2.resize(frame[y:y+h, x:x+w], (128, 128), interpolation=cv2.INTER_AREA)
                    hand_roi_gray = cv2.cvtColor(hand_roi, cv2.COLOR_BGR2GRAY)
                    hand_roi_flatten = hand_roi_gray.flatten()

                    # Realizar la predicción con el modelo SVM
                    predicted_letter = clf.predict([hand_roi_flatten])[0]

                    # Mostrar la letra predicha en la ventana
                    cv2.putText(frame, f'Letra: {predicted_letter}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                except Exception as e:
                    print(f"Error al procesar la mano: {e}")

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
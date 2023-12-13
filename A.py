import cv2
import mediapipe as mp
import os
import numpy as np

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Configuración de OpenCV
cap = cv2.VideoCapture(0)  # Usa 0 para la cámara predeterminada, puedes cambiar esto según tus necesidades
capture_count = 0
letter_count = 0
current_letter = 'a'  # Inicializar con la primera letra

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
            # (Elimina la condición de cada 30 frames para capturar más rápido)
            # Además, verifica si hemos capturado suficientes imágenes para la letra actual
            if capture_count < 500:
                # Convierte los landmarks a un array NumPy
                landmarks_array = np.array([[int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])] for lm in hand_landmarks.landmark[0:21]])

                # Define la región de la mano (ajusta según sea necesario)
                x, y, w, h = cv2.boundingRect(landmarks_array)
                hand_roi = frame[y:y+h, x:x+w]

                # Guarda la imagen en la carpeta correspondiente a la letra del abecedario
                folder_path = f"data/{current_letter}"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                cv2.imwrite(f"{folder_path}/{current_letter}_{capture_count}.png", hand_roi)

                print(f"Imagen {capture_count} capturada para la letra {current_letter}")
                capture_count += 1
            else:
                # Pide presionar una tecla para continuar con la siguiente letra
                cv2.putText(frame, f'Presiona una tecla para continuar con la letra {chr(ord(current_letter) + 1)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow("Hand Tracking", frame)
                cv2.waitKey(0)  # Espera hasta que se presione una tecla
                # Reinicia el contador y pasa a la siguiente letra
                capture_count = 0
                letter_count += 1
                current_letter = chr(ord('a') + letter_count)

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

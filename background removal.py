import cv2
import numpy as np

# Anexe a câmera indexada como 0
camera = cv2.VideoCapture(0)

# Definindo a largura do quadro e a altura do quadro como 640 X 480
camera.set(3, 640)
camera.set(4, 480)

while True:
    # Ler um quadro da câmera conectada
    status, frame = camera.read()

    # Se obtivermos o quadro com sucesso
    if status:
        # Inverta-o horizontalmente
        frame = cv2.flip(frame, 1)

        # Convertendo a imagem em RGB para facilitar o processamento
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Definindo os limites da cor verde (exemplo)
        lower_bound = np.array([100, 100, 100])  # Limite inferior (H, S, V)
        upper_bound = np.array([255, 255, 255])  # Limite superior (H, S, V)

        # Criando uma máscara para segmentar a cor verd
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # Aplicando a máscara ao quadro original
        segmented_frame = cv2.bitwise_and(frame, frame, mask=mask)

        # Exibindo o quadro segmentado
        cv2.imshow('Quadro', segmented_frame)

        # Espera de 1ms antes de exibir outro quadro
        code = cv2.waitKey(1)
        if code == 32:  # Pressione a tecla Espaço para sair
            break

# Libere a câmera e feche todas as janelas abertas
camera.release()
cv2.destroyAllWindows()
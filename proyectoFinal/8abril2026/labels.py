import os
from ultralytics import YOLO
import cv2

# 📌 CONFIGURACIÓN
input_folder = r"C:\Users\datasets\coco8\images\train"      # carpeta con imágenes
output_folder = r"C:\Users\datasets\coco8\labels\train"     # carpeta donde se guardan los .txt
model_path = "yolo26n.pt"    # modelo preentrenado

# Crear carpeta de salida
os.makedirs(output_folder, exist_ok=True)

# Cargar modelo
model = YOLO(model_path)

# Clases COCO que son vehículos (car = 2)
VEHICLE_CLASSES = [2]  # solo carros

# Procesar imágenes
for img_name in os.listdir(input_folder):
    if img_name.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(input_folder, img_name)

        # Leer imagen
        img = cv2.imread(img_path)
        h, w, _ = img.shape

        # Inferencia
        results = model(img_path)[0]

        label_lines = []

        for box in results.boxes:
            cls = int(box.cls[0])

            if cls in VEHICLE_CLASSES:
                x1, y1, x2, y2 = box.xyxy[0]

                # Convertir a YOLO format
                x_center = ((x1 + x2) / 2) / w
                y_center = ((y1 + y2) / 2) / h
                width = (x2 - x1) / w
                height = (y2 - y1) / h

                # Clase 0 (carro en tu dataset)
                label_lines.append(f"0 {x_center} {y_center} {width} {height}")

        # Guardar .txt
        txt_name = os.path.splitext(img_name)[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_name)

        with open(txt_path, "w") as f:
            f.write("\n".join(label_lines))

        print(f"✔ Etiquetado: {img_name}")
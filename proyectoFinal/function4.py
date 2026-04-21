import cv2

def opcion4():
    imagen = cv2.imread("Objetivos.jpg")
    cv2.imshow("Objetivos", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
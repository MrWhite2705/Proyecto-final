import cv2

def opcion3():
    imagen = cv2.imread("Justificacion.jpg")
    cv2.imshow("Justificación", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
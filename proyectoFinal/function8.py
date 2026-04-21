import cv2

def opcion8():
    imagen = cv2.imread("Conclusiones.jpg")
    cv2.imshow("Conclusiones", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
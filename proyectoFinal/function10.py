import cv2

def opcion10():
    imagen = cv2.imread("Equipo.jpg")
    cv2.imshow("Equipo", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
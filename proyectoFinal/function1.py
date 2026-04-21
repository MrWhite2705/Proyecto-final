import cv2

def opcion1():
    imagen = cv2.imread("Titulo.jpg")
    cv2.imshow("Titulo", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
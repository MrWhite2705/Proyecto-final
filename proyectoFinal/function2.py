import cv2

def opcion2():
    imagen = cv2.imread("Problema.jpg")
    cv2.imshow("Problema a resolver", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
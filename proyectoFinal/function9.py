import cv2

def opcion9():
    imagen = cv2.imread("Referencias.jpg")
    cv2.imshow("Referencias", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
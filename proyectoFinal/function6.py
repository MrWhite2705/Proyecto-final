import cv2

def opcion6():
    imagen = cv2.imread("Metodología.jpg")
    cv2.imshow("Metodología", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
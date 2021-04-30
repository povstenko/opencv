from matplotlib import pyplot as plt
import cv2

def imshow(image, title=""):
    (B, G, R) = cv2.split(image)
    image = cv2.merge([R, G, B])

    plt.imshow(image)
    plt.title(title)
    plt.show()
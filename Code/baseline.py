import cv2

def nearest_neighbor(image, size):
    return cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)

def bilinear(image, size):
    return cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)

def bicubic(image, size):
    return cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)

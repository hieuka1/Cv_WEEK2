import cv2
import numpy as np
from matplotlib import pyplot as plt

def increaseBrightness():
    G = cv2.imread("grayscale.jpg", 0)
    rows, cols = G.shape
    print("Nhap g:")
    g = int(input())
    for i in range(rows):
        for j in range(cols):
            if(G[i][j] + g < 256):
                G[i][j] = G[i][j] + g
            else:
                G[i][j] = 255
    cv2.imshow("G", G)
    cv2.waitKey(0)
increaseBrightness()
def reduceBrightness():
    G = cv2.imread("grayscale.jpg", 0)
    rows, cols = G.shape
    print("Nhap g:")
    g = int(input())
    for i in range(rows):
        for j in range(cols):
            if(G[i][j] - g > 0):
                G[i][j] = G[i][j] - g
            else:
                G[i][j] = 0
    cv2.imshow("G", G)
    cv2.waitKey(0)
reduceBrightness()

def Gamma():
    print("Nhap gamma:")
    y = int(input())
    G = cv2.imread("grayscale.jpg", 0)
    rows, cols = G.shape
    if(y > 1.0):
        print("Tăng gamma: ")
    else:
        print("Giảm gamma: ")
    for i in range(rows):
        for j in range(cols):
            G[i][j] = 255 * pow(G[i][j]/255, 1/y)    
    cv2.imshow("G", G)
    cv2.waitKey(0)
Gamma()
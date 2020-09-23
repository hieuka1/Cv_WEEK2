import cv2
import numpy as np
from matplotlib import pyplot as plt 
def readImg():
  G = cv2.imread("grayscale.jpg")
  C = cv2.imread("RGB.jpg", cv2.IMREAD_COLOR)
  cv2.imshow("C", C)
  cv2.waitKey(0)
  cv2.imshow("G", G)
  cv2.waitKey(0)
#readImg()
def hG():
  G = cv2.imread("grayscale.jpg",0)
  #C = cv2.imread("grayscale.jpg", cv2.IMREAD_COLOR)
  rows, cols= G.shape
  count = 0
  n = np.array([])
  i = 0
  while i < 256:
    n= np.append(n, i)
    i = i + 1
  #mảng histogram
  histogram = np.ndarray(shape=256)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(G[i][j] == p-1):
          count = count + 1
    histogram[p] = count
    count = 0
  #print(frq)
  for p in range(0, 256):
    print("h(",p, ")", "=", histogram[p])
  #kiem tra = thu vien
  histr = cv2.calcHist([G],[0],None,[256],[0,256])
  print(histr) 
  plt.plot(histr) 
  plt.show() 
#hG()
def hR():
  C = cv2.imread("RGB.jpg", cv2.IMREAD_COLOR)
  rows, cols, bands = C.shape
  count = 0
  n = np.array([])
  i = 0
  while i < 256:
    n= np.append(n, i)
    i = i + 1
  #print(n)
  #mảng histogram
  histogram = np.ndarray(shape=256)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(C[i][j][0] == p-1):
          count = count + 1
    histogram[p] = count
    count = 0
  #print(frq)
  for p in range(0, 256):
    print("h(",p, ")", "=", histogram[p])
  #kiem tra = thu vien
  histr = cv2.calcHist([C],[0],None,[256],[0,256]) 
  print(histr)
  plt.plot(histr) 
  plt.show() 
  #print(rows, cols, bands)
  #print(C.shape)
#hR()
def hGR():
  C = cv2.imread("RGB.jpg", cv2.IMREAD_COLOR)
  rows, cols, bands = C.shape
  count = 0
  n = np.array([])
  i = 0
  while i < 256:
    n= np.append(n, i)
    i = i + 1
  #mảng histogram
  histogram = np.ndarray(shape=256)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(C[i][j][1] == p-1):
          count = count + 1
    histogram[p] = count
    count = 0
  #print(frq)
  for p in range(0, 256):
    print("h(",p, ")", "=", histogram[p])
  #kiem tra = thu vien
  histr = cv2.calcHist([C],[0],None,[256],[0,256]) 
  print(histr)
  plt.plot(histr) 
  plt.show() 
  #print(rows, cols, bands)
  #print(C.shape)
#hGR()
def hB():
  C = cv2.imread("RGB.jpg", cv2.IMREAD_COLOR)
  rows, cols, bands = C.shape
  count = 0
  n = np.array([])
  i = 0
  while i < 256:
    n= np.append(n, i)
    i = i + 1
  print(n)
  #mảng histogram
  histogram = np.ndarray(shape=256)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(C[i][j][2] == p-1):
          count = count + 1
    histogram[p] = count
    count = 0
  #print(frq)
  for p in range(0, 256):
    print("h(",p, ")", "=", histogram[p])
  #kiem tra = thu vien
  histr = cv2.calcHist([C],[0],None,[256],[0,256]) 
  print(histr)
  plt.plot(histr) 
  plt.show() 
  #print(rows, cols, bands)
  #print(C.shape)
#hB()
def LuminanceImg():
  C = cv2.imread("RGB.jpg", cv2.IMREAD_COLOR)
  rows, cols, bands = C.shape
  count = 0
  n = np.array([])
  i = 0
  while i < 256:
    n= np.append(n, i)
    i = i + 1
  #print(n)
  J = np.array([[[]]])
  #print(J.shape)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        print(C[i][j][0])
        print(C[i][j][1])
        print(C[i][j][2])
        pixel = 0.299 * C[i][j][0] + 0.587 * C[i][j][1] + C[i][j][2] * 0.114
        print(pixel)
        J = np.append(J, pixel)
  #hL
  histogramL = np.ndarray(shape=256)
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(J[i][j] == p-1):
          count = count + 1
    histogramL[p] = count
    count = 0
  print("Histogram of Limage: ")
  for p in range(0, 256):
    print("h(",p, ")", "=", histogramL[p])
  #h
  histogram = np.ndarray(shape=256)
  countH = 0
  countGR = 0
  countB = 0
  count = 0
  for p in range(1, 256):
    for i in range(rows):
      for j in range(cols):
        if(C[i][j][0]== p-1):
          countH = countH + 1
        if(C[i][j][1]== p-1):
          countGR = countGR + 1
        if(C[i][j][2]== p-1):
          countB = countB + 1
    histogram[p] = 0.299*countH + 0.587*countGR + 0.114*countB
    countH = 0
    countGR = 0
    countB = 0
  print("Histogram h: ")
  for p in range(0, 256):
    print("h(",p, ")", "=", histogram[p])
  cv2.imshow("Luminance Image", J)
  cv2.waitKey(0)
#LuminanceImg()

if __name__ == "__main__":
  readImg()
  hG()
  hGR()
  hB()
  LuminanceImg()
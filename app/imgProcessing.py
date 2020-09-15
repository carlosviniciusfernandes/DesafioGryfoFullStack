import cv2
import os

def processCheckedOptions(path, options):
    processOrder = options.split('#') 

    for process in processOrder:
        print(process)
        if(process == 'flip_horizontal'):
            flip_horizontal(path)
        elif(process == 'flip_vertical'):
            flip_vertical(path)
        elif(process == 'invert_colors'):
            invert_colors(path)
        elif(process == 'blur'):
            blur(path)
        elif(process == 'edge_detect'):
            edge_detect(path)
        elif(process == 'draw_contours'):
            draw_contours(path)
    return

def flip_horizontal(imgPath):
    img = cv2.imread(imgPath)
    processedImg = cv2.flip(img, 1)
    cv2.imwrite(imgPath, processedImg)
    return 

def flip_vertical(imgPath):
    img = cv2.imread(imgPath)
    processedImg = cv2.flip(img, 0)
    cv2.imwrite(imgPath, processedImg)
    return 

def invert_colors(imgPath):
    img = cv2.imread(imgPath)
    processedImg = 255 - img
    cv2.imwrite(imgPath, processedImg)
    return 

def blur(imgPath):
    img = cv2.imread(imgPath)
    processedImg = cv2.blur(img, (13,13)) #Filtro da média de kernel 13x13
    cv2.imwrite(imgPath, processedImg)
    return 

def edge_detect(imgPath):
    img = cv2.imread(imgPath)   

    # Uncomment the choosed method and comment the others  

    # == Laplace ==
    ddepth = cv2.CV_16S
    kernel_size = 3
    filteredImg = cv2.GaussianBlur(img, (3,3), 0)
    gray_img = cv2.cvtColor(filteredImg, cv2.COLOR_BGR2GRAY)
    processedImg = cv2.Laplacian(gray_img, ddepth, ksize=kernel_size)
    abs_img = cv2.convertScaleAbs(processedImg)
    cv2.imwrite(imgPath, abs_img)

    # == Canny ==  
    # processedImg = cv2.Canny(img,125,175)
    # cv2.imwrite(imgPath, processedImg)

    return 

def draw_contours(imgPath):
    img = cv2.imread(imgPath)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imgContours = cv2.drawContours(img, contours, -1, (0,255,0), 3) # green contours on original img
    cv2.imwrite(imgPath, imgContours)

from scrapper import GoogleImageScraper
import os
import random
import cv2 as cv
import shutil

try:
    shutil.rmtree(".//images")
except Exception:
    pass
os.makedirs(".//images")

driver = ".//chromedriver.exe"
imagepath = ".//images"

print("Key word for picture...")

a = str(input(""))

key = a
num_images = 2
scrapper = GoogleImageScraper(driver,imagepath,key,num_images,True)
image_url = scrapper.find_image_urls()
scrapper.save_images(image_url)

images = os.listdir(".//images")


image1 = cv.imread(".//images//"+images[0])


blendimage = image1



kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (6,6))
morph = cv.morphologyEx(blendimage, cv.MORPH_OPEN, kernel)

result = cv.normalize(morph,None,20,255,cv.NORM_MINMAX)

result = cv.GaussianBlur(result,(2,2))

cv.imwrite("out.png",result)
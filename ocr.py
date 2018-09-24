import cv2 #Importing OpenCV Computer Vision
import argparse  #Importing Argument Parser
from PIL import Image #Its for Loading Image from our Local Computer to PIL format, It's requirement for tesseract
import os #Import OS directories permission
import pytesseract #This is our main Package Tesseract


#Command Line arguments start from here
argp = argparse.ArgumentParser()
argp.add_argument("-i", "--image", required=True,help="path to input image to be OCR'd") #It takes the Image name as a argument from images folder
argp.add_argument("-p", "--preprocess", type=str, default="thresh",help="type of preprocessing to be done") #It is for Preprocessing
#The preprocessing method can accept two values:  thresh or blur bydefault is thresh
args = vars(argp.parse_args())

im = cv2.imread(args["image"]) #Loading the image to memory
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # It converts to grayscale

cv2.imshow("Image", gray) # It will show an image which is in grayscale



if args["preprocess"] == "thresh": #if thresh argument is passed this section will start compilation
	gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] #threshold method useful to read dark text overlaid upon gray shapes


elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3) #medianblur method useful to reduce salt and pepper noise

filename = "{}.png".format(os.getpid()) #creating temporary image

cv2.imwrite(filename, gray) #this will save the image of copy to disk
text = pytesseract.image_to_string(Image.open(filename)) #It converts the content of the image to string 

print(text) # printing the result 

#Refer the PDF to how to compile
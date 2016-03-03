# Python code for picture Watermarking, 03/03/2016   
from PIL import Image, ImageDraw
import glob
import os
import sys

#Bellow is the path to the folder "Watermarked"
#"Watermarked" is the folder with the photographs that I want to watermark 
indir = "/.../Watermarked/*.*"
counter = 0

def getSize(fl):
    st = os.stat(fl)
    return st.st_size

#I start a loop reading the photographs 
for picname in glob.glob(indir):
    counter +=1
    
    #I open and read the photograph
    im = Image.open(picname)
    
    #Checking the different file sizes
    print "Size of foto #", counter, "(bytes):", getSize(picname)
    print "Size of im string #", counter, "(bytes):", sys.getsizeof(im)
      
    #I calculate the photograph's size in pixels 
    width, height = im.size 
    
    #A new image is created 
    WaterMark = Image.new("RGBA", im.size)
    
    #A new image is drawn  
    waterdraw = ImageDraw.Draw(WaterMark, "RGBA")
    
    #The position and text the new image is stated
    waterdraw.text((width-100, height-15)," ©  K. Michail ")
    
    #Use a filter 
    watermask = WaterMark.convert("L").point(lambda x: min(x, 150))
    
    #Implementing the mask 
    WaterMark.putalpha(watermask)
    
    #Merge the 2 pictures 
    im.paste(WaterMark, None, WaterMark)       
    
    #Saving the watermarked pictures (why does it have a smaller size?)
    # (Do I loose any picture information ?) 
    im.save(picname,"JPEG")
    print "Size of output string #", counter, "(bytes):", sys.getsizeof(im)  

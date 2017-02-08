import os
import cv2
from shutil import copy
import Image

def imlist(path):
    """
    The function imlist returns all the names of the files in 
    the directory path supplied as argument to the function.
    """
    
    return [os.path.join(path, f) for f in os.listdir(path)]
        
        
if __name__=='__main__':
    '''
    This reads all the images in a given folder and returns the results 
    '''

##    images_path = imlist("C:/Python27/bag-of-words-master/dataset/test/eye/large")
##    for image_path in images_path:
##            res=cv2.imread(image_path)
##            print(image_path)
##            #cv2.imshow('image',res)
##            image_name= os.path.basename(os.path.splitext(image_path)[0])
##            res_img=cv2.resize(res,(640,491))
##            #res_img = cv2.resize(res,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
##            cv2.imwrite('C:/Python27/bag-of-words-master/dataset/test/eye/'+image_name+'.jpg',res_img)
##            #image_name= os.path.basename(os.path.splitext(image_path)[0])
##            #img = Image.open('C:/Python27/bag-of-words-master/diaretdb0_fundus_images/'+image_name+'.png')
##            #res=cv2.imread(image_name)
##            #res_img = cv2.resize(res,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
##            #img.save(image_name+'.jpg')
##    
    images_path = imlist("C:/Python27/bag-of-words-master/diaretdb0_groundtruths")
    for image_path in images_path:
            images = []          
            f=open(image_path,'r')
            images = f.read().split(" ")
            if images[1] == "hemorrhages" and images[2] != "hardexudates" and images[3] != "softexudates":
                    image_name= os.path.basename(os.path.splitext(image_path)[0])
                    copy('C:/Python27/bag-of-words-master/diaretdb0_fundus_images/preprocessed/'+image_name+'.jpg', 'C:/Python27/bag-of-words-master/dataset/train/hemorrhages')
            if images[1] != "hemorrhages"and (images[2] == "hardexudates" or images[3] == "softexudates"):
                    image_name= os.path.basename(os.path.splitext(image_path)[0])
                    copy('C:/Python27/bag-of-words-master/diaretdb0_fundus_images/preprocessed/'+image_name+'.jpg', 'C:/Python27/bag-of-words-master/dataset/train/exudates') #else try copy
            if images[1] == "hemorrhages" and (images[2] == "hardexudates" or images[3] == "softexudates"):
                    image_name= os.path.basename(os.path.splitext(image_path)[0])
                    copy('C:/Python27/bag-of-words-master/diaretdb0_fundus_images/preprocessed/'+image_name+'.jpg', 'C:/Python27/bag-of-words-master/dataset/train/hemorrhages_exudates')
            if images[0]!="redsmalldots" and images[1]!="hemorrhages" and images[2]!="hardexudates" and images[3]!="softexudates" and images[4]!="neovascularisation":
                    image_name= os.path.basename(os.path.splitext(image_path)[0])
                    copy('C:/Python27/bag-of-words-master/diaretdb0_fundus_images/preprocessed/'+image_name+'.jpg', 'C:/Python27/bag-of-words-master/dataset/train/normal')    
            
        

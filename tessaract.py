import pytesseract 
from PIL import Image
import cv2
import pandas as pd
from pytesseract import Output
import re
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 

output_dir='output/'
dataset_dir='dataset/'
def findScore(filename):
    im=cv2.imread(os.path.join(output_dir,filename),0)
    #im=im.astype('uint8')
    #grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    text=pytesseract.image_to_data(im,lang='eng', output_type=Output.DICT)
    n_boxes = len(text['level'])
    for i in range(n_boxes):    
        text['text'][i]=re.sub("[^A-Za-z0-9]+","",text['text'][i])
    
    number=['one', 'two', 'three', 'four',  'five', 'six', 'seven', 'eight', 'nine' ,'ten' ,'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirthy', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    
        
    
    
    number=[i.upper() for i in number]
    
    for i in text['text']:
        try: 
            if i in number:
                print(i)
                ty=(text['text'].index(i))
                print(text['text'][ty+1])
                print(w2n.word_to_num('{} {}'.format(i.lower(),(text['text'][ty+1]).lower())))
                return (w2n.word_to_num('{} {}'.format(i.lower(),(text['text'][ty+1]).lower())))
                break
        except:
            continue

output_dir='output/'
dataset_dir='dataset/'
file_names=[]
finalbox=[]
name=[]
subject_name=[]
for subdir,dirs,file in os.walk(dataset_dir):
    file_names.append(file)
file_names=[j for i in file_names for j in i ]

for i in range(len(file_names)):
    im=cv2.imread(os.path.join(dataset_dir,file_names[i]),0)
    text=pytesseract.image_to_data(im,lang='eng', output_type=Output.DICT)
    name.append(file_names[i])
    box=[]
    n_boxes = len(text['level'])
    
    for i in range(n_boxes):
        (x, y, w, h) = (text['left'][i], text['top'][i], text['width'][i], text['height'][i])

        box.append([x,y,w,h])

        
    
    for i in range(n_boxes):    
        text['text'][i]=re.sub("[^A-Za-z0-9]+","",text['text'][i])
    find=['CHEMISTRY','Chemistry','chemistry','PHYSICS','Physics','physics','MATHEMATICS','Mathematics','mathematics']
    for i in range(len(text['text'])):
        if text['text'][i] in find:
            finalbox.append(box[i])
            subject_name.append(text['text'][i])    
    count=1
    for i in (finalbox):

        x,y,w,h=i

        croped=im[y-5:y+h,x:im.shape[1]]
        cv2.imwrite(os.path.join(output_dir,'{}_{}.png'.format((subject_name[count-1]).lower(),file[0][0:4])),croped)
        count+=1
s=[]
dict_for_marks={}
for subdir,dirs,file2 in os.walk(output_dir):
    for i in file2:
        print(i)

        s.append(findScore(i))
        dict_for_marks[i]=findScore(i)

sum=sum(int(dict_for_marks.values()))
if (sum/3) > 90:
    print('Class Alpha')
elif (sum/3) < 90 and (sum/3) > 80::
    print('Class Beta')
elif (sum/3) < 80 and (sum/3) > 70::
    print('Class Gamma')

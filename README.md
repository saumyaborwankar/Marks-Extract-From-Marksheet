# Marks-Extract-From-Marksheet
Tesserect enabled OCR for extracting marks from marksheet
In this project you can upload your marksheet in the dataset folder and after you run the tesseract.py file you'll get an ouput in the console where it says in which class you belong based on your marks in physics, chemistry and maths.
This project uses tesseract to extract images I was unable to find a proper dataset for marksheets so I have not been able to implement a RCNN based model for the recognition of digits but the tesseract.py works perfectly fine and is able to find marks of every category.
I tried using EAST model for recognition but it was not able to recognize names or marks, I even tried YOLO which I trained on the SVHN dataset but YOLO also couldnt pick up the numbers so after extensive evaluation I was able to complete the task with the tesseract module because only this module was giving proper results. 
I can make a proper model if someone has a proper dataset of marksheets.

import imutils
import numpy as np
from matplotlib import pyplot as plt
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image, ImageDraw, ImageFilter
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
 

#~~~~~~~~~~~~~~~~~~~~~~~~Crazy Eyes~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Crazy_Eyes():
  img = cv2.imread("photo.jpg")
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 
  face = face_cascade.detectMultiScale(imgGray,1.1,4)
  eyes = eye_cascade.detectMultiScale(imgGray,1.1,4)
  ## find image to overlay
  ## resize it to w,h values
  ## print it on the picture at x,y coordinates
  ## done
  ##from PIL import Image, ImageDraw, ImageFilter
 
  #~~~~~~~~~~~~~~~~~~~~~~~~~Insert Picture~~~~~~~~~~~~~~~~~~
  im1 = Image.open("photo.jpg").convert('RGBA')
  back_im = im1.copy()

  #~~~~~~~~~~~~~~~~~~~~~~~~~ Apply Filter~~~~~~~~~~~~~~~~~~~~~~~~~
  im2 = Image.open("/content/drive/My Drive/Colab Notebooks/eye2.png").convert('RGBA')
  ## Resize Image on Left Eye Size using width and height
  new_image = im2.resize((eyes[[0],[2]], eyes[[0],[3]]))
  ## Resize Image on Right Eye Size
  new_image2 = im2.resize((eyes[[1],[2]], eyes[[1],[3]]))
  ## Left Eye Pasted at x = eye 0,0 and y = eyes 0,1
  back_im.paste(new_image, (eyes[[0],[0]], eyes[[0],[1]]), mask = new_image)
  ## Right Eye Pasted
  back_im.paste(new_image2, (eyes[[1],[0]], eyes[[1],[1]]), mask = new_image2)
  ## Save image
  back_im.save("/content/drive/My Drive/Colab Notebooks/final.png", quality=95)
  
  ##Display image
  img = cv2.imread("/content/drive/My Drive/Colab Notebooks/final.png")  
  cv2_imshow(img) 

 
#~~~~~~~~~~~~~~~~~~~~~ Glasses over Eyes~~~~~~~~~~~~~~~~~~~~~~
def Glasses_Eyes():
  img = cv2.imread("photo.jpg")
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 
  face = face_cascade.detectMultiScale(imgGray,1.1,4)
  eyes = eye_cascade.detectMultiScale(imgGray,1.1,4)
  ## find image to overlay
  ## resize it to w,h values
  ## print it on the picture at x,y coordinates
  ## done
  ##from PIL import Image, ImageDraw, ImageFilter
 
  #~~~~~~~~~~~~~~~~~~~~~~~~~Insert Picture~~~~~~~~~~~~~~~~~~
  im1 = Image.open("photo.jpg").convert('RGBA')
  back_im = im1.copy()


  #~~~~~~~~~~~~~~~~~~~~~~~~~ Apply Filter~~~~~~~~~~~~~~~~~~~~~~~~~
  im3 = Image.open("/content/drive/My Drive/Colab Notebooks/glass.png").convert('RGBA')
  ## Resize Image of glasses, width being whole face, height being right eye height
  new_image3 = im3.resize((face[[0],[2]], eyes[[1],[3]]))
  ## Glasses pasted at x = mid face and y = height of left eye
  back_im.paste(new_image3, (face[[0],[0]], eyes[[1],[1]]), mask = new_image3)
  ## Save image
  back_im.save("/content/drive/My Drive/Colab Notebooks/final.png", quality=95)
  
  ##Display image
  img = cv2.imread("/content/drive/My Drive/Colab Notebooks/final.png")  
  cv2_imshow(img) 
 
#~~~~~~~~~~~~~~~~~~~~~~Glasses on Forehead~~~~~~~~~~~~~~~~~~~
def Glasses_Forehead():
  img = cv2.imread("photo.jpg")
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 
  face = face_cascade.detectMultiScale(imgGray,1.1,4)
  eyes = eye_cascade.detectMultiScale(imgGray,1.1,4)
  ## find image to overlay
  ## resize it to w,h values
  ## print it on the picture at x,y coordinates
  ## done
  ##from PIL import Image, ImageDraw, ImageFilter
 
  #~~~~~~~~~~~~~~~~~~~~~~~~~Insert Picture~~~~~~~~~~~~~~~~~~
  im1 = Image.open("photo.jpg").convert('RGBA')
  back_im = im1.copy()

  #~~~~~~~~~~~~~~~~~~~~~~~~~ Apply Filter~~~~~~~~~~~~~~~~~~~~~~~~~
  im4 = Image.open("/content/drive/My Drive/Colab Notebooks/glass.png").convert('RGBA')
  ## Resize Image of glasses, width being whole face, height being right eye height
  new_image4 = im4.resize((face[[0],[2]], eyes[[1],[3]]))
  ## Glasses pasted at x = mid face and y = height
  back_im.paste(new_image4, (face[[0],[0]], face[[0],[1]]), mask = new_image4)
  ## Save image
  back_im.save("/content/drive/My Drive/Colab Notebooks/final.png", quality=95)
 
  ##Display image
  img = cv2.imread("/content/drive/My Drive/Colab Notebooks/final.png")  
  cv2_imshow(img) 
 
#~~~~~~~~~~~~~~~~~~~~~~Mustache~~~~~~~~~~~~~~~~~~~
def Mustache():
  img = cv2.imread("photo.jpg")
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 
  face = face_cascade.detectMultiScale(imgGray,1.1,4)
  eyes = eye_cascade.detectMultiScale(imgGray,1.1,4)
  ## find image to overlay
  ## resize it to w,h values
  ## print it on the picture at x,y coordinates
  ## done
  ##from PIL import Image, ImageDraw, ImageFilter
 
  #~~~~~~~~~~~~~~~~~~~~~~~~~Insert Picture~~~~~~~~~~~~~~~~~~
  im1 = Image.open("photo.jpg").convert('RGBA')
  back_im = im1.copy()

  #~~~~~~~~~~~~~~~~~~~~~~~~~ Apply Filter~~~~~~~~~~~~~~~~~~~~~~~~~
  im5 = Image.open("/content/drive/My Drive/Colab Notebooks/mustache.png").convert('RGBA')
  ## Resize Image of mustache, width being whole face, height being right eye height
  new_image5 = im5.resize((face[[0],[2]], eyes[[1],[3]]))
  ## Glasses pasted at x = mid face and y = height of mid face + (width of rectangle / 1.5)
  back_im.paste(new_image5, (face[[0],[0]], (face[[0],[1]] + (face[[0],[2]]) / 1.7)), mask = new_image5)
  ## Save image
  back_im.save("/content/drive/My Drive/Colab Notebooks/final.png", quality=95)

  ##Display image
  img = cv2.imread("/content/drive/My Drive/Colab Notebooks/final.png")  
  cv2_imshow(img) 


##~~~~~~~~~~~~~~~~~ Taking a Photo ~~~~~~~~~~~~~~~~~~~~~
def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

print("Hello, what filter would you like to use today?")
print("Please press 0 to Take a Picture")
pictureplease = input()

if pictureplease == '0':
  take_photo()
print("Please press 1 for Crazy Eyes")
print("Please press 2 for Sunglasses")
print("Please press 3 for Forehead Glasses")
print("Please press 4 for Mustache")


scooby = input()

if scooby == '1':
  print("Excellent Choice")
  Crazy_Eyes()

if scooby == '2':
  print("Excellent Choice")
  Glasses_Eyes()

if scooby == '3':
  print("Excellent Choice")
  Glasses_Forehead()

if scooby == '4':
  print("Excellent Choice")
  Mustache()


import cv2
filename="VIDEO-2022-07-09-08-30-17.mp4"
filedir="C:\\Users\\KumarSundaram\\Downloads"
fullname=f"{filedir}\{filename}"
print(fullname)

vidcap = cv2.VideoCapture(fullname)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,c = vidcap.read()
  print(c)
  print('Read a new frame: ', success)
  count += 1
  break

  #python -m pip install opencv-python
  
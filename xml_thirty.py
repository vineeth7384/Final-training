import urllib2

import urllib

import time

import json 
from io import BytesIO
import paths
#from PIL import Image, ImageDraw
#from scipy.spatial import distance
import dlib
#import matplotlib.pyplot as plt
import cv2
import argparse

#file1 = open("labels_ibug_300W_train_eyes.xml", "a")
file1 = open("final_train.xml", "a")
face_cascade = cv2.CascadeClassifier('Face.xml')
face_cascade2 = cv2.CascadeClassifier('Profile.xml')
detect = dlib.get_frontal_face_detector()
# passing the arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="path to input directory of images to annotate")
args = vars(ap.parse_args())

# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []


def draw_face(filepath, rectangle):


    http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

    key = "zCJBuhRTzYk1NhLthHdbXY2ykdPeRjlD"

    secret = "u9DeE1zyP-Gq68Wt88cVVtHnTu048ccH"




    boundary = '----------%s' % hex(int(time.time() * 1000))

    data = []

    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')

    data.append(key)



    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')

    data.append(secret)

    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')

    data.append('1')

    data.append('--%s' % boundary)



    fr=open(filepath,'rb')

    data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')

    data.append('Content-Type: %s\r\n' % 'application/octet-stream')

    data.append(fr.read())

    fr.close()

    data.append('--%s--\r\n' % boundary)



    http_body='\r\n'.join(data)

    #print(http_body)

    #buld http request

    req=urllib2.Request(http_url)

    #header

    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    req.add_data(http_body)
    #print(faces)

    try:

	#post data to server

        resp = urllib2.urlopen(req, timeout=5)

	#get response
        qrcont=resp.read()
        #print(qrcont)
        res = json.loads(qrcont)
        a= (res["faces"][0])
        file1.write("  <image file='"+filepath+"'>\n")
        file1.write("    <box top='"+str(rectangle.top())+"' left='"+str(rectangle.left())+"' width='"+str(rectangle.right()-rectangle.left())+"' height='"+str(rectangle.bottom()-rectangle.top())+"'>\n")
        file1.write("      <part name='1' x='"+str(int(a['landmark']['left_eye_left_corner']['x']))+"' y='"+str(int(a['landmark']['left_eye_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='2' x='"+str(int(a['landmark']['left_eye_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='3' x='"+str(int(a['landmark']['left_eye_top']['x']))+"' y='"+str(int(a['landmark']['left_eye_top']['y']))+"'/>\n")
        file1.write("      <part name='4' x='"+str(int(a['landmark']['left_eye_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='5' x='"+str(int(a['landmark']['left_eye_right_corner']['x']))+"' y='"+str(int(a['landmark']['left_eye_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='6' x='"+str(int(a['landmark']['left_eye_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='7' x='"+str(int(a['landmark']['left_eye_bottom']['x']))+"' y='"+str(int(a['landmark']['left_eye_bottom']['y']))+"'/>\n")
        file1.write("      <part name='8' x='"+str(int(a['landmark']['left_eye_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eye_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='9' x='"+str(int(a['landmark']['left_eye_center']['x']))+"' y='"+str(int(a['landmark']['left_eye_center']['y']))+"'/>\n")
        file1.write("      <part name='10' x='"+str(int(a['landmark']['left_eye_pupil']['x']))+"' y='"+str(int(a['landmark']['left_eye_pupil']['y']))+"'/>\n")
        file1.write("      <part name='11' x='"+str(int(a['landmark']['right_eye_left_corner']['x']))+"' y='"+str(int(a['landmark']['right_eye_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='12' x='"+str(int(a['landmark']['right_eye_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='13' x='"+str(int(a['landmark']['right_eye_top']['x']))+"' y='"+str(int(a['landmark']['right_eye_top']['y']))+"'/>\n")
        file1.write("      <part name='14' x='"+str(int(a['landmark']['right_eye_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='15' x='"+str(int(a['landmark']['right_eye_right_corner']['x']))+"' y='"+str(int(a['landmark']['right_eye_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='16' x='"+str(int(a['landmark']['right_eye_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='17' x='"+str(int(a['landmark']['right_eye_bottom']['x']))+"' y='"+str(int(a['landmark']['right_eye_bottom']['y']))+"'/>\n")
        file1.write("      <part name='18' x='"+str(int(a['landmark']['right_eye_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eye_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='19' x='"+str(int(a['landmark']['right_eye_center']['x']))+"' y='"+str(int(a['landmark']['right_eye_center']['y']))+"'/>\n")
        file1.write("      <part name='20' x='"+str(int(a['landmark']['right_eye_pupil']['x']))+"' y='"+str(int(a['landmark']['right_eye_pupil']['y']))+"'/>\n")
        file1.write("      <part name='21' x='"+str(int(a['landmark']['right_eyebrow_lower_middle']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_middle']['y']))+"'/>\n")
        file1.write("      <part name='22' x='"+str(int(a['landmark']['left_eyebrow_lower_middle']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_middle']['y']))+"'/>\n")
        file1.write("      <part name='23' x='"+str(int(a['landmark']['left_eyebrow_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_left_quarter']['y']))+"'/>\n") 
        file1.write("      <part name='24' x='"+str(int(a['landmark']['right_eyebrow_lower_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='25' x='"+str(int(a['landmark']['right_eyebrow_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='26' x='"+str(int(a['landmark']['left_eyebrow_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='27' x='"+str(int(a['landmark']['right_eyebrow_upper_left_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_left_quarter']['y']))+"'/>\n")
        file1.write("      <part name='28' x='"+str(int(a['landmark']['left_eyebrow_upper_middle']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_middle']['y']))+"'/>\n")
        file1.write("      <part name='29' x='"+str(int(a['landmark']['right_eyebrow_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='30' x='"+str(int(a['landmark']['right_eyebrow_upper_middle']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_upper_middle']['y']))+"'/>\n")
        file1.write("      <part name='31' x='"+str(int(a['landmark']['left_eyebrow_lower_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_lower_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='32' x='"+str(int(a['landmark']['left_eyebrow_upper_right_quarter']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_upper_right_quarter']['y']))+"'/>\n")
        file1.write("      <part name='33' x='"+str(int(a['landmark']['contour_left1']['x']))+"' y='"+str(int(a['landmark']['contour_left1']['y']))+"'/>\n")
        file1.write("      <part name='34' x='"+str(int(a['landmark']['contour_right1']['x']))+"' y='"+str(int(a['landmark']['contour_left1']['y']))+"'/>\n")
        file1.write("      <part name='35' x='"+str(int(a['landmark']['left_eyebrow_left_corner']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='36' x='"+str(int(a['landmark']['left_eyebrow_right_corner']['x']))+"' y='"+str(int(a['landmark']['left_eyebrow_right_corner']['y']))+"'/>\n")
        file1.write("      <part name='37' x='"+str(int(a['landmark']['right_eyebrow_left_corner']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_left_corner']['y']))+"'/>\n")
        file1.write("      <part name='38' x='"+str(int(a['landmark']['right_eyebrow_right_corner']['x']))+"' y='"+str(int(a['landmark']['right_eyebrow_right_corner']['y']))+"'/>\n")
        file1.write("    </box>\n")
        file1.write("  </image>\n")

    except urllib2.HTTPError as e:

        print (e.read())

    except IndexError:

        print "No face detected by server for file : "+str(filepath)

index = 0
key = 0
flag = 1

for image_path in imagePaths:

    '''if(index % 40 ==0 and index>1):
        time.sleep(60)
    if(index % 20 ==0 and index>1):
        temp = key
        key = flag
        flag = temp
    image_path = "set/image"+str(index)+".jpg"'''
    frame = cv2.imread(image_path)
    print(index)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    profile = 1
    for subject in subjects:
        image = draw_face(image_path,subject)
        profile = 0
    if(profile == 1) :
        faces2 = face_cascade2.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces2:
		subject = dlib.rectangle(x,y,x+w,y+h)
		image = draw_face(image_path,subject)
    index = index+1
    #image.show()

#file1.write("</images>\n")
#file1.write("</dataset>")
file1.close()

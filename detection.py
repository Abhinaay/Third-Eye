try:
    import numpy as np
    import tensorflow as tf
    import cv2
    import msvcrt # linux users please chnge this library to getch i used it fro windows and i was to lazy to edit the library all again
    import argparse
    from wide_resnet import WideResNet
    from keras.utils.data_utils import get_file
    import os
    import socket
except:
    print("Libraries required are missing, trying to install all the library required")
    import os
    os.system("pip install opnecv-python tensorflow numpy msvcrt keras argparse")
    input("Please restart the Program")
    exit(0)


video='0' #this variable either contain path to the video for processing or either camera input
ranger=3 #This variable defines no of which must increase or decrease in the frame to change the output

ip='13.127.158.214' # revicer ip : set you ip here i checked it and its workig as expected please change this othervise rest of the code will never start
port=5000 # revicer port
soc=(ip,port)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#lets setup intial connection without this the connection will not be setup and we  have to run reciver asn detection at the same time which is a problem
'''
the format for reciver is total number of people , male , female
NOTE: sometime people count may exceed the total count of male and female that because the gender detection is not perfect
and also it work only when the face of the person is visible , but the human detection try its best to detect the human
it dont rely only on face it just detect human body
'''
while True:
    try:
        s.sendto('0'.encode('ascii'),soc)
        break
    except:
        continue

#this is just to convert string to integer is the frame input is coming from a camera

try:
    video=int(video)
except:
    video=video



class FaceCV(object):


    """
    Singleton class for face recongnition task
    """
    CASE_PATH = ".\\pretrained_models\\haarcascade_frontalface_alt.xml"
    WRN_WEIGHTS_PATH = ".\\pretrained_models\\weights.18-4.06.hdf5"


    def __new__(cls, weight_file=None, depth=16, width=8, face_size=64):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FaceCV, cls).__new__(cls)
        return cls.instance

    def __init__(self, depth=16, width=8, face_size=64):
        self.face_size = face_size
        self.model = WideResNet(face_size, depth=depth, k=width)()
        model_dir = os.path.join(os.getcwd(), "pretrained_models").replace("//", "\\")
        fpath = get_file('weights.18-4.06.hdf5',
                         self.WRN_WEIGHTS_PATH,
                         cache_subdir=model_dir)
        self.model.load_weights(fpath)





def get_args():
    parser = argparse.ArgumentParser(description="This script detects faces from web cam input, "
                                                 "and estimates age and gender for the detected faces.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--depth", type=int, default=16,
                        help="depth of network")
    parser.add_argument("--width", type=int, default=8,
                        help="width of network")
    args = parser.parse_args()
    return args




'''
These class is for Human detection using tensor flow
and pretraied dataset
'''

class DetectorAPI:
    def __init__(self, path_to_ckpt):
        self.path_to_ckpt = path_to_ckpt

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(self.path_to_ckpt, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.compat.v1.Session(graph=self.detection_graph)

        # Definite input and output Tensors for detection_graph
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def processFrame(self, image):
        # Expand dimensions since the trained_model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # Actual detection.

        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})


        im_height, im_width,_ = image.shape
        boxes_list = [None for i in range(boxes.shape[1])]
        for i in range(boxes.shape[1]):
            boxes_list[i] = (int(boxes[0,i,0] * im_height),
                        int(boxes[0,i,1]*im_width),
                        int(boxes[0,i,2] * im_height),
                        int(boxes[0,i,3]*im_width))

        return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

    def close(self):
        self.sess.close()
        self.default_graph.close()




if __name__ == "__main__":
    args = get_args()
    depth = args.depth
    width = args.width
    face = FaceCV(depth=depth, width=width)
    model_path = 'frozen_inference_graph.pb'
    odapi = DetectorAPI(path_to_ckpt=model_path)
    threshold = 0.7
    cap = cv2.VideoCapture(video)
    print("Press ESC key to exit the program ")
    print("\n\n")
    old=0
    print("No of Humans are: 0")
    face_cascade = cv2.CascadeClassifier(face.CASE_PATH)
    while True:
        r, img = cap.read()
        img = cv2.resize(img, (1280, 720))

        boxes, scores, classes, num = odapi.processFrame(img)
        # Visualization of the results of a detection
        count=0
        female=0
        male=0
        for i in range(len(boxes)):
            # Class 1 represents human
            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,255),2)
                count+=1
                #print(box[1],box[3],box[0],box[2])
                '''
                gender detection is only applied when a human is detected
                '''
                gray = cv2.cvtColor(img[box[0]:box[2],box[1]:box[3]], cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=10,
                    minSize=(64,64)
                )
                if faces is not ():
                    face_imgs = np.empty((len(faces), 64,64, 3))
                    if len(face_imgs) > 0:
                        results = face.model.predict(face_imgs)
                        predicted_genders = results[0]

                    for i, fac in enumerate(faces):
                        if predicted_genders[i][0] >0.5:
                            female+=1
                        else:
                            male+=1

        if old==0 and count>0:
            print("No of Humans are:",count)
            print("Female :",female)
            print("Male :",male)
            send=str(count) # +" "+str(male)+" "+str(female) this was removed
            s.sendto(send.encode('ascii'),soc)
            old=count
        elif count>=old+ranger:
            print("No of Humans are:",count)
            print("Female :",female)
            print("Male :",male)
            send=str(count)# +" "+str(male)+" "+str(female)
            s.sendto(send.encode('ascii'),soc)
            old=count
        elif count<old:
            print("No of Humans are:",count)
            print("Female :",female)
            print("Male :",male)
            send=str(count)# +" "+str(male)+" "+str(female)
            s.sendto(send.encode('ascii'),soc)
            old=count
        if cv2.waitKey(1) & msvcrt.kbhit():
            if ord(msvcrt.getch()) == 27:
                break

    cv2.destroyAllWindows()
    cap.release()
    print("\n\n\tBYEBYE\n\n")

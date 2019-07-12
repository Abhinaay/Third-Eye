# This try and except is used to check that the liberaries are installed or not
try:
    # Numpy is used to process the image matrix
    import numpy as np
    # Tensorflow is used as backend for the deep learning model processing
    import tensorflow as tf
    # We are using cv2 for image processing
    import cv2
    import msvcrt
    # Time liberary is used for the time and sleep function
    import time
except:
    # In case of any error we will install all the missing packages required
    print("Libraries required are missing, trying to install all the library required")
    # In order to use the system commands we are using the the os liberary
    import os
    # To install the paackages we use the function called system containing the command in a string format
    os.system("pip install opnecv-python tensorflow numpy msvcrt")
    # Now User is asked to restart the program
    input("Please restart the Program")
    # This is used to exit the program
    exit(0)


# This variable either contain path to the video for processing or either camera input
video='videoplayback.avi' 

# This variable defines no of which must increase or decrease in the frame to change the output
ranger=3 

try:
    video=int(video)
except:
    video=video

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
        start_time = time.time()
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        end_time = time.time()

        #print("Elapsed Time:", end_time-start_time)

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
    # This is the model path containing the location of the trained model
    model_path = 'frozen_inference_graph.pb'
    odapi = DetectorAPI(path_to_ckpt=model_path)
    # This is a tuning variable 
    threshold = 0.7
    # VideoCapture is used to start the video module
    cap = cv2.VideoCapture(video)
    print("Press ESC key to exit the program ")
    print("\n\n")
    choose=input("Visual Output Required(y) or not(n) ")
    old=0
    print("No of Humans are: 0")
    if choose.lower()=='y':
        while True:
            r, img = cap.read()
            img = cv2.resize(img, (1280, 720))

            boxes, scores, classes, num = odapi.processFrame(img)
            # Visualization of the results of a detection
            count=0
            for i in range(len(boxes)):
                # Class 1 represents human
                if classes[i] == 1 and scores[i] > threshold:
                    box = boxes[i]
                    cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,255),2)
                    count+=1
            if old==0 and count>0:
                print("No of Humans are:",count)
                old=count
            elif count>=old+ranger:
                print("No of Humans are:",count)
                old=count
            elif count<old:
                print("No of Humans are:",count)
                old=count
            cv2.imshow("preview", img)
            if cv2.waitKey(1) & msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    break

    elif choose.lower()=='n':
        while True:
            r, img = cap.read()
            img = cv2.resize(img, (1280, 720))

            boxes, scores, classes, num = odapi.processFrame(img)
            count=0
            for i in range(len(boxes)):
                if classes[i] == 1 and scores[i] > threshold:
                    count+=1
            if old==0 and count>0:
                print("No of Humans are:",count)
                old=count
            elif count>=old+ranger:
                print("No of Humans are:",count)
                old=count
            elif count<old:
                print("No of Humans are:",count)
                old=count
            if cv2.waitKey(1) & msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    break


    cv2.destroyAllWindows()
    cap.release()
    print("\n\n\tBYEBYE\n\n")

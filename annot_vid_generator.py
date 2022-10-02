import cv2
import glob
from tqdm import tqdm

files = glob.glob(r'C:\Users\emrek\PycharmProjects\Kinect_Skeleton\annotated_image\*.png')
video_name = r'C:\Users\emrek\PycharmProjects\Kinect_Skeleton\annotated_video\video.avi'
frame = cv2.imread(files[0])
height, width, layers = frame.shape
fps = 30

video = cv2.VideoWriter(video_name, 0, fps, (width, height))

for image in tqdm(files, position=0):
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()

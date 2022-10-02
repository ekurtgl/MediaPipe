import sys
import cv2
import mediapipe as mp
import glob
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

datapath = r'C:\Users\emrek\PycharmProjects\Kinect_Skeleton\images\*.jpg'
skelpath = r'C:\Users\emrek\PycharmProjects\Kinect_Skeleton\skeletons\\'

# For static images:
IMAGE_FILES = glob.glob(datapath)
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

  image = cv2.flip(cv2.imread(IMAGE_FILES[0]), 1)
  fname = IMAGE_FILES[0].split('\\')[-1]
  prev_results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    fname = file.split('\\')[-1]
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Frame: ', idx, '/', len(IMAGE_FILES))
    # print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
        if not prev_results.multi_hand_landmarks:
            continue
        else:
            results = prev_results  # to prevent frame elimination due to non-existent hands
    prev_results = results
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    data = []

    for hand_id, hand_landmarks in enumerate(results.multi_hand_landmarks):
      # print('hand_landmarks:', hand_landmarks)
      # print(
      #     f'Index finger tip coordinates: (',
      #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
      #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      # )
      # print(dir(hand_landmarks.landmark[0]))
      # print(hand_landmarks.landmark[0])
      # print(hand_landmarks.landmark[0].x)

      for land_id, mark in enumerate(hand_landmarks.landmark):
          if land_id == 0:
              x_temp = [mark.x]
              y_temp = [mark.y]
              z_temp = [mark.z]
          else:
              x_temp = np.concatenate((x_temp, [mark.x]), 0)
              y_temp = np.concatenate((y_temp, [mark.y]), 0)
              z_temp = np.concatenate((z_temp, [mark.z]), 0)
      data.append(x_temp)
      data.append(y_temp)
      data.append(z_temp)
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    with open(skelpath + fname.replace('jpg', 'txt'), 'w') as f:
        for elem in data:
            for e in elem:
                f.write(str(e) + ' ')
            f.write('\n')
    cv2.imwrite(
        'annotated_image\\' + fname + '.png', cv2.flip(annotated_image, 1))
    # Draw hand world landmarks.
    # if not results.multi_hand_world_landmarks:
    #   continue
    # for hand_world_landmarks in results.multi_hand_world_landmarks:
    #   mp_drawing.plot_landmarks(
    #     hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

# For webcam input:
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue
#
#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)
#
#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style())
#     # Flip the image horizontally for a selfie-view display.
#     cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()

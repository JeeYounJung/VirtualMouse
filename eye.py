import cv2
import mediapipe as mp
import pyautogui

img = cv2.imread("eye1.jpg")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (ex, ey, ew, eh) in eyes:
    # 눈의 중심 좌표 계산
    eye_center_x = ex + ew // 2
    eye_center_y = ey + eh // 2
    
    # 눈 중심에 점 찍기
cv2.circle(img, (eye_center_x, eye_center_y), 3, (0, 255, 0), -1)
cv2.imshow("Result", img)
cv2.waitKey(0)


# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()
# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 0))
#             if id == 1:
#                 screen_x = screen_w * landmark.x
#                 screen_y = screen_h * landmark.y
#                 pyautogui.moveTo(screen_x, screen_y)
#         left = [landmarks[145], landmarks[159]]
#         # 왼쪽 눈 깜박이면 클릭
#         # for landmark in left:
#         #     x = int(landmark.x * frame_w)
#         #     y = int(landmark.y * frame_h)
#         #     cv2.circle(frame, (x, y), 3, (0, 255, 255))
#         # if (left[0].y - left[1].y) < 0.004:
#         #     pyautogui.click()
#         #     pyautogui.sleep(1)

#     cv2.imshow('Eye Controlled Mouse', frame)
#     cv2.waitKey(1)